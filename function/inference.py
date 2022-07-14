import os
import torch
import uuid

from boto3 import resource as boto3_resource

if os.environ.get("Env") is None:
    os.environ["Env"] = "dev"

dynamodb = boto3_resource('dynamodb', "eu-west-3")
table = dynamodb.Table("rekognitionObjectDet-{}".format(os.environ["Env"]))
ts = torch.jit.load('function/doubleit_model.pt')


def lambda_handler(event, context):
    print(event)
    # Example or inference. This model returns a 1-dim tensor multiplied by 2
    sample_tensor = torch.tensor([1, 2, 3, 4])
    result = ts(sample_tensor)
    print(round(uuid.uuid4().int, 10))
    """
        response = table.put_item(
            Item={"id": int,
                "result": result.tolist()}
    )"""
    print(result)  # <- tensor([2, 4, 6, 8])
