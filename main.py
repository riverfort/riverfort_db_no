from db.configuration.config import DatabaseConnection
from utils.utils import remove_lse_company_ticker_suffix
from utils.utils import push_notification_run
import feedparser
import asyncio

db = DatabaseConnection("riverFort_no", "river", "fort", "localhost", 5432)

def read_article_feed(company_ticker):
    symbol = remove_lse_company_ticker_suffix(company_ticker)
    feed = feedparser.parse('https://www.investegate.co.uk/Rss.aspx?company={}'.format(symbol))
    for article in feed['entries'][:1]:
        title    = article["title"]
        pub_date = article["published"]
        if is_article_in_db(company_ticker, pub_date):
            print(company_ticker + ": no new feed")
        else:
            print(company_ticker + ": new feed!")
            push_notification(company_ticker, title)
            delete_all_articles(company_ticker)
            add_article_to_db(company_ticker, pub_date, title)

def is_article_in_db(company_ticker, pub_date):
    result = db.filter_data("SELECT * FROM company_news WHERE company_ticker=%s AND pub_date=%s", (company_ticker, pub_date))
    if result == []:
        return False
    else:
        return True

def add_article_to_db(company_ticker, pub_date, title):
    db.insert_data("INSERT INTO company_news (company_ticker, pub_date, title) VALUES (%s, %s, %s) RETURNING company_ticker", (company_ticker, pub_date, title))

def delete_all_articles(company_ticker):
    db.delete("DELETE FROM company_news WHERE company_ticker=%s", (company_ticker,))

def push_notification(company_ticker, title):
    result = db.filter_data("SELECT device_token FROM watchlist WHERE company_ticker=%s", (company_ticker,))
    for device_token in result:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(push_notification_run(device_token[0], company_ticker, title))

companies = db.select_data("SELECT * FROM company")
for company in companies:
    read_article_feed(company[0])
