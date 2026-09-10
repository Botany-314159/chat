import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"\nFriend: {message}")
            print("You: ", end="")
        except:
            print("\nConnection closed by server.")
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '192.168.68.88' 
    port = 5000

    try:
        client.connect((server_ip, port))
        print(f"Successfully connected to the chat!")
    except Exception as e:
        print(f"Could not connect: {e}")
        return

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    while True:
        msg = input("You: ")
        if msg.lower() == 'exit':
            break
        client.send(msg.encode('utf-8'))

    client.close()

if __name__ == "__main__":
    start_client()

