
from curses.ascii import isalpha
import random

a = random.randrange(200)

if a >= 100:
    print(f"{a}は100以上")
else:
    print(f"{a}は100より小さい")

input_text = input("好きな文字や数値を入力：")

if input_text.isdecimal():
    print("入力された文字は数字です。")
elif input_text.isalpha(): 
    print("入力された文字はアルファベットです。")
else:
    print("入力された文字は数字でもアルファベットでもありません。")