import sys
sys.path.append('C:/Users/hp/OneDrive/Desktop/Blockchain')

from Blockchain.backend.core.block import Block
from Blockchain.backend.core.blockheader import BlockHeader
from Blockchain.backend.util.util import hash256
from Blockchain.backend.core.database.database import BlockchainDB
import time


ZERO_HASH = '0' * 64
VERSION = 1
class Blockchain:
    def __init__(self):
        self.blockchainDB = BlockchainDB()

    def write_on_disk(self, block):
        self.blockchainDB.write(block)

    def fetch_last_block(self):
        return self.blockchainDB.lastBlock()
    
    def GenesisBlock(self):
        BlockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)

    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        Transaction = f"Codies Alert sent {BlockHeight} Bitcoins to Jeo"
        merkleRoot = hash256(Transaction.encode()).hex()
        bits = 'ffff001f'
        blockheader = BlockHeader(VERSION, prevBlockHash, merkleRoot, timestamp, bits)
        blockheader.mine()
        self.write_on_disk([Block(BlockHeight, 1, blockheader.__dict__, 1, Transaction).__dict__])
        

    # def main(self):
    #     while True:
    #         lastBlock = self.fetch_last_block()
    #         BlockHeight = lastBlock['Height'] + 1
    #         prevBlockHash = lastBlock['BlockHeader']['blockHash']
    #         self.addBlock(BlockHeight, prevBlockHash)/
        
    def main(self):
        while True:
            lastBlock = self.fetch_last_block()
            if lastBlock is not None:
                BlockHeight = lastBlock['Height'] + 1
                prevBlockHash = lastBlock['BlockHeader']['blockHash']
            else:
                # If no blocks exist yet, initialize the blockchain with the genesis block
                self.GenesisBlock()
                continue
            self.addBlock(BlockHeight, prevBlockHash)

            
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.main()
