# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from config import DevelopmentConfig
# from app.routes.questions import questions_bp
from app import create_app


# app = Flask(__name__)
# app.config.from_object(DevelopmentConfig)
# db = SQLAlchemy(app)


# app.register_blueprint(questions_bp, url_prefix='/questions')


# @app.route('/')
# def home():
#     return "Welcome to the Flask!"
#
#
# @app.route('/question/<int:question_id>')
# def show_question(question_id):
#     return f"Question ID {question_id}"
#
#
# @app.route('/add-question', methods=['POST'])
# def add_question():
#     return "A question has been added"

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
