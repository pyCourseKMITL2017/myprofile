import sys
from flask import Flask, send_from_directory, render_template
from data import data

sys.path.insert(0, '../')
app = Flask(__name__, static_folder='')

@app.route('/<path:path>')
def send_file(path):
    return send_from_directory(app.static_folder, path)

@app.route("/")
def myprofile():
    # print(render_template('index.html', data=data))
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9000)
