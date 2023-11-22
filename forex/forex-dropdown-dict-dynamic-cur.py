from flask import Flask, render_template, request

# We will have to do pip install requests before trying out this example
import requests

import json

app = Flask(__name__)

@app.route('/convert', methods = ['POST', 'GET'])
def convert() -> 'html':

    ta = 0
    
    try:     
        #sc = request.form['source_currency']
        sc='USD'
        tc = request.form['target_currency']                
        
        sa = int (request.form['source_amount'])
        
        endpoint = 'live'
        access_key = '543a56c467acd67c321bdf4d2142d5d8'
        
        url = 'http://api.exchangerate.host/live'            
        fullUrl = url + "?access_key=" + access_key + "&currencies=" + tc       
                
        print(fullUrl)        
        
        response = requests.get(fullUrl)
        
        # Will convert the json into a Python dictionary
        response_json = response.json() 
        print(response_json)
        
        currencycombo = 'USD' + tc
        
        # From the response json dictionary, extract the target amount from the 'quotes' key
        #print (response_json ['quotes'][currencycombo])
        ta = float(response_json ['quotes'][currencycombo]) * sa
        	           
    except:
        data = 'Error'
          
    title = 'Here is the result of the conversion:'  
    
    return render_template('result.html', 
                            the_title=title,
                            source_currency=sc,
                            target_currency=tc,
                            source_amount=sa,
                            target_amount=ta,)
    
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':

    currency_dict = {}
    
    url = 'http://api.exchangerate.host/list?access_key=543a56c467acd67c321bdf4d2142d5d8'
    
    response = requests.get(url)
    response_json = response.json()
    print(response_json)
    
    #currencies = response_json ['symbols']
    currency_dict = response_json ['currencies']
    
    return render_template('entry_dropdown_dict_dynamic_cur.html', the_title='Welcome to our forex calculator!', source_currency_dict = currency_dict, target_currency_dict = currency_dict)    

app.run(debug=True, host='0.0.0.0')

