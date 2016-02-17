from flask_restful import reqparse

parser = reqparse.RequestParser()

parser.add_argument(
    'date',
    location='args',
    required=True,
    type=str
)

parser.add_argument(
    'amount',
    location='args',
    required=True,
    type=float
)


def get_basis_parser():
    return parser