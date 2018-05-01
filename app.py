#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, render_template, redirect, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/__webpack_hmr')
def npm():
    return redirect('http://localhost:8081/__webpack_hmr')

# 测试接口
@app.route('/test/')
def test():
    return jsonify({ 'res': 'hello , world!' })


if __name__ == '__main__':
    app.run(debug=True)

# 作者：非梦nj
# 链接：https://www.jianshu.com/p/3f6964028ec3
# 來源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。