from infra.adapters.flaskAdapter import FlaskAdapter

flask_adapter = FlaskAdapter(None)  # Crie uma instância sem referência ao Flask
route = flask_adapter.route

@route('/')
def home():
    return 'Resultado: Algo da rota no adaptador'
