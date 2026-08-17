from pathlib import Path # importa o pathlib pra organização de arquivos
import shutil # o shutil ajuda a mover arquivos e pastas com segurança

pasta_home = Path.home() # cria variável da pasta principal da área de trabalho

ORGANIZACAO = { # dicionário para listar a organização das pastas de acordo com os sufixos dos arquivos
    ".txt": pasta_home / "Documents",
    ".pdf": pasta_home / "Documents",
    ".docx": pasta_home / "Documents",
    ".jpg": pasta_home / "Pictures",
    ".png": pasta_home / "Pictures",
    ".mp4": pasta_home / "Videos",
    ".mp3": pasta_home / "Music"
}

pastas_para_organizar = { # dicionário com as 5 pastas onde o script vai entrar para procurar arquivos perdidos
    pasta_home / "Documents",
    pasta_home / "Music",
    pasta_home / "Pictures",
    pasta_home / "Videos",
    pasta_home / "Downloads",
}

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