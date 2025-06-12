import random
import time

print("反射神経テストをします")
print("準備ができたらenterを押してください")
input()

wait_time=random.randint(3,5)
print("合図が出たらenterを押してください")
time.sleep(wait_time)

start_time = time.time()
input("押せ！！！")
end_time = time.time()
reaction_time = end_time - start_time

if reaction_time<0.01:
    print("速すぎます。連打していませんか？")
else:
    print(f"反応時間：{reaction_time:.4f} 秒")

        


    




