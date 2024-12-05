import yt_dlp

def baixar_video_yt_dlp(url, pasta_destino="."):
    try:
        ydl_opts = {
            'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',  # Nome do arquivo de saída
            'format': 'best'  # Melhor qualidade disponível
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído!")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

# Teste
url = input("Digite o link do vídeo do YouTube: ")
baixar_video_yt_dlp(url)
