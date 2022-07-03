import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr
from uuid import uuid4
from datetime import datetime


class ImageController:
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")
        self.table = self.dynamodb.Table("Images")

    def create_item(self, item):
        payload = {
            "image_id": str(uuid4()),
            "email": item["email"],
            "created_at": str(datetime.now().isoformat()),
            "first_name": item["first_name"],
            "last_name": item["last_name"],
        }
        try:
            self.table.put_item(Item=payload)
            response = self.table.get_item(Key={"image_id": payload["image_id"]})
            return response["Item"]
        except ClientError as e:
            return e.response["Error"]["Message"]

    def get_item(self, image_id):
        try:
            response = self.table.get_item(Key={"image_id": image_id})
            return response["Item"]
        except ClientError as e:
            return e.response["Error"]["Message"]

    def get_items(self):
        try:
            response = self.table.scan()
            return response["Items"]
        except ClientError as e:
            return e.response["Error"]["Message"]

    def update_item(self, image_id, item):
        try:
            self.table.update_item(
                Key={"image_id": image_id},
                UpdateExpression="set email = :email, first_name = :first_name, last_name = :last_name",
                ExpressionAttributeValues={
                    ":email": item["email"],
                    ":first_name": item["first_name"],
                    ":last_name": item["last_name"],
                },
            )
            response = self.table.get_item(Key={"image_id": image_id})
            return response["Item"]
        except ClientError as e:
            return e.response["Error"]["Message"]

    def delete_item(self, image_id):
        try:
            self.table.delete_item(Key={"image_id": image_id})
            return True
        except ClientError as e:
            return e.response["Error"]["Message"]
