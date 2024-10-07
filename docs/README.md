# Blockchain Compression Project

### Overview
The **Blockchain Compression Project** is designed to optimize blockchain data storage and management by incorporating a series of advanced techniques. The project focuses on reducing the storage overhead of full blockchain nodes, while maintaining data integrity, scalability, and security. It leverages block compression, state delta management, Merkle trees, and zero-knowledge proofs (ZK-SNARKs) to efficiently manage blockchain data without compromising the reliability of the system.

---

### Features
- **Block Compression**: Compresses blockchain block data using the LZMA algorithm to minimize storage requirements.
- **State Delta Management**: Efficiently stores only the changes (deltas) in blockchain states, instead of complete snapshots, reducing unnecessary data storage.
- **Merkle Tree Construction**: Provides cryptographic assurance for data integrity by hashing transactions into a Merkle tree structure, enabling efficient verification.
- **Blockchain Pruning**: Limits the number of stored blocks, removing old, unnecessary blocks, while retaining only the most recent blocks for operational efficiency.
- **Zero-Knowledge Proofs (ZK-SNARKs)**: A conceptual framework for privacy-preserving data verification without revealing underlying data, enabling the blockchain to verify transactions without exposing sensitive information.

---

### Getting Started

#### Prerequisites
- **Python**: Version 3.6 or higher
- **Required Libraries**: While the project relies heavily on Python’s standard libraries, ensure that `pytest` is installed for development and testing purposes.

You can install the required packages by running:

```bash
pip install -r requirements.txt
```

---

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dkrizhanovskyi/blockchain_compression_project.git
   ```

2. Navigate to the project directory:
   ```bash
   cd blockchain_compression_project
   ```

3. Install the necessary dependencies:
   ```bash
   pip install .
   ```

4. To run the project using the command-line interface (CLI):
   ```bash
   blockchain-compress
   ```

---

### Usage

Once installed, you can run the project to simulate blockchain compression and management. The following components are demonstrated in the system:

1. **Block Compression**: Compresses and decompresses blockchain block data to reduce storage overhead.
2. **State Delta**: Applies transactions and tracks state changes efficiently.
3. **Merkle Tree**: Builds a Merkle tree from a list of transactions, allowing for efficient cryptographic verification of transaction data.
4. **Blockchain Pruning**: Removes outdated blocks, retaining only the most recent ones.
5. **ZK-SNARKs**: Demonstrates proof generation and verification using zero-knowledge proof concepts.

To run the system, you can execute the `main.py` file:

```bash
python src/main.py
```

---

### Example Output

After running the program, you should see outputs demonstrating various components:

```
=== Blockchain Data Compression and Management ===

--- Block Compression ---
Original block data: b'Sample blockchain block data'
Compressed block data: b'\xfd7zXZ\x00\x00\x04...'
Decompressed block data: b'Sample blockchain block data'

--- State Delta Storage ---
Current state: {'Alice': 100, 'Bob': 50}

--- Merkle Tree Verification ---
Merkle Tree root hash: 5e3229cc92783d3338f52205539346f83a73c96b208958cf7259809f393577c1

--- Blockchain Pruning ---
Blocks after pruning: [{'block_number': 2, 'data': 'Block 2 data'}, {'block_number': 3, 'data': 'Block 3 data'}]

--- ZK-SNARK Proof Generation and Verification ---
Generated proof: {'proof': 'zk-snark-proof-placeholder', 'data_hash': '3b18ffb6b8912fdef...'}
Proof verification result: True
```

---

### Development and Testing

If you want to contribute to the project or run tests, follow the steps below.

#### Running Unit Tests

We use **pytest** for testing. To run all tests, use the following command:

```bash
pytest
```

The tests ensure that each module functions correctly, covering block compression, state delta application, Merkle tree integrity, blockchain pruning, and ZK-SNARK proof verification.

---

### Contributing

We welcome contributions to the project. Please follow these steps:

1. Fork the repository.
2. Create a new feature branch.
3. Make changes and ensure all tests pass.
4. Submit a pull request with a clear description of your changes.

For more detailed guidelines, see our [CONTRIBUTING.md](CONTRIBUTING.md) file.

---

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Acknowledgments

Special thanks to the open-source community and Python developers who provided tools, libraries, and insights to support the development of this project.
