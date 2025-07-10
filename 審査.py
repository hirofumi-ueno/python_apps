import random
import time


def print_slow(text, delay=0.02):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()


def pachinko(money, vip_mode=False):
    bet = 10000 if not vip_mode else 100000
    print_slow(
        f"\n🎰『パチンコ{'（VIPカジノ）' if vip_mode else ''}』に突っ込む！{bet:,}円使用！"
    )
    money -= bet

    if vip_mode:
        outcome = random.choices(
            ["大当たり", "リーチ", "スルー", "爆死"], weights=[5, 10, 35, 50]
        )[0]
        if outcome == "大当たり":
            win = random.randint(100000, 500000)
            print_slow(f"🌟🌟【超大当たり!!】{win:,}円GET!!!🌟🌟")
            money += win
    else:
        outcome = random.choices(
            ["大当たり", "リーチ", "スルー", "爆死"], weights=[5, 15, 50, 30]
        )[0]
        if outcome == "大当たり":
            win = random.randint(50000, 200000)
            print_slow(f"🎉【大当たり!!】{win:,}円GET!!!")
            money += win

    if outcome == "リーチ":
        print_slow("🔁 リーチ...！（ドキドキ）→ハズレ！")
    elif outcome == "スルー":
        print_slow("・・・何も起きなかった。")
    elif outcome == "爆死":
        print_slow("💥 爆死！お金が消えた...")

    return money


def slot(money, vip_mode=False):
    bet = 5000 if not vip_mode else 50000
    print_slow(
        f"\n🎰『スロット{'（VIPカジノ）' if vip_mode else ''}』開始！{bet:,}円使用！"
    )
    money -= bet

    reels = [random.choice(["7", "BAR", "🍒", "💎"]) for _ in range(3)]
    time.sleep(0.5)
    print_slow(" | ".join(reels))

    if reels.count("7") == 3:
        win = 100000 if not vip_mode else 1000000
        print_slow(f"🎉【777揃い!!!】{win:,}円GET！")
        money += win
    elif reels.count("BAR") >= 2:
        win = 30000 if not vip_mode else 300000
        print_slow(f"✨ BARが揃った！{win:,}円GET！")
        money += win
    elif reels.count("🍒") >= 2:
        win = 10000 if not vip_mode else 100000
        print_slow(f"🍒 チェリー揃い！{win:,}円GET！")
        money += win
    else:
        print_slow("ハズレ！何も出ず…")

    return money


def keiba(money, vip_mode=False):
    bet = 10000 if not vip_mode else 100000
    print_slow(
        f"\n🐎『競馬{'（VIPカジノ）' if vip_mode else ''}』に賭ける！{bet:,}円使用！"
    )
    money -= bet

    if vip_mode:
        multiplier = random.choices(
            [0, 1.5, 3, 10, 30, 100], weights=[60, 10, 10, 10, 5, 5]
        )[0]
    else:
        multiplier = random.choices(
            [0, 0.5, 2, 5, 10, 30], weights=[30, 20, 20, 15, 10, 5]
        )[0]

    if multiplier == 0:
        print_slow("💀 全部スッた！")
    else:
        win = int(bet * multiplier)
        print_slow(f"🎯 的中！倍率 {multiplier}倍 → {win:,}円GET！")
        money += win

    return money


def suspicious_investment(money, vip_mode=False):
    bet = 10000 if not vip_mode else 1000000
    print_slow(f"\n🧢『怪しい投資話』が舞い込んできた…{bet:,}円投資")
    money -= bet
    chance = random.randint(1, 100)

    if vip_mode:
        if chance == 1:
            print_slow(f"💸💸 成功！1億円のリターン！！ 💸💸")
            money += 100000000
        else:
            print_slow("😱 詐欺だった！全部持ってかれた…")
    else:
        if chance <= 10:
            win = random.randint(100000, 500000)
            print_slow(f"🤑 投資成功！{win:,}円のリターン！")
            money += win
        else:
            print_slow("😱 詐欺だった！お金は帰ってこなかった…")

    return money


def main():
    money = 100000  # 初期所持金：10万円
    vip_activated = False  # 初回のVIP突入演出に使う

    print("💸 ようこそ『地獄のギャンブル生活』へ")
    print_slow("目指せ1億円…生き残れるか？\n")

    while money > 0 and money < 100000000:
        print(f"\n【現在の所持金】：{money:,}円")
        vip_mode = money >= 1000000

        # VIPモード突入演出
        if vip_mode and not vip_activated:
            print_slow("\n🎊🎊🎊 VIPカジノモード突入！勝者の世界へようこそ… 🎊🎊🎊")
            vip_activated = True

        print("何をする？")
        print("1: パチンコ")
        print("2: スロット")
        print("3: 競馬")
        print("4: 怪しい投資")
        print("5: 帰って寝る（ゲーム終了）")

        choice = input(">>> ")

        if choice == "1":
            if money >= (100000 if vip_mode else 10000):
                money = pachinko(money, vip_mode)
            else:
                print_slow("💥 所持金が足りない…")
        elif choice == "2":
            if money >= (50000 if vip_mode else 5000):
                money = slot(money, vip_mode)
            else:
                print_slow("💥 所持金が足りない…")
        elif choice == "3":
            if money >= (100000 if vip_mode else 10000):
                money = keiba(money, vip_mode)
            else:
                print_slow("💥 所持金が足りない…")
        elif choice == "4":
            if money >= (1000000 if vip_mode else 10000):
                money = suspicious_investment(money, vip_mode)
            else:
                print_slow("💥 所持金が足りない…")
        elif choice == "5":
            print_slow("\n🏠 あなたは帰宅した…。")
            break
        else:
            print("無効な入力です。")

    # ゲーム終了メッセージ
    if money >= 100000000:
        print_slow("\n💰💰💰 あなたは1億円を達成！伝説のギャンブラー！ 💰💰💰")
    elif money <= 0:
        print_slow("\n💀 所持金が尽きた…ゲームオーバー。")
    else:
        print_slow(f"\n👋 最終所持金：{money:,}円\nまた挑戦してね。")


if __name__ == "__main__":
    main()
