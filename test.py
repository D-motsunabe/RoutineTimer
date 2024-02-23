import time
import os
import pyttsx3




def read_text_after_delay(text, minutes, seconds):
    total_seconds = minutes * 60 + seconds
    time.sleep(total_seconds)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    

if __name__ == "__main__":
    minute = int(input("何分後に読み上げますか？: "))
    second = int(input("何秒後に読み上げますか？: "))

    
    text = str(input("読み上げるテキストを入力してください: "))
    print(text)

    print(f"{minute}分{second}秒後に「{text}」を読み上げます。")
    read_text_after_delay(text, minute, second)