from flask import Flask, jsonify, request
import boto3
from uuid import uuid4
from datetime import datetime
from apps.controller import ImageController

app = Flask(__name__)

# dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")
# table = dynamodb.Table("Images")
image_controller = ImageController()

@app.route("/items", methods=["GET", "POST"])
def create_item():
    if request.method == "GET":
        return jsonify(image_controller.get_items())
    elif request.method == "POST":
        return jsonify(image_controller.create_item(request.get_json()))


@app.route("/items/<image_id>", methods=["GET", "PUT", "DELETE"])
def item(image_id=None):
    if request.method == "GET":
        return jsonify(image_controller.get_item(image_id))
    elif request.method == "PUT":
        return jsonify(image_controller.update_item(image_id, request.get_json()))
    elif request.method == "DELETE":
        return jsonify(image_controller.delete_item(image_id))


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
