

class blockHeader:
    def __init__(self):
        self.previousBlock = 0
        self.merkleRoot = 0
        self.nonce = 0
        self.timeStamp = 0
        self.difficultyTarget = 0

class transactionInput:
    def __init__(self):
        self.hashPrevious = 0
        self.index = 0
        self.key = 0
        self.signature = 0

class transactionOutput:
    def __init__(self):
        self.value = 0
        self.receiver = 0


class transaction:
    def __init__(self):
        self.hash = 0
        self.protocol = 0
        self.nrInputs = 0
        self.nrOutputs = 0
        self.time = 0
        self.sizer = 0

class block:
    def __init__(self):
        self.blockSize = 0
        self.blockHeader = 0
        self.numberTransactions = 0
        self.transactions = 0




class merkleRoot:
    def __init__(self):
        self.hashVal = 0
        self.child0 = 0
        self.child1 = 0
        pass


class merkleNode(merkleRoot):
    def __init__(self):
        self.parent = 0

