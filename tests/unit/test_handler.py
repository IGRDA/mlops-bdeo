import pytest
import json
import os
os.environ["Env"] = "dev"
from function  import inference


#@pytest.fixture()
def test_lambda_handler():
    ret = inference.lambda_handler("","")
    print()
    #data = json.loads()
    #assert ret["statusCode"] == 200
    #assert "message" in ret["body"]
    #assert data["message"] == "hello world"