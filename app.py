import explorerhat
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/motor")
def motor():
    left_speed = request.args.get('left', '')
    right_speed = request.args.get('right', '')
    msg = f"Move motor left {left_speed} and right {right_speed}"
    explorerhat.motor.one.speed(right_speed)
    explorerhat.motor.two.speed(left_speed)
    return msg

@app.route("/motor/stop")
def stop():
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    return "Stop all motors"