# **API Documentation**

This document provides detailed information on the various modules, classes, and functions in the **Blockchain Compression Project**. Each section explains the purpose, input parameters, and return values of each function, along with examples of how to use them.

---

## **Table of Contents**

1. [Compression Module](#compression-module)
    - [BlockCompressor](#blockcompressor)
2. [State Delta Module](#state-delta-module)
    - [StateDelta](#statedelta)
3. [Merkle Tree Module](#merkle-tree-module)
    - [MerkleTree](#merkletree)
4. [Blockchain Pruner Module](#blockchain-pruner-module)
    - [BlockchainPruner](#blockchainpruner)
5. [ZK-SNARK Module](#zk-snark-module)
    - [ZKSnark](#zksnark)

---

## Compression Module

### **BlockCompressor**

The `BlockCompressor` class provides functionality to compress and decompress blockchain block data using the LZMA algorithm.

#### **Methods:**

##### `compress_block(self, block_data: bytes) -> bytes`
- **Description**: Compresses the raw blockchain block data using the LZMA algorithm.
- **Parameters**: 
  - `block_data` (bytes): The raw data of the blockchain block to be compressed.
- **Returns**: 
  - Compressed block data (bytes).
- **Example**:
  ```python
  compressor = BlockCompressor()
  compressed_data = compressor.compress_block(b"Sample blockchain block data")
  ```

##### `decompress_block(self, compressed_block_data: bytes) -> bytes`
- **Description**: Decompresses the compressed blockchain block data back to its original form.
- **Parameters**: 
  - `compressed_block_data` (bytes): The compressed block data.
- **Returns**: 
  - Decompressed block data (bytes).
- **Example**:
  ```python
  decompressed_data = compressor.decompress_block(compressed_data)
  ```

---

## State Delta Module

### **StateDelta**

The `StateDelta` class handles the storage and management of state changes (deltas) in the blockchain. Instead of storing the full state, it keeps only the changes applied by each transaction.

#### **Methods:**

##### `apply_transaction(self, transaction: dict) -> dict`
- **Description**: Applies a transaction to the blockchain state and stores only the delta (difference).
- **Parameters**: 
  - `transaction` (dict): A dictionary representing the transaction to apply. Must contain the keys:
    - `account`: The account to update.
    - `amount`: The change to apply to the account.
- **Returns**: 
  - A dictionary representing the delta (difference) applied to the state.
- **Example**:
  ```python
  state_delta = StateDelta()
  delta = state_delta.apply_transaction({'account': 'Alice', 'amount': 100})
  ```

##### `get_current_state(self) -> dict`
- **Description**: Returns the current full state of the blockchain.
- **Parameters**: 
  - None.
- **Returns**: 
  - A dictionary representing the current state of the blockchain.
- **Example**:
  ```python
  current_state = state_delta.get_current_state()
  ```

---

## Merkle Tree Module

### **MerkleTree**

The `MerkleTree` class is responsible for constructing a Merkle tree from a list of transactions and providing the root hash for verifying the integrity of those transactions.

#### **Methods:**

##### `__init__(self, transactions: list)`
- **Description**: Initializes a Merkle tree from a list of transactions.
- **Parameters**: 
  - `transactions` (list): A list of transaction strings.
- **Example**:
  ```python
  merkle_tree = MerkleTree(["tx1", "tx2", "tx3", "tx4"])
  ```

##### `get_root(self) -> str`
- **Description**: Returns the root hash of the Merkle tree.
- **Parameters**: 
  - None.
- **Returns**: 
  - The root hash as a string.
- **Example**:
  ```python
  root_hash = merkle_tree.get_root()
  ```

##### `hash_data(self, data: str) -> str`
- **Description**: Returns the SHA-256 hash of the given data.
- **Parameters**: 
  - `data` (str): The data to hash.
- **Returns**: 
  - A string representing the SHA-256 hash of the input data.
- **Example**:
  ```python
  hashed_data = merkle_tree.hash_data("tx1")
  ```

---

## Blockchain Pruner Module

### **BlockchainPruner**

The `BlockchainPruner` class manages the pruning (removal) of old blocks in the blockchain to reduce storage space. It ensures that only a specified number of recent blocks are retained.

#### **Methods:**

##### `__init__(self, max_blocks: int)`
- **Description**: Initializes the pruner with a maximum number of blocks to retain.
- **Parameters**: 
  - `max_blocks` (int): The maximum number of recent blocks to retain.
- **Example**:
  ```python
  pruner = BlockchainPruner(max_blocks=10)
  ```

##### `add_block(self, block: dict)`
- **Description**: Adds a new block to the blockchain and prunes old blocks if necessary.
- **Parameters**: 
  - `block` (dict): A dictionary representing a blockchain block. 
- **Example**:
  ```python
  block = {'block_number': 1, 'data': 'Block data'}
  pruner.add_block(block)
  ```

##### `get_blocks(self) -> list`
- **Description**: Returns the current list of blocks stored in the blockchain after pruning.
- **Parameters**: 
  - None.
- **Returns**: 
  - A list of dictionaries representing the retained blocks.
- **Example**:
  ```python
  blocks = pruner.get_blocks()
  ```

---

## ZK-SNARK Module

### **ZKSnark**

The `ZKSnark` class is a placeholder for implementing Zero-Knowledge Succinct Non-Interactive Arguments of Knowledge (ZK-SNARKs) for blockchain data verification.

#### **Methods:**

##### `generate_proof(self, data: dict) -> dict`
- **Description**: Generates a zero-knowledge proof for the given blockchain data. This is a placeholder and not a full ZK-SNARK implementation.
- **Parameters**: 
  - `data` (dict): A dictionary representing the blockchain data.
- **Returns**: 
  - A dictionary representing the generated proof.
- **Example**:
  ```python
  zk = ZKSnark()
  proof = zk.generate_proof({"account": "Alice", "balance": 100})
  ```

##### `verify_proof(self, proof: dict, data: dict) -> bool`
- **Description**: Verifies the given zero-knowledge proof against the provided blockchain data.
- **Parameters**: 
  - `proof` (dict): A dictionary representing the zero-knowledge proof.
  - `data` (dict): A dictionary representing the blockchain data to verify against.
- **Returns**: 
  - `True` if the proof is valid, `False` otherwise.
- **Example**:
  ```python
  is_valid = zk.verify_proof(proof, {"account": "Alice", "balance": 100})
  ```

##### `hash_data(self, data: str) -> str`
- **Description**: A placeholder for a cryptographic hash function used to create a proof. Returns the SHA-256 hash of the data.
- **Parameters**: 
  - `data` (str): The data to be hashed.
- **Returns**: 
  - A string representing the SHA-256 hash of the input data.
- **Example**:
  ```python
  hashed_data = zk.hash_data("sample data")
  ```
