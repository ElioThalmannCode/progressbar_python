import time
import os
clear = lambda: os.system('clear')
def progressbar(length):
    '''
    args: 
    length |   how long should the progressbar be
    '''
    progressbar_symbol = "█"
    progressbar_counter = 1
    done = False
    while not done:
        print(f"Laden: |{progressbar_counter * progressbar_symbol}| {progressbar_counter}/{length}")
        progressbar_counter = progressbar_counter + 1
        time.sleep(0.5)
        clear()
        if progressbar_counter == length:
            print(f"Laden: |{progressbar_counter * progressbar_symbol}| {progressbar_counter}/{length}")
            time.sleep(1)
            done = True
progressbar(100)