from infra.adapters.DjangoAdapter import FlaskAdapter
from usecases.GetProcessFromWebUseCase import GetProcessFromWebUseCase
flask_adapter = FlaskAdapter(None)
route = flask_adapter.route

@route('/search')
def home():
    
    return 'Resultado: Algo da rota no adaptador'


