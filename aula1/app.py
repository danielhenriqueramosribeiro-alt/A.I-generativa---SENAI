#proconding
#vou usar a biblioteca 

import streamlit as st

st.title ('TITULO H1')

n1 = st.number_input('numero: ')
n2 = st.number_input('numero:', value =0.0)

if st.button('calcular +'):
    soma = n1 + n2
    st.success(soma)

elif st.button('subtração -'):
    subtração = n1 - n2
    st.success(subtração)

elif st.button('divisão /'):
    divisão = n1 / n2
    st.success(divisão)


st.title('DENIAL GRU')

import streamlit as st

st.title("DENNIS SAMPA")

st.write("Preencha os dados abaixo:")

nome = st.text_input("Nome")

idade = st.number_input(
    "Idade",
    min_value=0,
    max_value=120,
    step=1
)

aceitou_termos = st.checkbox("Aceito os termos de uso")

enviar = st.button("Enviar")

if enviar:
    st.subheader("Dados enviados")

    st.write(f"**Nome:** {nome}")
    st.write(f"**Idade:** {idade}")
    st.write(f"**Aceitou os termos:** {aceitou_termos}")

