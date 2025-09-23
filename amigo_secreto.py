import streamlit as st
import random
import time

st.set_page_config(page_title="Amigo Secreto / Secret Santa - Made For Deyanira Cerda", page_icon="🎁")

# 🌐 Idioma
idioma = st.radio("Idioma / Language", ["Español", "English"])

# 📝 Estado
if "historial" not in st.session_state:
    st.session_state.historial = []

if "nombres_restantes" not in st.session_state:
    st.session_state.nombres_restantes = []

if "nombres_input" not in st.session_state:
    st.session_state.nombres_input = ""

# 🎯 Título
titulo = "🎁 Tombola de Amigo Secreto" if idioma == "Español" else "🎁 Secret Santa Draw"
st.title(titulo)

# 🧑‍🤝‍🧑 Entrada de nombres
placeholder = "Ej: Ana, Luis, Pedro, Carla" if idioma == "Español" else "E.g.: Ana, Luis, Peter, Carla"
st.session_state.nombres_input = st.text_area(
    "Ingresa los nombres separados por coma" if idioma == "Español" else "Enter names separated by commas",
    value=st.session_state.nombres_input,
    placeholder=placeholder
)

# 📋 Botón para mostrar lista
if st.button("📋 Ver lista de participantes" if idioma == "Español" else "📋 Show participant list"):
    nombres = [n.strip() for n in st.session_state.nombres_input.split(",") if n.strip()]
    if nombres:
        st.session_state.nombres_restantes = nombres.copy()
        st.subheader("🎯 Lista de participantes" if idioma == "Español" else "🎯 Participant list")
        st.write(nombres)
    else:
        st.warning("⚠️ Ingresa al menos un nombre." if idioma == "Español" else "⚠️ Please enter at least one name.")

# 🎲 Botón de sorteo
if st.button("🎡 Sortear Amigo Secreto" if idioma == "Español" else "🎡 Draw Secret Santa"):
    if st.session_state.nombres_restantes:
        with st.spinner("Girando la ruleta..." if idioma == "Español" else "Spinning the wheel..."):
            time.sleep(2)
        elegido = random.choice(st.session_state.nombres_restantes)
        st.session_state.historial.append(elegido)
        st.session_state.nombres_restantes.remove(elegido)
        st.success(f"🎉 ¡Tu amigo secreto es: **{elegido}**!" if idioma == "Español" else f"🎉 Your Secret Santa is: **{elegido}**")
    else:
        st.warning("⚠️ Ya se han sorteado todos los nombres." if idioma == "Español" else "⚠️ All names have already been drawn.")

# 📜 Historial
if st.session_state.historial:
    st.subheader("📜 Historial de sorteos" if idioma == "Español" else "📜 Draw history")
    st.write(st.session_state.historial)

# 📤 Exportar (simulado)
if st.session_state.historial:
    if st.button("📤 Exportar resultados" if idioma == "Español" else "📤 Export results"):
        st.info("✅ Resultados exportados (simulado)" if idioma == "Español" else "✅ Results exported (simulated)")

# 🔄 Botón de reinicio
if st.button("🔄 Reiniciar juego" if idioma == "Español" else "🔄 Reset game"):
    st.session_state.historial = []
    st.session_state.nombres_restantes = []
    st.session_state.nombres_input = ""
    st.rerun()