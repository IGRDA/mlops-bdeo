'''
CHALLENGE: Create needed resources/files to deploy this model in production

It is not necessary to deploy anything from this code in a cloud environment (Demo or Video-demo is optional). We just
want to know how you implement every aspect we requiere and the quality of the implementation and code structure.

Imagine that you have got this model from Data Scientists and you have to deploy this model in production. What would
you implement to deploy this model? Please remind that in real world this code has to be maintainable, the model has
to pass all tests and be deployed in production automatically.

If you want to explain any aspect of your code/implementation please feel free adding descriptions in README.md

Mandatory Requirements:

1. Containerization (Docker, LXC...)
2. Unit Tests
2. CI/CD (GitLab, Github, Jenkins, Tracis...)
3. IaC (CDK, Terraform, Ansible...)
4. Documentation (At least in functional/productive code)

Optional requirements:

    - If you want, you can use python package managers such as pipenv, poetry or virtualenv
    - Suppose that the model inference call comes from backend, so you can choose either synchronous or asynchronoun communication
    - You can use a sentry-like application monitoring (Alarms in AWS Cloudwatch...)
    - Persistent data is optional, if you want to save the model events/results in a database
'''

import torch
import os
import uuid
from boto3 import resource as boto3_resource

dynamodb = boto3_resource('dynamodb')
table = dynamodb.Table("rekognitionObjectDet-{}".format(os.environ["Env"]))
ts = torch.jit.load('./doubleit_model.pt')

def lambda_handler(event, context):
    # Example or inference. This model returns a 1-dim tensor multiplied by 2
    sample_tensor = torch.tensor([1, 2, 3, 4])
    result = ts(sample_tensor)

    response = table.put_item(
        Item={"id": int(uuid.uuid4().int),
              "result":result}
    )
    print(result)  # <- tensor([2, 4, 6, 8])
