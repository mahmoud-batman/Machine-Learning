from threading import Thread
import time

def character(ch , delay , repeat):
    while repeat > 0:
        time.sleep(delay)
        print(ch)
        repeat -= 1
    print("character "+ch+" complete")
        
def main():
    t1 = Thread(target= character , args=("a",0.1 , 1000))
    t2 = Thread(target= character , args=("b",0.2 , 1000))
    t1.start()
    t2.start()
    