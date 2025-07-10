import socket

HOST = "10.21.42.23"  # Replace with your phone's IP
PORT = 12345

def send_command(command):
    try:
        s = socket.socket()
        s.connect((HOST, PORT))
        s.send(command.encode())
        s.close()
        print(f"✅ Sent: {command}")
    except ConnectionRefusedError:
        print("❌ Connection refused. Is the server running?")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    while True:
        print("\n📱 Available commands:")
        print("1. Open WhatsApp")
        print("2. Open Chrome")
        print("3. Open Camera")
        print("4. Dial Mom")
        print("5. Say Something")
        print("6. Custom Command")
        print("7. Shutdown Server")
        print("0. Exit")

        choice = input("👉 Enter your choice: ").strip()

        if choice == "1":
            send_command("open whatsapp")
        elif choice == "2":
            send_command("open chrome")
        elif choice == "3":
            send_command("open camera")
        elif choice == "4":
            send_command("dial mom")
        elif choice == "5":
            message = input("🗣️ What should the phone say? ")
            send_command(f"say {message}")
        elif choice == "6":
            command = input("⌨️ Enter custom command: ")
            send_command(command)
        elif choice == "7":
            send_command("shutdown")
            print("🛑 Server shutdown requested.")
            break
        elif choice == "0":
            print("👋 Exiting client.")
            break
        else:
            print("❗ Invalid option")

if __name__ == "__main__":
    main()

