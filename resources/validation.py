from datetime import datetime


errors = {
    'InvalidAccount': {
        'errorCode': '...',
        'httpStatusCode': 400,
        'status': 400,
    },
    'InvalidDate': {
        'errorCode': '...',
        'httpStatusCode': 400,
        'status': 400,
    },
    'InvalidAmount': {
        'errorCode': '...',
        'httpStatusCode': 400,
        'status': 400,
    }
}


class InvalidAccount(Exception):
    pass


class InvalidDate(Exception):
    pass


class InvalidAmount(Exception):
    pass


def is_valid_account(account):
    pass  # should raise InvalidAccount


def is_valid_date(date):
    if not date:
        return
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except (ValueError, TypeError):
        raise InvalidDate


def is_valid_amount(amount):
    pass  # should raise InvalidAmount


def validate_args(args):
    is_valid_date(args.get('date'))
    is_valid_amount(args.get('amount'))