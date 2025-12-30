import re
import numpy as np

file_path = "data/input_day2.txt"

from functools import reduce
def factors(n):
  return reduce(list.__add__,
    ([i, n//i] for i in range(1, int(n**0.5) + 1) if not n % i))

if __name__ == "__main__":
    invalidID_sum = 0

    with open(file=file_path, mode="r+") as file:
        
        lines = file.readlines()
        ranges = lines[0].split(",")
        for r in ranges:
            begin, end = r.split("-")

            for value in range(int(begin),int(end)+1):
                str_value = str(value)
                l = len(str_value)
                for step in factors(l):
                    if step == l:
                        # if step equals length, then the whole string would repeat only once
                        continue
                    repeat_exists = True
                    for i in range(0, l-step, step):
                        if str_value[i:i+step] != str_value[i+step:i+2*step]:
                            repeat_exists = False
                            break
                    if repeat_exists:
                        invalidID_sum += value
                        break
        

            # if len(begin) != len(end) or (len(begin) % 2 == 0) or (len(end) % 2 == 0):
            #     for value in range(int(begin),int(end)+1):
            #         str_value = str(value)
            #         l = len(str_value)
            #         if str_value[:l//2] == str_value[l//2:]:
            #             invalidID_sum += value

print("Zero was reached", invalidID_sum, "times.")