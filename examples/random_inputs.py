# ボタンや十字キーをランダムに押すマクロ例

import random
from macro_sender import press, delay

commands = [
    "A", "B", "X", "Y",
    "UP", "DOWN", "LEFT", "RIGHT"
]

try:
    while True:
        cmd = random.choice(commands)
        duration = random.randint(100, 300)
        press(cmd, duration)
        delay(random.randint(200, 500))

except KeyboardInterrupt:
    print("\n中断されました（Ctrl+C）")