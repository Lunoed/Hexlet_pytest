import pytest


def test_stak_with_pop():
    stack = []
    stack.append('one')
    stack.append('two')
    assert stack.pop() == 'two'
    assert stack.pop() == 'one'


def test_pop_with_empty_stack():
    stack = []
    assert not stack
    with pytest.raises(IndexError):
        stack.pop()
