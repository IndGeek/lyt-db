from client.lyt_client import LytDBClient

client = LytDBClient("lyt://127.0.0.1:8080")

print(client.create_database("test_db"))

print(client.read_database("test_db"))