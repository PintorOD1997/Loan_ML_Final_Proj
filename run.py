# run.py
from keras.models import load_model
def run(input_dict):
    model = load_model('model')
    pred = model.predict(input_dict)
    return pred[0][0]

def output(input_dict):
    pred = run(input_dict)
    rate = 1 - pred
    if pred > 0.6:
        return f"Felicidades, tu crédito ha sido aprobado con una tasa de interés de {rate*100}%"
    else:
        return f"Lo sentimos, tu crédito ha sido rechazado"