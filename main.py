import random
from flask import Flask

app = Flask(__name__)

facts_list = ["Większość osób cierpiących na uzależnienie technologiczne doświadcza silnego stresu, gdy znajdują się poza zasięgiem sieci lub nie mogą korzystać ze swoich urządzeń"], ["Według badania przeprowadzonego w 2018 roku ponad 50% osób w wieku od 18 do 34 lat uważa się za zależne od swoich smartfonów"] , ["Badanie zależności technologicznych jest jednym z najważniejszych obszarów współczesnych badań naukowych"] , ["Według badania z 2019 r. ponad 60% osób odpowiada na wiadomości służbowe na swoich smartfonach w ciągu 15 minut po wyjściu z pracy"

]


@app.route("/")
def hello_world():
    return f'<p><a href="/random_fact">Zobacz losowy fakt!</a></p>'

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)




