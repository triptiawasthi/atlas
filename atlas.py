from random import *
import enchant
import time

def start():
    print "lets play ATLAS "
    time.sleep(1)
    print "the starting alphabet is given"
    time.sleep(1)
    a=choice("abcdefghijklmnopqrstuvwxyz")
    print a
    print("\n")
    time.sleep(1)
    begin()
    
def begin():
        global user
        user =raw_input("make a meaningfull word starting from the mentioned alphabet if possible otherwise write retry")
        if user=="retry":
           start()
        else:
           checkkaro()

           
def checkkaro():
    global user
    lang_dict=enchant.Dict("en_US")
    boolean=lang_dict.check(user)
    if boolean:
        print "you won ....yes the word "+user+" do exist"
    else:
        print "you lose.....such a word don't exist..."
        print "the related words are"
        print lang_dict.suggest(user)
        
start()
