from flask import Flask
from infra.adapters.flaskAdapter import FlaskAdapter

app = Flask(__name__)
httpServer = FlaskAdapter(app)

if __name__ == "__main__":
    app.run(debug=True)
