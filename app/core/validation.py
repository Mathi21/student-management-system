import re
from marshmallow import ValidationError 

    
# Function used to validate a id 
def validate_id(value):
    if not re.match("^[A-Z]{3}[0-9]{3,4}$", value):
        raise ValidationError("id must be in proper format")
    

# Function used to check input contains only alphabet
def validate_alphabet(value):
    if not re.match(r'^[a-zA-Z]*(?:\s[a-zA-Z]*)*$', value):
        raise ValidationError("Input value error")


# Function used to check input contains only alphanumeric 
def validate_alphanumeric(value):
    if not re.match(r'^[a-zA-Z0-9.:-]*(?:\s[a-zA-Z0-9.:-]*)*$', value):
        raise ValidationError("Input value error")
