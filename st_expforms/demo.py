import streamlit as st
import pandas as pd
st. set_page_config(layout="wide")

choices = st.session_state.setdefault("choices", [])
with st.form("Form F", clear_on_submit=True):
    c1, c2 = st.columns(2)
    with c1:
        with st.expander("Section A", expanded=True):
            x = st.slider("X", min_value=-100, max_value=100, value=0)
    with c2:
        with st.expander("Section B", expanded=True):
            g = ["alpha", "beta", "gamma", "delta"]
            y = st.multiselect("Y", g, g[0])
    with st.expander("Section C", expanded=True):
        z = st.file_uploader("Z")
    c1, c2, c3 = st.columns([10,1,10])
    with c2:
        submitted = st.form_submit_button("Submit")
    if submitted:
        choice = {"X":x, "Y":",".join(y), "Z":None if z is None else z.name }
        choices.append(choice)
        st.write(f"Current choice: {choice}")
  
st.write("History of choices")
df = pd.DataFrame(choices)
st.dataframe(df)