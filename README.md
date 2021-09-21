# Mindee case

## Backend
The backend is written in Python Flask.
It has one route that takes an image as input and returns the predictions from Mindee.

### Setup the environnement
- `cd backend`
- `pipenv shell`
- `pipenv install`

### Run the app
- `python run.py`

### Limitations
- No authentification is required to run the API
- No file check is done
- Credential are hard coded in the `__init__.py`
- The code is not covered by unit tests


## Frontend
The frontend is written in VueJS.
It allows the user to check and correct the predictions from Mindee.

### Setup the environnement
- `cd frontend`
- `npm install`

### Run the app
- `npm run serve`

### Limitations
- The app is not responsive
- The code is not covered by unit tests