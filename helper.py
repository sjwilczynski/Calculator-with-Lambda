def process_request(params, operation):
    if operation == 'add':
        return params['a'] + params['b']