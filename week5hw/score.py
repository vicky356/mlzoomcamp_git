import pickle
from flask import Flask
from flask import request
from flask import jsonify


def load_m(file_name):
    with open(file_name, 'rb') as f_in:
        return pickle.load(f_in)


dv = load_m('dv.bin')

model = load_m('model2.bin')

app = Flask('score')


@app.route('/givescore', methods=['POST'])
def givescore():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]

    result = {"score": float(y_pred)}

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
