get_otp_successful_response = {
    "status": "success",
    "message": "OTP sent to your mobile number"
}
get_otp_missing_mobile_number_response = {
    "status": "error",
    "message": "Missing mobile number"
}

get_otp_invalid_mobile_number_response = {
    "status": "error",
    "message": "Invalid mobile number format"
}

validate_otp_new_user_response = {
    "status": "success",
    "message": "OTP verified successfully. User does not exist.",
    "user_exists": False,
    "user_details": {}
}

validate_otp_existing_user_response = {
    "status": "success",
    "message": "OTP verified successfully. User exists.",
    "user_exists": True,
    "user_details": {
        "name": "Ujjwal",
        "mobile": "8000080000",
        "email": "sharanujjwal02@gmail.com"
    }
}

internal_server_error = {
    "status": "error",
    "message": "Internal server error"
}

bad_request = {
    "status": "error",
    "message": "Bad request"
}

validate_otp_invalid_otp_response = {
    "status": "error",
    "message": "Invalid or expired OTP"
}

quiz_mock_response = {
  "status": "success",
  "status_code": 200,
  "message": "Quiz data fetched successfully",
  "data": {
    "quiz_id": "quiz_001",
    "quiz_name": "General Awareness Mega Quiz",
    "logo_url": "https://example.com/assets/quiz_logo.png",
    "description": "Test your knowledge across current affairs, history, and science in this mega quiz challenge!",
    "background_music_url": "https://example.com/audio/quiz_theme.mp3",
    "skip_and_answer_later_enabled": True,
    "time_enabled": True,
    "total_time_limit": 900,
    "show_timer_per_question": True,
    "allow_negative_marking": True,
    "randomize_questions": True,
    "shuffle_options": True,
    "questions": [
      {
        "question_id": "q001",
        "question_statement": {
          "en": "Which of the following is the largest planet in our Solar System?",
          "hi": "निम्नलिखित में से कौन ग्रह हमारे सौर मंडल का सबसे बड़ा ग्रह है?"
        },
        "image_url": None,
        "type": "single_select",
        "time_limit": 30,
        "options": [
          { "option_id": "a", "text": {"en": "Earth", "hi": "पृथ्वी"} },
          { "option_id": "b", "text": {"en": "Jupiter", "hi": "बृहस्पति"} },
          { "option_id": "c", "text": {"en": "Saturn", "hi": "शनि"} },
          { "option_id": "d", "text": {"en": "Mars", "hi": "मंगल"} }
        ],
        "correct_option_id": "b",
        "marks": 2,
        "negative_marks": -0.5
      },
      {
        "question_id": "q002",
        "question_statement": {
          "en": "Select all prime numbers from the list below.",
          "hi": "नीचे दी गई सूची से सभी अभाज्य संख्याएँ चुनें।"
        },
        "image_url": None,
        "type": "multiple_select",
        "time_limit": 45,
        "options": [
          { "option_id": "a", "text": {"en": "2", "hi": "2"} },
          { "option_id": "b", "text": {"en": "4", "hi": "4"} },
          { "option_id": "c", "text": {"en": "5", "hi": "5"} },
          { "option_id": "d", "text": {"en": "9", "hi": "9"} }
        ],
        "correct_option_ids": ["a", "c"],
        "marks": 2,
        "negative_marks": -0.5
      },
      {
        "question_id": "q003",
        "question_statement": {
          "en": "The capital of Australia is ___?",
          "hi": "ऑस्ट्रेलिया की राजधानी ___ है?"
        },
        "image_url": None,
        "type": "fill_in_the_blank",
        "time_limit": 30,
        "correct_answer": "Canberra",
        "case_sensitive": False,
        "marks": 2,
        "negative_marks": 0
      },
      {
        "question_id": "q004",
        "question_statement": {
          "en": "The boiling point of water is 100°C at sea level.",
          "hi": "समुद्र तल पर पानी का क्वथनांक 100°C होता है।"
        },
        "image_url": None,
        "type": "True_False",
        "time_limit": 20,
        "correct_answer": True,
        "marks": 1,
        "negative_marks": 0
      },
      {
        "question_id": "q005",
        "question_statement": {
          "en": "Which historical event is depicted in the image?",
          "hi": "चित्र में कौन सी ऐतिहासिक घटना दर्शाई गई है?"
        },
        "image_url": "https://example.com/images/event.jpg",
        "type": "single_select",
        "time_limit": 40,
        "options": [
          { "option_id": "a", "text": {"en": "French Revolution", "hi": "फ्रांसीसी क्रांति"} },
          { "option_id": "b", "text": {"en": "American Civil War", "hi": "अमेरिकी गृह युद्ध"} },
          { "option_id": "c", "text": {"en": "World War I", "hi": "प्रथम विश्व युद्ध"} },
          { "option_id": "d", "text": {"en": "Indian Independence Movement", "hi": "भारतीय स्वतंत्रता आंदोलन"} }
        ],
        "correct_option_id": "d",
        "marks": 2,
        "negative_marks": -1
      }
    ]
  },
  "timestamp": "2025-04-16T12:34:56Z"
}

