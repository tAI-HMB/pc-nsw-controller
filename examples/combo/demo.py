# コナミコマンド（↑↑↓↓←→←→BA）を再現するマクロ

from macro_sender import press, delay

def konami_code():
    sequence = [
        "UP", "UP",
        "DOWN", "DOWN",
        "LEFT", "RIGHT",
        "LEFT", "RIGHT",
        "B", "A"
    ]
    for cmd in sequence:
        press(cmd, 100)
        delay(200)

try:
    while True:
        print("コナミコマンド発動！")
        konami_code()
        delay(3000)  # 次の発動まで待機

except KeyboardInterrupt:
    print("\n中断されました（Ctrl+C）")