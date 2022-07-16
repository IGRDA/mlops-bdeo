import pytest
import os
from function  import inference
#import json


#@pytest.fixture()
def test_lambda_handler():
    ret = inference.lambda_handler("","")
    #data = json.loads()
    #assert ret["statusCode"] == 200
    #assert "message" in ret["body"]
    #assert data["message"] == "hello world"


@pytest.mark.parametrize(
    "test_input,expected", 
    [("3+5", 8),
     ("2+4", 6), 
     ("6*9", 42)])
def test_lambda_handler(test_input, expected):
    assert eval(test_input) == expected
