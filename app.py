from flask import Flask, jsonify

app = Flask(_name_)
employee_count = 20  # Simulated value

@app.route('/')
def home():
    return jsonify({"employee_count": employee_count})

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)