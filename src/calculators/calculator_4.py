from flask import request as FlaskRequest
from typing import Dict, List
from statistics import mean

class Calculator_4:
    def __init__(self):
        pass

    def calculate(self, request: FlaskRequest) -> Dict: #type: ignore
        body = request.json
        user_data = self.__validate_body(body)
        average = self.__calculate_average(user_data)
        server_response = self.__format_response(average)

        return server_response


    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("Body incorreto")
        
        sent_data = body['numbers']
        return sent_data
    
    def __calculate_average(self, numbers: List[float]) -> float:
        average = mean(numbers)
        return average
    
    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "result": round(calc_result, 2)
            }
        }