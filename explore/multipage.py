from mp_resource import abstract_text, overview_text, methods_text, results_text, further_text
import streamlit as st

st.title("Remote Sensing Image Scene Classification: Benchmark and State of the Art")

nav = st.sidebar.radio("Menu", ["Abstract", "Overview", "Methods",
                                "Results", "Further Research"], index=0)

if nav == "Abstract":
    st.write("## Abstract")
    st.text(abstract_text)
if nav == "Overview":
    st.write("## Overview")
    st.text(overview_text)
elif nav == "Methods":
    st.write("## Methods")
    st.text(methods_text)
elif nav == "Results":
    st.write("## Results")
    st.text(results_text)
elif nav == "Further Research":
    st.write("## Further Research")
    st.text(further_text)
