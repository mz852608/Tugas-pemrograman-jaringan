import socket

# Konfigurasi server
server_ip = "0.0.0.0"  # Dengarkan di semua alamat
server_port = 5000

# Buat socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print(f"Server berjalan di {server_ip}:{server_port}")
print("Menunggu koneksi dari client...")

# Terima koneksi
client_socket, client_address = server_socket.accept()
print(f"Terhubung dengan client: {client_address}")

while True:
    # Terima pesan dari client
    data = client_socket.recv(1024).decode()
    if not data:
        print("Client memutus koneksi.")
        break

    print(f"Client: {data}")

    # Kirim balasan ke client
    reply = input("Server: ")
    client_socket.send(reply.encode())

# Tutup koneksi
client_socket.close()
server_socket.close()