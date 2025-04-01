from flask import Flask, request, jsonify
import numpy as np
import base64
import uuid

app = Flask(__name__)


# By default, a route only answers to GET requests
@app.route('/')
def basics():
    return "<p>Flask quickstart</p>"


# return data as JSON
@app.route('/json_get', methods=['GET'])
def json_get():
    x = np.array([[1, 2],
                  [3, 4]])
    y = np.array([[5, 6],
                  [7, 8]])
    test_data = {"x": x.tolist(), "y": y.tolist()}

    return jsonify(test_data)


# Accept incoming data as JSON
@app.route('/json_post', methods=['POST'])
def json_post():
    data = request.get_json()

    return f"{data}"


# Accept incoming data as JSON abd return JSON data
@app.route('/json_get_post', methods=['GET', 'POST'])
def json_get_post():
    data = request.get_json()
    x = data["x"]
    y = data["y"]
    z = np.matmul(x, y)
    return jsonify(z.tolist())


# Accept incoming data as JSON
@app.route('/image_post', methods=['POST'])
def image_post():
    data = request.get_json()
    image_data = base64.b64decode(data["image"])

    file_name = str(uuid.uuid4()) + ".jpg"
    with open(file_name, "wb") as file:
        file.write(image_data)
    return f"{data}"
    # return ""


if __name__ == '__main__':
    app.run()
