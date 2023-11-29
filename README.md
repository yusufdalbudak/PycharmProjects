# Python Server-Client Example with Sockets

This project demonstrates a simple server-client model implemented using the Python programming language. The socket library is utilized to establish basic communication between the server and the client.

## Server (`server.py`) Features:

- The server listens on a specific port and accepts incoming connections.
- It executes commands received from the client, responding with the results of system commands.

## Client (`client.py`) Features:

- The client can connect to a specific server IP address and port, sending commands.
- It receives and displays the results of commands entered by the user from the server.

## Usage

1. Start the server by running the `server.py` file.
2. Launch the client by running the `client.py` file.
3. Enter the commands you want to send to the server in the client interface.
4. The client will display the responses received from the server.

## Notes

- This project is for educational purposes only and may contain security issues.
- If the client and server are running on the same machine, use local IP addresses such as "localhost" or "127.0.0.1."

---

**Warning:** This project may not adhere to security standards applicable to real systems. Use it at your own risk.
