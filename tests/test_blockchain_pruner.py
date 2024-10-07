# test_blockchain_pruner.py

import pytest
from src.pruning.blockchain_pruner import BlockchainPruner

def test_add_block_and_prune():
    pruner = BlockchainPruner(max_blocks=3)
    
    block_1 = {'block_number': 1, 'data': 'Block 1 data'}
    block_2 = {'block_number': 2, 'data': 'Block 2 data'}
    block_3 = {'block_number': 3, 'data': 'Block 3 data'}
    block_4 = {'block_number': 4, 'data': 'Block 4 data'}
    
    pruner.add_block(block_1)
    pruner.add_block(block_2)
    pruner.add_block(block_3)
    pruner.add_block(block_4)
    
    # Expect only the last 3 blocks to be present
    assert len(pruner.get_blocks()) == 3, "Block pruning failed"
    assert pruner.get_blocks()[0]['block_number'] == 2, "Oldest block should have been pruned"

def test_no_pruning_needed():
    pruner = BlockchainPruner(max_blocks=5)
    
    block_1 = {'block_number': 1, 'data': 'Block 1 data'}
    block_2 = {'block_number': 2, 'data': 'Block 2 data'}
    
    pruner.add_block(block_1)
    pruner.add_block(block_2)
    
    # No pruning needed, expect 2 blocks
    assert len(pruner.get_blocks()) == 2, "Pruner should not prune when block limit is not exceeded"
