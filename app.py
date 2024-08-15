from flask import Flask, render_template, request
from models import db, Pessoa

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pessoas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def format_to_float(value):
    """ Converte o valor no formato brasileiro para float. """
    try:
        # Substitui pontos por nada e vírgulas por pontos.
        value = value.replace('.', '').replace(',', '.')
        return float(value)
    except ValueError:
        raise ValueError("Formato de número inválido")

def format_to_brl(value):
    """ Converte o valor float para o formato brasileiro. """
    return "{:,.2f}".format(value).replace(',', 'X').replace('.', ',').replace('X', '.')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            nome = request.form['nome']
            profissao = request.form['profissao']
            salario_bruto = format_to_float(request.form['salario'])
            aliquota = float(request.form['aliquota']) / 100
            imposto = salario_bruto * aliquota
            salario_liquido = salario_bruto - imposto

            # Armazenar dados no banco de dados
            nova_pessoa = Pessoa(
                nome=nome,
                profissao=profissao,
                salario_bruto=salario_bruto,
                aliquota=aliquota,
                imposto=imposto,
                salario_liquido=salario_liquido
            )
            db.session.add(nova_pessoa)
            db.session.commit()

            return render_template('index.html', nome=nome, profissao=profissao, 
                                   salario_bruto=format_to_brl(salario_bruto),
                                   imposto=format_to_brl(imposto),
                                   salario_liquido=format_to_brl(salario_liquido),
                                   resultado=True)
        except (KeyError, ValueError) as e:
            return render_template('index.html', error="Por favor, preencha todos os campos corretamente.")
    
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas
    app.run(debug=True)
