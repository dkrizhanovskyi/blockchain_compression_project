# test_merkle_tree.py

import pytest
from src.merkle.merkle_tree import MerkleTree

def test_merkle_tree_construction():
    transactions = ["tx1", "tx2", "tx3", "tx4"]
    merkle_tree = MerkleTree(transactions)

    root_hash = merkle_tree.get_root()
    assert root_hash is not None, "Merkle tree root hash should not be None"

def test_merkle_tree_root_hash():
    transactions = ["tx1", "tx2", "tx3", "tx4"]
    merkle_tree = MerkleTree(transactions)

    # Calculate the expected root hash step by step
    hash_tx1 = merkle_tree.hash_data("tx1")
    hash_tx2 = merkle_tree.hash_data("tx2")
    hash_tx3 = merkle_tree.hash_data("tx3")
    hash_tx4 = merkle_tree.hash_data("tx4")

    # Level 1 (leaf nodes)
    hash_12 = merkle_tree.hash_data(hash_tx1 + hash_tx2)
    hash_34 = merkle_tree.hash_data(hash_tx3 + hash_tx4)

    # Level 2 (root node)
    expected_root_hash = merkle_tree.hash_data(hash_12 + hash_34)
    
    assert merkle_tree.get_root() == expected_root_hash, "Merkle tree root hash is incorrect"