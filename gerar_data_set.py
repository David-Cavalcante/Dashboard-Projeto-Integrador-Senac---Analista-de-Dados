import pandas as pd
import numpy as np
from datetime import date, timedelta
import random

np.random.seed(42)
random.seed(42)

n = 2000  # número de registros

categorias = {
    "Eletrônicos": ["Smartphone", "Notebook", "Fone de Ouvido", "Tablet", "Smartwatch"],
    "Vestuário": ["Camiseta", "Calça Jeans", "Tênis", "Vestido", "Jaqueta"],
    "Alimentos": ["Café Premium", "Whey Protein", "Azeite Importado", "Chocolate Belga", "Granola"],
    "Casa & Decoração": ["Luminária", "Tapete", "Quadro Decorativo", "Vaso", "Almofada"]
}

precos = {
    "Smartphone": 1800, "Notebook": 3500, "Fone de Ouvido": 350, "Tablet": 1200, "Smartwatch": 800,
    "Camiseta": 59, "Calça Jeans": 149, "Tênis": 299, "Vestido": 189, "Jaqueta": 249,
    "Café Premium": 45, "Whey Protein": 189, "Azeite Importado": 79, "Chocolate Belga": 35, "Granola": 28,
    "Luminária": 129, "Tapete": 299, "Quadro Decorativo": 189, "Vaso": 89, "Almofada": 69
}

estados = ["SP", "RJ", "MG", "BA", "RS", "PR", "CE", "PE", "GO", "SC"]
cidades_por_estado = {
    "SP": ["São Paulo", "Campinas", "Santos"], "RJ": ["Rio de Janeiro", "Niterói", "Petrópolis"],
    "MG": ["Belo Horizonte", "Uberlândia", "Juiz de Fora"], "BA": ["Salvador", "Feira de Santana", "Vitória da Conquista"],
    "RS": ["Porto Alegre", "Caxias do Sul", "Pelotas"], "PR": ["Curitiba", "Londrina", "Maringá"],
    "CE": ["Fortaleza", "Juazeiro do Norte", "Caucaia"], "PE": ["Recife", "Caruaru", "Olinda"],
    "GO": ["Goiânia", "Anápolis", "Aparecida de Goiânia"], "SC": ["Florianópolis", "Joinville", "Blumenau"]
}

nomes = [f"Cliente_{i:04d}" for i in range(1, 501)]
formas_pagamento = ["Cartão de Crédito", "PIX", "Boleto", "Dinheiro"]

data_inicio = date(2024, 1, 1)
registros = []

for i in range(1, n + 1):
    cat = random.choice(list(categorias.keys()))
    prod = random.choice(categorias[cat])
    estado = random.choice(estados)
    cidade = random.choice(cidades_por_estado[estado])
    qtd = random.randint(1, 5)
    valor_unit = precos[prod] * np.random.uniform(0.9, 1.1)
    desconto = round(random.choice([0, 0, 0, 0.05, 0.10, 0.15, 0.20]), 2)
    valor_total = round(qtd * valor_unit * (1 - desconto), 2)
    dias = random.randint(0, 364)
    data_venda = data_inicio + timedelta(days=dias)
    id_cliente = random.randint(1, 500)
    nome = f"Cliente_{id_cliente:04d}"
    avaliacao = random.choices([1, 2, 3, 4, 5], weights=[2, 5, 15, 40, 38])[0]
    pagamento = random.choices(formas_pagamento, weights=[45, 30, 15, 10])[0]

    registros.append({
        "id_venda": i,
        "data_venda": data_venda,
        "id_cliente": id_cliente,
        "nome_cliente": nome,
        "cidade": cidade,
        "estado": estado,
        "categoria": cat,
        "produto": prod,
        "quantidade": qtd,
        "valor_unitario": round(valor_unit, 2),
        "desconto": desconto,
        "valor_total": valor_total,
        "forma_pagamento": pagamento,
        "avaliacao_cliente": avaliacao
    })

# Inserir alguns valores nulos propositalmente para o exercício de limpeza
df = pd.DataFrame(registros)
indices_nulos = np.random.choice(df.index, size=40, replace=False)
df.loc[indices_nulos[:20], "avaliacao_cliente"] = np.nan
df.loc[indices_nulos[20:], "desconto"] = np.nan

df.to_csv("vendas_varejo_facil.csv", index=False, encoding="utf-8-sig")
print(f"Dataset gerado com {len(df)} registros.")
print(df.head())