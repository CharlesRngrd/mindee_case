# Mindee case

## Backend
The backend is written in Python Flask.
It has one route that takes an image as input and returns the predictions from Mindee.

### Setup the environnement
`pipenv shell`
`pipenv install`

### Run the app
`python run.py`

### Limitations
- No authentification is required to run the API
- Credential are hard coded in the `__init__.py`
- The code is not covered by unit tests
