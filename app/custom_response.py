import json
from typing import Any, List


class CustomResponse:
    """
    The class responsible for preparing the appropriate JSON response
    """

    # do not bubble error messages to user if debug is false
    debug: bool = False
    # generic message which is not particularly an error
    message: str = None
    # the certificate data
    certificate_data: List[Any] = None
    # the error message
    error_message: str = None

    def __init__(self, message: str = None) -> None:
        self.status = "OK"
        self.message = message

    def set_certificate_data(self, certificate_data: List[Any]) -> None:
        self.certificate_data = certificate_data

    def set_error_message(self, error_message: str) -> None:
        if self.debug is True:
            self.error_message = error_message
        else:
            self.error_message = "Please provide a valid URL"

    def get_json(self) -> str:
        response = {}
        response["status"] = self.status
        if self.message is not None and len(self.message) > 0:
            response["message"] = self.message
        elif self.error_message is not None and len(self.error_message) > 0:
            response["error"] = self.error_message
        elif self.certificate_data is not None and len(self.certificate_data) > 0:
            response["certificate data"] = self.certificate_data
        return json.dumps(response)
