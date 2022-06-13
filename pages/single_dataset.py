import json
import pandas as pd
import streamlit as st

import streamlit_pydantic as sp
import folium
from folium.plugins import Draw
from streamlit_folium import st_folium
from pages.utils.models import UploadedFile, GeneralInfo, RolesOrgLevel, IdentificationAndVersioning, SpatialAndTemporalCoverage, GenerationAndMethods, FormatAndStorage, Content

'''
############################
#### Page Content #####
############################
'''

## Section: Upload dataset
st.header("1. Upload dataset")
data0 = UploadedFile(file="") ## populate data0 first
uploaded_file = st.file_uploader("Upload file", accept_multiple_files=False)
if uploaded_file: ## if file is uploaded update data0
    st.write("Filename: ", uploaded_file.name)
    data0 = UploadedFile(file=uploaded_file.name)

## Section: General Information
st.header("2. General Information")
data1 = sp.pydantic_input(
    key="my_form1", model=GeneralInfo, group_optional_fields="expander"
    )

## Section: Roles/contacts (organisation level)
st.header("3. Roles/contacts (organisation level)")
data2 = sp.pydantic_input(
    key="my_form2", model=RolesOrgLevel, group_optional_fields="expander"
)

## Section: Identification / Versioning
st.header("4. Identification / Versioning")
data3 = sp.pydantic_input(
    key="my_form3", model=IdentificationAndVersioning, group_optional_fields="expander"
)

## Section: Spatial and Temporal Coverage
st.header("5. Spatial and Temporal Coverage")
data4 =  sp.pydantic_input(key="union_input", model=SpatialAndTemporalCoverage, group_optional_fields="expander")

### Adding map (reactive) using folium
if 'observation' in dict(data4)['bounding_box'].keys():
    m = folium.Map(location=[-41.178654, -186.328125], zoom_start=5)
    Draw(export=True).add_to(m)
    output = st_folium(m, width = 700, height=500)
    if output['last_active_drawing'] is not None:
        st.write(output['last_active_drawing'])
        data4['bounding_box'] = ({**dict(data4['bounding_box']),**dict(output['last_active_drawing'])}) # update data4

## Section: Generations / Methods
st.header("6. Generations / Methods")
data5 = sp.pydantic_input(
    key="my_form5", model=GenerationAndMethods, group_optional_fields="expander"
)

## Section: Format / Storage
st.header("7. Format / Storage")
data6 = sp.pydantic_input(
    key="my_form6", model=FormatAndStorage, group_optional_fields="expander"
)

## Section: Content
st.header("8. Content")
data7 = sp.pydantic_input(
    key="my_form7", model=Content, group_optional_fields="expander"
)

## Submit button.
submitted = st.button("Submit")

'''
############################
#### Validation #####
############################
'''

## mandatory fields
fields = ["file","title", "description", "type", "keywords", "license", 
    "provider", "provider_contact", #"start_datetime", "end_datetime",
    "geographic_region", "bounding_box"]

## If submit button is clicked combine all inputs:
if submitted:

    # combine all inputs
    res = {**dict(data0), **dict(data1), **dict(data2), **dict(data3), 
    **dict(data4), **dict(data5), **dict(data6), **dict(data7)}

    # print
    st.write(res) # Check


    ## check if mandatory fields were informed
    if all([res[field] != "" and res[field] is not None for field in fields]):
        st.warning("Please, review the final metadata above before downloading it. If needed, fix the information provided above and generate a new metadata by re-submitting the form.")
        st.write(res) # Check

        # create button to dowload metadata as json    
        st.download_button(
            label="Download data as json",
            data=json.dumps(res, default=str),
            file_name='geospatial_metadata.json')
        
        # create button to dowload metadata as csv    
        st.download_button(
            label="Download data as csv",
            data= pd.DataFrame.to_csv(pd.json_normalize(res)),
            file_name='geospatial_metadata.csv')
        st.success('Success')
    
    else:
        st.warning("There are some required information missing. Please, provide information for the fields listed below and re-submit the form.")
        for field in fields:
            if res[field] == "" or res[field] is None or len(res[field]) == 0:
                st.error('Required field: ' + field)
   