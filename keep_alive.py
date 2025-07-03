from flask import Flask
app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"  # ← This is the keyword to check from UptimeRobot

def keep_alive():
    from threading import Thread
    app.run(host='0.0.0.0', port=8080)