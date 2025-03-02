from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
SERVER_PORT = os.getenv("SERVER_PORT")
HOST_PORT = os.getenv("HOST_PORT")

url_host_service ='http://127.0.0.1:{}/services/match'.format(HOST_PORT)
url_server_service ='http://127.0.0.1:{}/services/match'.format(SERVER_PORT)
