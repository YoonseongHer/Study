from flask import Flask, render_template, request, jsonify
import pandas as pd
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('input.html')

@app.route("/post",methods=['POST'])
def post():
	value = request.form['input']
	msg = "%s 님 환영합니다." %value
	return msg

@app.route('/response', methods=['POST']) #post echo api
def post_echo_call():
    param = request.get_json()
    pd.DataFrame(param).to_csv("response_data.csv", index=False)
    return "Success Response"

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)