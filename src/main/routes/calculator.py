from flask import Blueprint, jsonify, request
from src.calculators.calculator_4 import Calculator_4

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route('/calculator/4', methods=['POST'])
def calculator_4():
    calc = Calculator_4()
    response = calc.calculate(request)

    return jsonify(response)
