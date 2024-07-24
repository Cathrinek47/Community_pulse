# questions.py
from flask import Blueprint, request

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


# @questions_bp.route('/questions')
# def list_questions():
#     return "List of all questions"
#
#
# @questions_bp.route('/questions/add', methods=['POST'])
# def add_question():
#     return "Question added"

@questions_bp.route('/', methods=['GET'])
def get_questions():
    """Получение списка всех вопросов."""
    return '<h1> Questions </h1>'


@questions_bp.route('/', methods=['POST'])
def create_question():
    """Создание нового вопроса."""
    return 'Question was created'


@questions_bp.route('/<int:question_id>', methods=['GET'])
def get_question(question_id):
    """Получение деталей конкретного вопроса по его ID."""
    return f"Detailed question {question_id}"


@questions_bp.route('/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    """Обновление конкретного вопроса по его ID."""
    return f"Question {question_id} was updated"


@questions_bp.route('/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    """Удаление конкретного вопроса по его ID."""
    return f"Question {question_id} was deleted"








