import pandas as pd
import glob
import warnings

warnings.filterwarnings('ignore')

padrao = "Pedidos*.xlsx"

lista_arquivos = [f for f in glob.glob(padrao) if "Final" not in f and not f.endswith(".py")]

print(f"📂 Arquivos encontrados: {lista_arquivos}")

todas_as_tabelas = []
for arquivo in lista_arquivos:
    print(f"\nProcessando arquivo: {arquivo}")
    
    try:
        dict_abas = pd.read_excel(arquivo, sheet_name=None, dtype=str)
        
        for nome_aba, tabela in dict_abas.items():
            print(f"   --> Extraindo aba: '{nome_aba}' | Linhas: {len(tabela)}")
            nome_limpo = arquivo.replace("Pedidos.xlsx - ", "").replace(".csv", "") 
            tabela['Nome_Loja'] = nome_limpo
            tabela['Origem_Aba'] = nome_aba
            
            todas_as_tabelas.append(tabela)
            
    except Exception as e:
        print(f"   ❌ Erro crítico ao ler {arquivo}: {e}")

if len(todas_as_tabelas) > 0:
    print("\n📦 Juntando todas as abas de todos os arquivos...")
    df_final = pd.concat(todas_as_tabelas, ignore_index=True)
    
    arquivo_saida = "Pedidos_Geral_TodasAbas.csv"
    df_final.to_csv(arquivo_saida, index=False)
    
    print(f"✅ SUCESSO ABSOLUTO! Arquivo '{arquivo_saida}' gerado.")
    print(f"📊 Total de linhas processadas: {len(df_final)}")
else:
    print("⚠️ Nenhuma tabela foi encontrada em nenhum arquivo.")