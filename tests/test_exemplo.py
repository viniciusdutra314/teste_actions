import sys 
from typing import NamedTuple, TypeVar, Generic
import LabIFSC as lab
def test_simples():
    assert 1 + 1 == 2 

def test_python_311():
    T = TypeVar("T")

    class Group(NamedTuple, Generic[T]):
        key: T
        group: list[T]

    # A functional syntax is also supported
    Employee = NamedTuple('Employee', [('name', str), ('id', int)])
def test_labifsc1():
    x=lab.Medida(1,'m',1)
    assert x.nominal==1
