# EthereumMiddleware

# When whole data structure cannot fit into memory
Current solution trades memory for efficiency of retrieval balances.
To reduces memory consumption:
1. Each block caches the view of changed balances, not all account balances. However, querying for median requires traversal of block history in order to achieve full balances.
2. Another strategy is to take a snapshot of all account balances on a block with large certainty that there will be no chain reorganisation that affects it. Then, the memory for the cached views of blocks before the snapshot can be released.

# Describe what needs to be considered in the client app
1. To be able to send transaction, the client app has to allow user to sign transaction with private key.
2. Possibly user might use recovery phrase and password access the client app. That requires client app have strong security to protect private key locally.

# Describe what edge cases you can think about



# Describe a system architecture and communication pattern for updating the client app
Both publish/subscribe and request/response patterns are adopted.
- A client app capable of sending requests to middleware server, such as sending transactions, quering balances of subset accounts etc. Those request should be handled in a synchronous way.
- Client app also subscribes to updates on changes of median of all account balances, reorg of chain etc.


# Which field of computer science address the described problems? What are the standard patterns for this (if any)?
For the system architecture and communication pattern, I studied at distributed system design, which provides useful knowledge on solving such issues.
For encryption of private key, security and cryptography can help us with it.
To solve memory issues, we can use some compression technique and efficient data storage and retrieval techinques from database.


# Questions
1. Is the median of all account balances the only thing a client app can show?
2. The lastest block means the Ethereum has chosen it as the HEAD block, which means the old block of same height is discarded?


