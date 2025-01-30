from flask import Flask, render_template
import sys
sys.path.append('C:/Users/hp/OneDrive/Desktop/Blockchain')

from Blockchain.backend.core.block import Block
from Blockchain.backend.core.database.database import BlockchainDB

app = Flask(__name__)

@app.route('/')
def index():
    blockchainDB = BlockchainDB()
    last_block = blockchainDB.lastBlock()
    print("Last Block:", last_block)  # Debug statement

    return render_template('index.html', block=last_block)

if __name__ == "__main__":
    app.run(debug=True)