# Function used to check existence of a record with given id 
def find_record(id_name, id_value, collection):
    record = collection.find_one({f"{id_name}": id_value})
    if record:
        return True
    return False 


# Function used to check a student with same id or roll for academic_record
def find_academic_record(id, roll_number, standard, academic_records_collection, year):
    academic_record = academic_records_collection[year].find_one({"id": id})
    if academic_record:
        return True
    else:
        record = academic_records_collection[year].find_one({"roll_number": roll_number, "standard": standard})
        if record:
            return True
        return False
    

# Function used to remove extra white spaces 
def remove_extra_spaces(value):
    if isinstance(value, str):
        return ' '.join(value.split())  
    elif isinstance(value, list):
        return [remove_extra_spaces(item) for item in value]
    elif isinstance(value, dict):
        return {key: remove_extra_spaces(val) for key, val in value.items()}
    else:
        return value
    

# Function used to update only editable field for student
def student_update_validation(student):
    updated_student = {
        "personal_information": student["personal_information"]
    }
    return updated_student


# Function used to update only editable field for subject
def subject_update_validation(subject):
    updated_subject = {
        "min_mark": subject["min_mark"],
        "max_mark": subject["max_mark"],
        "pass_percentage": subject["pass_percentage"]
    }
    return updated_subject


# Function used to update only editable field for teacher
def teacher_update_validation(teacher_record):
    updated_record = {
        "qualification": teacher_record["qualification"],
        "personal_info": teacher_record["personal_info"]
    }
    return updated_record


# Function used to update only editable field for academic_record
def academic_update_validation(student_academic_record):
    updated_academic_record = {
        "section": student_academic_record.section
    }
    return updated_academic_record 


# Function used to update exam results
def update_result(data):
    data["total"] = 0
    data["average"] = 0.0
    data["result"] = "PASS"
    if(len(data["marks"]) < 2 or len(data["marks"]) > 6):
        return "inproper data"
    for i in range(len(data["marks"])):
        data["total"] += data["marks"][i]["obtained_mark"]
        data["marks"][i]["subject_result"] = "PASS" if data["marks"][i]["obtained_mark"] >35 else "FAIL"
        if(data["marks"][i]["subject_result"].upper() == "FAIL" ):
            data["result"] = "FAIL"
    data["average"] = data["total"] / len(data["marks"])
    print(data)
    return data
    

