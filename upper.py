# 1. Abrir o arquivo em modo leitura
with open("linguagens.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# 2. Transformar todas as palavras em maiúsculas
conteudo_maiusculo = conteudo.upper()

# 3. Exibir ou salvar o resultado (aqui salvando em outro arquivo)
with open("arquivo_maiusculo.txt", "w", encoding="utf-8") as novo_arquivo:
    novo_arquivo.write(conteudo_maiusculo)
