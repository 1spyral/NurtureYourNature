from personality import generate
from flask import Flask, request, jsonify
from arduino_snake import move_motor
from twilio.rest import Client
num_no = 0

app = Flask(__name__)

# Twilio credentials
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

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


    for_human, for_robot = generate(message_content)

    # Check if we got "no" twice in a row from the health monitor
    
    
    #frown
    print(for_robot)
    if for_robot == "no" and num_no < 2:
        num_no += 1
        pin = 2
    else:
        num_no = 0
        
        #the throwing pin
        pin = 3
        
    move_motor(pin, for_robot)
    #send message to arduino
    return f"""
    <Response>
        <Message>{for_human}</Message>
    </Response>
    """

if __name__ == "__main__":
    # Send initial welcome message
    client.messages.create(
        body="Hi! I'm your friendly health monitoring bot. How are you feeling today?",
        from_='+',
        to='+',
    )
    
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000, debug=True)
