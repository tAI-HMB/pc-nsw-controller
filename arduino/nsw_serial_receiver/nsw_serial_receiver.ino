/*
 * nsw_serial_receiver.ino
 * 
 * PCからシリアル変換機（Serial1）経由で受け取ったコマンドを元に
 * Nintendo Switch に操作信号を送信するスケッチ。
 *
 * 使用ライブラリ: NintendoSwitchControlLibrary
 * 対応ボード: Arduino Leonardo / Pro Micro（ATmega32u4系）
 * 通信ポート: Serial1（D0: RX, D1: TX）
 */

 #include <NintendoSwitchControlLibrary.h>

 void setup() {
   Serial1.begin(9600);  // シリアル変換機との通信開始
   pushButton(Button::B, 100, 3);  // Switch接続確認のBボタン3連打
   Serial1.println("Ready to receive commands via Serial1.");
 }
 
 void loop() {
   if (Serial1.available()) {
     String line = Serial1.readStringUntil('\n');
     line.trim();
 
     String cmd = "";
     int duration = 100;
 
     int spaceIndex = line.indexOf(' ');
     if (spaceIndex != -1) {
       cmd = line.substring(0, spaceIndex);
       duration = line.substring(spaceIndex + 1).toInt();
     } else {
       cmd = line;
     }
 
     // 受信ログ
     Serial1.print("Received: ");
     Serial1.print(cmd);
     Serial1.print(" ");
     Serial1.println(duration);
 
     // === コマンド判定 ===
 
     // ボタン
     if      (cmd == "A")    pushButton(Button::A, duration);
     else if (cmd == "B")    pushButton(Button::B, duration);
     else if (cmd == "X")    pushButton(Button::X, duration);
     else if (cmd == "Y")    pushButton(Button::Y, duration);
     else if (cmd == "BP")   pushButton(Button::PLUS, duration);
     else if (cmd == "BM")   pushButton(Button::MINUS, duration);
     else if (cmd == "HOME") pushButton(Button::HOME, duration);
     else if (cmd == "SC")   pushButton(Button::CAPTURE, duration);
     else if (cmd == "L")    pushButton(Button::L, duration);
     else if (cmd == "R")    pushButton(Button::R, duration);
     else if (cmd == "ZL")   pushButton(Button::ZL, duration);
     else if (cmd == "ZR")   pushButton(Button::ZR, duration);
 
     // 十字キー（HAT）
     else if (cmd == "UP")    holdHat(Hat::UP, duration);
     else if (cmd == "DOWN")  holdHat(Hat::DOWN, duration);
     else if (cmd == "LEFT")  holdHat(Hat::LEFT, duration);
     else if (cmd == "RIGHT") holdHat(Hat::RIGHT, duration);
 
     // 左スティック
     else if (cmd == "LJ_L")  tiltLeftStick(-127,   0, duration);
     else if (cmd == "LJ_R")  tiltLeftStick( 127,   0, duration);
     else if (cmd == "LJ_U")  tiltLeftStick(   0, 127, duration);
     else if (cmd == "LJ_D")  tiltLeftStick(   0, -127, duration);
     else if (cmd == "LJ_C")  tiltLeftStick(   0,   0, duration);
 
     // 右スティック
     else if (cmd == "RJ_L")  tiltRightStick(-127,   0, duration);
     else if (cmd == "RJ_R")  tiltRightStick( 127,   0, duration);
     else if (cmd == "RJ_U")  tiltRightStick(   0, 127, duration);
     else if (cmd == "RJ_D")  tiltRightStick(   0, -127, duration);
     else if (cmd == "RJ_C")  tiltRightStick(   0,   0, duration);
 
     // 未対応コマンド
     else {
       Serial1.print("Unknown command: ");
       Serial1.println(cmd);
     }
   }
 }