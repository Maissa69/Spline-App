import os
import sys
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import http.server
import socketserver

# Fonction pour démarrer le serveur HTTP
def start_server():
    # Démarrer le serveur HTTP sur le port 8000 dans un sous-processus
    os.chdir('./')  # Assurez-vous d'être dans le bon répertoire pour trouver index.html
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(('localhost', 8000), handler) as httpd:
        print("Server started at http://localhost:8000")
        httpd.serve_forever()

# Classe principale de la fenêtre PyQt5
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spline Viewer")

        # Créer un widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Disposition verticale pour le widget central
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        central_widget.setStyleSheet("background-color: black;")

        # Ajouter une WebView pour afficher le modèle Spline
        web_view = QWebEngineView()
        layout.addWidget(web_view)

        # Charger l'URL du fichier HTML via le serveur local
        web_view.setUrl(QUrl("http://localhost:8000/index.html"))

# Fonction principale
if __name__ == "__main__":
    # Démarrer le serveur HTTP dans un thread séparé
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True  # Cela permet de fermer le thread lorsque le programme principal se ferme
    server_thread.start()

    # Lancer l'application PyQt5
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(1024, 768)
    window.show()
    sys.exit(app.exec_())
