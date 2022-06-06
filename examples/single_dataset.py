from datetime import datetime
from pickle import TRUE
from typing import Optional, List, Set, Union
from datetime import datetime
from numpy import double

import streamlit as st
from pydantic import BaseModel, Field
from enum import Enum

import streamlit_pydantic as sp
import folium
from folium.plugins import Draw
from streamlit_folium import st_folium

## Auxiliar classes ##

class Types(str, Enum):
    t1 = "Acoustic"
    t2 = "Age"
    t3 = "Aid to navigation"
    t4 = "Bathymetry"
    t5 = "Biosecurity"
    t6 = "Bycatch"
    t7 = "Coastline"
    t8 = "Communication structures & coverage"
    t9 = "CTD"
    t10 = "Currents"
    t11 = "Earthquake locations"
    t12 = "Energy/resource production sites" 
    t13 = "Fault locations"
    t14 = "Fauna"
    t15 = "Fishing catch effort"
    t16 = "Fishing/aquaculture areas"
    t17 = "Flora"
    t18 = "Geology"
    t19 = "Geothermal features"
    t20 = "Gravity"
    t21 = "Heat flow"
    t22 = "Magnetic features"
    t23 = "Māori customary interest areas "
    t24 = "Marine conservation areas"
    t25 = "Marine habitats/ecosystems"
    t26 = "Maritime jurisdictions"
    t27 = "Meteorology"
    t28 = "Mining extraction/exploration areas"
    t29 = "Nutrients"
    t30 = "Optical properties"
    t31 = "Permitted dumping ground"
    t32 = "Physical obstructions"
    t33 = "Pipelines & underwater cables"
    t34 = "Port/harbour facilities"
    t35 = "Recreational areas"
    t36 = "Regulatory use restrictions"
    t37 = "Sea level information"
    t38 = "Seafloor backscatter"
    t39 = "Sediment"
    t40 = "Seismic reflection/refraction"
    t41 = "Shoreline constructions"
    t42 = "Suspended particles"
    t43 = "Transportation"
    t44 = "Volcanoes"
    t45 = "Water column backscatter"
    t46 = "Water pollution"
    t47 = "Water quality"

class Licenses(str, Enum):
    l1 = "CC-BY-4.0"

class Frequency(str, Enum):
    f1= "daily"
    f2 = "fortnightly"
    f3 = "monthly"
    f4 = "quarterly"
    f5 = "anually"

class Geographic_sites(str, Enum):
    auckland = "Auckland"
    wellington = "Wellington"

class CRS(str, Enum):
    wgs84 = "WGS84"

class Spatial_coverage_dec(BaseModel): ## add info: only inform min and max if it is a point 
    latitude_min_decimal_degrees: Optional[double]
    longitude_min_decimal_degrees: Optional[double]
    latitude_max_decimal_degrees: Optional[double]
    longitude_max_decimal_degrees: Optional[double]    
    crs: CRS

class Spatial_coverage_dms(BaseModel):
    lat_min_degrees: Optional[int]
    lat_min_minutes: Optional[double]
    lat_min_seconds: Optional[double]
    
    lon_min_degrees: Optional[int]
    lon_min_minutes: Optional[double]
    lon_min_seconds: Optional[double]
    
    lat_max_degrees: Optional[int]
    lat_max_minutes: Optional[double]
    lat_max_seconds: Optional[double]
 
    lon_max_degrees: Optional[int]
    lon_max_minutes: Optional[double]
    lon_max_seconds: Optional[double]

    crs: CRS

class DrawInTheMap(BaseModel):
    Observation: str = Field(
        ..., description="Draw spatial coverage in the map and add any observation in the box provided."
    )

## Main Classes

class GeneralInfo(BaseModel):
    title: str = Field(description="Title for the dataset. Should be not more than several words, short sentence")
    description: str = Field(description = "Description of the dataset shall cover summary information on the why, what, and how of the dataset. This should include following elements. Purpose of the data collection; Used methods and/or protocols; Broad spatial coverage; Time period of data collection; Types of data; Taxonomic coverage (if applicable); Other relevant descriptive information; Note: This replicates some field contents – but provides important summary information in one place")
    # theme: Set[Themes] = Field(
    #     ..., description="Allows multiple themes."
    # )
    
    type: Set[Types] = Field(
        ..., description="Allows multiple themes."
    )
    keywords: str
    license: Set[Licenses]
    publication_statement:Optional[str]
    constraints:Optional[str]
    release_date:Optional[datetime]
    citation:Optional[str]
    attribution:Optional[str]
    lineage:Optional[str]

