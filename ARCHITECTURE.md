## Motive
Aim is to create a very lightweight self hosted database with custom protocols and easy to use; having a connection string like `lyt://user:pw@ip:port/db-name`

```
LytDB/
├── server/                 # Backend server implementation
│   ├── __init__.py         # Makes this a Python package
│   ├── app.py              # Main server application (entry point)
│   ├── db_engine/          # Core database engine logic
│   │   ├── storage.py      # Data storage implementation
│   │   ├── parser.py       # Query parser
│   │   ├── indexer.py      # Indexing algorithms
│   │   ├── config.py       # Configuration management
│   │   └── __init__.py     # Engine package initializer
│   ├── api/                # HTTP API or custom protocol
│   │   ├── endpoints.py    # HTTP route handlers
│   │   ├── socket_server.py# For socket-based communication
│   │   └── auth.py         # Authentication handlers
│   ├── utils/              # Utilities and helpers
│   │   ├── logger.py       # Logging utility
│   │   ├── uri_parser.py   # Parses lyt:// URIs
│   │   └── helpers.py      # General-purpose helpers
│   └── tests/              # Backend unit tests
│       ├── test_storage.py # Test storage logic
│       ├── test_api.py     # Test API endpoints
│       └── __init__.py
├── client/                 # Client library for developers
│   ├── lyt_client.py      # Python library to interact with the database
│   ├── examples/           # Examples showing usage of the library
│   │   └── basic_usage.py
│   └── tests/              # Client-side unit tests
│       └── test_client.py
├── dashboard/              # Frontend for visualizations (optional)
│   ├── public/             # Static assets (e.g., images, fonts)
│   ├── src/                # Frontend source code
│   │   ├── components/     # Reusable components
│   │   ├── pages/          # Pages (e.g., Dashboard, Login)
│   │   └── styles/         # Styling
│   └── tests/              # Frontend tests
├── docker/                 # Docker-related configurations
│   ├── Dockerfile          # Dockerfile for the server
│   ├── docker-compose.yml  # Multi-container setup
│   └── README.md           # Instructions for using Docker
├── docs/                   # Project documentation
│   ├── getting_started.md  # Getting started guide
│   ├── contribution.md     # Guidelines for contributing
│   ├── architecture.md     # Detailed project architecture
│   └── api_reference.md    # API documentation
├── .github/                # GitHub-specific files
│   ├── ISSUE_TEMPLATE/     # Issue templates
│   ├── workflows/          # GitHub Actions for CI/CD
│   │   ├── build.yml       # Build and test workflow
│   │   └── release.yml     # Release workflow
├── .env.example            # Example environment variables
├── .gitignore              # Git ignore file
├── LICENSE                 # License for the project
├── README.md               # Project overview
├── requirements.txt        # Python dependencies
└── setup.py                # For packaging the project
```