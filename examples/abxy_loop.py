# ABXYボタンを順番に押し続けるマクロ例

from macro_sender import press, delay

buttons = ["A", "B", "X", "Y"]

try:
    while True:
        for button in buttons:
            press(button, 100)   # 100ms 押す
            delay(300)           # 300ms 待つ

except KeyboardInterrupt:
    print("\n中断されました（Ctrl+C）")
