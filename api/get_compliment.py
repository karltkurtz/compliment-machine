from http.server import BaseHTTPRequestHandler
import json
import random
from datetime import datetime
import os

# Compliment database
COMPLIMENTS = {
    'motivational': [
        "You're capable of amazing things!",
        "Today is your day to shine",
        "You're stronger than you know",
        "Your potential is limitless",
        "You're making progress every day",
        "Believe in yourself - we do!",
        "You've got this!",
        "Your future is bright",
        "You're doing better than you think",
        "Keep going, you're almost there"
    ],
    'affirming': [
        "You are enough, just as you are",
        "You deserve good things",
        "You matter more than you know",
        "You're exactly where you need to be",
        "Your presence makes a difference",
        "You are worthy of love and respect",
        "You're more resilient than you realize",
        "Your journey is valuable",
        "You bring light to the world",
        "Someone is proud of you right now"
    ],
    'silly': [
        "You're cooler than the other side of the pillow",
        "You're the reason the gene pool needs a lifeguard",
        "If you were a vegetable, you'd be a cute-cumber",
        "You're so awesome, you make onions cry",
        "You're the human equivalent of a high-five",
        "Your smile could power a small city",
        "You're like a software update - whenever I see you, I think 'not now'... just kidding, you're perfect!",
        "You're the reason bubble wrap was invented",
        "You're more fun than a ball pit",
        "Even your typos are endearing"
    ],
    'deep': [
        "Your story isn't over yet",
        "The universe conspired to create you",
        "You're writing your own legend",
        "Your kindness creates ripples in time",
        "You're part of something greater",
        "Every breath you take is a victory",
        "You're a unique expression of existence",
        "Your struggles are shaping your strength",
        "You're exactly who you're meant to be",
        "The world is better with you in it"
    ],
    'golden': [
        "✨ GOLDEN COMPLIMENT ✨\nYou are extraordinary in ways words can barely capture",
        "✨ GOLDEN COMPLIMENT ✨\nYour existence is a gift to those around you",
        "✨ GOLDEN COMPLIMENT ✨\nYou have infinite worth simply by being you",
        "✨ GOLDEN COMPLIMENT ✨\nThe universe smiled when you were born"
    ]
}

# Simple file-based storage for Vercel
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

def save_stats(stats):
    """Save stats to file"""
    try:
        with open(STATS_FILE, 'w') as f:
            json.dump(stats, f)
    except:
        pass

def get_random_compliment():
    """Get a random compliment"""
    stats = load_stats()
    
    # 1% chance of golden
    if random.random() < 0.01:
        category = 'golden'
        stats['golden_count'] += 1
    else:
        categories = ['motivational'] * 4 + ['affirming'] * 3 + ['silly'] * 2 + ['deep'] * 1
        category = random.choice(categories)
    
    compliment = random.choice(COMPLIMENTS[category])
    stats['total_compliments'] += 1
    save_stats(stats)
    
    return {
        'text': compliment,
        'category': category,
        'number': stats['total_compliments'],
        'is_golden': category == 'golden'
    }

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET request"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        compliment = get_random_compliment()
        self.wfile.write(json.dumps(compliment).encode())
        return
