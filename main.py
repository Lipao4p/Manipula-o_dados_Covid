import pandas as pd

df = pd.read_excel("Base_Ba_Tratada1.xlsx")
df['TESTE_FEITO'] = df['TESTE_FEITO'].map({'Sim': 1, 'Não': 0})
df['CASOS_CONF'] = df['CASOS_CONF'].map({'Sim': 1, 'Não': 0})
df['TENDA_FEITA'] = df['TENDA_FEITA'].map({'Sim': 1, 'Não': 0})
df['INTERN'] = df['INTERN'].map({'Sim': 1, 'Não': 0})
df['FALTOU_LEITO'] = df['FALTOU_LEITO'].map({'Sim': 1, 'Não': 0})
df['HOSP_CAMP'] = df['HOSP_CAMP'].map({'Sim': 1, 'Não': 0})
df['OBTOS'] = df['OBTOS'].map({'Sim': 1, 'Não': 0})

df['TESTE_FEITO'] = pd.to_numeric(df['TESTE_FEITO'])
df['CASOS_CONF'] = pd.to_numeric(df['CASOS_CONF'])
df['TENDA_FEITA'] = pd.to_numeric(df['TENDA_FEITA'])
df['INTERN'] = pd.to_numeric(df['INTERN'])
df['FALTOU_LEITO'] = pd.to_numeric(df['FALTOU_LEITO'])
df['HOSP_CAMP'] = pd.to_numeric(df['HOSP_CAMP'])
df['OBTOS'] = pd.to_numeric(df['OBTOS'])

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

descricao = df.describe().T
print(descricao)
print('-----------------------------------------------------')
print('------ANALISE DE DADOS DOS NUMEROS DA COVID----------')
print('----------------NO ESTADO DA BAHIA------------------')
print('------FAZENDO O LEVANTAMENTO DOS 310 MUNICIPIOS--------')
print('--------------- 1 = SIM   0 = NÃO ---------------------')
print(df[['TESTE_FEITO']].value_counts())

contagem = df['TESTE_FEITO'].value_counts()
porcentagem = contagem /len(df) *100
print(porcentagem)
print('-----------------------------------------------------')
print(df[['CASOS_CONF']].value_counts())

contagem = df['CASOS_CONF'].value_counts()
porcentagem = contagem /len(df) *100
print(porcentagem)
print('-----------------------------------------------------')
print(df[['INTERN']].value_counts())

contagem = df['INTERN'].value_counts()
porcentagem = contagem /len(df) *100
print(porcentagem)
print('-----------------------------------------------------')
print(df[['FALTOU_LEITO']].value_counts())

contagem = df['FALTOU_LEITO'].value_counts()
porcentagem = contagem /len(df) *100
print(porcentagem)
print('-----------------------------------------------------')
print(df[['HOSP_CAMP']].value_counts())

contagem = df['HOSP_CAMP'].value_counts()
porcentagem = contagem /len(df) *100
print(porcentagem)
print('-----------------------------------------------------')
print(df[['OBTOS']].value_counts())

contagem = df['OBTOS'].value_counts()
porcentagem = contagem /len(df) *100
print(porcentagem)



