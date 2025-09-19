# server-launcher.py
import http.server
import socketserver
import os
import subprocess
import time
import threading
import requests

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

    def translate_path(self, path):
        # Redirigir solicitudes de /libs/ a TMChess3D/libs/
        if path.startswith('/libs/'):
            return os.path.join(os.getcwd(), 'TMChess3D', path[1:])
        # Redirigir otras rutas del ajedrez
        if path.startswith('/TMChess3D/'):
            return os.path.join(os.getcwd(), path[1:])
        if path.startswith('/Objects/'):
            return os.path.join(os.getcwd(), 'TMChess3D', path[1:])
        if path.startswith('/our_libs/'):
            return os.path.join(os.getcwd(), 'TMChess3D', path[1:])
        # REDIRIGIR MODELOS 3D - NUEVA REGLA
        if path.startswith('/Models/'):
            return os.path.join(os.getcwd(), 'TMChess3D', path[1:])
        if path.startswith('/piece-showcase/'):
            return os.path.join(os.getcwd(), 'TMChess3D', path[1:])
        if path.startswith('/2d/'):
            return os.path.join(os.getcwd(), 'TMChess3D', path[1:])
        return super().translate_path(path)

def start_ngrok():
    """Inicia ngrok para hacer el servidor público"""
    try:
        time.sleep(2)
        
        print("Iniciando ngrok...")
        ngrok_process = subprocess.Popen([
            'ngrok', 'http', str(PORT),
            '--region=us',
            '--log=stdout'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        time.sleep(5)  # Dar más tiempo para que ngrok se inicie
        
        try:
            # Intentar obtener la URL pública de ngrok
            response = requests.get('http://localhost:4040/api/tunnels', timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data['tunnels'] and len(data['tunnels']) > 0:
                    public_url = data['tunnels'][0]['public_url']
                    print(f"\n=== SERVIDOR PÚBLICO ===")
                    print(f"URL: {public_url}")
                    print(f"=======================\n")
                    
                    update_datajs_with_public_url(public_url)
                else:
                    print("Ngrok iniciado pero no se encontraron túneles activos")
                    print("Ejecuta manualmente: ngrok http 8000")
            else:
                print(f"Error al conectar con API de ngrok: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print("Ngrok no está ejecutándose o no está instalado")
            print("Instala ngrok desde https://ngrok.com/")
            print("Luego ejecuta manualmente en otra terminal: ngrok http 8000")
        except Exception as e:
            print(f"Error al obtener URL de ngrok: {e}")
            
    except FileNotFoundError:
        print("Ngrok no encontrado. Instálalo desde https://ngrok.com/")
        print("Luego ejecuta manualmente: ngrok http 8000")

def update_datajs_with_public_url(public_url):
    """Actualiza data.js para que el proyecto de ajedrez use la URL pública"""
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

def check_ngrok_installed():
    """Verifica si ngrok está instalado"""
    try:
        subprocess.run(['ngrok', '--version'], capture_output=True, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

if __name__ == '__main__':
    # Verificar si ngrok está instalado
    if check_ngrok_installed():
        ngrok_thread = threading.Thread(target=start_ngrok, daemon=True)
        ngrok_thread.start()
    else:
        print("Ngrok no está instalado. Para acceso público:")
        print("1. Instala ngrok desde https://ngrok.com/")
        print("2. Ejecuta manualmente: ngrok http 8000")
        print("3. Comparte la URL que genera ngrok")
    
    # Iniciar el servidor HTTP
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
    print("Disponible en red local en http://" + subprocess.getoutput('hostname -I').strip() + ":8000")
    
    if check_ngrok_installed():
        print("Iniciando ngrok para acceso público...")
    else:
        print("Para acceso público externo, instala ngrok y ejecuta: ngrok http 8000")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nCerrando servidor...")
        httpd.shutdown()