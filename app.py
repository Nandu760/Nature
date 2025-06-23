from flask import Flask
from Blueprint import bp  # import the Blueprint object

def create_app():
    app = Flask(__name__)
    
    # register blueprint
    app.register_blueprint(bp)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)