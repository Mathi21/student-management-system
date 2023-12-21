from flask import Blueprint, request, jsonify
import json, os
from core.handling import find_record, teacher_update_validation, remove_extra_spaces 
from models.teacher import TeacherSchema
from database import teachers_collection, subjects_collection


# Creating blueprint for teacher route 
teacher_bp = Blueprint("teacher_bp", __name__)


# Schema validates input request
teacher_schema = TeacherSchema()


# This route creates teacher record in the database
@teacher_bp.route('/teachers', methods=['POST'])
def create_teachers():
    data = request.json
    teacher_id = data["teacher_id"]
    # Checks whether teacher record created with this teacher id
    if find_record("teacher_id", teacher_id, teachers_collection):
        return jsonify({"message": "Teacher id already in use"}), 400
    error = teacher_schema.validate(data)
    data = remove_extra_spaces(data)
    if error:
        return error, 400
    result = teachers_collection.insert_one(data)
    return jsonify({"message": "Teacher record created successfully"}), 201


# This route displays all teacher records
@teacher_bp.route('/teachers', methods=['GET'])
def get_teacher_records():
    teacher_record = list(teachers_collection.find())
    if teacher_record:
        return json.dumps(teacher_record, default=str), 200
    return jsonify({"message": "No teacher record found"}), 404


# This route displays a specific teacher record
@teacher_bp.route('/teachers/<string:teacher_id>', methods=['GET'])
def get_teacher_record(teacher_id):
    teacher_record = teachers_collection.find_one({"teacher_id": teacher_id})
    if teacher_record:
        return json.dumps(teacher_record, default=str), 200
    return jsonify({"message": "Teacher record not found"}), 404


# This route displays certain records in the page no. specified
@teacher_bp.route('/teachers/pagination', methods=['GET'])
def get_teacher_pages():
    page_no = int(request.args.get("page_no"))
    page_length = int(os.environ.get("page_length"))
    teacher_records = list(teachers_collection.find().skip(
        page_no*page_length).limit(page_length))
    if teacher_records:
        return json.dumps(teacher_records, default=str), 200
    return jsonify({"message": "No record found at this page"}), 404


# This route updates a teacher record
@teacher_bp.route('/teachers/<string:teacher_id>', methods=['PUT'])
def update_teacher_record(teacher_id):
    data = request.json
    error = teacher_schema.validate(data)
    if error:
        return error, 400
    # This method ensures to update only editable fields
    updated_data = teacher_update_validation(data)
    updated_data = remove_extra_spaces(updated_data)
    result = teachers_collection.update_one(
        {"teacher_id": teacher_id}, {"$set": updated_data})
    if result.modified_count > 0:
        return jsonify({"message": "Teacher record updated successfully"}), 200
    return jsonify({"message": "Teacher record not updated, check whether record exists or update the record"}), 404


# This route deletes a teacher record
@teacher_bp.route('/teachers/<string:teacher_id>', methods=['DELETE'])
def delete_teacher_record(teacher_id):
    result = teachers_collection.delete_one({"teacher_id": teacher_id})
    if result.deleted_count > 0:
        return jsonify({"message": "Teacher record deleted successfully"}), 200
    return jsonify({"message": "Teacher record not found"}), 404


# This route displays details of subject handled by a specific teacher
@teacher_bp.route('/teachersub/<string:subject_code>', methods=['GET'])
def get_teacher_subdetails(subject_code):
    result = subjects_collection.find_one({"subject_code": subject_code})
    if result:
        return jsonify(str(result)), 200
    return jsonify({"message": "Subjects not found"}), 404

