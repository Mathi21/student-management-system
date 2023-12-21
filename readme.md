## STUDENT MANAGEMENT SYSTEM USING FLASK AND MONGODB  

---

## Introduction 

This Student management system is built using python-flask and mongodb database.<br>
It provides basic operations like creating, reading, updating and deleting the record. Thus providing easier way to maintain student details for management purpose in schools and colleges. <br>

---

## Requirements 

**Flask python framework** - Used to write api routes to access database.<br>
**Flask-marshmallow** - Used for serialization and validation of input
**MongoDB database** - Used to store unstructured data or records.<br>
**Pymongo** - Used to connect python-flask with MongoDB database.<br>

---

## Modules 


## Student-api module 

**/students** 
Requesting this url with **post** method is used to store students record in the database. The input json is fed to body of this request.<br>

**Input json format for student detail should be as follows**
```
{      
        "id" : "115",
        "student_name" : "vijay kadhar S",
        "personal_information" : {
            "first_name" : "vijay",
            "last_name" : "kadhar",
            "initial" : "S",
            "identification_marks" : [
                {
                    "location" : "near eyborws",
                    "identification_type" : "MOLE",
                    "identification_marks_description" : ""
                }
            ],
            "address_info" : {
                "address_line_1" : "address line one goes here",
                "address_line_2" : "address line two goes here",
                "address_line_3" : "address line three goes here",
                "nationality" : "Indian",
                "locality" : "",
                "pincode" : "23232"
            },
            "fathers_name" : "fathers name",
            "mothers_name" : "mothers name",
            "fathers_occupation" : "Driver",
            "mothers_occupation" : "homemaker",
            "gross_annual_income" : "< 3 LAKHS"                                    
        },
        "date_of_admission" : "2023-10-09T11:04:37Z",
        "month_of_admission" : "MAR"                    
}
```
Record will be created only if the id of new request is unique and the input field values are in the correct format.


**/students**
Requesting this url with **get** method is used to retrieve all the student records stored in the database. No params is required to send in the request.<br>


**/students/<string: student_id>**
Requesting this url with **get** method is used to retrieve the record with given student_id as specified in the url. No params is required to send in the request.<br>


**/students/pagination** 
Requesting this url with **get** method is used to retrieve the records found on the given page_no with page_length specified on config file.<br>
**page_no** is passed as params and **page_length** is given in config file.<br> 


**/students/<string: student_id>**
Requesting this url with **put** method is used to update the student record. Updation is allowed only to specified field. Here, the personal information of student is kept as editable field, while restricting others to get modified.<br>
Updated data must be in the correct format, to get the record updated. 


**/students/<string: student_id>** 
Requesting this url with **delete** method is used to delete the student record having id as same as specified in the url. 



## Subject-api module

**/subjects**
Requesting this url with **post** is used to used to store subjects record in the database. The input json is fed to body of this request.<br>

**Input json format for subject detail should be as follows**
```
    {
        "subject_code": "MA18510",
        "subject_name": "MATH",
        "min_mark": 0,
        "max_mark": 100,
        "pass_percentage" : 35,
        "board" : "STATE-BOARD",
        "standard_type" : "PRIMARY"
    }
```
Record will be created only if the subject code of new request is unique and the input field values are in the correct format.


**/subjects** 
Requesting this url with **get** method is used to retrieve all the subject records stored in the database. No params is required to send in the request.<br>


**/subjects/<string: subject_code>** url with **get** method is used to retrieve the record with subject_code as specified in the url. No params is required to send in the request.<br>


**/subjects/pagination**
Requesting this url with **get** method is used to retrieve the records found on the given page_no with page_length specified on config file.<br>
**page_no** is passed as params and **page_length** is given in config file.<br> 


**/subjects/<string: subject_code>** 
Requesting this url with **put** method is used to update the subject record. Updation is allowed only to specified field. Here, the min, max and percentage score is kept as editable field, while restricting others to get modified.<br>
Updated data must be in the correct format, to get the record updated. 


**/subjects/<string: subject_code>** 
Requesting this url with **delete** method is used to delete the student record having subject_code as same as specified in the url.



## Teacher-api module 

**/teachers** 
Requesting this url with **post** is used to used to store teacher record in the database. The input json is fed to body of this request.<br>

