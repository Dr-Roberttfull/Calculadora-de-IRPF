# Calculadora-de-IRPF
Esse projeto criado com python,serve para fazer o cálculo de quanto será descontado do seu salário o Imposto de Renda cobrado pelo Governo Federal
Esse projeto criado com python back, usado flask com Framework (front) e o Db Browse SQLite como gerenciador de banco de dados.

INSTRUÇÕES BÁSICAS
a) instale o vscode studio;
b) instale o pip na sua máquina, abra um NOVO TERMINAL no vscode studio e digite: "python get-pip.py"(sem aspas)
c) instale o flask no vscode studio por meio de um NOVO TERMINAL, DIGITE: pip install flask. MAS ANTES..... Se você estiver usando um ambiente virtual (virtualenv) para o seu projeto, certifique-se de ativá-lo antes de instalar o Flask. Caso ainda não tenha um ambiente virtual, você pode criar e ativar um com os seguintes comandos: "python -m venv venv" (sem aspas zezim rsrs), logo em seguinda digite o próximo comando: venv\Scripts\activate (PARA ATIVAR NO WINDOWS), já no Mac ou no LINUX : "source venv/bin/activate" (já sabe ner que é sem aspas";
d) para conferir se o flask está instalado, digite: "pip show flask" ( não preciso falar sobre o lance das aspas ner rsrs);
e) instale Db Browse SQLite: https://sqlitebrowser.org/

Como montar o projeto.
1º Abra seu windows explorer e vá na unidade c: e crie uma pasta chamada flask_app;
2º Abra o VSCODE STUDIO e abra essa pasta chamada flask_app que você criou e dentro dela crie um arquivo chamado app.py, vou mostrar a estrutura básica do projeto em flask (sem o banco de dados). Após fazer os ajustes, resolvir fazer a integração do projeto com o banco de dados de todas as pessoas que ultizarem a calculadora.

flask_app/
│
├── app.py
├── templates/
│   └── index.html
└── static/
    └── (caso você tenha arquivos CSS, JS, etc.)
Agora vou mostrar a estrutura do projeto após está incrementado.

flask_app/
├── app.py
├── models.py
├── templates/
│   └── index.html
├── static/
├── requirements.txt
└── README.md
Na hora de fazer a integração no banco de dados, você terá problemas, então peça ajuda ao CHAT GPT, ele foi meu grande amigo nessa façanha, é tipo eu sonho e idealizo e ele bota a mão na massa.
3º Na hora de estilizar, lembrar que o arquivo css, o STYLE.CSS ficará dentro da pasta STATIC, que ficará dentro da pasta Flask_app.
4º O banco de dados é o arquivo chamado PESSOAS.DB, que ficará dentro da pasta INSTANCE que é criada no momento que você executar o projeto, ou seja, subir o servidor EXECUTANDO o arquivo APP.PY, se der erro, peça ajuda no chat gpt, copie e cola o erro nele que você será bem atendido, siga as instruções que vai dar certo. Comigo deu e nem sou lá essas coca cola na programação.
