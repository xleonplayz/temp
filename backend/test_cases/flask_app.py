"""
Flask Test Application - Various Route Patterns
"""

from flask import Flask, request, jsonify

app = Flask(__name__)


# Basic GET route
@app.route('/')
def index():
    return "Hello World"


# Route with methods parameter
@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return get_all_users()
    else:
        return create_user()


# Multiple HTTP methods as separate routes
@app.get('/items')
def get_items():
    return fetch_items_from_db()


@app.post('/items')
def create_item():
    data = request.json
    return save_item(data)


@app.put('/items/<int:item_id>')
def update_item(item_id):
    data = request.json
    return update_item_in_db(item_id, data)


@app.delete('/items/<int:item_id>')
def delete_item(item_id):
    return remove_item(item_id)


# Route with multiple decorators
@app.route('/admin/dashboard')
def admin_dashboard():
    check_admin_access()
    return render_dashboard()


# Blueprint-style routes (common pattern)
from flask import Blueprint

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')


@api_bp.route('/health')
def health_check():
    return {"status": "healthy"}


@api_bp.route('/products', methods=['GET'])
def get_products():
    return fetch_products()


# Nested function calls
def get_all_users():
    users = db_query("SELECT * FROM users")
    return jsonify(users)


def create_user():
    data = request.json
    validate_user_data(data)
    user = insert_user(data)
    send_welcome_email(user['email'])
    return jsonify(user)


def fetch_items_from_db():
    return db_query("SELECT * FROM items")


def save_item(data):
    return db_insert("items", data)


def update_item_in_db(item_id, data):
    return db_update("items", item_id, data)


def remove_item(item_id):
    return db_delete("items", item_id)


def check_admin_access():
    pass


def render_dashboard():
    return "Dashboard"


def fetch_products():
    return []


def db_query(sql):
    pass


def db_insert(table, data):
    pass


def db_update(table, id, data):
    pass


def db_delete(table, id):
    pass


def validate_user_data(data):
    pass


def insert_user(data):
    return data


def send_welcome_email(email):
    pass


# Server start
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
