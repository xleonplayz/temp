from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        'message': 'Flask Backend API',
        'status': 'running'
    })

@app.route('/api/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'World')
    return jsonify({
        'message': f'Hello, {name}!'
    })

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({
        'received': data,
        'status': 'success'
    }), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
