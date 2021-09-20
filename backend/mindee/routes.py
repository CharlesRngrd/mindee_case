from flask import jsonify, make_response, request
from mindee import app

import requests


@app.route('/image_parsing', methods=['POST'])
def image_parsing():
    """
    Step 1 : Make the API call
    Step 2 : Return the client values
    """

    files = {"document": request.files['document']}
    headers = {"Authorization": f"Token {app.config['TOKEN']}"}
    response = requests.post(app.config['URL'], files=files, headers=headers)

    error = response['api_request']['error']
    status_code = response['api_request']['status_code']
    predictions = response['document']['inference']['prediction']

    if error:
        return(make_response(error, status_code))

    output = {}
    output['high_level'] = {}
    output['business'] = {}

    output['high_level']['client_account'] = predictions['client_account']['values'][0]['content']
    output['high_level']['fullname'] = predictions['fullname']['values'][0]['content']
    
    output['business']['index'] = predictions['index']['values'][0]['content']
    output['business']['sphere'] = predictions['sphere']['values'][1]['content']
    output['business']['cylinder'] = predictions['cylinder']['values'][0]['content']
    output['business']['axe'] = predictions['axe']['values'][0]['content']
    output['business']['a'] = predictions['a']['values'][0]['content']
    output['business']['b'] = predictions['b']['values'][0]['content']
    output['business']['nose'] = predictions['nose']['values'][0]['content']

    return(make_response(output, status_code))