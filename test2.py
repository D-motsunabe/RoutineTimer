import time
import pyttsx3
import threading

def multitask(process1,process2):
        thread1=threading.Thread(target=process1)
        thread2=threading.Thread(target=process2)

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def start(minutes,seconds,text):
        sentence=f"{minutes}分{seconds}秒後までに「{text}」をしましょう。"
        print(sentence)
        speak(sentence)

def read_text(minutes,seconds,text):
    print(1)
    rest_seconds=minutes*60+seconds
    while rest_seconds>60:
        rest_seconds-=60
        time.sleep(60)
        print(f"残り{rest_seconds}秒")
        speak(f"残り{rest_seconds}秒")
    
    time.sleep(rest_seconds)
    speak(f"{text}は終わりです。")

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as file:  # input.txtはテキストファイルの名前です
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split()
        minutes, seconds = map(int, parts[:2])
        text = ' '.join(parts[2:])
        multitask(start(minutes,seconds,text),read_text(minutes,seconds,text))
        