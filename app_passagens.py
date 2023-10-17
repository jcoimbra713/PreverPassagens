import pickle
import streamlit as st
import numpy as np

# Carregando a Máquina Preditiva
pickle_in = open('maquina_preditiva_passagens.pkl', 'rb') 
maquina_preditiva_passagens = pickle.load(pickle_in)

# Essa função é para criação da página web
def main():  
    # Elementos da página web
    # Nesse ponto, você deve personalizar o sistema com sua marca
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:white;text-align:center;">PREVISÃO DE PREÇOS DE PASSAGENS AÉREAS</h1> 
    <h2 style ="color:white;text-align:center;">SISTEMA DE PREVISÃO DE PASSAGENS AÉREAS</h2> 
    </div> 
    """
      
    # Função do Streamlit que faz o display da página web
    st.markdown(html_temp, unsafe_allow_html=True) 
      
    # As linhas abaixo criam as caixas nas quais o usuário vai inserir os dados da passagem que deseja prever o preço
    CompanhiaAérea = st.selectbox('Companhia Aérea', ("ASIA", "INDIA","FIRST","INDIGO","SPICEJET","VISTARA"))
    CidadeOrigem = st.selectbox("Cidade de Origem",("BANGALORE","CHENNAI","DELHI","HYDERABAD","KOLKATA","MUMBAI")) 
    CidadeDestino = st.selectbox("Cidade de Destino",("BANGALORE","CHENNAI","DELHI","HYDERABAD","KOLKATA","MUMBAI"))
    ClasseEconomica = st.selectbox('Classe', ("Classe Executiva", "Classe Economica"))
    Paradas = st.selectbox('Paradas', ("NENHUMA", "UMA",'DUAS OU MAIS'))
      
    # Quando o usuário clicar no botão "Verificar", a Máquina Preditiva fará seu trabalho
    if st.button("Verificar"): 
        result = prediction(CompanhiaAérea, CidadeOrigem, CidadeDestino, ClasseEconomica,Paradas) 
        st.success(f'O PREÇO DA PASSAGEM SERÁ DE: {result}')

# Essa função faz a predição usando os dados inseridos pelo usuário
def prediction(CompanhiaAérea, CidadeOrigem, CidadeDestino, ClasseEconomica,Paradas):   
    # Pre-processando a entrada do Usuário    
    
    CompanhiaAérea_dict = {
        "ASIA": 0,
        "INDIA": 1,
        "FIRST": 2,
        "INDIGO": 3,
        "SPICEJET": 4,
        "VISTARA": 5
    }
    CompanhiaAérea = CompanhiaAérea_dict[CompanhiaAérea]

    CidadeOrigem_dict = {
        "BANGALORE": 0,
        "CHENNAI": 1,
        "DELHI": 2,
        "HYDERABAD": 3,
        "KOLKATA": 4,
        "MUMBAI": 5
    }
    CidadeOrigem = CidadeOrigem_dict[CidadeOrigem]

    CidadeDestino_dict = {
        "BANGALORE": 0,
        "CHENNAI": 1,
        "DELHI": 2,
        "HYDERABAD": 3,
        "KOLKATA": 4,
        "MUMBAI": 5
    }
    CidadeDestino = CidadeDestino_dict[CidadeDestino]

    ClasseEconomica_dict = {
        "Classe Executiva": 1,
        "Classe Economica": 0
    }
    ClasseEconomica = ClasseEconomica_dict[ClasseEconomica]

    Paradas_dict = {
        "NENHUMA": 0,
        "UMA": 1,
        "DUAS OU MAIS": 2
    }
    Paradas = Paradas_dict[Paradas]

    # Fazendo a Predição
    parametro = np.array([[CompanhiaAérea, CidadeOrigem, CidadeDestino, ClasseEconomica, Paradas]])
    fazendo_previsao = maquina_preditiva_passagens.predict(parametro)

    return fazendo_previsao[0]

if __name__ == '__main__':
    main()

