import datetime
import hashlib 
import random, time
from binascii import unhexlify, hexlify
#64
#ssqdifficultpasscrypt
#captain fade naive dish when quality token brief change volume fix chase
symbols_hash = '1234567890'
pas = ''
for x in  range(4): 
    pas = pas + random.choice(list(symbols_hash)) 
    


class Block_1: 
    def __init__ (self, prev_hash, transaction, amount): 
        self.next = None
        self.__data = {
            'prev_hash': prev_hash, 
            'transaction': transaction, 
            'amount': amount, 
            'hash': '', 
            'time': datetime.datetime.now().time()
        } 
        self.__data['hash'] = self.make_hash()

    def get_data_1(self): 
        return self.__data  
    
    def make_hash(self): 
        global test_hash
        test_hash = hexlify(hashlib.sha256(unhexlify(self.get_data_1()['prev_hash'])).digest()).decode('utf-8') 
        start = time.time()
        while test_hash [:1]!= "0":
             test_hash = hexlify(hashlib.sha256(unhexlify(test_hash)).digest()).decode('utf-8') 
             print(test_hash)
        finish = time.time() - start
        print(finish)
        print(test_hash)
        return test_hash
        

test_1 = Block_1(pas, 'ilay', 100)

print(test_1.get_data_1())