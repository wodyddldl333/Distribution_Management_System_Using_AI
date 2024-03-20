import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

delay = 0.03
# motor and capture code(run jetson gpio & CSI-camera coding)
# for 1st Motor on ENA
ENA = 38
IN1 = 31
IN2 = 33
IN3 = 35
IN4 = 37
ENB = 40


# set pin numbers to the board's
GPIO.setmode(GPIO.BOARD)

# initialize EnA, In1 and In2
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(ENA, GPIO.HIGH)
GPIO.output(ENB, GPIO.HIGH)

def motor():
    # Stop
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(0)

    # Forward
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(1.76)

    # Stop
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(0.5)


def capture():
    cap = cv2.VideoCapture(1)
    ret, frame = cap.read()
    return frame

def image_make():

    cap1 = capture(); motor()
    cap2 = capture(); motor()
    cap3 = capture(); motor()
    cap4 = capture()
    img_con1 = np.concatenate([cap1, cap2], axis=0)
    img_con2 = np.concatenate([cap3, cap4], axis=0)
    img_con3 = np.concatenate([img_con1, img_con2], axis=1)
    cv2.imshow('capture image', cv2.resize(img_con3, dsize=(0, 0), fx=0.3, fy=0.3, interpolation=cv2.INTER_LINEAR))

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    return img_con3