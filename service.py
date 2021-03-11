"""
"""

import os
import random
import flask
from gevent import pywsgi

MOD_PATH, _ = os.path.split(os.path.abspath(__file__))
_, MOD_NAME = os.path.split(MOD_PATH)
APP = flask.Flask(MOD_NAME)
SERVICE_HOST = os.getenv("SERVICE_HOST", "0.0.0.0")
SERVICE_PORT = int(os.getenv("SERVICE_PORT", "80"))

@APP.route("/")
def index():
    """
    """
    return b"%f" % random.random(), 200, {"Content-Type": "text/plain; charset=utf-8"}

def main():
    """
    """
    print("Starting service %s on %s:%u..." % (MOD_NAME, SERVICE_HOST, SERVICE_PORT))
    pywsgi.WSGIServer((SERVICE_HOST, SERVICE_PORT), APP).serve_forever()

if __name__ == "__main__":
    main()
