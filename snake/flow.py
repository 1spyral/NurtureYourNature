from personality import generate
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/sms", methods=["POST"])
def sms_reply():
    # Debug: Log the incoming request data
    print("Incoming request data:", request.form)

    # Extract message details
    message_content = request.form.get("Body")  # SMS message body
    from_number = request.form.get("From")  # Sender's phone number

    if message_content and from_number:
        print(f"Received SMS from {from_number}: {message_content}")
    else:
        print("Missing required data in request.")

    # Optional: Respond back to sender
    response = generate(message_content)

    return f"""
    <Response>
        <Message>{response}</Message>
    </Response>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
