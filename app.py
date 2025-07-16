import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="Dashboard Fitossanitário para Videiras", layout="wide")

# Estilo renovado: mais moderno, profissional e com imagens
st.markdown("""
    <style>
    body {
        background-color: #f4f6f9;
        color: #1c1c1e;
        font-family: 'Segoe UI', sans-serif;
    }
    .block-container {
        padding: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        border-radius: 10px;
        margin: 0 0.5rem;
        padding: 1rem;
        border: 1px solid #ddd;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #e6f7ff;
    }
    .stTabs [aria-selected="true"] {
        background-color: #cce5ff;
        border-bottom: 4px solid #1e88e5;
    }
    </style>
""", unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1600694322840-e50ec0fd1d6f", caption="Monitoramento fitossanitário em tempo real", use_column_width=True)

# Abas principais
tabs = st.tabs([
    "🏠 Visão Geral Técnica",
    "🌦️ Clima Atual",
    "💨 Janela de Pulverização",
    "🦠 Risco de Doenças",
    "📄 Aplicações & Histórico",
    "📊 Análises Técnicas",
    "📘 Guia Técnico & Suporte"
])

# Aba 1: Visão Geral Técnica
with tabs[0]:
    st.title("🏠 Diagnóstico Integrado da Lavoura")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Última Pulverização", "10/07/2025")
        st.metric("Risco Atual - Míldio", "Alto", delta="+25%")
    with col2:
        st.success("Situação Geral: Atenção")

    st.markdown("""
    Painel inteligente com base em clima, doença e manejo recente:
    - Alertas automatizados
    - Cards com recomendações rápidas
    - Análise integrada por talhão e produto
    """)
    st.image("https://images.unsplash.com/photo-1615911542565-5d8b4d32c56a", caption="Status atual da lavoura", use_column_width=True)

# Aba 2: Clima Atual
with tabs[1]:
    st.title("🌦️ Monitoramento Climático - 7 Dias")
    dias = pd.date_range(datetime.today(), periods=7)
    clima_df = pd.DataFrame({
        'Data': dias,
        'Chuva (mm)': np.random.randint(0, 30, size=7),
        'Temperatura (°C)': np.random.uniform(15, 30, size=7),
        'Vento (km/h)': np.random.uniform(2, 15, size=7),
        'Umidade (%)': np.random.uniform(60, 95, size=7)
    })

    st.markdown("""
    Condições meteorológicas dos próximos dias para tomada de decisão agronômica.
    """)
    st.line_chart(clima_df.set_index("Data"))

# Aba 3: Janela de Pulverização
with tabs[2]:
    st.title("💨 Janela Ideal para Pulverização")
    st.markdown("""
    Avaliação técnica dos horários mais seguros para aplicação considerando:
    - Velocidade do vento
    - Previsão de chuva
    - Eficiência estimada da calda
    """)

    horas = [f"{h}:00" for h in range(6, 19)]
    vento = np.random.uniform(1, 12, len(horas))
    chuva_chance = np.random.uniform(0, 0.6, len(horas)) * 100

    janela_df = pd.DataFrame({
        'Hora': horas,
        'Velocidade do Vento (km/h)': vento,
        'Chance de Chuva (%)': chuva_chance
    })

    fig = px.line(janela_df, x='Hora', y='Velocidade do Vento (km/h)', markers=True)
    fig.add_scatter(x=janela_df['Hora'], y=janela_df['Chance de Chuva (%)'], mode='lines+markers', name='Chuva (%)')
    st.plotly_chart(fig, use_container_width=True)

# Aba 4: Doenças
with tabs[3]:
    st.title("🦠 Modelos Epidemiológicos de Risco")
    risco = np.clip(np.random.normal(60, 20, 7), 0, 100)
    fig2 = px.area(x=dias, y=risco, title="Risco de Infecção por Botrytis", labels={'x': 'Data', 'y': 'Risco (%)'})
    st.plotly_chart(fig2, use_container_width=True)

# Aba 5: Aplicações
with tabs[4]:
    st.title("📄 Histórico de Aplicações e Eficiência")
    aplicacoes = pd.DataFrame({
        'Data': pd.date_range("2025-06-20", periods=4),
        'Produto': ['Cobre', 'Isaria', 'Trichoderma', 'Captan'],
        'Doença Alvo': ['Míldio', 'Botrytis', 'Oídio', 'Míldio'],
        'Eficácia (%)': [75, 88, 92, 70]
    })
    st.dataframe(aplicacoes)
    st.bar_chart(aplicacoes.set_index("Data")["Eficácia (%)"])

# Aba 6: Análises Técnicas
with tabs[5]:
    st.title("📊 Avaliação de Produtos e Clima")
    st.markdown("""
    Comparação entre produtos, variações climáticas e surtos por safra:
    - Exportação de relatórios
    - Índice de Eficiência Técnica (IET)
    - Comparativo de talhões e fases
    """)

# Aba 7: Guia Técnico
with tabs[6]:
    st.title("📘 Manual e Suporte Técnico")
    st.markdown("""
    > 🧠 **Como usar o dashboard:**
    - Navegue entre abas para visualizar clima, doenças e histórico
    - Clique nos ícones ℹ️ para entender cada gráfico
    - Ajuste o modo para técnico ou produtor (em breve)
    
    Em breve:
    - Vídeos explicativos
    - Diagnóstico visual por imagem
    - Chatbot agronômico para dúvidas
    """)