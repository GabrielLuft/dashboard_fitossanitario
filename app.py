import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="Dashboard Fitossanitário - Videiras", layout="wide")

# --- Estilo global e cores de alerta ---
st.markdown("""
    <style>
    body {
        background: #f0f4f8;
        font-family: 'Segoe UI', sans-serif;
        color: #1c1c1e;
    }
    .sidebar .sidebar-content {
        background-color: #e3f2fd;
        padding: 1.5rem;
        border-radius: 12px;
    }
    .metric-label {
        font-weight: 600 !important;
    }
    .alert-high {
        color: #b00020;
        font-weight: 700;
    }
    .alert-medium {
        color: #f57c00;
        font-weight: 700;
    }
    .alert-low {
        color: #2e7d32;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# --- Dados fictícios ---
dias = pd.date_range(datetime.today(), periods=7)
clima = pd.DataFrame({
    'Data': dias,
    'Chuva (mm)': np.random.randint(0, 30, 7),
    'Temperatura (°C)': np.random.uniform(15, 30, 7),
    'Vento (km/h)': np.random.uniform(2, 15, 7),
    'Umidade (%)': np.random.uniform(60, 95, 7)
})
pulverizacao_horas = [f"{h}:00" for h in range(6, 19)]
vento = np.random.uniform(1, 12, len(pulverizacao_horas))
chuva_chance = np.random.uniform(0, 0.5, len(pulverizacao_horas)) * 100
janela_pulverizacao = pd.DataFrame({
    'Hora': pulverizacao_horas,
    'Vento (km/h)': vento,
    'Chance de Chuva (%)': chuva_chance
})
aplicacoes = pd.DataFrame({
    'Data': pd.date_range("2025-06-20", periods=5),
    'Produto': ['Cobre', 'Isaria', 'Trichoderma', 'Captan', 'Mancozeb'],
    'Doença Alvo': ['Míldio', 'Botrytis', 'Oídio', 'Oídio', 'Míldio'],
    'Eficiência (%)': [75, 88, 92, 70, 76]
})
risco_doenca = np.clip(np.random.normal(65, 20, 7), 0, 100)

# --- Sidebar Navegação ---
st.sidebar.title("📋 Menu Rápido")
menu = st.sidebar.radio("Escolha uma opção:", 
                        ['🏠 Resumo', '💧 Pulverização', '🦠 Riscos e Doenças', '📊 Histórico', '📘 Manual'])

# --- Dashboard principal ---
if menu == '🏠 Resumo':
    st.title("🌿 Resumo da Lavoura - Visão Geral")
    col1, col2, col3 = st.columns(3)
    col1.metric("Última Pulverização", "10/07/2025")
    risco_nivel = 'Alto'
    col2.metric("Risco Atual de Míldio", risco_nivel)
    if risco_nivel == 'Alto':
        col2.markdown('<p class="alert-high">⚠️ Atenção: risco elevado!</p>', unsafe_allow_html=True)
    col3.success("Recomendação: Aguardar 12h antes da próxima aplicação")

    st.markdown("### Previsão Climática para os Próximos 7 Dias")
    st.line_chart(clima.set_index('Data')[['Chuva (mm)', 'Temperatura (°C)', 'Umidade (%)']])

elif menu == '💧 Pulverização':
    st.title("💧 Janela Ideal para Pulverização")
    st.markdown("Avalie os melhores horários para aplicação considerando vento e chuva.")
    fig = px.line(janela_pulverizacao, x='Hora', y='Vento (km/h)', markers=True, title="Velocidade do Vento")
    fig.add_scatter(x=janela_pulverizacao['Hora'], y=janela_pulverizacao['Chance de Chuva (%)'], mode='lines+markers', name='Chance de Chuva (%)')
    st.plotly_chart(fig, use_container_width=True)

elif menu == '🦠 Riscos e Doenças':
    st.title("🦠 Risco Estimado de Doenças")
    st.markdown("Previsão do risco para oídio baseado nas condições climáticas e fenologia.")
    fig_risco = px.area(x=dias, y=risco_doenca, labels={'x':'Data', 'y':'Risco (%)'}, title="Risco de Oídio")
    st.plotly_chart(fig_risco, use_container_width=True)

elif menu == '📊 Histórico':
    st.title("📊 Histórico de Aplicações e Eficiência")
    st.dataframe(aplicacoes)
    st.bar_chart(aplicacoes.set_index('Data')['Eficiência (%)'])

elif menu == '📘 Manual':
    st.title("📘 Manual de Uso do Dashboard")
    st.markdown("""
    ### Como usar este painel:
    - Navegue pelo menu lateral para acessar as informações rapidamente.
    - Na aba 'Resumo' acompanhe os dados mais importantes da lavoura.
    - Em 'Pulverização' veja a janela ideal para aplicação.
    - Em 'Riscos e Doenças' monitore o risco das principais doenças.
    - No 'Histórico' consulte o desempenho dos produtos aplicados.
    
    Para dúvidas, entre em contato com seu técnico agrícola.
    """)
