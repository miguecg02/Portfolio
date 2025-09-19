# server-launcher.py
import http.server
import socketserver
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Headers necesarios para Three.js y modelos 3D
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

    def translate_path(self, path):
        # Redirigir solicitudes de /libs/ a TMChess3D/libs/
        if path.startswith('/libs/'):
            return os.path.join(os.getcwd(), 'TMChess3D', path[1:])
        return super().translate_path(path)

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
});

httpd = socketserver.TCPServer(("", PORT), Handler)

print("Serviendo en el puerto", PORT)
print("Disponible en http://localhost:8000")
print("Proyecto de ajedrez en: http://localhost:8000/TMChess3D/")
httpd.serve_forever()
