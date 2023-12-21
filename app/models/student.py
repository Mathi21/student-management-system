from marshmallow import Schema, validates, fields, ValidationError, validate
from core.validation import validate_id, validate_alphabet, validate_alphanumeric

    
months = [
    "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"
]


class AddressSchema(Schema):
    address_line_1 = fields.Str(required=True, validate=[
                                validate_alphanumeric, validate.Length(min=3, max=50)])
    address_line_2 = fields.Str(required=True, validate=[
                                validate_alphanumeric, validate.Length(min=3, max=50)])
    address_line_3 = fields.Str(required=True, validate=[
                                validate_alphanumeric, validate.Length(min=3, max=50)])
    nationality = fields.Str(required=True, validate=[
                             validate_alphabet, validate.Length(min=3, max=20)])
    locality = fields.Str(required=True, validate=[
                          validate_alphabet, validate.Length(min=0, max=10)])
    pincode = fields.Int(required=True)


class IdentificationMarkSchema(Schema):
    location = fields.Str(required=True, validate=[
                          validate_alphabet, validate.Length(min=3, max=20)])
    identification_type = fields.Str(required=True)
    identification_marks_description = fields.Str(
        allow_none=True, validate=[validate_alphabet, validate.Length(min=0, max=40)])

    @validates("identification_type")
    def validate_identification_type(self, value):
        if value not in ['SCAR', 'WOUND', 'MOLE', 'COLOR-PATCH']:
            raise ValidationError("Input value error")


class PersonalInformationSchema(Schema):
    first_name = fields.Str(required=True, validate=[
                            validate_alphabet, validate.Length(min=3, max=25)])
    last_name = fields.Str(allow_none=True, validate=[
                           validate_alphabet, validate.Length(min=3, max=25)])
    initial = fields.Str(required=True, validate=validate_alphabet)
    identification_marks = fields.List(
        fields.Nested(IdentificationMarkSchema, required=True))
    address_info = fields.Nested(AddressSchema, required=True)
    fathers_name = fields.Str(required=True, validate=[
                              validate_alphabet, validate.Length(min=3, max=25)])
    mothers_name = fields.Str(required=True, validate=[
                              validate_alphabet, validate.Length(min=3, max=25)])
    fathers_occupation = fields.Str(required=True, validate=validate_alphabet)
    mothers_occupation = fields.Str(required=True, validate=validate_alphabet)
    gross_annual_income = fields.Str(required=True)

    @validates("gross_annual_income")
    def validate_gross_annual_income(self, value):
        if value not in ['< 3 LAKHS', '> 5 LAKHS && 10 LAKHS <', '> 10 LAKHS && 15 LAKHS <', '> 15 LAKHS && 20 LAKHS <', '> 20 LAKHS']:
            raise ValidationError("Error in type identification")


class StudentSchema(Schema):
    id = fields.Str(required=True, validate=validate_id)
    student_name = fields.Str(required=True, validate=validate_alphabet)
    personal_information = fields.Nested(
        PersonalInformationSchema, required=True)
    date_of_admission = fields.DateTime(required=True)
    month_of_admission = fields.Str(
        allow_none=True, validate=validate.OneOf(months))


'''
SAMPLE DATA FOR STUDENT 

{      
        "id" : "MAT900",
        "student_name" : "vijay rose  S",
        "personal_information" : {
            "first_name" : "vijay",
            "last_name" : "rose",
            "initial" : "S",
            "identification_marks" : [
                {
                    "location" : "near eyborws",
                    "identification_type" : "MOLE",
                    "identification_marks_description" : "it is very small"
                }
            ],
            "address_info" : {
                "address_line_1" : "address line one goes here",
                "address_line_2" : "address line two goes here",
                "address_line_3" : "address line three goes here",
                "nationality" : "Indian",
                "locality" : "chennai",
                "pincode" :23232
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

'''
