#Name: Dan-Ha Le
#Lab 2:

import time
import threading
import os
from os.path import join
import json
import requests
import pathlib
import asyncio


def practice():
    done = False
    def worker(text):
        counter = 0
        while True:
            time.sleep(1)
            counter += 1 
            print(f"{text}:{counter}")
    #Not calling it, but passing the instance of the worker (function, entity)
    t1 =threading.Thread(target=worker, daemon=True, args = {"ABC"})
    t2= threading.Thread(target=worker, daemon=True, args = {"XYZ"})
    t1.start()
    t2.start()
    #join ensures that a thread has been terminated. The caller will block indefinitely if the thread does not terminate.
    t1.join()
    t2.join()

    input ("Press enter to quit")
    done = True

#Break a list into evenly sized chunks and calculate the sum of all sublists
#in paralel and write the results to a file named output.txt. Remember to keep the
#order of the original list
# - lst is the list of number untruncated
# - n is the number of steps
def problem1(lst, n):

    output = open("/Users/danhale/Documents/GitHub/FPT_Python/.venv/lab2/output.txt", 'w')

    def chunk (lst, n):
        results = []
        for i in range(0, len(lst), n):
           results.append(lst[i:i+n])
        return results
    
    #This is the worker function for threading
    def worker(i):
        sum = 0
        for number in i:
            sum += number
        output.write(str(sum)+"\n")
    
    #This is where the threading happen
    sublists = chunk(lst, n)
    for i in sublists:
        threading.Thread(target=worker, args=[i]).start()
    
    output.close()

#Write a function that reads 10 json files and merge into one json file.
#Takes argument as the directory containing the Json files.
def problem2(ld):
    final = []
    for i in ld:
        print(i)
        f = open("/Users/danhale/Documents/GitHub/FPT_Python/.venv/lab2/json_files/"+i)
        data = json.loads(f.read())
        final.extend(data)
        f.close()
    output = open("/Users/danhale/Documents/GitHub/FPT_Python/.venv/lab2/json_output.json", "w")
    print(final)
    json.dump(final, output)
    output.close()

#Download images from a list of URL strings
def problem3(lst):
    for i in range(len(lst)):
        threading.Thread(target=save_img, args=[str(i+1), lst[i]]).start()
        
def save_img(name:str, url:str):
        img_source = requests.get(url)
        suffix = pathlib.Path(url).suffix
        if suffix not in ['.jpg', '.jpeg', '.png', '.gif']:
            output = name+'.jpg'
        else:
            output = name + suffix
        with open("/Users/danhale/Documents/GitHub/FPT_Python/.venv/lab2/img_files/"+output, "wb") as f:
            f.write(img_source.content)

def problem4(lst):
    async def save_first_img ():
        task = asyncio.create_task(save_second_img())
        save_img("first", lst[0])
        print("Saving first image")
        await asyncio.sleep(3)
        save_img("async", lst[1])
        print("Saving third image")
    async def save_second_img():
        save_img("second",lst[1])
        print("Saving second Image")
        
    asyncio.run(save_first_img())
        

def problem5(path:str):
    items = os.listdir(path)
    count = 0
    for item in items:
        if os.path.isdir(join(path, item)):
            count+=1

    print(count)
    


def main():
    problem1([1, 2, 3, 4, 5, 6], 1)
    problem2(os.listdir("/Users/danhale/Documents/GitHub/FPT_Python/.venv/lab2/json_files"))
    #problem3(["https://i.pinimg.com/564x/b0/bd/24/b0bd245611f64cf3b0b3826fcdad6b64.jpg", "https://i.pinimg.com/564x/9c/ae/9b/9cae9b1674b081528c6abc2bc2b32a39.jpg"])
    #problem4(["https://i.pinimg.com/564x/b0/bd/24/b0bd245611f64cf3b0b3826fcdad6b64.jpg", "https://i.pinimg.com/564x/9c/ae/9b/9cae9b1674b081528c6abc2bc2b32a39.jpg"])
    problem5("/Users/danhale/Documents/GitHub/FPT_Python/.venv")
    #should be five.
main()


