import pandas as pd


def limpeza(tabela, indice, coluna, valores):
    a = any(x.lower() in str(tabela[coluna][indice]).lower() for x in valores)
    return a


df = pd.read_csv(r'dados_completos.csv', dtype=str)

print('Passo 1/3')

for idx in df.index:
    a = limpeza(df, idx, 'Estado', ['BR-RS', 'BR-SC', 'BR-PR'])
    if not a:
        df.drop(idx, inplace=True)
        continue

    b = limpeza(df, idx, 'Form Veg', [
                                      'restinga',
                                      ])
    if not b:
        df.drop(idx, inplace=True)

print('Passo 2/3')

df.to_csv('dados_limpos.csv', index=False)

print('Passo 3/3')
