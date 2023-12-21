from flask import Blueprint, request, jsonify
from core.handling import subject_update_validation, find_record, remove_extra_spaces
from models.subject import SubjectSchema
from database import subjects_collection
import json, os
 

# Creating blueprint for subject route
subject_bp = Blueprint('subject_bp', __name__)


# Schema for validating input request
subject_schema = SubjectSchema()


# This route creates subject records in database
@subject_bp.route('/subjects', methods=['POST'])
def create_subject():
    data = request.json
    subject_code = data["subject_code"]
    # checking whether subject record created with this subject_code
    if find_record("subject_code", subject_code, subjects_collection):
        return jsonify({"message": "Subject code already in use"}), 400
    error = subject_schema.validate(data)
    data = remove_extra_spaces(data)
    if error:
        return error, 400
    else:
        result = subjects_collection.insert_one(data)
        return jsonify({"message": "Subject record created successfully"}), 201


# This route displays all the subject records
@subject_bp.route('/subjects', methods=['GET'])
def get_subjects():
    subjects = list(subjects_collection.find())
    if subjects:
        return json.dumps(subjects, default=str), 200
    return jsonify({"message": "No subject records found"}), 404


# This route displays specific subject record
@subject_bp.route('/subjects/<string:subject_code>', methods=['GET'])
def get_subject(subject_code):
    subject = subjects_collection.find_one({"subject_code": subject_code})
    if subject:
        return json.dumps(subject, default=str), 200
    return jsonify({"message": "Subject record not found"}), 404


# This route displays certain records in the page no. specified
@subject_bp.route('/subjects/pagination', methods=['GET'])
def get_subject_pages():
    page_no = int(request.args.get("page_no"))
    page_length = int(os.environ.get("page_length"))
    subject_records = list(subjects_collection.find().skip(
        page_no*page_length).limit(page_length))
    if subject_records:
        return json.dumps(subject_records, default=str), 200
    return jsonify({"message": "No record found at this page"})


# This route updates a subject record
@subject_bp.route('/subjects/<string:subject_code>', methods=['PUT'])
def update_subject(subject_code):
    data = request.json
    error = subject_schema.validate(data)
    if error:
        return error, 400
    # This method ensures to update only editable fields
    updated_data = subject_update_validation(data)
    updated_data = remove_extra_spaces(updated_data)
    result = subjects_collection.update_one(
        {"subject_code": subject_code}, {"$set": updated_data})
    if result.modified_count > 0:
        return jsonify({"message": "Subject record updated successfully"}), 200
    return jsonify({"message": "Subject record not found"}), 404


# This route deletes a subject record
@subject_bp.route('/subjects/<string:subject_code>', methods=['DELETE'])
def delete_subject(subject_code):
    result = subjects_collection.delete_one({"subject_code": subject_code})
    if result.deleted_count > 0:
        return jsonify({"message": "Subject record deleted successfully"}), 200
    return jsonify({"message": "Subject record not found"}), 404

