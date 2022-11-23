from flask import ( 
    Flask,
    render_template,
    request,
)
from Model import Model

app = Flask(__name__)

model = Model()

@app.route("/predict")
def getModelResult():
    input = request.args.to_dict(flat=True)
    print(input)
    
    input["Credit_History"] = int(input["Credit_History"])
    input["Loan_Amount_Term"] = int(input["Loan_Amount_Term"])


    input["ApplicantIncome"] = float(input["ApplicantIncome"])
    input["CoapplicantIncome"] = float(input["CoapplicantIncome"])
    input["LoanAmount"] = float(input["LoanAmount"])

    prediction = model.predict(input_dict=input)

    if prediction:
        return render_template("approved.html", loan_amount=input["LoanAmount"], rate=prediction)
    else:
        return render_template("denied.html")


    #return input

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=1607)
