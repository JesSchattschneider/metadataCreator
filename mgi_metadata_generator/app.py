import os
import pathlib
import streamlit as st
from streamlit_pydantic.ui_renderer import _name_to_title
from PIL import Image

## Paths
path_of_script = pathlib.Path(__file__).parent.resolve()
path_of_image = pathlib.Path(__file__).parent.joinpath("img/women-geospatial-logo.jpg").resolve()
path_to_examples = pathlib.Path(path_of_script).parent.joinpath("examples").resolve()
image = Image.open(path_of_image)

## Page configuration
st.set_page_config(page_title="Geospatial metadata generator", page_icon=":magic_wand:")
st.sidebar.image(image, width = 5, use_column_width = True)
st.sidebar.title("Auto-generate metadata to geospatial data.")
st.sidebar.markdown("Upload a geospatial file and fill out the form to generate a JSON document with the metadata assoaciated to the uploaded file.")
st.markdown(f'<h1 style="background-color:#00549e ;color:#ffffff;font-size:28px;border-radius:1%;">{"Geospatial metadata generator"}</h1>', unsafe_allow_html=True)

## Select form
DEFAULT_DEMO = "single_dataset.py"

demos = []
for example_file in os.listdir(path_to_examples):
    file_path = path_to_examples.joinpath(example_file).resolve()
    if not file_path.is_file():
        continue
    demos.append(example_file)

## create title to demos
title_to_demo = {}

demo_titles = []
default_index = 0
for i, demo in enumerate(demos):
    if demo == DEFAULT_DEMO:
        # Use single_dataset as default
        default_index = i
    demo_title = _name_to_title(demo.replace(".py", ""))
    title_to_demo[demo_title] = demo
    demo_titles.append(demo_title)

selected_demo_title = st.selectbox(
    "Select the type of dataset", options=demo_titles, index=default_index
)
selected_demo = title_to_demo[selected_demo_title]

## Add source code
with st.expander("Source Code", expanded=False):
    with open(path_to_examples.joinpath(selected_demo), encoding="UTF-8") as f:
        st.code(f.read(), language="python")

exec(open(path_to_examples.joinpath(selected_demo)).read())