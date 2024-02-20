from flask import Flask, render_template
from dotenv import load_dotenv
import os

from config.mongodb import mongo
from routes.todo import todo

load_dotenv()

app = Flask(__name__)

# Desactiva la protección CSRF para tu aplicación Flask
app.config['WTF_CSRF_ENABLED'] = False

app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(todo, url_prefix='/todo')

if __name__ == '__main__':
    app.run(debug=False) #DESACTIVAR LA DEPUTACION PARA ENTORNO DE PRODUCION
