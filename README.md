# Django Chat Application with Redis and Channels

This guide provides step-by-step instructions on setting up and running the Django chat application using **Redis**, **Django Channels**, and **Daphne**.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- Redis Server
- Daphne
- Django Channels
- Channels Redis

## Installation Steps

### 1. Clone the Repository
```sh
git clone https://github.com/your-repository/chatapp.git
cd chatapp
```

### 2. Create and Activate Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```
If you don't have a `requirements.txt`, install manually:
```sh
pip install django channels channels_redis daphne
```

### 4. Start Redis Server
Make sure Redis is installed. To start it, run:
```sh
sudo service redis-server start  # On Linux/macOS
redis-server  # On Windows (if installed separately)
```

### 5. Apply Migrations
```sh
python manage.py migrate
```

### 6. Run the Development Server
```sh
python manage.py runserver
```
For WebSockets to work in production, you need to run **Daphne**:
```sh
DJANGO_SETTINGS_MODULE=chatapp.settings daphne -b 0.0.0.0 -p 8080 chatapp.asgi:application
```

### 7. Access the Application
Open your browser and go to:
```
http://127.0.0.1:8000/
```


## WebSockets & Django Channels
- Django Channels handles real-time communication.
- Daphne serves as the ASGI server.
- Redis is used as a message broker for WebSocket connections.

### Checking Redis Connection
To verify Redis is running, use:
```sh
redis-cli ping
```
If it returns `PONG`, Redis is working correctly.

## Stopping Services
- Stop Redis:
```sh
sudo service redis-server stop
```
- Stop Django Server:
Press `CTRL + C`

## Troubleshooting
### Error: Daphne Not Found
If `daphne` is missing, install it manually:
```sh
pip install daphne
```
### Error: Redis Connection Refused
Ensure Redis is running:
```sh
sudo service redis-server start
```

---
Now your chat application should be up and running with Redis and Django Channels! 
