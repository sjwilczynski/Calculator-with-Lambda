def process_request(params, operation):
    if operation == 'add':
        return int(params['a']) + int(params['b'])
    if operation == 'subtract':
        return int(params['a']) - int(params['b'])
    if operation == 'multiply':
        return int(params['a']) * int(params['b'])
    if operation == 'divide':
        return float(params['a']) / float(params['b'])
    if operation == 'eval':
        return eval(params['exp'])
