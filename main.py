import streamlit as st
# import pandas as pd
from infos import info
from selecao_dia import selecao_dia



with st.sidebar:
    st.write("sidebar yeah!")











st.write("""
# Holy Hour
""")

# load data into a DataFrame object:
# df = pd.DataFrame(data)


lista_paroquias = [info[i]["nome"] for i in info]

option = st.selectbox('Selecione uma Paróquia', lista_paroquias)

print(info[lista_paroquias.index(option)]["seg"])
print(len(info[lista_paroquias.index(option)]["seg"]))

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"])
for i in info[lista_paroquias.index(option)]["dom"]:
    tab1.write(i)
for i in info[lista_paroquias.index(option)]["seg"]:
    tab2.write(i)
for i in info[lista_paroquias.index(option)]["ter"]:
    tab3.write(i)
for i in info[lista_paroquias.index(option)]["qua"]:
    tab4.write(i)
for i in info[lista_paroquias.index(option)]["qui"]:
    tab5.write(i)
for i in info[lista_paroquias.index(option)]["sex"]:
    tab6.write(i)
for i in info[lista_paroquias.index(option)]["sab"]:
    tab7.write(i)

st.text("""
⛪
⛪
⛪
""")
 selecao_dia()


# print(lista_horarios_dom)
# print(info[0]["nome"])
# for i in info:
#     print(info[i]["nome"])

