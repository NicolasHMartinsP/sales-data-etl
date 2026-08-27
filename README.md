# Consolidador de Pedidos (ETL)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Manipulation-150458)
![Status](https://img.shields.io/badge/Status-Concluído-success)

> Um pipeline de ETL (Extração, Transformação e Carga) automatizado para consolidar múltiplas planilhas em uma única base de dados estruturada.

## Problema e Solução

Um banco de dados central era alimentado por diversas filiais que possuíam dezenas de planilhas iguais com várias abas diferentes. Juntar todas em apenas uma principal iria demorar dias e poderia gerar erros. Este script automatiza 100% desse processo em segundos.

## Funcionalidades

- **Busca:** Varre automaticamente o diretório em busca de arquivos padronizados (`Pedidos*.xlsx`), ignorando arquivos já finalizados.
- **Extração:** Lê todas as abas (Sheets) de cada arquivo, não apenas a primeira.
- **Rastreabilidade:** Adiciona colunas indicando a `Nome_Loja` e a `Origem_Aba` de cada linha processada, para não perder o contexto da origem do dado.
- **Tipagem:** Protege dados numéricos com zeros à esquerda (CEPs e SKUs).
- **Interface:** CLI que passa parâmetros sem alterar o código-fonte.
- **Logs Profissionais:** Registra todo o processo e eventuais erros no terminal para fácil monitoramento.
- **Exporta:** Gera um arquivo único pronto para uso (ex: no AppSheet).

## Como usar

### Pré-requisitos

Certifique-se de ter o Python instalado. Clone o repositório e instale as dependências:

```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git

# Entre na pasta
cd SEU_REPOSITORIO

# Instale os requisitos
pip install -r requirements.txt

Coloque os arquivos .xlsx que deseja processar na mesma pasta (ou em uma pasta específica) e rode o script:

Execução Simples (Usa a pasta atual e gera Pedidos_Geral_TodasAbas.csv):
python processar_pedidos.py

Execução Customizada (Escolhendo pasta de entrada e arquivo de saída):
python processar_pedidos.py --entrada ./arquivos_brutos --saida relatorio_final.csv

## Estrutura do Projeto

/
├── processar_pedidos.py    # Script principal do ETL
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação
└── LICENSE                 # Licença do projeto
```
