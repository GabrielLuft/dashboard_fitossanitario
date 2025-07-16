import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="Dashboard Fitossanitário para Videiras", layout="wide")

# Estilo mais amigável e interativo para produtores
st.markdown("""
    <style>
    body {
        background-color: #f9fafb;
        font-family: 'Segoe UI', sans-serif;
    }
    .block-container {
        padding: 2rem 2rem 4rem;
    }
    h1, h2, h3 {
        color: #1f2937;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        border-radius: 12px;
        margin: 0 0.5rem;
        padding: 1rem;
        border: 2px solid #cbd5e1;
    }
    .stTabs [aria-selected="true"] {
        background-color: #e0f2fe;
        border-bottom: 4px solid #0284c7;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1600694322840-e50ec0fd1d6f", caption="Painel inteligente para decisões de campo", use_container_width=True)

# Menu lateral simplificado para produtores
st.sidebar.title("Menu do Produtor")
st.sidebar.info("Selecione uma aba acima para começar")
modo = st.sidebar.radio("Modo de Visualização", ["Produtor", "Técnico"], index=0)

# Abas principais organizadas
abas = st.tabs([
    "🏠 Visão Geral",
    "🌦️ Clima Atual",
    "💨 Janela de Pulverização",
    "🦠 Risco de Doenças",
    "📄 Aplicações",
    "📊 Análises",
    "📘 Ajuda"
])

# Aba 1: Visão Geral
with abas[0]:
    st.header("🌿 Visão Geral da Lavoura")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Última Pulverização", "10/07/2025")
        st.metric("Risco Atual: Míldio", "Alto", delta="+25%")
    with col2:
        st.success("Situação: ⚠️ Atenção — monitorar condições")

    st.markdown("""
    Este painel resume as principais informações da lavoura:
    - Condições atuais do tempo
    - Histórico de aplicações
    - Doenças em alerta
    """)

# Aba 2: Clima Atual
with abas[1]:
    st.header("🌦️ Previsão Climática - 7 Dias")
    dias = pd.date_range(datetime.today(), periods=7)
    clima_df = pd.DataFrame({
        'Data': dias,
        'Chuva (mm)': np.random.randint(0, 25, size=7),
        'Temperatura (°C)': np.random.uniform(14, 29, size=7),
        'Vento (km/h)': np.random.uniform(2, 12, size=7),
        'Umidade (%)': np.random.uniform(60, 95, size=7)
    })
    st.line_chart(clima_df.set_index("Data"))

# Aba 3: Janela de Pulverização
with abas[2]:
    st.header("💨 Melhor Horário para Aplicação")
    horas = [f"{h}:00" for h in range(6, 19)]
    vento = np.random.uniform(1, 12, len(horas))
    chuva = np.random.uniform(0, 0.5, len(horas)) * 100
    janela_df = pd.DataFrame({
        'Hora': horas,
        'Vento (km/h)': vento,
        'Chance de Chuva (%)': chuva
    })
    fig = px.line(janela_df, x='Hora', y='Vento (km/h)', markers=True, title="Velocidade do Vento")
    fig.add_scatter(x=janela_df['Hora'], y=janela_df['Chance de Chuva (%)'], mode='lines+markers', name='Chuva (%)')
    st.plotly_chart(fig, use_container_width=True)

# Aba 4: Risco de Doenças
with abas[3]:
    st.header("🦠 Previsão de Doenças")
    risco = np.clip(np.random.normal(60, 20, 7), 0, 100)
    fig2 = px.area(x=dias, y=risco, title="Risco Estimado para Míldio", labels={'x': 'Data', 'y': 'Risco (%)'})
    st.plotly_chart(fig2, use_container_width=True)

# Aba 5: Aplicações
with abas[4]:
    st.header("📄 Histórico de Pulverizações")
    aplicacoes = pd.DataFrame({
        'Data': pd.date_range("2025-06-20", periods=4),
        'Produto': ['Cobre', 'Isaria', 'Trichoderma', 'Captan'],
        'Doença Alvo': ['Míldio', 'Botrytis', 'Oídio', 'Míldio'],
        'Eficácia (%)': [75, 88, 92, 70]
    })
    st.dataframe(aplicacoes)
    st.bar_chart(aplicacoes.set_index("Data")["Eficácia (%)"])

# Aba 6: Análises
with abas[5]:
    st.header("📊 Comparativos Técnicos")
    st.markdown("""
    Analise o desempenho dos produtos e das aplicações em relação às condições climáticas:
    - Eficiência por talhão
    - Comparativo por estação ou variedade
    """)

# Aba 7: Ajuda
with abas[6]:
    st.header("📘 Guia do Usuário")
    st.markdown("""
    > **Como usar este painel:**
    - Navegue pelas abas acima
    - Cada aba possui dados interativos
    - Use os gráficos para entender o momento ideal de ação

    Em breve:
    - Vídeos com tutoriais rápidos
    - Chat de ajuda automatizado
    """)
