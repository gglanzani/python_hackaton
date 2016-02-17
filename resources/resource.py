from flask_restful import Resource

from parser import get_basis_parser
from validation import validate_args


class SimpleResource(Resource):
    def get(self, account):
        parser = self.get_parser()
        args = parser.parse_args()
        self.validate_account(account)
        self.validate_args(args)
        response = self.query(args)
        return response

    def query(self, args):
        pass

    def get_parser(self):
        return get_basis_parser()

    def validate_args(self, args):
        validate_args(args)

    def validate_account(self, idf):
        pass
