from flask import Flask, request, render_template

app = Flask(__name__)

def calculer_imc(poids, taille):
    return round(poids / (taille ** 2), 2)

def categorie_imc(imc):
    if imc < 18.5:
        return "Maigreur"
    elif imc < 25:
        return "Poids normal"
    elif imc < 30:
        return "Surpoids"
    else:
        return "Obésité"

@app.route('/', methods=['GET', 'POST'])
def index():
    resultat = None
    if request.method == 'POST':
        poids = float(request.form['poids'])
        taille = float(request.form['taille'])
        imc = calculer_imc(poids, taille)
        categorie = categorie_imc(imc)
        resultat = f"Votre IMC est de {imc} ({categorie})"
    return render_template('index.html', resultat=resultat)

if __name__ == '__main__':
    app.run(debug=True)
