def process_request(params, operation):
    if operation == 'add':
        return params['a'] + params['b']
    if operation == 'subtract':
        return params['a'] - params['b']