import sys
from io import BytesIO

import aiohttp
import responder
import numpy as np
import cv2 as cv

api = responder.API()


async def download_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()


@api.route("/upload")
async def upload(req, resp):
    files = await req.media("files")
    if "file" in files:
        data = files["file"]["content"]
        resp.media = predict_image_from_bytes(data)
    else:
        resp.text = "Image is required."


@api.route("/classify-url")
async def classify_url(req, resp):
    if "url" in req.params:
        url = req.params["url"]
        data = await download_url(url)
        resp.media = predict_image_from_bytes(data)
    else:
        resp.text = "URL is required."


def predict_image_from_bytes(data):
    file_bytes = np.asarray(bytearray(data), dtype=np.uint8)
    img = cv.imdecode(file_bytes, cv.IMREAD_COLOR)
    return {
        "predictions": ['Blah', 'Bloo']
    }


@api.route("/", default=True)
def index(req, resp):
    # Default template_dir in responder is 'templates'
    resp.content = api.template("index.html")


if __name__ == "__main__":
    api.run(port=8000)
