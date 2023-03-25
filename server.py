from flask import Flask
from flask import request
import os

hostName = "localhost"
serverPort = 8080

image_folder = ".\\output_compressed_images"
images = []

# iterate over files in
# that directory
for filename in os.listdir(image_folder):
    f = os.path.join(image_folder, filename)
    # checking if it is a file
    if os.path.isfile(f):
        images.append(filename)

app = Flask(__name__)

@app.route('/images', methods = ['POST'])
def get_images():

    page = int(request.json.get('page'))
    offset = page * 100

    num_images = len(images)

    if offset < num_images:
        return {
            "id": images[offset: min(offset + 100, num_images)]
        }
    
    return { "id": [] }

app.run(debug = True)