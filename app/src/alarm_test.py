import time
import RPi.GPIO as GPIO

pin_number = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_number, GPIO.OUT)

tone = GPIO.PWM(pin_number, 440)
volume = 99

notes = [262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 523]
tone_duration = 1
rest_duration = 1


tone.start(volume)

def play_a_tone(freq, duration):
    tone.ChangeFrequency(freq)
    tone.ChangeDutyCycle(volume)
    time.sleep(duration)

def play_a_rest(duration):
    tone.ChangeDutyCycle(0)
    time.sleep(duration)

for note in notes:
    print("playing ", note)
    play_a_tone(note, tone_duration)
    play_a_rest(rest_duration)

tone.stop()
GPIO.cleanup()
    