from flask import request
import pickle
import base64


@app.route("/load_state")
def load_state():
    # Intentionally vulnerable to Unsafe Deserialization
    encoded_state = request.args.get("state")

    if encoded_state:
        decoded_state = base64.b64decode(encoded_state)
        # Unmarshaling untrusted data
        state = pickle.loads(decoded_state)
        return str(state)
    return "No state provided"