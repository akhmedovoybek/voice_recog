import speech_recognition as sr
import pyfirmata
from time import sleep

board = pyfirmata.Arduino('COM3')
led_pin = board.get_pin('d:13:o')

r = sr.Recognizer()
mic = sr.Microphone()


with mic as source:
    r.adjust_for_ambient_noise(source)
    r.listen(source)

    while True:
        audio = r.listen(source)
        try:
            if (r.recognize_google(audio) == "forward"):
                # command = "ON"
                # serialInst.write(command.encode('utf-8'))
                led_pin.write(1)
                sleep(.5)
                led_pin.write(0)
                sleep(1)
                print("forward")
            else:
                print("smth else")
        except:
            print("No audio")
