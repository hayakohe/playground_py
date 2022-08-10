import math 
import calendar

# 動的型付け言語のため、型指定が不要
def print_arg(something):
    print(something)

print_arg(1000)
print_arg("hoge")

# 絶対値計算
arg_count = 100 * -1
return_value = abs(arg_count)
print(return_value)

arg_count = 10
return_value = abs(arg_count)
print(return_value)

# mathを利用
square_root = math.sqrt(2.0)
print(square_root)

# カレンダー機能
calendar.prmonth(2022, 8)
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.calendar(2019))
print(calendar.firstweekday())

# input()関数を利用
# 処理が一時停止するため、コメントアウト
# input_text = input("好きな文字を入力：")
# print("入力された文字：", input_text)

# strメソッドを利用
base_text = "hogehoge island"
upper_text = base_text.upper()
print(f"`{base_text}`を、大文字にすると`{upper_text}`となる")