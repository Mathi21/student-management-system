from flask import Blueprint, request, jsonify
from core.handling import academic_update_validation, find_academic_record, update_result, remove_extra_spaces 
from models.academic import AcademicRecordSchema
from database import academic_records_collection
import json, os


# Creating blueprint for academic record route
academic_bp = Blueprint("academic_bp", __name__)


# Schema for validating input request
academic_record_schema = AcademicRecordSchema()


# This route creates student's academic record in the database
@academic_bp.route('/academic-records', methods=['POST'])
def create_academic_record():
    year = request.args.get("academic_year")
    data = request.json
    id = data["id"]
    roll_number = data["roll_number"]
    standard = data["standard"]
    # Checks whether academic record created with this student id
    if find_academic_record(id, roll_number, standard, academic_records_collection, year):
        return jsonify({"message": "Student id or roll already in use"}), 400
    error = academic_record_schema.validate(data)
    data = remove_extra_spaces(data)
    if error:
        return error, 400
    result = academic_records_collection[year].insert_one(data)
    return jsonify({"message": "Student's Academic Record created successfully"}), 201


# This route displays all student's academic record
@academic_bp.route('/academic-records', methods=['GET'])
def get_academic_records():
    year = request.args.get("academic_year")
    academic_records = list(academic_records_collection[year].find())
    if academic_records:
        return json.dumps(academic_records, default=str), 200
    return jsonify({"message": "Student's Academic record not found"}), 404


# This route displays specific student's academic record
@academic_bp.route('/academic-records/<string:student_id>', methods=['GET'])
def get_academic_record(student_id):
    year = request.args.get("academic_year")
    academic_record = academic_records_collection[year].find_one({
                                                                 "id": student_id})
    if academic_record:
        return json.dumps(academic_record, default=str), 200
    return jsonify({"message": "Student's Academic record not found"}), 404


# This route displays certain records in the page no specified
@academic_bp.route('/academic-records/pagination', methods=['GET'])
def get_academic_records_pages():
    year = request.args.get("academic_year")
    page_no = int(request.args.get("page_no"))
    page_length = int(os.environ.get("page_length"))
    academic_records = list(academic_records_collection[year].find().skip(
        page_no*page_length).limit(page_length))
    if academic_records:
        return json.dumps(academic_records, default=str), 200
    return jsonify({"message": "No records found at this page"}), 404


# This route updates a student's academic record
@academic_bp.route('/academic-records/<string:student_id>', methods=['PUT'])
def update_academic_record(student_id):
    data = request.json
    year = request.args.get("academic_year")
    error = academic_record_schema.validate(data)
    if error:
        return error, 400
    # This method ensures update happens for only editable fields
    updated_data = academic_update_validation(data) 
    updated_data = remove_extra_spaces(updated_data)
    result = academic_records_collection[year].update_one(
        {"id": student_id}, {"$set": updated_data})
    if result.modified_count > 0:
        return jsonify({"message": "Student's Academic record updated successfully"}), 200
    return jsonify({"message": "Student's Academic record not updated, check whether record exists or update the record"}), 404


# This route deletes a student's academic record
@academic_bp.route('/academic-records/<string:student_id>', methods=['DELETE'])
def delete_academic_record(student_id):
    year = request.args.get("academic_year")
    result = academic_records_collection[year].delete_one({"id": student_id})
    if result.deleted_count > 0:
        return jsonify({"message": "Student Record deleted successfully"}), 200
    return jsonify({"message": "Student Record not found"}), 404


# This route updates exam details of a student
@academic_bp.route('/academic-records/exam/<string:student_id>', methods=['PUT'])
def update_exam_details(student_id):
    year = request.args.get("academic_year")
    exam_type = request.args.get("exam_type")
    data = request.json
    updated_data = update_result(data)
    if updated_data == "inproper data":
        return jsonify({"message": "enter marks for all subjects"})
    result = academic_records_collection[year].update_one(
        {"id": student_id}, {"$set": {f"exams.{exam_type}": updated_data}})
    if result.modified_count > 0:
        return jsonify({"message": "Updated exam successfully"}), 200
    return jsonify({"message": "exam details not added"}), 404


# This route updates rank detail of a student
@academic_bp.route('/academic-records/rank', methods=['PUT'])
def update_rank_details():
    year = request.args.get("academic_year")
    exam_type = request.args.get("exam_type")
    standard = request.args.get("standard")
    records = academic_records_collection[year].find(
        {"standard": standard}).sort(f"exams.{exam_type}.total", -1)
    rank = 1
    for student in records:
        print(student["exams"][exam_type])
        if ((student["exams"][exam_type]["result"]).upper() != "FAIL" ):
            academic_records_collection[year].update_one(
                {"id": student["id"]}, {"$set": {f"exams.{exam_type}.rank": rank}})
            rank += 1
    return jsonify({"message": "Ranks updated for given standard and exam"}), 200

 
