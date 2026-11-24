# Student Course API

A simple Flask REST API for retrieving student course information.

## Endpoints

- `GET /api/health` — checks whether the API is running.
- `GET /api/courses` — returns all courses.
- `GET /api/courses/<id>` — returns a course by ID, or an error if it is not found.

## Run locally

Install dependencies:

```bash
pip install -r requirements.txt
