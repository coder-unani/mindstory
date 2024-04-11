from django.core.exceptions import ValidationError

def validate_symbols(value):
    if "#" in value:
        raise ValidationError("'#'은 입력할 수 없습니다.")

def validate_feeling(value):
    for str in value:
        if str.isdigit():
            raise ValidationError("숫자는 입력할 수 없습니다.")

def validate_score(value):
    if value < 0 or value > 10:
        raise ValidationError("0에서 10 사이의 값을 입력해주세요.")
    
