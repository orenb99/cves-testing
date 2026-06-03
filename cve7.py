import hashlib
from flask import request


@app.route("/hash_password")
def hash_password():
    # Intentionally vulnerable to Weak Cryptography
    user_password = request.args.get("password")

    # MD5 is cryptographically broken and should not be used
    hasher = hashlib.md5()
    hasher.update(user_password.encode('utf-8'))

    return hasher.hexdigest()