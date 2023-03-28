#!/usr/bin/python

import time, logging
from flask import Flask
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
app = Flask(__name__)

START = time.time()

def elapsed():
    running = time.time() - START
    minutes, seconds = divmod(running, 60)
    hours, minutes = divmod(minutes, 60)
    logger.debug("DEBUG TOKEN SWORDFISH %s", seconds)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

@app.route('/')
def root():
    return "DEBUG Top-Security Information needed is here: (up %s)\n" % elapsed()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

