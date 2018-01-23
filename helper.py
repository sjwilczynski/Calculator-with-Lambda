import numpy as np


def process_request(params, operation):
    if operation == 'add':
        return np.float64(params['a']) + np.float64(params['b'])
    if operation == 'subtract':
        return np.float64(params['a']) - np.float64(params['b'])
    if operation == 'multiply':
        return np.float64(params['a']) * np.float64(params['b'])
    if operation == 'divide':
        return np.float64(params['a']) / np.float64(params['b'])
    if operation == 'eval':
        return eval(params['exp'])
