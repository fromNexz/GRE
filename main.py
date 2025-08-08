import webview
import os

# Caminho absoluto do HTML local
html_path = os.path.abspath(f"C:/Users/pedro/OneDrive/Documentos/Portifólio/epi/gre.html")

# Cria uma janela com o HTML local
webview.create_window("Projeto Umbra", f"file://{html_path}", width=800, height=800)

# Inicia o app
webview.start()
