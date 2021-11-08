import RPi.GPIO as GPIO
import random
import time

pins = [{'pin_num': 23, 'color': 'red'},
        {'pin_num': 24, 'color': 'yellow'},
        {'pin_num': 25, 'color': 'blue'},
        {'pin_num': 22, 'color': 'red'},
        {'pin_num': 12, 'color': 'yellow'},
        {'pin_num': 16, 'color': 'blue'},
        {'pin_num': 20, 'color': 'red'},
        {'pin_num': 21, 'color': 'green'},
        {'pin_num': 13, 'color': 'yellow'}]

GPIO.setmode(GPIO.BCM)  # use GPIO numbering, not generic
GPIO.setwarnings(False)

# setup all pins based on above configuration
for pin in pins:
    GPIO.setup(pin['pin_num'], GPIO.OUT, initial=GPIO.LOW)


def toggle_color(color: str, state: str):
    pin_nums = [pin['pin_num'] for pin in pins if pin['color'] == color]
    for pin_num in pin_nums:
        if state == 'on':
            GPIO.output(pin_num, GPIO.HIGH)
        elif state == 'off':
            GPIO.output(pin_num, GPIO.LOW)


def color_on(color: str):
    toggle_color(color, 'on')


def color_off(color: str):
    toggle_color(color, 'off')


def all_on():
    for pin in pins:
        GPIO.output(pin['pin_num'], GPIO.HIGH)


def all_off():
    for pin in pins:
        GPIO.output(pin['pin_num'], GPIO.LOW)


def strobe_reg(period=0.5, run_time=20):
    start = time.time()
    curr = time.time()
    while curr - start < run_time:
        all_on()
        time.sleep(period)
        all_off()
        time.sleep(period)
        curr = time.time()


def strobe_rand(min_time=0, max_time=1.2, run_time=20):
    start = time.time()
    curr = time.time()
    while curr-start < run_time:
        all_on()
        time.sleep(random.uniform(min_time, max_time))
        all_off()
        time.sleep(random.uniform(min_time, max_time))
        curr = time.time()


def wave_reg(period=0.1, run_time=20):
    start = time.time()
    curr = time.time()
    while curr - start < run_time:
        for pin in pins:
            GPIO.output(pin['pin_num'], GPIO.HIGH)
            time.sleep(period)

        for pin in reversed(pins):
            GPIO.output(pin['pin_num'], GPIO.LOW)
            time.sleep(period)
        curr = time.time()


def wave_rand(min_time=0, max_time=0.4, run_time=20):
    start = time.time()
    curr = time.time()
    while curr - start < run_time:
        period = random.uniform(min_time, max_time)
        for pin in pins:
            GPIO.output(pin['pin_num'], GPIO.HIGH)
            time.sleep(period)

        period = random.uniform(min_time, max_time)
        for pin in reversed(pins):
            GPIO.output(pin['pin_num'], GPIO.LOW)
            time.sleep(period)
        curr = time.time()


def wave_rand_ex(min_time=0, max_time=0.4, run_time=20):
    start = time.time()
    curr = time.time()
    while curr - start < run_time:
        for pin in pins:
            GPIO.output(pin['pin_num'], GPIO.HIGH)
            time.sleep(random.uniform(min_time, max_time))

        for pin in reversed(pins):
            GPIO.output(pin['pin_num'], GPIO.LOW)
            time.sleep(random.uniform(min_time, max_time))
        curr = time.time()