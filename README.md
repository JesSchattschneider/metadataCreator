# metadataGenerator
## create venv

- install python3-venv if needed:

`sudo apt install python3.9-venv`
`pip install virtualenv ` # powershell
- install venv

`python3 -m venv ./venv/`
`python -m venv venv` # powershell
- source venv

`source ./venv/bin/activate`
`.\venv\Scripts\Activate.ps1` # powershell

## create a requirements.txt

see requirements.txt

## install requirements

`pip install -r requirements.txt`

## deploy app - locally 
`streamlit run app.py`