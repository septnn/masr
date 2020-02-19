#! /usr/bin/env python3
from flask import Flask, request
import _init_path
from models.conv import GatedConv
import sys
import json

print("Loading model...")

import beamdecode

print("Model loaded")

app = Flask(__name__)

# 内存要设置大于等于4G
# cpu要设置大于等于4个

app.config['FLASK_ENV'] = "development" # 解决警告问题 no development
app.config['ENV'] = "development"


@app.route("/recognize", methods=["POST"])
def recognize():
    f = request.files["file"]
    f.save("test.wav")
    return beamdecode.predict("test.wav")


app.run("0.0.0.0", debug=True, use_reloader=False) # 解决 Restarting with stat 问题
