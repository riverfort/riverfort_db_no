import asyncio
from uuid import uuid4
from aioapns import APNs, NotificationRequest, PushType

def remove_lse_company_ticker_suffix(company_ticker):
    if company_ticker.endswith(".L"):
        return company_ticker[:-2]

async def push_notification_run(device_token, company_ticker, title, link):
    print("-- pushing notification to: " + device_token)
    apns_key_client = APNs(
        key='key/AuthKey_58M45W44RZ.p8',
        key_id='58M45W44RZ',
        team_id='A8X2W38P62',
        topic='com.RiverFort',  # Bundle ID
        use_sandbox=True,
    )
    request = NotificationRequest(
        device_token=device_token,
        message = {
            "aps": {
                "alert": {
                    "title": "New Feed Available: {}".format(company_ticker),
                    "subtitle": "{}".format(title),
                },
                "sound": "default",
                "company_ticker": "{}".format(company_ticker),
                "link": "{}".format(link),
                "category": "NEWS_CATEGORY",
            }
        },
    )
    await apns_key_client.send_notification(request)
