import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Dashboard Fitossanitário para Videiras", layout="wide")

# Estilo futurista e clean
st.markdown("""
    <style>
    body {
        background-color: #0f1117;
        color: #e5e5e5;
        font-family: 'Segoe UI', sans-serif;
    }
    .main .block-container {
        padding-top: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1c1f26;
        border-radius: 10px;
        margin: 0 0.5rem;
        padding: 0.8rem;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #282c34;
    }
    .stTabs [aria-selected="true"] {
        background-color: #343a40;
        border-bottom: 3px solid #5eead4;
    }
    </style>
""", unsafe_allow_html=True)

# Abas do dashboard
tabs = st.tabs([
    "\U0001F3E0 Visão Geral Técnica",
    "\U0001F327 Clima & Janela de Pulverização",
    "\U0001F9A0 Risco de Doenças & Modelos Epidemiológicos",
    "\U0001F4DE Registro de Aplicações & Histórico",
    "\U0001F4C8 Análises Técnicas & Comparativos",
    "\U0001F4DA Guia Técnico & Ajuda"
])

# Aba 1: Visão Geral Técnica
with tabs[0]:
    st.title("\U0001F3E0 Visão Geral Técnica")
    st.markdown("""
    ### Diagnóstico Integrado da Lavoura
    Exibe informações em tempo real com interpretação automática:
    - Clima atual, risco por doença e tempo desde última aplicação.
    - Códigos de cores para status fitossanitário: ✅ Estável | ⚠️ Atenção | ❌ Ação urgente.
    - Cards de recomendação técnica baseados em dados.
    """)

# Aba 2: Clima & Janela de Pulverização
with tabs[1]:
    st.title("\U0001F327 Clima & Janela de Pulverização")
    st.markdown("""
    ### Condições Climáticas e Eficiência de Aplicação
    Avalia a melhor janela de aplicação considerando:
    - Previsão para 7 dias (chuva, T°, umidade, vento).
    - Sobreposição de clima e tempo residual de produtos.
    - Horário ideal para aplicação com baixa perda.
    """)
    
    # Exemplo de gráfico fictício
    dias = pd.date_range(start="2025-07-15", periods=7)
    chuva = np.random.randint(0, 20, size=7)
    fig = px.bar(x=dias, y=chuva, labels={'x': 'Data', 'y': 'Precipitação (mm)'}, title="Previsão de Chuva (7 dias)")
    st.plotly_chart(fig, use_container_width=True)

# Aba 3: Risco de Doenças
with tabs[2]:
    st.title("\U0001F9A0 Risco de Doenças & Modelos Epidemiológicos")
    st.markdown("""
    ### Modelagem Epidemiológica e Nível de Risco
    Exibe curvas de risco com base em:
    - Clima (T°, umidade, molhamento foliar)
    - Estádio fenológico atual
    - Tipo de produto mais indicado (protetor/sistêmico)
    """)
    
    # Exemplo de curva de risco
    risco = np.random.rand(7) * 100
    fig2 = px.line(x=dias, y=risco, labels={'x': 'Data', 'y': 'Risco (%)'}, title="Risco Estimado para Míldio")
    st.plotly_chart(fig2, use_container_width=True)

# Aba 4: Registro de Aplicações
with tabs[3]:
    st.title("\U0001F4DE Registro de Aplicações & Histórico")
    st.markdown("""
    ### Controle de Aplicações e Avaliação de Eficiência
    Registra todas as intervenções:
    - Produto, dose, data, alvo, clima pós-aplicação.
    - Upload de fotos e anotações.
    - Linha do tempo de eficiência técnica.
    """)
    dados_ficticios = pd.DataFrame({
        'Data': pd.date_range(start="2025-07-01", periods=5),
        'Produto': ['Trichoderma', 'Cobre', 'Isaria', 'Bacillus', 'Mancozeb'],
        'Doença-Alvo': ['Míldio', 'Oídio', 'Botrytis', 'Míldio', 'Oídio']
    })
    st.dataframe(dados_ficticios)

# Aba 5: Análises Técnicas
with tabs[4]:
    st.title("\U0001F4C8 Análises Técnicas & Comparativos")
    st.markdown("""
    ### Avaliação Comparativa de Produtos e Manejos
    Permite comparar a performance por safra, talhão ou fase fenológica:
    - Eficiência média
    - Correlação clima x doença
    - Exportação de relatórios técnicos
    """)

# Aba 6: Guia Técnico
with tabs[5]:
    st.title("\U0001F4DA Guia Técnico & Ajuda")
    st.markdown("""
    ### Manual de Uso
    - Cada aba inclui um botão "Como usar esta aba?"
    - Glossário técnico com termos comuns
    - Tutoriais em vídeo e orientações para interpretação de gráficos
    """)
    st.info("Em breve: vídeos interativos e glossário completo.")
