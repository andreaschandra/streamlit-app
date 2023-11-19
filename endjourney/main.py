"""Streamlit app."""
import io
import replicate
import streamlit as st
import requests
import utils
import zipfile

st.set_page_config(page_title="Endjourney", page_icon=":railway_track:", layout="wide")


st.markdown("# :blue[Endjourney: Stable Diffusion XL App]")

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
        prompt = st.text_area(
            "Prompt",
            value="A potrait of yellow cat sitting near a window looking at the sea",
        )
        negative_prompt = st.text_area("Negative Prompt", value="bad quality, blury")
        with st.expander("Configuration:"):
            width = st.number_input("Width", value=768)
            height = st.number_input("Height", value=768)
            num_outputs = st.slider("# of Images", value=1, min_value=1, max_value=4)
            scheduler = st.selectbox(
                "Scheduler",
                [
                    "DDIM",
                    "DPMSolverMultistep",
                    "HeunDiscrete",
                    "KarrasDPM",
                    "K_EULER_ANCESTRAL",
                    "K_EULER",
                    "PNDM",
                ],
            )
            num_inference_steps = st.slider(
                "# of Inference Steps", value=25, min_value=1, max_value=500
            )
            guidance_scale = st.slider(
                "Guidance Scale", value=8.1, min_value=1.0, max_value=50.0, step=0.1
            )
            prompt_strength = st.slider(
                "Prompt Strength", value=0.8, min_value=0.0, max_value=1.0, step=0.1
            )
            random_seed = st.number_input("Seed", value=42)
            refine = st.selectbox(
                "Refine",
                ["no_refiner", "expert_ensemble_refiner", "base_image_refiner"],
            )
            high_noise_frac = st.slider(
                "High Noise Frac", value=0.8, min_value=0.0, max_value=1.0, step=0.1
            )

        submitted = st.form_submit_button(
            "Submit", type="primary", use_container_width=True
        )

    st.divider()
    st.markdown(
        utils.contributor_card(
            image_url="https://raw.githubusercontent.com/andreaschandra/git-assets/master/pictures/andreas.png",
            name="Andreas Chandra",
            role="Researcher",
            linkedin_url="https://linkedin.com/in/chandraandreas",
            github_url="https://github.com/andreaschandra",
        ),
        unsafe_allow_html=True,
    )

# --- Image Generation --- #
if submitted:
    with st.status("Generating...", expanded=True) as status:
        st.write("Requesting to API")

        if submitted:
            with generated_image_placeholder.container():
                all_images = []
                output = replicate.run(
                    REP_ENDPOINT,
                    input={
                        "prompt": prompt,
                        "negative_prompt": negative_prompt,
                        "width": width,
                        "height": height,
                        "num_outputs": num_outputs,
                        "scheduler": scheduler,
                        "num_inference_steps": num_inference_steps,
                        "guidance_scale": guidance_scale,
                        "prompt_stregth": prompt_strength,
                        "random_seed": random_seed,
                        "refine": refine,
                        "high_noise_frac": high_noise_frac,
                    },
                )
                if output:
                    st.toast("Your image has been generated!")
                    st.session_state.generated_image = output

                    # Display the image(s)
                    for image in st.session_state.generated_image:
                        with st.container():
                            st.image(
                                image, caption="Generated Image", use_column_width=True
                            )

                            all_images.append(image)

                            response = requests.get(image, timeout=120)

                st.session_state.all_images = all_images

                zip_io = io.BytesIO()

                # Download image
                with zipfile.ZipFile(zip_io, "w") as zipf:
                    for i, image in enumerate(st.session_state.all_images):
                        response = requests.get(image, timeout=120)
                        if response.status_code == 200:
                            image_data = response.content

                            zipf.writestr(f"output_file_{i+1}.png", image_data)
                        else:
                            st.error(f"Failed to fetch image {i+1} from {image}")

                st.download_button(
                    ":red[**Download All Images**]",
                    data=zip_io.getvalue(),
                    file_name="output_files.zip",
                    mime="application/zip",
                    use_container_width=True,
                )
        status.update(label="Image generated!", state="complete", expanded=False)

    pass
else:
    pass
