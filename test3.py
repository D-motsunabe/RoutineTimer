import pyttsx3
from datetime import datetime, timedelta
import time  # 忘れていたモジュールを追加

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def countdown_timer(minutes):
    total_seconds = minutes * 60
    start_time = datetime.now()

    while total_seconds > 0:
        current_time = datetime.now()
        elapsed_time = (current_time - start_time).total_seconds()
        remaining_time = max(total_seconds - elapsed_time, 0)
        
        mins, secs = divmod(int(remaining_time), 60)
        timeformat = '{:02d}分{:02d}秒'.format(mins, secs)
        speak(timeformat)
        
        # タイマーの精度を向上するために、1秒待機ではなく短い時間待機する
        time.sleep(0.1)

    speak("時間です！")

if __name__ == "__main__":
    try:
        input_minutes = int(input("タイマーを設定する時間（分）を入力してください："))
        countdown_timer(input_minutes)
    except ValueError:
        print("有効な数値を入力してください。")
