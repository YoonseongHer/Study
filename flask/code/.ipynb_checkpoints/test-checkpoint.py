import asyncio
from flask import Flask, render_template, request, jsonify
import pandas as pd
from time import time, sleep
app = Flask(__name__)

@app.route("/")
async def hello():
    sleep(100)
    return "b"


##############################################
async def async_get_data():
    await asyncio.sleep(10)
    return 'Done!'


@app.route("/data")
async def get_data():
    data = await async_get_data()
    return data
##############################################


def main():
    loop = asyncio.get_event_loop()
    func_set = asyncio.gather(test_2(), test_1())
    loop.run_until_complete(func_set)
    print(10)
    
async def test_1():
    print('test 1 start')
    await asyncio.sleep(5)
    print('test 1 end')
    return 'test1'

async def test_2():
    print('test 2 start')
    await test_1()
    print('test 2 end')
    return 'test2'


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
#     main()