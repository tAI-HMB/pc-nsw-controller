"""
macro_sender.py

このモジュールは、PCからArduino経由でNintendo Switchを操作するための
マクロ送信用ライブラリです。コマンドをシリアルで送信し、Switchの操作を行います。

使用例:
    from macro_sender import press, delay
    press("A", 100)          # Aボタンを100ms押し、100ms待機
    press("B", 100, 200)     # Bボタンを100ms押し、200ms待機
    delay(500)               # 500ms待機のみ
"""

from typing import Literal
import serial
import time

# 有効なコマンドの定義
ValidCommand = Literal[
    "A", "B", "X", "Y", "BP", "BM", "HOME", "SC",
    "L", "R", "ZL", "ZR",
    "UP", "DOWN", "LEFT", "RIGHT",
    "LJ_L", "LJ_R", "LJ_U", "LJ_D", "LJ_C",
    "RJ_L", "RJ_R", "RJ_U", "RJ_D", "RJ_C"
]

# シリアル接続設定（環境に応じてポート名変更）
ser = serial.Serial('COM6', 9600)
time.sleep(2)  # 接続安定待機

def press(command: ValidCommand, duration: int, post_delay: int = 100):
    """
    コマンド送信関数。

    Parameters:
        command (ValidCommand): 操作コマンド
        duration (int): 操作時間（ミリ秒）
        post_delay (int): 操作後の待機時間（ミリ秒、デフォルト100ms）
    """
    command = command.upper()
    full_cmd = f"{command} {duration}"
    print(f"送信: {full_cmd}")
    ser.write((full_cmd + '\n').encode())

    reply = ser.readline().decode(errors='ignore').strip()
    if reply:
        print(f"応答: {reply}")

    time.sleep(post_delay / 1000.0)

def delay(ms: int):
    """
    単純な待機関数。
    """
    print(f"待機: {ms}ms")
    time.sleep(ms / 1000.0)
