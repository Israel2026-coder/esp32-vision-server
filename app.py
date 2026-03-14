from flask import Flask, request
import cv2
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return "Server running"

@app.route("/process", methods=["POST"])
def process():

    distance = float(request.form["distance"])

    file = request.files["image"]
    img = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(img, cv2.IMREAD_COLOR)

    print("distance:", distance)

    return {"status":"processed"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
