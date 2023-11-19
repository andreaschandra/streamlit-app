import streamlit as st


st.set_page_config(
    page_title="Stable Diffusion", page_icon=":railway_track:", layout="wide"
)


st.markdown("# :blue[Stable Diffusion XL App]")

# --- Setup Session --- #
if "generated_image" not in st.session_state:
    st.session_state.generated_image = None

# --- Setup Replicate Token --- #
REP_TOKEN = st.secrets["REP_TOKEN"]
REP_ENDPOINT = st.secrets["REP_ENDPOINT"]

# --- Placeholders for Images and Gallery ---#
generated_image_placeholder = st.empty()
gallery_placeholder = st.empty()

# --- Sidebar Elements ---#
with st.sidebar:
    with st.form("sdxl_form"):
        st.info("Menu")
        with st.expander("")
        submitted = st.form_submit_button(
            "Submit", type="primary", use_container_width=True
        )
