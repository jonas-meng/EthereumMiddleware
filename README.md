# EthereumMiddleware

# When whole data structure cannot fit into memory
1. Store snapshot of balances for transactions with large amount of confirmations, since they are unlikely to be reverted. For instance, balances with more than 6 confirmations. In other words, only store balances of blocks with less than certain confirmations (e.g. 6)
2. If the median is the only thing the client app cares, instead of maintaining full balances data, we can try to only maintain the median for all account balances, which means only re-calculate median when performed transactions affect it.
3. Each block stores balances that affected by contained transactions, such that reduce memory usage. However, such method will certainly increases the time required to calculate median since retrieval of full account balances might require traversal of block history.

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


