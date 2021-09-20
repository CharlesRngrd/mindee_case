from flask import Flask


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False

# FIXME : Move those values to the .env file
app.config['SECRET_KEY'] = '12345'
app.config['URL'] = 'https://api.mindee.net/v1/products/CharlesRangheard/OpticalOrderForm/v1/predict'
app.config['TOKEN'] = '1b86c2e3027f0b37b8d4f7eec72a3797'


from mindee import routes
