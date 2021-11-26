from flask import Flask, request

from app.custom_response import CustomResponse
from app.domain_parser import DomainParser

# Instantiating Flask object
app = Flask(__name__)


@app.route("/")
def index() -> str:
    domain = request.args.get("domain", default=None)
    if domain is None:
        return CustomResponse("A domain was not provided").get_json()
    else:
        return DomainParser(domain).parse_certificate(domain).get_json()


@app.route("/health")
def health() -> str:
    return CustomResponse().get_json()
