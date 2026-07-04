import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header("Previsão de Vendas")

# Dados: [Investimento em Marketing] -> Faturamento
dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

# Exibe o gráfico de dispersão com os dados reais
st.scatter_chart(dados_vendas, x='investimento', y='faturamento')

# Cria e treina o modelo de Regressão Linear do scikit-learn
modelo_vendas = LinearRegression()
modelo_vendas.fit(dados_vendas[['investimento']], dados_vendas['faturamento'])

# Cria um slider interativo para o usuário escolher o valor do investimento
investimento_usuario = st.slider('Investimento em Marketing (R$)', 0, 1000, 300)

# Realiza a previsão do faturamento baseado no valor do slider
faturamento_previsto = modelo_vendas.predict([[investimento_usuario]])

# Exibe o resultado na tela utilizando um componente de métrica do Streamlit
st.metric('Faturamento Estimado', faturamente_formatado := f'R$ {faturamento_previsto[0]:.2f}')