# server-launcher.py CORREGIDO
import http.server
import socketserver
import os
import subprocess
import time
import threading

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

    def translate_path(self, path):
        if path.startswith('/libs/'):
            return os.path.join(os.getcwd(), 'TMChess3D', path[1:])
        return super().translate_path(path)

def start_ngrok():
    """Inicia ngrok para hacer el servidor público"""
    try:
        time.sleep(2)

        ngrok_process = subprocess.Popen([
            'ngrok', 'http', str(PORT),
            '--region=us',
            '--log=stdout'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        time.sleep(3)

        try:
            import requests
            response = requests.get('http://localhost:4040/api/tunnels')
            data = response.json()
            public_url = data['tunnels'][0]['public_url']
            print(f"\n=== SERVIDOR PÚBLICO ===\nURL: {public_url}\n=======================\n")

            update_datajs_with_public_url(public_url)

        except Exception as e:
            print(f"No se pudo obtener la URL pública de ngrok: {e}")

    except FileNotFoundError:
        print("Ngrok no encontrado. Instálalo desde https://ngrok.com/")

def update_datajs_with_public_url(public_url):
    """CORREGIDO: chess.html está en la raíz"""
    try:
        with open('data.js', 'r') as file:
            content = file.read()

        # URL CORRECTA: chess.html está en la raíz
        chess_url = f"{public_url}/chess.html"
        updated_content = content.replace('"chess.html"', f'"{chess_url}"')

        with open('data.js', 'w') as file:
            file.write(updated_content)

        print(f"Archivo data.js actualizado con URL: {chess_url}")
    except Exception as e:
        print(f"No se pudo actualizar data.js: {e}")

if __name__ == '__main__':
    ngrok_thread = threading.Thread(target=start_ngrok, daemon=True)
    ngrok_thread.start()

    Handler = MyHTTPRequestHandler
    Handler.extensions_map.update({
        ".js": "application/javascript",
        ".wasm": "application/wasm",
        ".glb": "model/gltf-binary",
        ".gltf": "model/gltf+json",
        ".obj": "model/obj",
        ".mtl": "model/mtl",
        ".stl": "model/stl",
        ".dae": "model/vnd.collada+xml"
    })

    httpd = socketserver.TCPServer(("", PORT), Handler)

    print("Serviendo en el puerto", PORT)
    print("Disponible localmente en http://localhost:8000")
    print("Iniciando ngrok para acceso público...")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nCerrando servidor...")
        httpd.shutdown()
