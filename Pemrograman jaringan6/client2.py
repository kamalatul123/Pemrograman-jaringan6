import socket
import threading

SERVER_IP = "10.42.2.57"  # Ganti dengan IP laptop server
SERVER_PORT = 5000

def terima_pesan(client):
    while True:
        try:
            data = client.recv(1024)
            if not data:
                print("[SERVER PUTUS] Koneksi terputus.")
                break
            print("\n" + data.decode('utf-8'))
        except:
            print("[DISKONEK] Server tidak dapat diakses.")
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, SERVER_PORT))
    print(f"[TERHUBUNG] Ke server {SERVER_IP}:{SERVER_PORT}")

    # Jalankan thread untuk menerima pesan dari server
    terima_thread = threading.Thread(target=terima_pesan, args=(client,))
    terima_thread.start()

    # Kirim pesan ke server
    try:
        while True:
            pesan = input()
            if pesan.lower() == "exit":
                break
            client.sendall(pesan.encode('utf-8'))
    except KeyboardInterrupt:
        pass
    finally:
        client.close()
        print("[TUTUP] Koneksi ditutup.")

if __name__ == "__main__":

    start_client()