class RolesOrgLevel(BaseModel):
    creator:Optional[str]
    owner:Optional[str]
    manager:Optional[str]
    provider:str
    provider_contact:str    

class IdentificationAndVersioning(BaseModel):  ## includes url
    identifier: Optional[str]
    version: Optional[str]
    date_created: Optional[datetime]
    date_updated: Optional[datetime]
    maintenance_freq: Optional[Frequency]
    organisation_url: Optional[str]
    data_url: Optional[str]

class SpatialAndTemporalCoverage(BaseModel):
    start_datetime = datetime
    end_datetime = datetime
    geographic_region: Set[Geographic_sites] = Field(
        ..., description="Allows multiple sites from a set."
    )
    bounding_box: Union[DrawInTheMap, Spatial_coverage_dec, Spatial_coverage_dms]

class GenerationAndMethods(BaseModel):
    generation_method: Optional[str] = Field(description="This field allows for a text-based/human readable description of the method used for generating the dataset. The content of this element would be similar to a description of sampling procedures found in the methods section of a journal article.")
    collection_instrument_type:	Optional[str] = Field(description="High level instrument category according to agreed vocabulary. This field enables to filter data collected in a similar technical way")
    collection_instrument:	Optional[str] = Field(description="Instrument make / model used in data collection.")
    collection_platform_category: Optional[str] = Field(description="High level platform type used for data collection, e.g. vessel, AUV, sensor platform to agreed vocabulary. This field enables to filter data collected in a similar technical way.")
    collection_platform: Optional[str] = Field(description="Specifics of platform used for data collection, e.g. make/model, vessel name, etc")

class FormatAndStorage(BaseModel):
    format_type: Optional[str] = Field(description="General description of the format of the dataset according to an agreed vocabulary: ascii, binary, …")
    format_spec: Optional[str] = Field(description="Specific description of data format for dataset; for example specific manufacture binary format reference")

class Content(BaseModel):
    parameter_category: Optional[str] = Field(description="This field describes in high level categories, the environmental parameters included with in dataset.High level parameter type/ category that applies to parameter to agreed vocabulary. This field enables to filter data of similar type")
    parameter: Optional[str] = Field(description="This field describes the environmental parameters included with in dataset (e.g. ‘water temperature’)")



# class Content:
with st.form(key='my_form'):
    st.subheader("File")
    uploaded_files = st.file_uploader("Upload a file", accept_multiple_files=False)
    if uploaded_files:
        print(uploaded_files.name)
    #   st.write("Filename: ", uploaded_file.name)

    st.subheader("General Information")
    data1 = sp.pydantic_input(
        key="my_form1", model=GeneralInfo, group_optional_fields="expander"
        )

    st.subheader("Roles/contacts (organisation level)")
    data2 = sp.pydantic_input(
        key="my_form2", model=RolesOrgLevel, group_optional_fields="expander"
    )

    st.subheader("Identification / Versioning")
    data3 = sp.pydantic_input(
        key="my_form3", model=IdentificationAndVersioning, group_optional_fields="expander"
    )

    st.subheader("Spatial and Temporal Coverage")
    data4 =  sp.pydantic_input(key="union_input", model=SpatialAndTemporalCoverage, group_optional_fields="expander")
    if 'Observation' in dict(data4)['bounding_box'].keys():
        # https://share.streamlit.io/randyzwitch/streamlit-folium/examples/streamlit_app.py
        m = folium.Map(location=[39.949610, -75.150282], zoom_start=5)
        Draw(export=True).add_to(m)

        output = st_folium(m, width = 700, height=500)
        st.write(output['last_active_drawing'])

    st.subheader("Generations / Methods")
    data5 = sp.pydantic_input(
        key="my_form5", model=GenerationAndMethods, group_optional_fields="expander"
    )

    st.subheader("Format / Storage")
    data6 = sp.pydantic_input(
        key="my_form6", model=FormatAndStorage, group_optional_fields="expander"
    )
    st.subheader("Content")
    data7 = sp.pydantic_input(
        key="my_form7", model=Content, group_optional_fields="expander"
    )

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("generalinfo", data1, "spatialtemp", data4)

if submitted:
    if any(data1):
        print(data1)
        st.warning('No selectboxes selected!')
        # st.header('You selected some checkboxes!')
    else:
        st.warning('No selectboxes selected!')

