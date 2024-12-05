import os
import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

def selecionar_pasta():
    """Abre o explorador de arquivos para selecionar a pasta de destino."""
    pasta = filedialog.askdirectory()
    if pasta:
        pasta_destino_var.set(pasta)

def baixar_video():
    """Faz o download do vídeo ou áudio do YouTube."""
    url = url_var.get()
    pasta_destino = pasta_destino_var.get()
    formato = formato_var.get()  # Obtém a escolha de formato (vídeo ou áudio)
    
    if not url:
        messagebox.showerror("Erro", "Por favor, insira o link do vídeo.")
        return
    if not pasta_destino:
        messagebox.showerror("Erro", "Por favor, selecione a pasta de destino.")
        return
    
    try:
        # Configurações do yt-dlp com base na escolha de formato
        ydl_opts = {
            'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',  # Caminho de saída
            'format': 'bestaudio/best' if formato == 'Áudio' else 'best',  # Define formato de áudio ou vídeo
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Sucesso", "Download concluído!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar o conteúdo: {e}")

# Criação da interface gráfica
root = tk.Tk()
root.title("Downloader de Vídeos e Áudios do YouTube")

# Variáveis para armazenar os inputs do usuário
url_var = tk.StringVar()
pasta_destino_var = tk.StringVar()
formato_var = tk.StringVar(value='Vídeo')  # Valor padrão é "Vídeo"

# Layout
tk.Label(root, text="Link do Vídeo:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=url_var, width=50).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Pasta de Destino:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=pasta_destino_var, width=50).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Selecionar", command=selecionar_pasta).grid(row=1, column=2, padx=10, pady=5)

# Opção para selecionar entre vídeo ou áudio
tk.Label(root, text="Escolha o formato:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Radiobutton(root, text="Vídeo", variable=formato_var, value="Vídeo").grid(row=2, column=1, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="Áudio", variable=formato_var, value="Áudio").grid(row=2, column=1, padx=10, pady=5, sticky="e")

# Botão para iniciar o download
tk.Button(root, text="Download", command=baixar_video, bg="green", fg="white").grid(row=3, column=0, columnspan=3, pady=10)

# Iniciar o loop da interface
root.mainloop()
