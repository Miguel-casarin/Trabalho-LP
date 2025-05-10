from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

# 1. Lê o arquivo
with open("arquivo_maiusculo.txt", "r", encoding="utf-8") as f:
    texto = f.read()

# 2. Deixa tudo em maiúsculas
texto = texto.upper()

# 3. Remove pontuação e separa as palavras
for p in ",.;:!?":
    texto = texto.replace(p, "")
palavras = texto.split()

# 4. Conta frequência das palavras
contagem = Counter(palavras)
contagem_ordenada = contagem.most_common()

# 5. DataFrame com todas as palavras
total_palavras = sum(contagem.values())
dados = [(palavra, freq, freq / total_palavras * 100) for palavra, freq in contagem_ordenada]
df = pd.DataFrame(dados, columns=["Palavra", "Frequência", "Porcentagem"])

# 6. Prepara dados para gráfico de pizza (5 + outras)
mais_comuns = contagem_ordenada[:5]
usadas = sum(freq for _, freq in mais_comuns)
restante = total_palavras - usadas

labels_pizza = [item[0] for item in mais_comuns]
valores_pizza = [item[1] for item in mais_comuns]
if restante > 0:
    labels_pizza.append("OUTRAS")
    valores_pizza.append(restante)

cores = [
    "#826AED", "#C879FF", "#FFC09F", "#8AE9C1", "#9EE493", "#ACECF7"
]

# 7. Cria subplots lado a lado
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Gráfico de Pizza
axs[0].pie(valores_pizza, labels=labels_pizza, autopct="%1.1f%%", startangle=90, colors=cores)
axs[0].set_title("Linguagens mais usadas (Top 5 + Outras)")
axs[0].axis("equal")

# Gráfico de Barras
axs[1].bar(df["Palavra"], df["Porcentagem"], color="#826AED")

axs[1].set_xlabel("Palavras")
axs[1].set_ylabel("Porcentagem (%)")

axs[1].tick_params(axis='x', rotation=90)

plt.tight_layout()
plt.show()
