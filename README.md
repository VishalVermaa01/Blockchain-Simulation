# Blockchain Simulation Project

This project is a basic simulation of a blockchain, designed to demonstrate the core concepts of blockchain technology, such as blocks, hashing, proof-of-work, and chain validation. It is built using Python and serves as an educational tool to understand how blockchains work under the hood.

## Features
### Block Creation: Simulates the creation of blocks with attributes like index, timestamp, data, previous_hash, and hash.

### Proof-of-Work: Implements a simple mining algorithm to add blocks to the blockchain.

### Chain Validation: Validates the integrity of the blockchain by checking the hashes of all blocks.

### Modular Design: Easy to extend and integrate with other systems.

### Hashing with SHA-256:
The SHA-256 algorithm is used to generate a unique hash for each block. The hash is computed by combining the block's index, timestamp, data, and previous_hash into a single string and passing it through the SHA-256 hashing function. This ensures the integrity and immutability of the blockchain.




## Setup
Prerequisites
Python 3.x
pip (Python package manager)

## Installation

Clone the repository:
git clone https://github.com/your-username/blockchain-simulation.git 
cd blockchain-simulation

Install the required dependencies:
pip install -r requirements.txt


## How It Works
### Block Structure
Each block contains the following attributes:

index: The position of the block in the blockchain.

timestamp: The time when the block was created.

data: The data stored in the block (e.g., transactions or messages).

previous_hash: The hash of the previous block in the chain.

hash: The hash of the current block (calculated using the block's attributes).


## Proof-of-Work
The proof-of-work algorithm ensures that blocks are added to the blockchain only after solving a computational puzzle. This process is called "mining."

## Chain Validation
The blockchain is validated by ensuring that:

Each block's previous_hash matches the hash of the previous block.

Each block's hash is correctly calculated.
