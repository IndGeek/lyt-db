import re

class LytURIParser:
    def __init__(self, uri):
        self.scheme = None
        self.host = None
        self.port = None
        self.db_name = None
        self.parse_uri(uri)

    def parse_uri(self, uri):
        pattern = r"^lyt://(?P<host>[\w\.]+):(?P<port>\d+)/(?P<db_name>\w+)$"
        match = re.match(pattern, uri)
        if not match:
            raise ValueError("Invalid URI format. Expected: lyt://<host>:<port>/<db_name>")
        self.scheme = "lyt"
        self.host = match.group("host")
        self.port = int(match.group("port"))
        self.db_name = match.group("db_name")

    def to_http_url(self):
        return f"http://{self.host}:{self.port}/{self.db_name}"

# Example Usage
if __name__ == "__main__":
    uri = "lyt://127.0.0.1:8000/my_database"
    parser = LytURIParser(uri)
    print(parser.to_http_url())  # Output: http://127.0.0.1:8000/my_database
