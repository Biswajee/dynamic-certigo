import json
import re
import subprocess
from json.decoder import JSONDecodeError
from typing import Any, List

from app.custom_response import CustomResponse


class DomainParser:
    """
    A custom class that represents a domain, checks if it is
    valid and parses the SSL certificate
    """

    def __init__(self, domain_name: str):
        self.domain_name = domain_name

    def is_url_valid(self, url_string: str) -> bool:
        """
        Checks if the user input to the request parameter
        does not pwn the application
        """
        regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"
        pattern = re.compile(regex)
        if pattern.match(url_string):
            return True
        return False

    def parse_certificate(self, domain: str) -> CustomResponse:
        response = CustomResponse()

        if not self.is_url_valid(domain):
            response.set_error_message(f"{domain} is an invalid URL")
            return response

        try:
            result = subprocess.run(
                ["certigo", "connect", domain, "-j"], capture_output=True
            )
            certigo_result: List[Any] = json.loads(result.stdout.decode("utf-8"))[
                "certificates"
            ]

            if result.returncode != 0 or len(certigo_result) == 0:
                response.set_error_message("An error occured")
            else:
                response.set_certificate_data(certigo_result)

        except (FileNotFoundError, JSONDecodeError) as err:
            self.set_error_message(err)

        finally:
            return response
