from flask import Flask, request, jsonify
import os

app = Flask(__name__)

SLACK_VERIFICATION_TOKEN = os.getenv("SLACK_VERIFICATION_TOKEN")
STATIC_HOURS = "40"  # Static number to return

@app.route("/hours", methods=["POST"])
def hours():
    token = request.form.get("token")
    if token != SLACK_VERIFICATION_TOKEN:
        return jsonify({"error": "Unauthorized"}), 403
    
    response = {
        "response_type": "ephemeral",  # Only visible to the user
        "text": f"You have logged {STATIC_HOURS} hours."
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)