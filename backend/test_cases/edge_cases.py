"""
Edge Cases - Testing various patterns that might be tricky to detect
"""

from flask import Flask
from fastapi import FastAPI

# Multiple apps in one file
flask_app = Flask(__name__)
fastapi_app = FastAPI()


# Flask routes with unusual patterns
@flask_app.route('/path/with/many/segments')
def long_path():
    return "deep"


@flask_app.route('/path/<string:name>/<int:id>')
def path_with_params(name, id):
    return f"{name}: {id}"


@flask_app.route('/optional', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def all_methods():
    return "all"


# FastAPI routes with unusual patterns
@fastapi_app.get('/path/{param}/nested/{other}')
async def nested_params(param: str, other: int):
    return {"param": param, "other": other}


@fastapi_app.options('/cors-test')
async def cors_preflight():
    return {}


@fastapi_app.head('/head-check')
async def head_only():
    pass


# Decorated with non-route decorators (should not be detected as routes)
def some_decorator(f):
    return f


@some_decorator
def not_a_route():
    return "not a route"


# Class-based views (common in Flask)
class UserAPI:
    @flask_app.route('/class/users')
    def get_users(self):
        return []


# Lambda routes (unusual but valid)
flask_app.add_url_rule('/lambda', 'lambda_view', lambda: "lambda")


# Routes defined as variables (harder to detect)
def dynamic_route():
    return "dynamic"


# This won't be detected as easily
# flask_app.add_url_rule('/dynamic', 'dynamic', dynamic_route)


# Async Flask routes (Flask 2.0+)
@flask_app.route('/async-flask')
async def async_flask_route():
    result = await async_operation()
    return result


async def async_operation():
    return "async"


# Function with many nested calls
@flask_app.route('/complex')
def complex_handler():
    data = get_request_data()
    validated = validate_data(data)
    processed = process_data(validated)
    result = save_data(processed)
    notify_subscribers(result)
    log_operation(result)
    return format_response(result)


def get_request_data():
    return {}


def validate_data(data):
    check_required_fields(data)
    check_data_types(data)
    return data


def process_data(data):
    transform_data(data)
    enrich_data(data)
    return data


def save_data(data):
    return db_save(data)


def notify_subscribers(result):
    get_subscribers()
    send_notifications(result)


def log_operation(result):
    pass


def format_response(result):
    return result


def check_required_fields(data):
    pass


def check_data_types(data):
    pass


def transform_data(data):
    pass


def enrich_data(data):
    pass


def db_save(data):
    return data


def get_subscribers():
    return []


def send_notifications(result):
    pass


# Server starts
if __name__ == '__main__':
    flask_app.run(port=5001, debug=False)
