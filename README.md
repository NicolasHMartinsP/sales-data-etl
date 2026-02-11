# Consolidador de Pedidos (ETL)

Este projeto é um script em Python que automatiza a consolidação de múltiplos arquivos de pedidos em Excel.

## 🚀 O que ele faz
- Varre a pasta em busca de arquivos `Pedidos*.xlsx`.
- Lê todas as abas de cada arquivo (não apenas a primeira).
- Limpa e padroniza os nomes das lojas baseados no nome do arquivo.
- Gera um arquivo único `Pedidos_Geral_TodasAbas.csv` pronto para uso (ex: no AppSheet).

## 🛠️ Tecnologias
- Python
- Pandas
- OpenPyXL

## 📦 Como usar
1. Coloque os arquivos `.xlsx` na mesma pasta do script.
2. Execute o script:
   ```bash
   python processar_pedidos.py
