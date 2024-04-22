import pytest
from tree import Tree
from node import Node

@pytest.fixture
def my_tree():
    tree = Tree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(3)

    return tree

def test_find_existing(my_tree):

    # Test finding existing nodes
    assert my_tree.find(10) != None
    assert my_tree.find(5) != None
    assert my_tree.find(15) != None
    assert my_tree.find(3) != None
 
    # Test finding non-existing nodes
    

def test_find_nonexisting(my_tree):
    assert my_tree.find(20) == None
    assert my_tree.find(1) == None