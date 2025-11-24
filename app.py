from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/collect', methods=['POST'])
def collect():
    print("Data received:", request.json)  # visible in Gunicorn logs
    return jsonify({"status": "ok"})
