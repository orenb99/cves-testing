from flask import request
import requests


@app.route("/fetch_image")
def fetch_image():
    # Intentionally vulnerable to SSRF
    image_url = request.args.get("url")

    # The server makes a request to an arbitrary URL provided by the user
    response = requests.get(image_url)

    return response.content