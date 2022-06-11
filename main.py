from flask import Flask, render_template, request

app = Flask(__name__)

Exos = {
    "Développé couché classique altère":('0d', '2x20', '4x9'), 
    "Écarté poulie bas":('Bas','2x7.5', '4x8'), 
    "Chest press":('Prise horizontale, 4s', '25', '4x3x10'),
    "Extension triceps":('27p, accroupi', '2x7.5', '4x8'),
    "Extension triceps overhead":('0p', '2x7.5', '4x8'),
    "Développé militaire":('60d', '2x14', '4x6'),
    "Élévation latérales":('', '2x8 + 2x6 + 2x5', '3x8')
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/push/", methods=['POST'])
def push():
    if request.method == "POST":
        exo = request.form.get('exercice')
        instructions = request.form.get('instructions')       
        charge = request.form.get('charge')
        reps = request.form.get('reps')
        Exos[exo] = (instructions, charge, reps)
    return render_template('seance.html', exos=Exos)

if __name__ == "__main__":
    app.run(debug = True)