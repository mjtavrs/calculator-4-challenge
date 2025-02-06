from .calculator_4 import Calculator_4
from typing import Dict
from pytest import raises

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body = {"numbers": [2, 2]})
    calculator = Calculator_4()

    response = calculator.calculate(mock_request)

    assert "data" in response
    assert "result" in response['data']

    assert response['data']['result'] == 2

def test_calculate_with_body_error():
    # This test is supposed to fail because of the wrong key below
    mock_request = MockRequest(body = {"wrong_key": [2, 2]})
    calculator = Calculator_4()

    with raises(Exception) as excinfo:
        calculator.calculate(mock_request)

    assert str(excinfo.value) == "Body incorreto"