
from flask import Flask, jsonify
import os

app = Flask(__name__)

courses = [
    {
        "id": 1,
        "course_code": "CS 101",
        "course_name": "Introduction to Computing",
        "instructor": "Dr. Elena Marquez",
        "units": 3
    },
    {
        "id": 2,
        "course_code": "IT 204",
        "course_name": "Web Development",
        "instructor": "Dr. Daniel Reyes",
        "units": 3
    },
    {
        "id": 3,
        "course_code": "IS 310",
        "course_name": "Systems Integration and Architecture",
        "instructor": "Dr. Aisha Rahman",
        "units": 4
    }
]


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "success",
        "message": "Student Course API is running"
    })


@app.route("/api/courses", methods=["GET"])
def get_courses():
    return jsonify(courses)


@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            return jsonify(course)

    return jsonify({
        "status": "error",
        "message": "Course not found"
    }), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
