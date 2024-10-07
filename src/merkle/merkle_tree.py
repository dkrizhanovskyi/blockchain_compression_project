# merkle_tree.py

"""
Module: MerkleTree
Purpose:
    The `MerkleTree` module is responsible for constructing and verifying Merkle trees, which are 
    fundamental in blockchain systems for ensuring data integrity and efficient verification. 
    In a blockchain, a Merkle tree is used to verify that a set of transactions has not been tampered 
    with by calculating a single root hash based on all transaction data.

    The key feature of Merkle trees is that even if only a small subset of data (transactions) needs 
    to be verified, the entire data structure doesn't need to be exposed. This allows blockchain nodes 
    to confirm the inclusion of specific transactions efficiently and securely.

    Key Features:
    - Builds a Merkle tree from a list of transactions.
    - Provides the root hash of the Merkle tree, which serves as a cryptographic commitment to the entire set of transactions.
    - Efficient and secure hashing using the SHA-256 algorithm to ensure cryptographic integrity.

    Cryptographic Considerations:
    The Merkle tree structure relies on the cryptographic properties of SHA-256, which ensures that the 
    root hash reflects the entirety of the data without exposing individual transactions. Any alteration 
    to the data will result in a completely different root hash, making the Merkle tree a robust method 
    for verifying data integrity in a distributed system like a blockchain.
"""
import hashlib  # Importing hashlib to use SHA-256 for cryptographic hashing of the transaction data.

class MerkleTree:
    """
    The `MerkleTree` class handles the construction and verification of Merkle trees.
    A Merkle tree allows efficient and secure verification of large amounts of data by 
    hashing transactions in pairs until a single root hash is derived.

    This root hash serves as a cryptographic fingerprint of the entire set of transactions.
    Any change to the transactions will result in a different root, providing integrity guarantees.
    """

    def __init__(self, transactions: list):
        """
        Initializes the `MerkleTree` object by accepting a list of transactions and building the tree.

        :param transactions: A list of transaction strings to be hashed and structured in a Merkle tree.

        Design Consideration:
        The transactions are hashed individually, and the Merkle tree is constructed from the bottom-up,
        where each level represents the hash of the concatenation of two child hashes.
        """
        self.transactions = transactions  # Store the original transactions.
        self.tree = self.build_tree(transactions)  # Construct the Merkle tree immediately upon initialization.

    def hash_data(self, data: str) -> str:
        """
        Returns the SHA-256 hash of the given data.

        :param data: The data to be hashed as a string, usually a transaction or concatenated hash.
        :return: The hexadecimal representation of the SHA-256 hash.
        
        Cryptographic Integrity:
        SHA-256 is chosen for its collision resistance and pre-image resistance properties, 
        making it a secure choice for hashing in Merkle trees. Any small change in the input data 
        will result in a completely different hash, ensuring the integrity of the Merkle tree.
        """
        return hashlib.sha256(data.encode()).hexdigest()  # Perform SHA-256 hashing of the input data.

    def build_tree(self, transactions: list) -> list:
        """
        Builds a Merkle tree from a list of transactions. Each transaction is hashed, 
        and hashes are combined pairwise to form a tree until only one hash (the root) remains.

        :param transactions: A list of transactions (strings), where each transaction is hashed and used to build the tree.
        :return: A list representing the full Merkle tree, with each level stored as a list of hashes.
        
        Tree Construction Process:
        - Each transaction is first hashed individually.
        - Hashes are then combined in pairs and hashed again to form the next level.
        - If there is an odd number of hashes at any level, the last hash is duplicated to form a pair.
        - The process continues until a single root hash remains.
        
        Security Note:
        The bottom-up structure ensures that the root hash depends on every transaction in the list. 
        Modifying any single transaction will result in a completely different root hash.
        """
        tree = []  # Initialize the list to store each level of the Merkle tree.

        # Hash each transaction individually and store them as the first layer (leaves) of the tree.
        layer = [self.hash_data(tx) for tx in transactions]
        tree.append(layer)  # Append the leaf layer to the tree.

        # Continue building the tree until only one hash (the root) remains.
        while len(layer) > 1:
            next_layer = []  # Initialize the next layer of the tree.
            
            # Combine hashes in pairs and hash the concatenated result.
            for i in range(0, len(layer), 2):
                left = layer[i]  # Take the left child hash.
                
                # If there's an odd number of hashes, duplicate the last hash to form a pair.
                right = layer[i + 1] if i + 1 < len(layer) else layer[i]
                
                # Hash the concatenation of the two child hashes.
                combined_hash = self.hash_data(left + right)
                
                # Add the result to the next layer.
                next_layer.append(combined_hash)

            tree.append(next_layer)  # Append the next layer to the tree.
            layer = next_layer  # Move to the next level of the tree.

        return tree  # Return the complete Merkle tree.

    def get_root(self) -> str:
        """
        Returns the root hash of the Merkle tree, which serves as the cryptographic commitment to the entire set of transactions.

        :return: The root hash as a string. If the tree has no transactions, return None.
        
        Root Hash Integrity:
        The root hash is the topmost node of the tree and represents the cumulative hash of all transactions. 
        This hash can be used as a secure reference to the entire data set in blockchain systems.
        """
        return self.tree[-1][0] if self.tree else None  # Return the root hash, or None if the tree is empty.
"""
Security and Architectural Considerations:

1. **Cryptographic Security**:
   The use of SHA-256 ensures that the Merkle tree is secure against tampering and modification. 
   Any change to even a single transaction will propagate through the tree and result in a completely 
   different root hash. This makes the Merkle tree a reliable structure for verifying data integrity.

2. **Efficiency**:
   The Merkle tree allows for efficient verification of large datasets by only requiring a small subset 
   of hashes (Merkle proof) to confirm the inclusion of a particular transaction. This reduces the computational 
   and storage overhead in blockchain systems, making it scalable.

3. **Fault Tolerance**:
   If there is an odd number of transactions, the Merkle tree duplicates the last hash to maintain the pairing 
   structure. This ensures that the tree can always be constructed, even with an uneven number of leaves.
"""
