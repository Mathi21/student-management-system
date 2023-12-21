from marshmallow import Schema, validate, fields, validates, ValidationError
from core.validation import validate_id, validate_alphabet


class SubjectSchema(Schema):
    subject_code = fields.Str(required=True, validate=validate_id)
    subject_name = fields.Str(required=True, validate=validate_alphabet)
    min_mark = fields.Int(required=True, validate=validate.Range(min=0))
    max_mark = fields.Int(required=True, validate=validate.Range(min=0))
    pass_percentage = fields.Float(
        required=True, validate=validate.Range(min=0, max=100))
    board = fields.Str(required=True)
    standard_type = fields.Str(required=True)

    @validates("board")
    def validate_board(self, board):
        if board not in ['STATE-BOARD', 'CBSE', 'ICSE']:
            raise ValidationError("Input value error")

    @validates("standard_type")
    def validate_standard_type(self, standard):
        if standard not in ['PRIMARY', 'HIGHER-SECONDARY']:
            raise ValidationError("Input value error")


'''
SAMPLE DATA FOR SUBJECT 

{
        "subject_code": "MAT510",
        "subject_name": "MATH",
        "min_mark": 0,
        "max_mark": 100,
        "pass_percentage" : 35,
        "board" : "STATE-BOARD",
        "standard_type" : "PRIMARY"
}
'''
