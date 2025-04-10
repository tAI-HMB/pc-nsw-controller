# nsw_serial_receiver

このスケッチは、PCとArduino Leonardo（または互換マイコン）をUSBシリアル変換機で接続し、PCから送られるコマンドを受け取って Nintendo Switch を操作するためのものです。

NintendoSwitchControlLibrary を使用し、受け取ったコマンドに応じてボタンやスティックの操作を自動で行います。

---

## 特徴

- PCからシリアル通信で命令を受信（Serial1 使用）
- Nintendo Switch に HID 操作信号を送出
- コマンドは `"コマンド名 数値"` の形式（例：`A 100`）
- 無効なコマンドは無視され、ログに表示されます

---

## 対応ボード

- Arduino Leonardo
- Pro Micro（ATmega32u4 搭載）

---

## 配線例（FTDI などのシリアル変換機を使用）

| シリアル変換機 | Arduino Leonardo |
|----------------|------------------|
| TXD            | D0 (RX)          |
| RXD            | D1 (TX)          |
| GND            | GND              |

> ※ スケッチ書き込み時は D0/D1 の接続を外してください。

---

## 使用ライブラリ

- [NintendoSwitchControlLibrary](https://github.com/lefmarna/NintendoSwitchControlLibrary)  
  - MIT License © lefmarna

Arduino IDE で zip 形式から追加、またはクローンして `libraries/` に配置してください。

---

## コマンド仕様

すべてのコマンドは `コマンド名 数値` の形式で、ミリ秒単位で動作時間を指定します。

例：
```
A 100
RIGHT 200
RJ_L 300
```

### 対応コマンド一覧

#### ボタン系
- A, B, X, Y
- BP（＋）, BM（−）
- HOME, SC（スクリーンショット）
- L, R, ZL, ZR

#### 十字キー（HAT）
- UP, DOWN, LEFT, RIGHT

#### 左スティック
- LJ_L, LJ_R, LJ_U, LJ_D, LJ_C（中央）

#### 右スティック
- RJ_L, RJ_R, RJ_U, RJ_D, RJ_C（中央）

---

## ライセンス

このスケッチは MIT ライセンスで公開されています。  
また、NintendoSwitchControlLibrary（© lefmarna）も MIT ライセンスに従って利用・クレジット記載しています。

