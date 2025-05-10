import matplotlib.pyplot as plt

# Linguagens com suas frequências (popularidade) e tempo médio de experiência (em anos)
linguagens = {
    "PHP": (13, 2),
    "JAVA": (8, 4),
    "C": (7, 10),
    "JAVASCRIPT": (7, 10),
    "PYTHON": (4, 10),
    "TYPESCRIPT": (3, 4),
    "C#": (2, 10),
    "DELPHI": (2, 10),
    "COBOL": (2, 10),
    "GOLANG": (2, 2),
    "SALESFORCE_APEX": (1, 2),
    "FLUTTER": (1, 10),
    "BASH_SCRIPT": (1, 10),
    "C++": (1, 10),
    "RUBY": (1, 2),
    "PASCAL": (1, 10),
}

# Criar gráfico
plt.figure(figsize=(12, 7))

# Plotar cada linguagem com uma cor única e adicionar à legenda
for nome, (pop, exp) in linguagens.items():
    ponto = plt.scatter(exp, pop, label=nome)  # cria o ponto e registra no rótulo da legenda

# Estilização
plt.title("Popularidade das Linguagens vs Tempo de Experiência")
plt.xlabel("Tempo Médio de Experiência (anos)")
plt.ylabel("Frequência (Popularidade)")
plt.grid(True)

# Adicionar legenda fora do gráfico
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Linguagens")

plt.tight_layout()
plt.show()
