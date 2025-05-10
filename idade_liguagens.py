from collections import Counter
import matplotlib.pyplot as plt

# Leitura e pré-processamento do texto
with open("arquivo_maiusculo.txt", "r", encoding="utf-8") as f:
    texto = f.read()

texto = texto.upper()
for p in ",.;:!?":
    texto = texto.replace(p, "")
palavras = texto.split()

# Contagem de frequência
contagem = Counter(palavras)
contagem_ordenada = contagem.most_common()

# Mapeamento dos anos de criação
anos_criacao = {
    "PHP": 1995, "JAVA": 1995, "C": 1972, "JAVASCRIPT": 1995,
    "PYTHON": 1991, "TYPESCRIPT": 2012, "C#": 2000, "DELPHI": 1995,
    "COBOL": 1959, "GOLANG": 2009, "SALESFORCE_APEX": 2006,
    "FLUTTER": 2017, "BASH_SCRIPT": 1989, "C++": 1985,
    "RUBY": 1995, "PASCAL": 1970
}

# Preparação dos dados para o gráfico
anos = []
freqs = []
nomes = []

for palavra, freq in contagem_ordenada:
    if palavra in anos_criacao:
        anos.append(anos_criacao[palavra])
        freqs.append(freq)
        nomes.append(palavra)

# Gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(anos, freqs, color="purple")

# Adiciona os nomes das linguagens
for x, y, nome in zip(anos, freqs, nomes):
    plt.text(x, y + 0.3, nome, ha='center', fontsize=8)

plt.xlabel("Ano de Criação")
plt.ylabel("Frequência Absoluta")
plt.title("Correlação entre Frequência e Ano de Criação das Linguagens")
plt.grid(True)
plt.tight_layout()
plt.show()
