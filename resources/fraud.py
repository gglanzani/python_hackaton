import json

from resource import SimpleResource
from validation import is_valid_account

dummy_response = """
...
"""


class Fraud(SimpleResource):
    def query(self, args):
        return json.loads(dummy_response)

    def validate_account(self, account):
        return is_valid_account(account)
