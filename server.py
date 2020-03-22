from flask import  Flask, request, jsonify 
from flask_cors import CORS
import os
covid19 = __import__('covid19')

app = Flask(__name__)
CORS(app)

@app.route('/countries', methods=['GET'])
def countries():
    return jsonify(covid19.get_countries()) 


@app.route('/curve', methods=['GET'])
def home():
    if 'country' not in request.args:
        return jsonify({"error" : 'country is required'})
    
    country = request.args['country']

    casos_por_dias, mortes_por_dia, curados_por_dia, ativos_por_dia = covid19.get_dias(country)
    
    novos_casos = covid19.get_cases_curve(casos_por_dias)
    novas_mortes = covid19.get_deaths_curve(mortes_por_dia)

    


    return jsonify({
        "cases_curve" : casos_por_dias,
        "deaths_curve" : mortes_por_dia,
        "recovered_curve" : curados_por_dia,
        "actives_curve" : ativos_por_dia,
        

        "new_cases_curve" : novos_casos,
        "new_deaths_curve" : novas_mortes
    })

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 5000)))