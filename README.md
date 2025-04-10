# pc-nsw-controller

このプロジェクトは、PCからNintendo Switchを操作するためのマクロ送信システムです。
Pythonで記述されたマクロスクリプトを通じて、シリアル経由でArduinoマイコンに命令を送り、Nintendo Switchのボタン操作・スティック操作を自動化できます。

---

## ディレクトリ構成

```
pc-nsw-controller/
├── README.md                     # プロジェクト概要（このファイル）
├── LICENSE                       # MITライセンス
├── requirements.txt              # Python依存ライブラリ（pyserial）
├── run_macro.py                  # マクロ実行サンプル
├── macro_sender.py               # シリアル送信ライブラリ（press, delay）
├── arduino/
│   └── nsw_serial_receiver/
│       ├── nsw_serial_receiver.ino
│       └── README.md             # Arduinoスケッチの詳細説明
└── examples/
    ├── abxy_loop.py
    ├── random_inputs.py
    └── combo_demo.py
```

---

## セットアップ手順

### 1. Python 環境を準備

```bash
pip install -r requirements.txt
```

必要なライブラリは `pyserial` のみです。

### 2. Arduino スケッチの書き込み

Arduino Leonardo または Pro Micro に
`arduino/nsw_serial_receiver/` 内のスケッチを書き込みます。

- 対応マイコン: ATmega32u4 搭載ボード（Leonardo / Pro Micro）
- 使用ライブラリ: [NintendoSwitchControlLibrary](https://github.com/lefmarna/NintendoSwitchControlLibrary)
- 詳細: [arduino/nsw_serial_receiver/README.md](arduino/nsw_serial_receiver/README.md)

### 3. シリアル変換機を接続

| シリアル変換機 | Arduino Leonardo |
|----------------|------------------|
| TXD            | D0 (RX)          |
| RXD            | D1 (TX)          |
| GND            | GND              |

> ※ スケッチ書き込み時は D0/D1 を一時的に外してください。

### 4. マクロを実行

```bash
python run_macro.py
```

---

## マクロ記述例

Pythonで以下のように記述することで、順番にコマンドを送信できます：

```python
from macro_sender import press, delay

press("A", 100)
delay(500)
press("RIGHT", 300)
```

- `press(command, duration, post_delay=100)`  
  コマンドを `duration` ミリ秒押し、`post_delay` ミリ秒待機します。
- `delay(ms)` 
  任意の時間だけ待機します。

使用可能なコマンド一覧は Arduino 用 README に記載されています。

---

## 使用ライブラリ

- [NintendoSwitchControlLibrary](https://github.com/lefmarna/NintendoSwitchControlLibrary)  
  - MIT License © lefmarna

---

## ライセンス

このリポジトリは [MIT License](LICENSE) で公開されています。
NintendoSwitchControlLibrary も MIT ライセンスに従って利用・クレジット記載しています。

