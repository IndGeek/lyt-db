import requests
from server.utils.uri_parser import LytURIParser

class LytDBClient:
    def __init__(self, uri):
        parser = LytURIParser(uri)
        self.base_url = f"http://{parser.host}:{parser.port}"
        self.db_name = parser.db_name

    def create_database(self):
        response = requests.post(f"{self.base_url}/create/{self.db_name}")
        return response.json()

    def read_database(self):
        response = requests.get(f"{self.base_url}/read/{self.db_name}")
        return response.json()

    def write_to_database(self, data):
        response = requests.post(f"{self.base_url}/write/{self.db_name}", json=data)
        return response.json()

# Example Usage
if __name__ == "__main__":
    client = LytDBClient("lyt://127.0.0.1:8000/test_db")
    print(client.create_database()) 
    print(client.write_to_database({"key": "value"}))
    print(client.read_database())
