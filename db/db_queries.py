# USER
user_device_table_query = "CREATE TABLE IF NOT EXISTS user_device (device_token VARCHAR(200) PRIMARY KEY)"

# Company
company_table_query = "CREATE TABLE IF NOT EXISTS company (company_ticker VARCHAR(25) PRIMARY KEY, company_name VARCHAR(100) NOT NULL)"

# Company_News
company_news_table_query = """
                           CREATE TABLE IF NOT EXISTS company_news (
                           company_ticker VARCHAR(25) REFERENCES company (company_ticker),
                           pub_date TIMESTAMP NOT NULL,
                           title VARCHAR(200) NOT NULL,
                           PRIMARY KEY (company_ticker, pub_date))
                           """

# Watchlist
watchlist_table_query = """
                        CREATE TABLE IF NOT EXISTS watchlist (
                        watchlist_id SERIAL PRIMARY KEY,
                        device_token VARCHAR(200) NOT NULL REFERENCES user_device (device_token) ON UPDATE CASCADE ON DELETE CASCADE, 
                        company_ticker VARCHAR(25) NOT NULL REFERENCES company (company_ticker) ON UPDATE CASCADE ON DELETE CASCADE,
                        UNIQUE (device_token, company_ticker))
                        """
