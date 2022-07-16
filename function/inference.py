import os
import uuid
import boto3
import torch


if os.environ.get("Env") is None:
    os.environ["Env"] = "dev"

dynamodb = boto3.resource('dynamodb', "eu-west-3")
table = dynamodb.Table("results-{}".format(os.environ["Env"]))
ts = torch.jit.load('function/doubleit_model.pt')


def lambda_handler(event, context):
    
    # Example or inference. This model returns a 1-dim tensor multiplied by 2
    sample_tensor = torch.tensor(eval(event["Records"][0]["body"]))

    result = ts(sample_tensor) # <- tensor([2, 4, 6, 8])

    table.put_item(
                     Item={"id": int(str(uuid.uuid4().int)[:-1]),
                           "result": str(result.tolist())}
                   )

    return result.tolist()

#