import pandas as pd

dados_pacientes = pd.read_json('pacientes.json')
dados_pacientes

dados_pacientes_2 = pd.read_json('pacientes_2.json')
dados_pacientes_2

df_normalizado = pd.json_normalize(dados_pacientes_2['Pacientes'])
df_normalizado

df_normalizado.to_json('pacientes_2_normalizado.json')

# %%