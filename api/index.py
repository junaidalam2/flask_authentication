import os
import sys
from asgiref.wsgi import WsgiToAsgi

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now we can import from the project package
from backend.project import create_app

# Create the Flask app using your factory
wsgi_app = create_app()

# Convert WSGI app to ASGI for Vercel's Python runtime
app = WsgiToAsgi(wsgi_app)