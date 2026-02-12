from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Read the HTML file
def get_html(filename):
    """Read HTML file from public directory"""
    file_path = os.path.join(os.path.dirname(__file__), '..', 'public', filename)
    with open(file_path, 'r') as f:
        return f.read()

@app.route('/')
def index():
    """Serve the main page"""
    return render_template_string(get_html('index.html'))

# Export for Vercel
def handler(request):
    """Vercel serverless handler"""
    with app.request_context(request.environ):
        return app.full_dispatch_request()
