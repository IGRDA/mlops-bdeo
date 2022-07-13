import pytest
import json
from function import inference

@pytest.fixture()
def test_lambda_handler(event):
    ret = inference.lambda_handler()
    data = json.loads(event)
    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "hello world"