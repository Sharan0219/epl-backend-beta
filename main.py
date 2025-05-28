from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from flask import request
from responses import quiz_mock_response, validate_otp_existing_user_response, get_otp_successful_response, \
    start_quiz_session_success_response, check_quiz_progress_success_response, save_quiz_progress_success_response, \
    submit_question_answer_success_response, complete_quiz_success_response, quiz_post_submit_response

app = Flask(__name__)
# Configure CORS to allow all origins
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization", "Access-Control-Allow-Origin"]
    }
})


@app.route('/api/get-otp', methods=['POST'])
def get_otp():
    data = request.json
    mobile = data.get("mobile")

    return jsonify(get_otp_successful_response)


@app.route('/api/validate-otp', methods=['POST'])
def validate_otp():
    data = request.json
    # {"mobile": "8000080000", "otp": "1234"}

    return jsonify(validate_otp_existing_user_response)


@app.route('/api/get-contests', methods=['GET'])
def get_contests():
    # data = request.json
    # {"mobile": "8000080000", "otp": "1234"}
    contest_data = {
        "name": "Daily Challenge - Quiz",
        "description": "Join this real-time quiz challenge and win amazing rewards! Time remaining: 30:00 mins.",
        "start_time": 123456,
        "end_time": 234566,
        "banner": "https://i.imgur.com/nUe0YJV.png",
        'is_live': True,
        "quiz_url": "",
        "quiz_id": "test_1",
        "reattempt_allowed": False,
        "user_attempt_status": {
            "has_attempted": True,
            "is_completed": False,
            "can_attempt": True,
            "status": "in_progress"
        }
    }
    return jsonify({"status": "success",
                    "message": "OTP verified successfully. User exists.", "contests": [contest_data]})


@app.route('/api/update-profile', methods=['POST'])
def update_profile():
    data = request.json
    """
    {"name":"user-213","email":"aditya.patra@expinfi.com","mobile":"8757636065","exam":"CAT"}
    """
    # {"mobile": "8000080000", "otp": "1234"}

    return jsonify({"name": data.get('name'), "mobile": data.get('mobile'), "email": data.get('email')})


@app.route('/api/get-quiz-by-id', methods=['GET'])
def get_quiz_by_id():
    quiz_id = request.args.get('quiz_id')
    # Mock quiz data

    return jsonify(quiz_mock_response), 200


@app.route('/api/start-quiz-session', methods=['POST'])
def start_quiz():
    quiz_id = request.args.get('quiz_id')
    # Mock quiz data

    return jsonify(start_quiz_session_success_response), 200


@app.route('/api/check-quiz-progress', methods=['GET'])
def check_quiz_progress():
    quiz_id = request.args.get('quiz_id')
    # Mock quiz data

    return jsonify(check_quiz_progress_success_response), 200


@app.route('/api/save-quiz-progress', methods=['POST'])
def save_quiz_progress():
    quiz_id = request.args.get('quiz_id')
    # Mock quiz data

    return jsonify(save_quiz_progress_success_response), 200


@app.route('/api/submit-question-answer', methods=['POST'])
def submit_question_answer():
    quiz_id = request.args.get('quiz_id')
    # Mock quiz data

    return jsonify(submit_question_answer_success_response), 200


@app.route('/api/complete-quiz', methods=['POST'])
def complete_quiz():
    quiz_id = request.args.get('quiz_id')
    # Mock quiz data

    return jsonify(complete_quiz_success_response), 200


@app.route('/api/get-quiz-result-by-id', methods=['POST'])
def get_user_quiz_response():
    quiz_id = request.args.get('quiz_id')
    # Mock quiz data

    return jsonify(quiz_post_submit_response), 200


@app.route('/api/get-quiz-eligibility', methods=['POST'])
def check_eligible():
    quiz_id = request.args.get('quiz_id')
    mobile = request.args.get('mobile')
    # Mock quiz data

    return jsonify(quiz_post_submit_response), 200


@app.route('/api/submit-answer', methods=['POST'])
def submit_answer():
    data = request.get_json()
    user_id = data.get("user_id")
    quiz_id = data.get("quiz_id")
    question_id = data.get("question_id")
    submitted_answer = data.get("submitted_answer")  # Can be string, list, or bool

    correct_answers = {
        "q1": "c",
        "q2": ["a", "c"],
        "q3": "Star",
        "q4": False
    }

    return jsonify({
        "status": "success",
        "status_code": 200,
        "message": "Answer submitted",
        "data": {
            "question_id": question_id,
            "is_correct": 10,
            "submitted_answer": submitted_answer,
            "correct_answer": correct_answers
        }
    }), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
