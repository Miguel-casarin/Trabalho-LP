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
mais_comuns = contagem.most_common(20)

# 6. Calcula "restante"
total = sum(contagem.values())
usadas = sum(freq for _, freq in mais_comuns)
restante = total - usadas

# 7. Prepara dados para o gráfico
labels = [item[0] for item in mais_comuns]
valores = [item[1] for item in mais_comuns]

# Adiciona "Restante" se houver
if restante > 0:
    labels.append("RESTANTE")
    valores.append(restante)

# 8. Cria gráfico de pizza
plt.figure(figsize=(6, 6))
plt.pie(valores, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Frequência das Palavras (com Restante)")
plt.axis("equal")
plt.show()
