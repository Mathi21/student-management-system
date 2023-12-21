from marshmallow import Schema, fields, validate, ValidationError
from core.validation import validate_id, validate_alphabet


exam_types = [
    "I-MID-TERM",
    "II-MID-TERM",
    "III-MID-TERM",
    "QUARTERLY",
    "HALF-YEARLY",
    "ANNUAL",
]


def validate_rank(data):
    if data == "U/A" or (isinstance(data, int) and data > 0):
        return
    raise ValidationError("Input value error")


class SubjectSchema(Schema):
    subject_code = fields.Str(required=True, validate=validate_id)
    teacher_id = fields.Str(required=True, validate=validate_id)

 
class MarksSchema(Schema):
    subject_code = fields.Str(required=True, validate=validate_id)
    obtained_mark = fields.Int(
        required=True, validate=validate.Range(min=0, max=500))
    subject_result = fields.Str(required=True, validate=validate.OneOf([
                                "PASS", "pass", "FAIL", "fail"]))
    teacher_id = fields.Str(required=True, validate=validate_id)


class ExamSchema(Schema):
    exam_date = fields.DateTime(required=True)
    marks = fields.Nested(MarksSchema, many=True)
    total = fields.Int(required=True, validate=validate.Range(min=0))
    average = fields.Float(required=True, validate=validate.Range(min=0.0))
    rank = fields.Field(required=True, validate=validate_rank)
    result = fields.Str(required=True, validate=validate.OneOf(
        ["PASS", "pass", "FAIL", "fail"]))
    comments = fields.Str(required=True)


class AcademicRecordSchema(Schema):
    id = fields.Str(required=True, validate=validate_id)
    roll_number = fields.Int(required=True, validate=validate.Range(min=1))
    standard = fields.Str(required=True, validate=validate_alphabet)
    section = fields.Str(required=True, validate=validate_alphabet)
    subjects = fields.List(fields.Nested(SubjectSchema), required=True)
    exams = fields.Dict(keys=fields.Str(validate=validate.OneOf(
        exam_types)), values=fields.Nested(ExamSchema), required=True)




'''
SAMPLE DATA FOR ACADEMIC RECORD
{
        "id" : "MAT115",
        "roll_number" : 115,
        "standard" : "XI",
        "section" : "B",
        "subjects" : [
            {
                "subject_code" : "SUB100",
                "teacher_id" : "TEA002"                
            },
            {
                "subject_code": "SUB200",
                "teacher_id": "TEA003"
            }                    
        ],

        "exams" : {
           "I-MID-TERM": {
                "exam_date" : "2023-10-09T11:04:37Z",
                "marks" : [
                    {
                        "subject_code" : "SUB100",
                        "obtained_mark" : 100,
                        "subject_result" : "PASS",
                        "teacher_id" : "TEA002"
                    },
                    {
                        "subject_code" : "SUB200",
                        "obtained_mark" : 10,
                        "subject_result" : "FAIL",
                        "teacher_id" : "TEA003"
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
'''
