from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
   # Retrieve data from form
   start = request.form.get('Dag')
   slutt = request.form.get('Måned')

   energimerke = request.form.get('Energimerke')
   kvadratmeter = request.form.get('Kvadratmeter')
   omraade = request.form.get('Område')
   beboere = request.form.get('Beboere')

   solcelleareal = request.form.get('Solcelleareal')
   virkningsgrad = request.form.get('Virkningsgrad')
   maks_sol = request.form.get('Maks Solinnstråling')
   temp_k = request.form.get('Temperaturkoeffisient')
   ref_temp = request.form.get('Referansetemperatur')
   

   return None

if __name__ == '__main__':
   app.run(debug=True)