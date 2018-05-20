'''
Created on May 15, 2018

@author: krishna kundu
'''
from eva_core import Eva
if __name__ == '__main__':
    eva = Eva()
    
    while True:
        ip = input("Enter Bot Text:: ")
        resp = eva.handle_request(ip, sender_id="1")

        print(resp)
    pass