import pandas as pd
import argparse
import logging
from pathlib import Path
from typing import Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)
    # Função para extrair dados de todas as abas 
def extrair_dados_planilha(caminho_arquivo: Path) -> Optional[pd.DataFrame]:
 
    todas_as_abas = []
    
    try:
        # dtype=str preserva os zeros à esquerda em códigos numéricos (ex: CEP, SKU)
        dict_abas = pd.read_excel(caminho_arquivo, sheet_name=None, dtype=str)
        
        for nome_aba, tabela in dict_abas.items():
            if tabela.empty:
                logger.warning(f"Aba '{nome_aba}' do arquivo '{caminho_arquivo.name}' está vazia. Pulando.")
                continue

            nome_limpo = caminho_arquivo.stem.replace("Pedidos - ", "")
            
            tabela['Nome_Loja'] = nome_limpo
            tabela['Origem_Aba'] = nome_aba
            
            todas_as_abas.append(tabela)
            logger.info(f"Extraída aba: '{nome_aba}' com {len(tabela)} linhas.")
            
    except Exception as e:
        logger.error(f"Erro crítico ao ler o arquivo {caminho_arquivo.name}: {e}")
        return None
        
    if todas_as_abas:
        return pd.concat(todas_as_abas, ignore_index=True)
    
    return None
    # Busca e extrai todos os arquivos no diretório de entrada, ignorando arquivos com 'Final' no nome.
def processar_arquivos(diretorio_entrada: Path, nome_padrao: str = "Pedidos*.xlsx") -> Optional[pd.DataFrame]:

    arquivos_encontrados = list(diretorio_entrada.glob(nome_padrao))
    arquivos_validos = [f for f in arquivos_encontrados if "Final" not in f.name]
    
    if not arquivos_validos:
        logger.warning(f"Nenhum arquivo correspondente ao padrão '{nome_padrao}' foi encontrado em {diretorio_entrada}.")
        return None
        
    logger.info(f"Foram encontrados {len(arquivos_validos)} arquivos válidos para processamento.")
    
    tabelas_consolidadas = []
    
    for arquivo in arquivos_validos:
        logger.info(f"Processando arquivo: {arquivo.name}")
        df_arquivo = extrair_dados_planilha(arquivo)
        
        if df_arquivo is not None:
            tabelas_consolidadas.append(df_arquivo)
            
    if tabelas_consolidadas:
        return pd.concat(tabelas_consolidadas, ignore_index=True)
    
    return None
    # Salva o DataFrame em um arquivo CSV
def salvar_dados(df: pd.DataFrame, caminho_saida: Path) -> None:
   
    try:
        df.to_csv(caminho_saida, index=False)
        logger.info(f"SUCESSO! Arquivo '{caminho_saida.name}' gerado com {len(df)} linhas.")
    except Exception as e:
        logger.error(f"Falha ao salvar o arquivo de saída: {e}")

def main():
    # Configuração do parser com base em argparse
    parser = argparse.ArgumentParser(description="Pipeline ETL para consolidação de Pedidos em Excel.")
    
    parser.add_argument(
        "--entrada", 
        type=str, 
        default=".", 
        help="Caminho do diretório contendo os arquivos Excel (default: pasta atual)."
    )
    parser.add_argument(
        "--saida", 
        type=str, 
        default="Pedidos_Geral_TodasAbas.csv", 
        help="Caminho/Nome do arquivo CSV consolidado (default: Pedidos_Geral_TodasAbas.csv)."
    )
    
    args = parser.parse_args()
    
    pasta_entrada = Path(args.entrada)
    arquivo_saida = Path(args.saida)
    
    logger.info("=== Iniciando Pipeline de ETL de Pedidos ===")
    
    df_consolidado = processar_arquivos(pasta_entrada)
    
    if df_consolidado is not None:
        logger.info("Salvando base de dados consolidada...")
        salvar_dados(df_consolidado, arquivo_saida)
    else:
        logger.warning("Pipeline finalizado sem gerar arquivo de saída (dados insuficientes).")

if __name__ == "__main__":
    main()