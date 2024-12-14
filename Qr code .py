import qrcode

# Replace with your Render-hosted chatbot URL
chatbot_url = "https://replit.com/@skarthikeyan211/project-of-chatbot#main.py"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(chatbot_url)
qr.make(fit=True)

# Save the QR Code as an image
img = qr.make_image(fill_color="black", back_color="white")
img.save("chatbot_qr_code.png")

print("QR Code generated and saved as chatbot_qr_code.png!")
