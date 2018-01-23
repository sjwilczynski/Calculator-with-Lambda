from helper import process_request


def test_helper_add():
    params = {'a': 10, 'b': 15}
    operation = 'add'
    assert process_request(params, operation) == 25


def test_helper_subtract():
    operation = 'subtract'
    params = {'a': 20, 'b': 15}
    assert process_request(params, operation) == 5


def test_helper_multiply():
    operation = 'multiply'
    params = {'a': 4, 'b': 6}
    assert process_request(params, operation) == 24


def test_helper_divide():
    operation = 'divide'
    params = {'a': 5, 'b': 4}
    assert process_request(params, operation) == 1.25


def test_helper_eval():
    operation = 'eval'
    params = {'exp': '2**11'}
    assert process_request(params, operation) == 2048
