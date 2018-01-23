from helper import process_request


def test_helper_add():
    params = {'a': 10, 'b': 15}
    operation = 'add'
    assert process_request(params, operation) == 25
