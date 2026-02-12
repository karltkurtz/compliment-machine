from http.server import BaseHTTPRequestHandler
import json
import os

STATS_FILE = '/tmp/compliment_stats.json'

def load_stats():
    """Load stats from file"""
    try:
        if os.path.exists(STATS_FILE):
            with open(STATS_FILE, 'r') as f:
                return json.load(f)
    except:
        pass
    return {'total_compliments': 0, 'golden_count': 0}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET request"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        stats = load_stats()
        self.wfile.write(json.dumps(stats).encode())
        return
