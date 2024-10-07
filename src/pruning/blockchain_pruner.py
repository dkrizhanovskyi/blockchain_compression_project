# blockchain_pruner.py

"""
Module: BlockchainPruner
Purpose:
    The `BlockchainPruner` module is designed to manage the storage of blockchain data by limiting 
    the number of blocks retained in the local blockchain state. Over time, blockchains can grow 
    significantly in size, resulting in storage overhead for full nodes. This module ensures that only 
    a specified number of recent blocks are kept, reducing disk usage while maintaining the most recent 
    and relevant data.

    The module performs "pruning" by removing the oldest blocks once the limit is exceeded, 
    which is critical for the long-term scalability of blockchain systems.

    Key Features:
    - Adds new blocks to the blockchain and automatically prunes old blocks to respect a size limit.
    - Ensures the system retains only the most recent `n` blocks as specified by the user.
    - Provides a method to retrieve the current blocks stored after pruning.

    Security and Data Integrity:
    Pruning is an optimization that reduces storage usage, but must be done carefully to avoid 
    removing data necessary for blockchain validation or security. It is important that the pruning process 
    does not interfere with the integrity of the current state of the blockchain.
"""
class BlockchainPruner:
    """
    The `BlockchainPruner` class is responsible for managing and pruning blocks from the blockchain.
    It allows the system to retain only a specified number of recent blocks, ensuring that old blocks 
    are discarded once the limit is reached, thus reducing storage space usage.

    This design is essential for maintaining blockchain scalability, particularly for nodes 
    with limited storage capacity.
    """

    def __init__(self, max_blocks: int):
        """
        Initializes the BlockchainPruner with a specified maximum number of blocks to store.

        :param max_blocks: The maximum number of recent blocks to retain in the blockchain.
        
        Design Consideration:
        - The `max_blocks` parameter ensures that the node only stores the most recent `n` blocks.
          This parameter is user-defined based on the storage capacity and needs of the node.
        - The internal `blocks` list stores the current blockchain data.

        Scalability:
        This approach allows the system to scale efficiently by managing data growth. By retaining 
        only the necessary recent data, the blockchain node can run on devices with smaller storage capacities.
        """
        self.max_blocks = max_blocks  # Store the maximum number of blocks the node should retain.
        self.blocks = []  # Initialize an empty list to store blocks.

    def add_block(self, block: dict):
        """
        Adds a new block to the blockchain and performs pruning if necessary.

        :param block: A dictionary representing a blockchain block, which contains block metadata 
                      (e.g., block number, transactions, timestamps).
        
        Block Addition Logic:
        - The block is appended to the `blocks` list.
        - After adding the block, if the total number of blocks exceeds the `max_blocks` limit, 
          the oldest blocks are pruned to keep the size within the limit.

        Data Integrity:
        It is important to ensure that the block being added is valid and has been verified elsewhere 
        in the system (e.g., via consensus mechanisms) before adding it to the pruned blockchain state.
        """
        # Add the new block to the list of blocks.
        self.blocks.append(block)
        
        # If the number of stored blocks exceeds the limit, prune the oldest blocks.
        if len(self.blocks) > self.max_blocks:
            self.prune_blocks()

    def prune_blocks(self):
        """
        Prunes the oldest blocks from the blockchain to ensure the total number of blocks 
        does not exceed the `max_blocks` limit.

        Pruning Strategy:
        - Only the most recent `max_blocks` blocks are retained.
        - The oldest blocks are removed, ensuring that the system keeps only relevant, 
          up-to-date data for validation and operational purposes.
        
        Performance:
        This pruning operation is computationally inexpensive, as it simply slices the list of blocks.
        It is optimized for scenarios where block additions occur frequently.
        """
        # Keep only the last `max_blocks` blocks by slicing the list.
        self.blocks = self.blocks[-self.max_blocks:]
        
        # Log a message indicating that pruning has occurred.
        print(f"Pruned blockchain to keep the last {self.max_blocks} blocks.")

    def get_blocks(self) -> list:
        """
        Returns the current list of blocks stored in the blockchain after pruning.

        :return: A list of current blocks that have been retained in the pruned blockchain.
        
        Use Case:
        This method allows other components or users of the blockchain to retrieve 
        the most recent blocks for further processing or validation.
        
        Data Integrity:
        This ensures that only the pruned blocks (up to `max_blocks`) are available, 
        providing an efficient way to access the most relevant data in the blockchain system.
        """
        # Return the current blocks that are stored in the pruned blockchain state.
        return self.blocks
"""
Security and Architectural Considerations:

1. **Storage Optimization**:
   The `BlockchainPruner` class is designed with scalability in mind, allowing blockchain nodes 
   to reduce their storage footprint while retaining critical recent blocks. This is crucial 
   for long-running blockchain systems where the block data grows continuously over time.

2. **Pruning Strategy**:
   Pruning ensures that only the most relevant and recent blocks are kept, but care must be taken 
   to ensure that no blocks necessary for blockchain validation or auditing are removed prematurely. 
   This class assumes that historical data can be safely discarded after it has been processed 
   by the blockchain's consensus mechanism.

3. **Data Integrity**:
   While pruning reduces the amount of stored data, the integrity of the most recent state must be preserved. 
   Additional cryptographic techniques, such as hash validation or consensus protocols, 
   should ensure that the blocks being retained are valid and consistent with the blockchain's overall state.
"""
