from flask import Blueprint, request, jsonify
from core.handling import student_update_validation, find_record, remove_extra_spaces
from models.student import StudentSchema
import json, os
from database import students_collection


# Creating blueprint for student_route
student_bp = Blueprint('student_bp', __name__)


# Schema for validating input request
student_schema = StudentSchema()


# This route creates student records in the database
@student_bp.route('/students', methods=['POST'])
def create_student():
    data = request.json
    id = data["id"]
    # Checks whether student record created with this id
    if find_record("id", id, students_collection):
        return jsonify({"message": "Student id already in use"}), 400
    error = student_schema.validate(data)
    data = remove_extra_spaces(data)
    if error:
        return error, 400
    else:
        result = students_collection.insert_one(data)
        return jsonify({"message": "Student record created successfully"}), 201


# This route displays all student records
@student_bp.route('/students', methods=['GET'])
def get_students():
    students = list(students_collection.find())
    if students:
        return json.dumps(students, indent=3, default=str), 200
    return jsonify({"message": "No student records found"}), 404


# This route displays specific student record
@student_bp.route('/students/<string:student_id>', methods=['GET'])
def get_student(student_id):
    student = students_collection.find_one({"id": student_id})
    if student:
        return json.dumps(student,default=str), 200
    return jsonify({"message": "Student record not found"}), 404


# This route displays certain records in the page no. specified
@student_bp.route('/students/pagination', methods=['GET'])
def get_student_pages():
    page_no = int(request.args.get("page_no"))
    page_length = int(os.environ.get("page_length"))
    student_records = list(students_collection.find().skip(
        page_no*page_length).limit(page_length))
    if student_records:
        return json.dumps(student_records, default=str), 200
    return jsonify({"message": "No record found at this page"}), 404


# This route updates a student record
@student_bp.route('/students/<string:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.json
    error = student_schema.validate(data)
    if error:
        return error, 400
    # This update_validation method ensures update for only editable fields
    updated_data = student_update_validation(data)
    updated_data = remove_extra_spaces(updated_data)
    result = students_collection.update_one(
        {"id": student_id}, {"$set": updated_data})
    if result.modified_count > 0:
        return jsonify({"message": "Student record updated successfully"}), 200
    return jsonify({"message": "Student record not updated, check whether student exists or update the record"}), 404


# This route deletes a student record
@student_bp.route('/students/<string:student_id>', methods=['DELETE'])
def delete_student(student_id):
    result = students_collection.delete_one({"id": student_id})
    if result.deleted_count > 0:
        return jsonify({"message": "Student deleted successfully"}), 200
    else:
        return jsonify({"message": "Student record not found"}), 404



