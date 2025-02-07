from typing import Dict
from .http_unprocessable_entity import HttpUnprocessableEntityException

def handle_errors(error: Exception) -> Dict:
    if isinstance(error, (HttpUnprocessableEntityException)):
        return {
            'body': {
                'errors': [{
                    'title': error.name,
                    'detail': error.message,
                    'status_code': error.status_code,
                }]
            }
        }
    
    return {
        'body': {
            'errors': [{
                'title': 'Server error',
                'details': str(error),
                'status_code': 500
            }]
        }
    }