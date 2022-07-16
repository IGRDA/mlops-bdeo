import pytest
from function  import inference
import json


@pytest.mark.parametrize(
    "test_input,expected", 
    [(json.load(open('events/event0.json')),  [0,0,0,0,0]),
     (json.load(open('events/event1.json')),  [2,2,2,2,2]), 
     (json.load(open('events/event.json')),   [2,4,6,8,10])])
def test_lambda_handler(test_input, expected):
    assert  inference.lambda_handler(test_input,"") == expected

