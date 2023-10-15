import pickle

def load_m(file_name):
    with open(file_name, 'rb') as f_in:
        return pickle.load(f_in)
    
dv = load_m('dv.bin')

model = load_m('model1.bin')

client = {
    "job": "retired",
    "duration": 445, 
    "poutcome": "success"
}

X = dv.transform([client])
y_pred = model.predict_proba(X)[0, 1]

print('input', client)
print(type(client))
print('score', y_pred)
print(type(y_pred))