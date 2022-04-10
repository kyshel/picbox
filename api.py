from flask import Flask, send_from_directory, request, url_for
import core


app = Flask(__name__)


# api
@app.route('/api/gray', methods=['GET','POST','DELETE','PUT'])
def gray():
    return core.do_gray(request)










# static 
@app.route('/<path:filename>')
def send_static(filename):
    return send_from_directory('static',
                               filename)
# index
@app.route('/')
def index():
    return send_static('index.html')   


if __name__ == '__main__':
    app.run(debug=True)


