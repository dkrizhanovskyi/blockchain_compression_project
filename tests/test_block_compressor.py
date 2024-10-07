# test_block_compressor.py

import pytest
from src.compression.block_compressor import BlockCompressor

def test_block_compression():
    compressor = BlockCompressor()
    block_data = b"This is some raw blockchain block data"
    
    compressed_data = compressor.compress_block(block_data)
    decompressed_data = compressor.decompress_block(compressed_data)
    
    assert decompressed_data == block_data, "Decompressed data does not match the original block data"

def test_empty_block_compression():
    compressor = BlockCompressor()
    block_data = b""
    
    compressed_data = compressor.compress_block(block_data)
    decompressed_data = compressor.decompress_block(compressed_data)
    
    assert decompressed_data == block_data, "Decompressed empty data does not match the original empty block data"
