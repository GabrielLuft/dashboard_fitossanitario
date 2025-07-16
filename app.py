import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="Dashboard Agrícola de Videiras", layout="wide")

# Estilo moderno e profissional
def estilo_global():
    st.markdown("""
        <style>
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f0f4f8;
        }
        .stTabs [data-baseweb="tab"] {
            background-color: #ffffff;
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 10px;
            margin-right: 10px;
        }
        .stTabs [aria-selected="true"] {
            background-color: #dbeafe;
            border-bottom: 4px solid #2563eb;
        }
        </style>
    """, unsafe_allow_html=True)

estilo_global()

# Abas reorganizadas
abas = st.tabs([
    "🌿 Início",
    "📡 Clima & Ambiente",
    "🛡️ Doenças e Riscos",
    "💧 Pulverizações",
    "📊 Desempenho Técnico",
    "📘 Ajuda e Manual"
])

# Aba 1 - Início
with abas[0]:
    st.title("🌿 Painel Inicial - Situação da Lavoura")
    st.markdown("""
    Esta página resume os principais indicadores da sua lavoura:
    - Última aplicação
    - Nível atual de risco
    - Recomendação rápida
    """)
    col1, col2, col3 = st.columns(3)
    col1.metric("Última Aplicação", "10/07/2025")
    col2.metric("Risco Atual - Míldio", "Alto")
    col3.success("Recomendação: Aguardar 12h")
    st.image("https://images.unsplash.com/photo-1600694322840-e50ec0fd1d6f", use_container_width=True)

# Aba 2 - Clima & Ambiente
with abas[1]:
    st.title("📡 Monitoramento Climático e Janela de Aplicação")
    dias = pd.date_range(datetime.today(), periods=7)
    clima = pd.DataFrame({
        'Data': dias,
        'Chuva (mm)': np.random.randint(0, 30, 7),
        'Temp (°C)': np.random.uniform(15, 30, 7),
        'Vento (km/h)': np.random.uniform(2, 14, 7),
        'Umidade (%)': np.random.uniform(60, 90, 7)
    })
    st.subheader("📈 Previsão Climática - 7 dias")
    st.line_chart(clima.set_index("Data"))

    st.subheader("💨 Melhor Horário para Aplicar")
    horas = [f"{h}:00" for h in range(6, 19)]
    vento = np.random.uniform(1, 12, len(horas))
    chuva = np.random.uniform(0, 0.5, len(horas)) * 100
    janela = pd.DataFrame({
        'Hora': horas,
        'Vento (km/h)': vento,
        'Chuva (%)': chuva
    })
    fig = px.line(janela, x='Hora', y='Vento (km/h)', markers=True)
    fig.add_scatter(x=janela['Hora'], y=janela['Chuva (%)'], mode='lines+markers', name='Chuva (%)')
    st.plotly_chart(fig, use_container_width=True)

# Aba 3 - Doenças e Riscos
with abas[2]:
    st.title("🛡️ Modelagem de Doenças")
    st.markdown("Risco previsto com base no clima e estágio da videira")
    risco = np.clip(np.random.normal(65, 20, 7), 0, 100)
    fig_risco = px.area(x=dias, y=risco, labels={'x': 'Data', 'y': 'Risco (%)'}, title="Risco Estimado para Oídio")
    st.plotly_chart(fig_risco, use_container_width=True)

# Aba 4 - Pulverizações
with abas[3]:
    st.title("💧 Histórico de Aplicações")
    dados = pd.DataFrame({
        'Data': pd.date_range("2025-06-15", periods=5),
        'Produto': ['Trichoderma', 'Cobre', 'Bacillus', 'Captan', 'Mancozeb'],
        'Doença-Alvo': ['Míldio', 'Oídio', 'Botrytis', 'Oídio', 'Míldio'],
        'Eficiência (%)': [84, 79, 88, 70, 76]
    })
    st.dataframe(dados)
    st.bar_chart(dados.set_index("Data")["Eficiência (%)"])

# Aba 5 - Desempenho Técnico
with abas[4]:
    st.title("📊 Análise Técnica por Talhão")
    st.markdown("Compare o desempenho técnico por produto ou ciclo")
    st.line_chart(dados.set_index("Data")["Eficiência (%)"])

# Aba 6 - Ajuda
with abas[5]:
    st.title("📘 Manual do Produtor")
    st.markdown("""
    Este painel foi desenvolvido para ajudar você a tomar decisões com base:
    - No clima e nas doenças
    - No histórico das aplicações
    - Na janela ideal de manejo

    Navegue pelas abas acima para visualizar os dados.
    Em breve: vídeos e IA para diagnóstico visual.
    """)
