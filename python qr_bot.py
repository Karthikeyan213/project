import cv2
from pyzbar.pyzbar import decode
import requests

# Function to scan QR code
def scan_qr_code():
    cap = cv2.VideoCapture(0)  # Open webcam
    print("Point the camera at the QR code...")
    
    while True:
        ret, frame = cap.read()  # Read frame from webcam
        if not ret:
            break
        
        for qr_code in decode(frame):
            qr_data = qr_code.data.decode('utf-8')
            print(f"QR Code Detected: {qr_data}")
            cap.release()
            cv2.destroyAllWindows()
            return qr_data  # Return QR code content
        
        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None

# Function to interact with bot
def talk_to_bot(qr_data):
    url = qr_data  # Assuming QR code contains a bot API URL
    print("Talking to the bot...")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat.")
            break
        
        response = requests.post(url, json={"message": user_input})
        if response.status_code == 200:
            print(f"Bot: {response.json().get('response', 'No response')}")
        else:
            print("Error talking to the bot.")

# Main function
if __name__ == "_main_":
    qr_data = scan_qr_code()
    if qr_data:
        talk_to_bot(qr_data)
    else:
        print("No QR code detected.")
