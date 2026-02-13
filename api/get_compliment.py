import json
import random

COMPLIMENTS = {
    "motivational": [
        "You're capable of amazing things!",
        "Today is your day to shine",
        "You're stronger than you know",
        "Your potential is limitless",
        "You're making progress every day",
        "Believe in yourself - we do!",
        "You've got this!",
        "Your future is bright",
        "You're doing better than you think",
        "Keep going, you're almost there",
    ],
    "affirming": [
        "You are enough, just as you are",
        "You deserve good things",
        "You matter more than you know",
        "You're exactly where you need to be",
        "Your presence makes a difference",
        "You are worthy of love and respect",
        "You're more resilient than you realize",
        "Your journey is valuable",
        "You bring light to the world",
        "Someone is proud of you right now",
    ],
    "silly": [
        "You're cooler than the other side of the pillow",
        "You're the human equivalent of a high-five",
        "Your smile could power a small city",
        "You're more fun than a ball pit",
        "Even your typos are endearing",
    ],
    "deep": [
        "Your story isn't over yet",
        "The universe conspired to create you",
        "You're writing your own legend",
        "Your kindness creates ripples in time",
        "You're part of something greater",
        "Every breath you take is a victory",
    ],
    "golden": [
        "✨ GOLDEN COMPLIMENT ✨\nYou are extraordinary in ways words can barely capture",
        "✨ GOLDEN COMPLIMENT ✨\nYour existence is a gift to those around you",
        "✨ GOLDEN COMPLIMENT ✨\nYou have infinite worth simply by being you",
        "✨ GOLDEN COMPLIMENT ✨\nThe universe smiled when you were born",
    ],
}

# NOTE: this counter will NOT persist reliably across serverless invocations.
# It's fine for now, but don't expect global stats accuracy.
_counter = {"total": 0, "golden": 0}


def handler(request):
    global _counter

    # 1% chance of golden
    if random.random() < 0.01:
        category = "golden"
        _counter["golden"] += 1
    else:
        categories = ["motivational"] * 4 + ["affirming"] * 3 + ["silly"] * 2 + ["deep"] * 1
        category = random.choice(categories)

    text = random.choice(COMPLIMENTS[category])
    _counter["total"] += 1

    body = {
        "text": text,
        "category": category,
        "number": _counter["total"],
        "is_golden": category == "golden",
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Cache-Control": "no-store",
        },
        "body": json.dumps(body),
    }
