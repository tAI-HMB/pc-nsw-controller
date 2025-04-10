from macro_sender import press, delay

def main():
    try:
        # AとBを順番に押す
        press("A", 100)
        press("B", 100)

        # 500ms待機
        delay(500)

        # 十字キーでぐるっと一周
        press("UP", 100)
        press("RIGHT", 100)
        press("DOWN", 100)
        press("LEFT", 100)

        # 最後に1秒待機
        delay(1000)

    except KeyboardInterrupt:
        print("\n中断されました（Ctrl+C）")

if __name__ == "__main__":
    main()
