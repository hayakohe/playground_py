# 動的型付け言語のため、型指定が不要
def print_arg(something):
    print(something)

print_arg(1000)
print_arg("hoge")

def abs(num):
    return num

arg_count = 100 * -1
return_value = abs(arg_count)
print(return_value)

arg_count = 10
return_value = abs(arg_count)
print(return_value)