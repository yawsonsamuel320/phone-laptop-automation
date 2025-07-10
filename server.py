import socket
import os

HOST = "10.21.42.23" 
PORT = 12345

# Start the socket server
server_socket = socket.socket()
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("🟢 Server started. Waiting for connection...")

conn, addr = server_socket.accept()
print(f"📲 Connected to {addr}")

try:
    while True:
        data = conn.recv(1024).decode().strip()
        if not data:
            break
        print(f"📥 Received command: {data}")

        # --- Command handlers ---
        if data == "open whatsapp":
            os.system("am start -n com.whatsapp/.Main")
        elif data == "open chrome":
            os.system("am start -n com.android.chrome/com.google.android.apps.chrome.Main")
        elif data == "open camera":
            os.system("am start -a android.media.action.IMAGE_CAPTURE")
        elif data == "dial mom":
            os.system("am start -a android.intent.action.DIAL -d tel:0542963751")
        elif data.startswith("say "):
            message = data[4:]
            os.system(f'termux-tts-speak "{message}"')
        elif data == "shutdown":
            print("🔴 Shutting down server.")
            break
        else:
            print("⚠️ Unknown command:", data)

except Exception as e:
    print("❌ Error:", e)

finally:
    conn.close()
    server_socket.close()
    print("🔌 Connection closed.")
