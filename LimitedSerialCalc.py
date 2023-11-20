# UGC Limited Serial Calculator // v1.2
import os
import sys

version = "1.2"  # Python Script Version


def calculate_serial(f, s):
    if f == 0:
        print("\033[38;5;196m[Error Code 1] Item does not have a stock.\033[0;0m")
    elif s == 0:
        print("\033[38;5;196m[Error Code 2] Item out of stock.\033[0;0m")
    elif f < s:
        print("\033[38;5;196m[Error Code 3] Remaining stock more than total stock.\033[0;0m")
    elif f < 0:
        print("\033[38;5;196m[Error Code 4] Total stock is a negative number.\033[0;0m")
    elif s < 0:
        print("\033[38;5;196m[Error Code 5] Remaining stock is a negative number.\033[0;0m")
    else:
        print("#", f - s + 1, sep="")


print("UGC Limited Serial Calculator by NicholasHong19 // v", version, sep="")
try:
    firstNum: int = int(input("Input total stock the item has: "))
    secondNum: int = int(input("Input total stock that's remaining for the item: "))
except ValueError:
    print("\033[38;5;196m[Error Code 6] Total or remaining stock is not a number.\033[0;0m")
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)


calculate_serial(firstNum, secondNum)
os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
