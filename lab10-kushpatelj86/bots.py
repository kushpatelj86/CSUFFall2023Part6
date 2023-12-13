import threading 
import json
from time import sleep
import time 

def bot_fetcher(items, cart, lock):
    
    inventory = {}
    with open('inventory.dat','r') as f:
        inventory = json.load(f)
    
    
    for key in items:

        value = inventory[key]
        duration = value[1]
        item = value[0]
        time.sleep(duration)
        lock.acquire()
        cart.append([key,item])
        lock.release()
    
    

def bot_clerk(items):

    bot1=[]
    bot2=[]
    bot3=[]
    cart_list=[]
    lock = threading.Lock()


    for n, item in enumerate(items):
        bot_num = n % 3
        if bot_num == 0:
            bot1.append(item)
        elif bot_num == 1:
            bot2.append(item)
        elif bot_num == 2:
            bot3.append(item)
    
    thread = []
    if len(bot1) > 0:
        t = threading.Thread(target=bot_fetcher, args=(bot1, cart_list,lock))
        t.start() 
        thread.append(t)

    if len(bot2) > 0:
        t = threading.Thread(target=bot_fetcher, args=(bot2, cart_list,lock))
        t.start() 
        thread.append(t)

    if len(bot3) > 0:
        t = threading.Thread(target=bot_fetcher, args=(bot3, cart_list,lock))
        t.start() 
        thread.append(t)

    for t in thread:
        t.join()
    
    
    return cart_list