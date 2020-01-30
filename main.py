from flask import Flask, render_template, request
import os
from google_images_download import google_images_download

CURR_DIR = os.getcwd()
OUTPUT_DIR = os.path.join(CURR_DIR, "output")

def getDataSet(conf):
    response = google_images_download.googleimagesdownload()
    paths = response.download(conf)
    return paths

app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',)

@app.route('/getImages',  methods=['GET'])
def get_images():
    nclass = request.args.get('nclass')
    nlimits = request.args.get('nlimits')
    arguments = {"keywords": nclass,
                "limit": nlimits,
                "print_urls":True,
                "output_directory": OUTPUT_DIR
                }
    
    return getDataSet(arguments)

# Port Configuartion
ON_HEROKU = os.environ.get('ON_HEROKU')
if ON_HEROKU:
    PORT = int(os.environ.get('PORT'))
else:
    PORT = 3000

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = PORT)