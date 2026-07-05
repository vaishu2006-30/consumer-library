from flask import Flask, request, jsonify
from calculator_master.advanced import calculate_all

app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    a, b = data["a"], data["b"]
    result = calculate_all(a, b)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)