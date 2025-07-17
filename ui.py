import streamlit as st

def render_dropdown(label, options_dict):
    return st.selectbox(label, list(options_dict.keys()))

def render_product_selector():
    return st.selectbox("Select Product Type", [
        "Non-Illuminated Pushbuttons",
        "Non-Illuminated Pushpulls",
        "Illuminated Incandescent Pushpulls",
        "Illuminated LED Pushpulls",
        "Illuminated Incandescent Pushbuttons",
        "Illuminated LED Pushbuttons"
    ])
