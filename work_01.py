
import random
number = random.randint(1,100)
print("1~100までの数字を当てなさい")
for i in range(5):
    input_line = input()
    print(f"{i+1}回目",input_line)
    if number == int(input_line):
        print("やるやん")
        break
    else:
        print("よわ＾＾")
        if number > int(input_line):
            print("ちっさw")
        elif number < int(input_line):
            print("デカw")
else:
    print(f"答えは{number}でした〜")