start_quiz_session_request_body = {"quiz_id": "test_1",
                                   "user_mobile": "8000080000",
                                   "started_at": "2025-01-16T10:30:00Z",
                                   "device_info": {
                                       "platform": "flutter",
                                       "timestamp": 1705404600000,
                                       "timezone": "Asia/Kolkata"}
                                   }

start_quiz_session_success_response = {
  "status": "success",
  "message": "Quiz session started",
  "session_id": "session_12345",
  "can_start": True,
  "shuffled_question_order": ["q003", "q001", "q005", "q002", "q004"], 
  "quiz_config": {
    "randomize_questions": True,
    "shuffle_options": True,
    "total_questions": 5
  }
}

start_quiz_session_error_responses = {
    "status": "error",
    "message": "Quiz already completed",
    "can_start": False,
    "completed_at": "2025-01-15T14:20:00Z"
}
start_quiz_session_error_responses_2 = {
    "status": "error",
    "message": "Quiz session already active",
    "can_start": False,
    "session_started_at": "2025-01-16T09:15:00Z"
}

check_quiz_progress_success_response = {
    "status": "success",
    "has_progress": True,
    "is_completed": False,
    "can_restart": False,
    "progress_data": {
        "current_question_index": 3,
        "current_score": 25.5,
        "time_elapsed": 180,
        "skipped_questions": ["q002", "q005"],
        "last_activity": "2025-01-16T10:25:00Z"
    }
}

check_quiz_progress_no_progress_response = {
    "status": "success",
    "has_progress": False,
    "is_completed": False,
    "can_restart": True
}

save_quiz_progress_request_body = {
    "quiz_id": "test_1",
    "user_mobile": "8000080000",
    "current_question_index": 3,
    "answers_progress": [
        {
            "question_id": "q001",
            "has_answer": True,
            "is_skipped": False,
            "is_timed_out": False
        },
        {
            "question_id": "q002",
            "has_answer": False,
            "is_skipped": True,
            "is_timed_out": False
        }
    ],
    "current_score": 25.5,
    "time_elapsed": 180,
    "skipped_questions": ["q002"],
    "last_activity": "2025-01-16T10:30:00Z"
}

save_quiz_progress_success_response = {
    "status": "success",
    "message": "Progress saved"
}

submit_question_answer_request_body = {
    "quiz_id": "test_1",
    "user_mobile": "8000080000",
    "question_id": "q001",
    "answer_data": {
        "question_id": "q001",
        "selected_option_id": "b",
        "selected_option_ids": None,
        "text_answer": None,
        "bool_answer": None,
        "is_correct": True,
        "is_skipped": False,
        "is_timed_out": False,
        "time_spent": 15,
        "submitted_at": "2025-01-16T10:30:15Z"
    },
    "submitted_at": "2025-01-16T10:30:15Z"
}

submit_question_answer_success_response = {
    "status": "success",
    "message": "Answer submitted",
    "is_correct": True,
    "points_earned": 2,
    "total_score": 12.5
}

complete_quiz_request_body = {
    "quiz_id": "test_1",
    "user_mobile": "8000080000",
    "final_score": 85.5,
    "total_time_spent": 450,
    "final_stats": {
        "correct_answers": 8,
        "total_questions": 10,
        "skipped_questions": 1,
        "timed_out_questions": 1,
        "accuracy_percentage": 80,
        "time_taken": 450
    },
    "completed_at": "2025-01-16T10:37:30Z"
}

complete_quiz_success_response = {
    "status": "success",
    "message": "Quiz completed successfully",
    "final_rank": 42,
    "leaderboard_position": 42,
    "rewards": {
        "points": 85,
        "badges": ["speed_demon"],
        "cash_prize": 100
    }
}

