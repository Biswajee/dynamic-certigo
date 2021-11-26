import re
import json
import subprocess
from typing import Any, List

from flask import Flask, jsonify, request
from json.decoder import JSONDecodeError

# Instantiating Flask object
app = Flask(__name__)


@app.route("/")
def index():
    send = {"status": "OK"}
    return jsonify(send)


@app.route("/certigo")
def certigo_util():
    try:
        send = {
            "status": "OK",
            "certificates": "a domain was not provided",
        }
        domain = request.args["domain"]
        result = sanitize_input(domain)
        if domain is not None and result is True:
            result = parse_certificate(domain)
        if result != "fail":
            send = {
                "status": "OK",
                "certificates": result,
            }
        return jsonify(send)
    except (JSONDecodeError, URLValidationError):
        send = {
            "status": "OK",
            "message": "Please ensure that the url is correct",
        }
        return jsonify(send)


def parse_certificate(domain: str) -> List[Any]:
    try:
        result = subprocess.run(
            ["certigo", "connect", domain, "-j"], capture_output=True
        )
        certigo_result: List[Any] = json.loads(result.stdout.decode("utf-8"))[
            "certificates"
        ]
        if result.returncode != 0 or len(certigo_result) == 0:
            return "fail"
        data = certigo_result
        return data
    except FileNotFoundError:
        return [{"message": "Something went wrong and we're investigating the cause"}]


def sanitize_input(url_string: str) -> bool:
    """
    Checks if the user input to the request parameter does not pwn the application
    """
    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"
    pattern = re.compile(regex)
    if pattern.match(url_string):
        return True
    raise URLValidationError()


class URLValidationError(Exception):
    """
    URLValidationError error is raised when the supplied url does not match a domain pattern
    """
    def __init__(self):
        pass
