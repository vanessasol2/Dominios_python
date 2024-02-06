from flask import Flask

# crear bloque principal Flask 
app = Flask(__name__)

# importar las rutas definidas
from app import routes

if __name__ =='__main__':
    app.run()