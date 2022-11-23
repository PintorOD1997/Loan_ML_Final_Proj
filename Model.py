import tensorflow as tf
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


if __name__ == "__main__":
    sample = {
    "Gender": "Male",
    "Married": "No",
    "Dependents": "0",
    "Education": "Graduate",
    "Self_Employed": "No",
    "ApplicantIncome": 6300, #Monthly income in USD
    "CoapplicantIncome": 0,
    "LoanAmount": 50, #Loan amount in thousands
    "Loan_Amount_Term": 180, #Term of loan in months
    "Credit_History": 1,
    "Property_Area": "Urban"
    }
    input_dict = {name: tf.convert_to_tensor([value]) for name, value in sample.items()}
    print(output(input_dict))

class Model:
	def __init__(self) -> None:
		self.model = load_model("model")
		

	def predict(self, input_dict) -> str:
		input_dict = {name: tf.convert_to_tensor([value]) for name, value in input_dict.items()}
		try:
			pred = self.model.predict(input_dict)
			pred = pred[0][0]
			rate = 1 - pred
			if pred > 0.6:
				return rate*100
			else:
				return 0
		except Exception as e:
			print(e)
			return 0

