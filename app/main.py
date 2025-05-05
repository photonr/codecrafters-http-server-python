# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    while True:
        client_socket, address = server_socket.accept()
        client_socket.sendall("HTTP/1.1 200 OK\r\n\r\n".encode())
        client_socket.close()


if __name__ == "__main__":
    main()
