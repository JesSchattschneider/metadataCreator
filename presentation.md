---
marp: true
---

# What

- Metadata for geospatial data - aim, future, spreadsheet, limitations

- Test Streamlit - open source app framework in Python language for creating web apps in a short time.

- Combine the above to develop an intermediate solution - a tool to generate metadata (JSON and csv) following the standards presented in the meeting/spreadsheet.

<!-- - Metadata for geospatial data - meeting [present spreadsheet, motivation is to one day store data from different institution in a single DB - metadata will help it to be findable!]
- Testing new tool - Streamlit - [transform spreadsheet into a form] - deploy with a single line, uses python and it can be deployed to the "outside world"
- Intermediate step - in the final would be amazing to have the data linked in the database for tracking versions. Use a tool to generate metadata associated to dataset [thinking in a National database] - before sending the data to the Organization in charge of putting new datasets into the DB they should use "metadata generator" to make sure that enough info is being provided and that it is in the right format. -->

---

# Why

- National standard
- Websites - without JS
- Simple - and it is not shiny
- Learn somethig new and upskill - python
- **Alternative to excel?**
- Validation
- Previous experience with metadata projects - metadata for datasets
- Geospatial data <3

---

# How

- **streamlit** for buiding the app
- **streamlit-pydantic** for creating models for form sections *+* validation *+* only required fields - templates with rules (pydantic with FastAPI)
- GitHub to develop and pull basic project - https://github.com/LukasMasuch/streamlit-pydantic- 
- reshuffle a lil bit...
- Folium for printing maps and selecting coordinates 
- **json, pandas and streamlit** for downloading metadata in different formats

# Structure

`metadataGenerator`
`|- app.py`
`|- pages`
`|   |- single_dataset.py`
`|   |- utils`
`|      |- models.py`
`|- img`
`|   |- logo.jpg`
`|- requirements.txt`

# Pros
- One language - python
- Deploy and share
- Reactive
- Supports different widgets - map
- Hide optional


# Limitations/ next steps
- New tool - especially streamlit-pydantic - validation, font
- Add additional fields based on pre-existing relationships
- Poor validation - improve logic, use optional arguments 
- Update - how to track versions? - implement a modify tab 
- Load data to extract file name
- Data cardinality - create multiple_dataset.py in pages
- How to use dictionaries? 
- Docker