**Input json format for teacher detail should be as follows**
```
    {
        "teacher_id" : "T002",
        "first_name" : "Amutha vel",
        "last_name" : "A",
        "gender" : "FEMALE",
        "subjects" : ["1000","2000"],
        "qualification" : [
            {
                "degree_type" : "Masters",
                "major" : "English",
                "degree_name" : "Bsc. English",
                "percentage" : 78.5,
                "passed_out_year" : "2016",
                "passed_out_month" : "MAR"

            }
        ],
        "date_of_joining" : "2023-10-09T11:04:37Z",
        "personal_info" : {
            "address_line_1" : "address line one goes here..",
            "address_line_2" : "address line two goes here..",
            "address_line_3" : "address line three goes here..",
            "nationality" : "Indian",
            "martial_status" : "SINGLE",
            "date_of_birth" : "1999-10-09T11:04:37Z",
            "fathers_name" : "father name",
            "mother_name" : "mothers name",
            "identification_document_details" : 
            [
                {
                    "document_type" : "RATION-CARD",
                    "identification_number" : "xxx-xxx-xxxx-xxx",
                    "document_availability_type" : "ORIGINAL"
                }
            ]        
        }    
    } 
```
Record will be created only if the teacher_id of new request is unique and the input field values are in the correct format.


**/teachers** 
Requesting this url with **get** method is used to retrieve all the teacher records stored in the database. No params is required to send in the request.<br>


**/teachers/<string: teacher_id>** 
Requesting this url with **get** method is used to retrieve the record with teacher_id as specified in the url. No params is required to send in the request.<br>


**/teachers/pagination** 
Requesting this url with **get** method is used to retrieve the records found on the given page_no with page_length specified on config file.<br>
**page_no** is passed as params and **page_length** is given in config file.<br> 


**/teachers/<string: teacher_id>**
Requesting this url with **put** method is used to update the teacher record. Updation is allowed only to specified field. Here, the teacher's qualification and personal information is kept as editable field, while restricting others to get modified.<br>
Updated data must be in the correct format, to get the record updated. 


**/teachers/<string: teacher_id>** 
Requesting this url with **delete** method is used to delete the teacher record having teacher_id as same as specified in the url.


**/teachersub/<string: subject_code>**
Requesting this url with **get** method is used to get details of subject handled by the teacher. Subject_code is passed as params here.



## Academic-api module 

**/academic-records** 
Requesting this url with **post** is used to used to store academic record of student in the database. The input json is fed to body of this request.<br>

**Input json format for academic_record detail should be as follows**
```
    {
        "id" : "115",
        "roll_number" : 115,
        "standard" : "XI",
        "section" : "B",
        "subjects" : [
            {
                "subject_code" : "32b7b788",
                "teacher_id" : "f219affa"                
            },
            {
                "subject_code": "adfdf",
                "teacher_id": "ateaklfd"
            }                    
        ],

        "exams" : {
           "I-MID-TERM": {
                "exam_date" : "2023-10-09T11:04:37Z",
                "marks" : [
                    {
                        "subject_code" : "32b7b788",
                        "obtained_mark" : 100,
                        "subject_result" : "PASS",
                        "teacher_id" : "f219affa"
                    },
                    {
                        "subject_code" : "32b7b788",
                        "obtained_mark" : 10,
                        "subject_result" : "FAIL",
                        "teacher_id" : "f219affa"
                    }
                ],
                "total" : 110,
                "average": 10.4,
                "rank" : "U/A",
                "result" : "FAIL",
                "comments": "none"
            }
        }
    }
```
Record will be created only if the teacher_id of new request is unique and the input field values are in the correct format.


**/academic-records** 
Requesting this url with **get** method is used to retrieve all the academic records stored in the database. academic_year is passed as params to the url.<br>


**/academic-records/<string: student_id>** 
Requesting this url with **get** method is used to retrieve the record with student_id as specified in the url. academic_year is passed as params to the url.<br>


**/academic-records/pagination** 
Requesting this url with **get** method is used to retrieve the records found on the given page_no with page_length specified on config file.<br>
**page_no** is passed as params and **page_length** is given in config file.<br> 
academic_year is also passed as params to the url.


**/academic-records/<string: student_id>**
Requesting this url with **put** method is used to update the academic record. academic_year is passed as params to the url. Updation is allowed only to specified field. Here, the section of the student is kept as editable field, while restricting others to get modified.<br>
Updated data must be in the correct format, to get the record updated.


**/academic-records/<string: student_id>** 
Requesting this url with **delete** method is used to delete the academic record having student_id as same as specified in the url.


**/academic-records/exam/<string: student_id>**
Requesting this url with **put** method is used to update the exam details of the student's academic record. academic_year and exam_type is passed as params.

**Input json for updating exam details**
```
    {
        "exam_date" : "2023-10-09T11:04:37Z",
        "marks" : [
            {
                "subject_code" : "32b7b788",
                "obtained_mark" : 100,
                "subject_result" : "PASS",
                "teacher_id" : "f219affa"
            },
            {
                "subject_code" : "32b7b788",
                "obtained_mark" : 10,
                "subject_result" : "FAIL",
                "teacher_id" : "f219affa"
            }
        ],
        "total" : 110,
        "average": 10.4,
        "rank" : "U/A",
        "result" : "FAIL",
        "comments": "none"
    }

```


**/academic-records/rank**
Requesting this url with **put** method is used to update the rank for all the students for a particular standard and exam_type, which are passed as params along with academic_year. 