from flask import Flask, render_template, make_response, url_for, request, send_from_directory
from encrypt import *
from decrypt import *

app = Flask(__name__)

 

@app.route('/<path:path>')
def home(path):
    return send_from_directory('./', path)



@app.route('/encrypt',methods=['POST'])
def encrypt():
    if request.method == 'POST':
        output = request.get_json(force=True)
        result = aesEncrypt(output['text'], output['pass'])
        res = make_response({'result':result}, 200)
        return res    


@app.route('/decrypt',methods=['POST'])
def decrypt():
    if request.method == 'POST':
        output = request.get_json(force=True)
        result = aesDecrypt(output['text'], output['pass'])
        res = make_response({'result':result}, 200)
        return res    

if __name__ == "__main__":
    app.run(debug=True)