quiz_post_submit_response = {
    "status": "success",
    "status_code": 200,
    "message": "User Quiz result successfully",
    "data": {
        "quiz_id": "quiz_001",
        "rank": 1,
        "quiz_status": "completed",
        "quiz_name": "General Awareness Mega Quiz",
        "logo_url": "https://example.com/assets/quiz_logo.png",
        "description": "Test your knowledge across current affairs, history, and science in this mega quiz challenge!",
        "background_music_url": "https://example.com/audio/quiz_theme.mp3",
        "total_time_limit": 900,
        "questions": [
            {
                "question_id": "q001",
                "question_statement": "Which of the following is the largest planet in our Solar System?",
                "image_url": None,
                "type": "single_select",
                "time_limit": 30,
                "options": [
                    {"option_id": "a", "text": "Earth"},
                    {"option_id": "b", "text": "Jupiter"},
                    {"option_id": "c", "text": "Saturn"},
                    {"option_id": "d", "text": "Mars"}
                ],
                "correct_option_id": "b",
                "marks": 2,
                "negative_marks": -0.5,
                "is_correct": False,
                "time_taken": 3,
            },
            {
                "question_id": "q002",
                "question_statement": "Select all prime numbers from the list below.",
                "image_url": None,
                "type": "multiple_select",
                "time_limit": 45,
                "options": [
                    {"option_id": "a", "text": "2"},
                    {"option_id": "b", "text": "4"},
                    {"option_id": "c", "text": "5"},
                    {"option_id": "d", "text": "9"}
                ],
                "correct_option_ids": ["a", "c"],
                "marks": 2,
                "negative_marks": -0.5,
                "is_correct": True,
                "time_taken": 12,
            },
            {
                "question_id": "q003",
                "question_statement": "The capital of Australia is ___?",
                "image_url": None,
                "type": "fill_in_the_blank",
                "time_limit": 30,
                "correct_answer": "Canberra",
                "case_sensitive": False,
                "marks": 2,
                "negative_marks": 0,
                "is_correct": False,
                "time_taken": 11,
            },
            {
                "question_id": "q004",
                "question_statement": "The boiling point of water is 100°C at sea level.",
                "image_url": None,
                "type": "True_False",
                "time_limit": 20,
                "correct_answer": True,
                "marks": 1,
                "negative_marks": 0,
                "is_correct": True,
                "time_taken": 18,
            },
            {
                "question_id": "q005",
                "question_statement": "Which historical event is depicted in the image?",
                "image_url": "https://example.com/images/event.jpg",
                "type": "single_select",
                "time_limit": 40,
                "options": [
                    {"option_id": "a", "text": "French Revolution"},
                    {"option_id": "b", "text": "American Civil War"},
                    {"option_id": "c", "text": "World War I"},
                    {"option_id": "d", "text": "Indian Independence Movement"}
                ],
                "correct_option_id": "d",
                "marks": 2,
                "negative_marks": -1,
                "is_correct": True,
                "time_taken": 23,
            }
        ]
    },
    "timestamp": "2025-04-16T12:34:56Z"
}

"""

  "database_schema_suggestions": {
    "quiz_sessions": {
      "session_id": "PRIMARY KEY",
      "quiz_id": "VARCHAR",
      "user_mobile": "VARCHAR",
      "started_at": "TIMESTAMP",
      "completed_at": "TIMESTAMP None",
      "is_active": "BOOLEAN DEFAULT True",
      "device_info": "JSON",
      "final_score": "DECIMAL None",
      "status": "ENUM('active', 'completed', 'abandoned')"
    },

    "quiz_progress": {
      "progress_id": "PRIMARY KEY",
      "session_id": "FOREIGN KEY",
      "quiz_id": "VARCHAR",
      "user_mobile": "VARCHAR",
      "current_question_index": "INT",
      "current_score": "DECIMAL",
      "time_elapsed": "INT",
      "answers_progress": "JSON",
      "skipped_questions": "JSON",
      "last_activity": "TIMESTAMP",
      "created_at": "TIMESTAMP",
      "updated_at": "TIMESTAMP"
    },

    "question_answers": {
      "answer_id": "PRIMARY KEY",
      "session_id": "FOREIGN KEY",
      "quiz_id": "VARCHAR",
      "user_mobile": "VARCHAR",
      "question_id": "VARCHAR",
      "selected_option_id": "VARCHAR None",
      "selected_option_ids": "JSON None",
      "text_answer": "TEXT None",
      "bool_answer": "BOOLEAN None",
      "is_correct": "BOOLEAN",
      "is_skipped": "BOOLEAN DEFAULT False",
      "is_timed_out": "BOOLEAN DEFAULT False",
      "time_spent": "INT",
      "points_earned": "DECIMAL",
      "submitted_at": "TIMESTAMP"
    },

    "quiz_completions": {
      "completion_id": "PRIMARY KEY",
      "session_id": "FOREIGN KEY",
      "quiz_id": "VARCHAR",
      "user_mobile": "VARCHAR",
      "final_score": "DECIMAL",
      "total_time_spent": "INT",
      "correct_answers": "INT",
      "total_questions": "INT",
      "skipped_questions": "INT",
      "timed_out_questions": "INT",
      "accuracy_percentage": "INT",
      "rank_position": "INT None",
      "rewards_data": "JSON",
      "completed_at": "TIMESTAMP"
    }
  },

  "security_considerations": {
    "session_validation": "Always check if session is active and belongs to user",
    "duplicate_prevention": "Prevent multiple active sessions per user per quiz",
    "progress_integrity": "Validate that progress data is consistent and not tampered",
    "time_validation": "Check that time_spent values are reasonable",
    "answer_validation": "Validate answers against correct options in database",
    "rate_limiting": "Prevent rapid-fire API calls that could indicate automation",
    "device_fingerprinting": "Track device info for suspicious activity detection"
  },

  "business_logic": {
    "fairness_rules": [
      "Once a quiz is started, user cannot restart it",
      "Progress is saved after every question to prevent cheating via app restarts",
      "Skipped questions can only be reviewed if quiz setting allows it",
      "Time limits are enforced server-side, not just client-side",
      "Screenshots and screen recording are blocked during quiz"
    ],
    "completion_criteria": [
      "All questions must be answered, skipped, or timed out",
      "Final submission creates immutable completion record",
      "Leaderboard position calculated immediately upon completion",
      "Rewards/prizes distributed based on performance and rank"
    ]
  }
}
"""
