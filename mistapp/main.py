import configparser

config = configparser.ConfigParser()

config.read("config.ini")

db_host = config["database"]["host"]
db_user = config["database"]["user"]
db_password = config["database"]["password"]

print(f"Host: {db_host}, User: {db_user}")