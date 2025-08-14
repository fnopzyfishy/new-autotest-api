from typing import Any

def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.
    :param actual:
    :param expected:
    :return:
    """
    assert actual == expected, (
        f'Incorrect response status code. '
        f'Expected status code: {expected}. '
        f'Actual status code: {actual}'
    )

def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param actual:
    :param expected:
    :param name:
    :return:
    """
    assert actual == expected, (
        f'Incorrect value: "{name}". '
        f'Expected value: {expected}. '
        f'Actual value: {actual}'
    )

def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.
    :param actual:
    :return:
    """
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )