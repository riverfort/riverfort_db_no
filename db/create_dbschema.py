from configuration.config import DatabaseConnection
import db_queries

db = DatabaseConnection("riverFort_no", "river", "fort", "localhost", 5432)

print("Creating table user_device...")
db.create_table(db_queries.user_device_table_query)

print("Creating table company...")
db.create_table(db_queries.company_table_query)

print("Creating table company_news...")
db.create_table(db_queries.company_news_table_query)

print("Creating table watchlist...")
db.create_table(db_queries.watchlist_table_query)
