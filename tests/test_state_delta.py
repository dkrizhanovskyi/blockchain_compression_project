# test_state_delta.py

import pytest
from src.compression.state_delta import StateDelta

def test_apply_transaction():
    state_delta = StateDelta()
    transaction_1 = {'account': 'Alice', 'amount': 100}
    transaction_2 = {'account': 'Bob', 'amount': 50}

    delta_1 = state_delta.apply_transaction(transaction_1)
    assert delta_1 == {'Alice': 100}, "Delta for Alice's transaction is incorrect"
    
    delta_2 = state_delta.apply_transaction(transaction_2)
    assert delta_2 == {'Bob': 50}, "Delta for Bob's transaction is incorrect"

def test_get_current_state():
    state_delta = StateDelta()
    transaction_1 = {'account': 'Alice', 'amount': 100}
    transaction_2 = {'account': 'Bob', 'amount': 50}

    state_delta.apply_transaction(transaction_1)
    state_delta.apply_transaction(transaction_2)
    
    current_state = state_delta.get_current_state()
    assert current_state == {'Alice': 100, 'Bob': 50}, "Current state is incorrect"
