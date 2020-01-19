from flask import Flask, request, jsonify
import requests
import json 

app = Flask(__name__)

language_codes = ['en', 'hi']

@app.route('/v1.0/nlp',methods=['GET', 'POST'])
def conector():

    if request.method == 'POST':
        in_json  = request.get_json()
        text = in_json['text'].lower()
        language_code = in_json['language_code']
        if language_code not in language_codes:
            return jsonify(error='invalid language code')

        if language_code == 'en':
            port = '5005'
        if language_code == 'hi':
            port = '5004'

        base_url = 'http://localhost:' + str(port) + '/model/parse'
        
        json_object = {'text' : text}
        payload = json.dumps(json_object)
        headers = {'content-type': 'application/json'}
        r = requests.post(base_url , data=payload, headers=headers)
        json_object = json.loads(r.text)

        intent = json_object['intent']['name']
        confidence = json_object['intent']['confidence']
        name = ''
        amount = 0
        return_json = {}
        
        if intent in ['send_money', 'request_money']:
            try:
                name = text.split(' to ')[1]
            except:
                pass
            try: 
                for entity in json_object['entities']:
                    if entity['entity'] == 'amount':
                        amount = entity['value']
            except:
                pass

            

            if name:
                return_json['name'] = name
            if amount:
                return_json['amount'] = amount

        return_json['intent'] = intent
        return_json['confidence'] = confidence
        
        return jsonify(return_json)
        
    if request.method == 'GET':
        return 'Welcome to NLP Engine.'
    

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
        
        
        
        
        
    
        
        
        
        
     
    
    


   
