import sys 
from typing import NamedTuple, TypeVar, Generic

def test_simples():
    assert 1 + 1 == 2 

def test_python_311():
    T = TypeVar("T")

    class Group(NamedTuple, Generic[T]):
        key: T
        group: list[T]

    # A functional syntax is also supported
    Employee = NamedTuple('Employee', [('name', str), ('id', int)])