from asgiref.wsgi import WsgiToAsgi
from project import create_app

# Create the Flask app using your factory
wsgi_app = create_app()

# Convert WSGI app to ASGI for Vercel's Python runtime
app = WsgiToAsgi(wsgi_app)