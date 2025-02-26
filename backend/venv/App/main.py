from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/get_user_id', methods=['GET', 'POST'])
def get_user_id():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        if not user_id:
            return jsonify({"error": "No user_id provided"}), 400
        return jsonify({"user_id": user_id})
    return render_template('get_user_id.html')

