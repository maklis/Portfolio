#coding=utf-8
from multiprocessing import Pool
from collections import Counter
import time
import re

result_list = []
symbols = ['"', "'", ",", ".", "?", "!", "-", ";", ":", "\n", "'''", "!", "(", ")", "[", "]", "{", "}","\ ", "<",">", "/","@", "#", "$", "%", "^", "&", "*", "_","~"]

def worker(sub):
    result = Counter(sub)
    return result

def log_result(result):
    result_list.append(result)

def main():
    pool = Pool(processes=5)

    with open('book-war-and-peace.txt') as origin:
        content = origin.read()
        for char in symbols:
             content=content.replace(char,' ')
        words = content.lower().split()

    step = (len(words)//6)
    subs = [words[pos : pos+step] for pos in range(0, len(words), step)]
    result = Counter()

    for sub in subs:
        pool.apply_async(worker, args=(sub,), callback = log_result)

    pool.close()
    pool.join()
    result = Counter()

    for item in result_list:
        result = result + item
    result = result
    count = (result.values())
    desc = result.most_common()


    # print("First Word:", result[0])
    # print("Last Word:", result[-1])


    for word, frequency in desc:
            print(f'{word}: {frequency}')
    print("Number of Words:", sum(count))

if __name__ == "__main__":
        start = time.perf_counter()
        main()
        print(time.perf_counter() - start)
