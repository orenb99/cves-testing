from flask import request, Flask
import os

app = Flask(__name__)


@app.route("/download")
def download_file():
    # Intentionally vulnerable to Path Traversal
    filename = request.args.get("filename")

    # Directly opening a file based on user input without validation
    file_path = os.path.join("/var/www/html/downloads", filename)

    with open(file_path, 'r') as f:
        return f.read()