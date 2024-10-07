# test_zk_proofs.py

import pytest
from src.zk_snark.zk_proofs import ZKSnark

def test_generate_proof():
    zk = ZKSnark()
    data = {"transaction": "tx1", "amount": 100}
    
    proof = zk.generate_proof(data)
    assert "proof" in proof, "Proof was not generated"
    assert proof["proof"] == "zk-snark-proof-placeholder", "Incorrect proof format"

def test_verify_proof():
    zk = ZKSnark()
    data = {"transaction": "tx1", "amount": 100}
    
    proof = zk.generate_proof(data)
    valid = zk.verify_proof(proof, data)
    
    assert valid, "Proof verification failed"
