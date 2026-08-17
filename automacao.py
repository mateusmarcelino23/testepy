from pathlib import Path # importa o pathlib pra organização de arquivos
import shutil # o shutil ajuda a mover arquivos e pastas com segurança

pasta_home = Path.home() # cria variável da pasta principal da área de trabalho


def idiomas_pasta(nome_en, nome_pt): # função para lidar com idiomas diferentes do sistema
    caminho_en = pasta_home / nome_en
    caminho_pt = pasta_home / nome_pt
    return caminho_en if caminho_en.exists() else caminho_pt # se o o idioma das pastas não estiverem em inglês, analisar em português

pasta_docs = idiomas_pasta("Documents", "Documentos")
pasta_pics = idiomas_pasta("Pictures", "Imagens")
pasta_vids = idiomas_pasta("Videos", "Vídeos")
pasta_mus = idiomas_pasta("Music", "Música")
pasta_down = idiomas_pasta("Downloads", "Downloads") # usando a função para encontrar o nome das pastas de acordo com o idioma

ORGANIZACAO = { # dicionário para listar a organização das pastas de acordo com os sufixos dos arquivos
    ".txt": pasta_docs,
    ".pdf": pasta_docs,
    ".docx": pasta_docs,
    ".jpg": pasta_pics,
    ".png": pasta_pics,
    ".mp4": pasta_vids,
    ".mp3": pasta_mus
}

pastas_para_organizar = [pasta_docs, pasta_pics, pasta_vids, pasta_mus, pasta_down] # lista de pastas a serem analisadas

for pasta_atual in pastas_para_organizar: # Pega todas as pastas para realizar o script, uma por uma
    if not pasta_atual.exists(): 
        continue # se uma delas não existe, o script ignora e continua

    print(f"\n--- Verificando: {pasta_atual.name} ---") # mostra no terminal a verificação das pastas para orgaizar os arquivos

    for item in pasta_atual.iterdir(): # inicia a análise de todos os itens da pasta atual
        if item.is_file(): # se o item analisado for um arquivo
            extencao = item.suffix.lower() # variável para pegar os sufixos dos arquivos

            if extencao in ORGANIZACAO: # se o sufixo de um arquivo da pasta estiver no dicionário de organização
                pasta_destino = ORGANIZACAO[extencao] # ação para mover o arquivo para a pasta correta

                if item.parent == pasta_destino: # se o arquivo estiver na pasta correta, ele pode continuar nela
                    continue

                pasta_destino.mkdir(parents=True, exist_ok=True) # Criar a pasta de destino caso ela não exista

                novo_caminho = pasta_destino / item.name # define o caminho final do arquivo

                shutil.move(item, novo_caminho) # move o arquivo pro novo caminho
                print(f"{item.name} movido com sucesso de {pasta_atual} para {pasta_destino}!")