from flask import Flask, request
import bz2file as bz2
import pickle
import pandas as pd
from json import loads
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

model = pickle.load(bz2.BZ2File('../model/model.pbz2', 'rb'))

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():

    input = request.get_json(force=True) 

    pred = pd.DataFrame([[input['bairro'], input['marca'], input['dia'], input['periodo'], input['idade'], input['sexo']]], columns=['BAIRRO', 'MARCA_OBJETO', 'DIA_SEMANA', 'PERIODO', 'IDADE', 'SEXO'])

    base_add = pd.read_csv("../data/base_to_single_predict.csv")
    pred = pd.concat([base_add, pred])

    pred["BAIRRO"] = pred["BAIRRO"].astype("category")
    pred["MARCA_OBJETO"] = pred["MARCA_OBJETO"].astype("category")
    pred["DIA_SEMANA"] = pred["DIA_SEMANA"].astype("category")
    pred["SEXO"] = pred["SEXO"].astype("category")
    pred["PERIODO"] = pred["PERIODO"].astype("category")

    result = model.predict_proba(pred)
    result = result[-1]
    result = pd.DataFrame(result)

    result = pd.DataFrame([[
        result[0][0],
        result[0][1],
        result[0][2],
        result[0][3],
        result[0][4],
        result[0][5],
        result[0][6],
        result[0][7],
        result[0][8],
        result[0][9]
    ]], columns=[
        "Escolas / Universidade", 
        "Escritórios", 
        "Saúde",
        "Entreterimento",
        "Alimentação",
        "Transporte Privado",
        "Estabelecimentos Comerciais / Industrias",
        "Residência / Hospedagem",
        "Transporte Público",
        "Via Pública"
    ])

    result *= 100

    result = result.sort_values(result.last_valid_index(), axis=1)

    result = result.to_json(orient="split")
    result = loads(result)
    response = []
    for x in range(10):
        data = {
                    "position":x,
                    "label":result['columns'][x],
                    "value": "{:.2f}".format(result['data'][0][x]),
                    "id": getId(result['columns'][x])
                }
        
        response.append(data)

    return response


def getId(label):
    definitions = [
        {"id":1, "label":"Escritórios"}, 
        {"id":2, "label":"Saúde"},
        {"id":3, "label":"Entreterimento"},
        {"id":4, "label":"Alimentação"},
        {"id":5, "label":"Transporte Privado"},
        {"id":6, "label":"Estabelecimentos Comerciais / Industrias"},
        {"id":7, "label":"Residência / Hospedagem"},
        {"id":8, "label":"Transporte Público"},
        {"id":9, "label":"Via Pública"},
        {"id":10, "label":"Escolas / Universidade"}
    ]
    for item in definitions:
        if item['label'] == label:
            return item['id']


@app.route('/health')
@cross_origin()
def health():
    return "healthy"