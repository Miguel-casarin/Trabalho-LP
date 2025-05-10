from collections import Counter
import matplotlib.pyplot as plt

# Leitura e pré-processamento do texto
with open("arquivo_maiusculo.txt", "r", encoding="utf-8") as f:
    texto = f.read()

texto = texto.upper()
for p in ",.;:!?":
    texto = texto.replace(p, "")
palavras = texto.split()

contagem = Counter(palavras)
contagem_ordenada = contagem.most_common()

palavras = [item[0] for item in contagem_ordenada]
frequencias = [item[1] for item in contagem_ordenada]

# Criar gráfico
fig, ax = plt.subplots(figsize=(max(12, len(palavras)//2), 6))
barras = ax.bar(palavras, frequencias, color="#826AED")

# Adicionar rótulos acima das barras
for bar, freq in zip(barras, frequencias):
    altura = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, altura + 1,  # << Aumenta distância vertical
            f"{freq}", ha='center', va='bottom', fontsize=8)

# Ajustar limites do eixo Y com margem extra
ax.set_ylim(0, max(frequencias) + 5)

# Estilização
ax.set_yticks([])

ax.set_title("Frequência Absoluta das Linguagens")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
