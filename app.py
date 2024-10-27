from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
   return "form processed"
   # Retrieve data from form
   dag = request.form.get['Dag']
   maaned = request.form.get['Måned']
   aar = request.form.get['År']

   energimerke = request.form.get['Energimerke']
   kvadratmeter = request.form.get['Kvadratmeter']
   omraade = request.form.get['Område']
   beboere = request.form.get['Beboere']

   solcelleareal = request.form.get['Solcelleareal']
   virkningsgrad = request.form.get['Virkningsgrad']
   maks_solinnstråling = request.form.get['Maks Solinnstråling']
   temperaturkoeffisient = request.form.get['Temperaturkoeffisient']
   referansetemperatur = request.form.get['Referansetemperatur']
   

   return f"""
        <h2>Submitted Data</h2>
        <ul>
            <li>Dag: {dag}</li>
            <li>Måned: {maaned}</li>
            <li>År: {aar}</li>
            <li>Energimerke: {energimerke}</li>
            <li>Kvadratmeter: {kvadratmeter}</li>
            <li>Område: {omraade}</li>
            <li>Beboere: {beboere}</li>
            <li>Solcelleareal: {solcelleareal}</li>
            <li>Virkningsgrad: {virkningsgrad}</li>
            <li>Maks Solinnstråling: {maks_solinnstråling}</li>
            <li>Temperaturkoeffisient: {temperaturkoeffisient}</li>
            <li>Referansetemperatur: {referansetemperatur}</li>
        </ul>
        """

if __name__ == '__main__':
   app.run(debug=True)