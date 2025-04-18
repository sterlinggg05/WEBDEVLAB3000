import streamlit as st

# ───────────────────────────────
# Sidebar content
# ───────────────────────────────
st.sidebar.title("🧭 Navigation")
st.sidebar.markdown("""
Use the pages on the sidebar to explore:

- 🧙‍♂ Wizarding Characters  
- ⚔️ Wizarding Duel  
- 🧠 Magic Chatbot  
""")

st.sidebar.divider()

st.sidebar.title("🎓 About This Project")
st.sidebar.markdown("""
- **Course**: CS 1301  
- **Section**: Web Development - Section B  
- **Team 20**  
- **Members**:  
  - Sterling Williams  
  - Hyejin Shim  
  - Nadine Tse  
""")

# ───────────────────────────────
# Main Page content
# ───────────────────────────────
st.title("Wizarding World EXPLORED! - Web Development Lab03")

st.image("images/music.jpg", width=500)

st.header("CS 1301")
st.subheader("Team 20, Web Development - Section B")
st.subheader("Sterling Williams, Hyejin Shim, Nadine Tse")

st.markdown("### 🔮 Welcome to the Wizarding World!")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🧙‍♂ Wizarding Characters")
    st.image("images/characters.jpg", use_container_width=True)
    st.write("""
    Search and explore wizards and witches.  
    Filter by name or gender, and view gender charts.
    """)

with col2:
    st.subheader("⚔️ Wizarding Duel")
    st.image("images/duel.jpg", use_container_width=True)
    st.write("""
    Select two wizards and watch them duel!  
    Gemini AI predicts the magical outcome.
    """)

with col3:
    st.subheader("🧠 Magic Chatbot")
    st.image("images/magic.jpg", use_container_width=True)
    st.write("""
    Ask our Hogwarts-style chatbot anything!  
    Spells, characters, or magical history.
    """)
    
