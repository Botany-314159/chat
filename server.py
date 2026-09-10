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
            print("\nConnection lost.")
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5000)) 
    server.listen(1)
    print("Waiting for a friend to connect...")

    client_socket, client_address = server.accept()
    print(f"Connected to {client_address}!")

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        msg = input("You: ")
        if msg.lower() == 'exit':
            break
        client_socket.send(msg.encode('utf-8'))

    client_socket.close()
    server.close()

if __name__ == "__main__":
    start_server()

