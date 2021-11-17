import json
import subprocess

from flask import Flask, jsonify, request
from typing import Any, List

# Instantiating Flask object
app = Flask(__name__)


@app.route('/')
def index():
    send = {
      "status": "OK"
    }
    return jsonify(send)


@app.route('/certigo')
def certigo_util():
    send = {
      "status": "OK",
      "certificates": "a domain was not provided",
    }
    domain = request.args['domain']
    if domain is not None:
        result = parse_certificate(domain)
    if result != 'fail':
        send = {
          "status": "OK",
          "certificates": result,
        }
    return jsonify(send)


def parse_certificate(domain: str) -> List[Any]:
    result = subprocess.run(
      ["certigo", "connect", domain, "-j"],
      capture_output=True
    )
    certigo_result: List[Any] = json.loads(
      result.stdout.decode('utf-8'))['certificates']
    if result.returncode != 0 or len(certigo_result) == 0:
        return "fail"
    data = certigo_result
    return data
