import random
import time

def reflex_game():
    best_time = None 
    while True:
        print("反射神経テストをします")
        print("準備ができたらenterを押してください")
        input()

        wait_time=random.uniform(5,15)
        print("合図が出たらenterを押してください")
        time.sleep(wait_time)

        start_time = time.time()
        input("押せ！！！")
        end_time = time.time() - start_time()
        if end_time<0.01:
            print("速すぎます。連打していませんか？")
        else:
            print(f"反応時間：{end_time:.4f} 秒")
            if best_time is None or end_time < best_time:
                best_time = end_time
        
        


    




