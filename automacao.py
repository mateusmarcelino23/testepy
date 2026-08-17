from pathlib import Path # importa o pathlib pra organização de arquivos

pasta_home = Path.home() # cria variável da pasta principal da área de trabalho
area_de_trabalho = pasta_home / "Desktop" # cria outra variável para destacar a página "Desktop da área de trabalho" 

ORGANIZACAO = { # dicionário para listar a organização das pastas de acordo com os sufixos dos arquivos
    ".txt": pasta_home / "Documents",
    ".pdf": pasta_home / "Documents",
    ".docx": pasta_home / "Documents",
    ".jpg": pasta_home / "Pictures",
    ".png": pasta_home / "Pictures",
    ".mp4": pasta_home / "Videos",
    ".mp3": pasta_home / "Music"
}

for item in area_de_trabalho.iterdir(): # Lista e processa todos os itens da Área de Trabalho
    if item.is_file(): # "Se o item da área de trabalho for um arquivo"
        extensao = item.suffix # variável que pega os sufixos do item (arquivo)
        if extensao in ORGANIZACAO:
            pasta_destino = ORGANIZACAO[extensao]
            pasta_destino.mkdir(exist_ok=True) # ação para garantir que o arquivo com sufixo presente no dicionário seja movido para a pasta correta

            novo_caminho = pasta_destino / item.name
            item.rename(novo_caminho) # ação para ajustar o caminho novo do arquivo na área de trabalho

            print(f"Movendo {item.name} para {pasta_destino.name}") # mostra os arquivos que estão sendo movidos no terminal

        else:
            print(f"Extensão {extensao} não reconhecida. Arquivo {item.name} não será movido.") # arquivos com sufixos não presentes no dicionário não serão movidos