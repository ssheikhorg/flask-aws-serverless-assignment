import boto3


def create_images_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            "dynamodb",
            region_name="ap-south-1",
        )

    table = dynamodb.create_table(
        TableName="Images",
        KeySchema=[
            {"AttributeName": "image_id", "KeyType": "HASH"},
        ],
        AttributeDefinitions=[
            {"AttributeName": "image_id", "AttributeType": "S"},
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
    )
    table.wait_until_exists()
    return table


if __name__ == "__main__":
    table = create_images_table()
    print(f"Table {table.name} created.")


# from dotenv import load_dotenv, find_dotenv
# from os import getenv

# load_dotenv(find_dotenv())

    # aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
    # aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"),