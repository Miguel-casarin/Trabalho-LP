from collections import Counter
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

# 5. Seleciona as 5 mais comuns
mais_comuns = contagem.most_common(5)

# 6. Calcula "restante"
total = sum(contagem.values())
usadas = sum(freq for _, freq in mais_comuns)
restante = total - usadas

# 7. Prepara dados para o gráfico
labels = [item[0] for item in mais_comuns]
valores = [item[1] for item in mais_comuns]

# Adiciona "Restante" se houver
if restante > 0:
    labels.append("OUTRAS")
    valores.append(restante)

cores = [
    "#826AED",  # Medium Slate Blue
    "#C879FF",  # Heliotrope
    "#FFC09F",  # Peach
    "#8AE9C1",  # Aquamarine
    "#9EE493",  # Russian Violet
    "#ACECF7"   # Usar a mesma para "Restante"
]

# Gráfico de pizza com cores personalizadas
plt.figure(figsize=(6, 6))
plt.pie(valores, labels=labels, autopct="%1.1f%%", startangle=90, colors=cores)
plt.title("Linguagens mais usadas")
plt.axis("equal")
plt.show()

