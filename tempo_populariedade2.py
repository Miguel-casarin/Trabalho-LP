import matplotlib.pyplot as plt
import numpy as np

# Seus dados
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

# Separar dados
experiencia = np.array([v[1] for v in linguagens.values()])
popularidade = np.array([v[0] for v in linguagens.values()])
nomes = list(linguagens.keys())

# Criar scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(experiencia, popularidade, color="#FF7F50")

# Adicionar linha de tendência (regressão linear)
coef = np.polyfit(experiencia, popularidade, 1)
poly1d_fn = np.poly1d(coef)
plt.plot(sorted(experiencia), poly1d_fn(sorted(experiencia)), color="blue", linestyle="--", label="Tendência Linear")

# Legenda
plt.title("Popularidade das Linguagens vs Tempo de Experiência")
plt.xlabel("Tempo Médio de Experiência (anos)")
plt.ylabel("Frequência (Popularidade)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
