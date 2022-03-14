class Grade:
    def __init__(self):
        self._value = 0
    
    def __get__(self, instance, instance_type):
        return self._value

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._value = value

class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

if __name__ == '__main__':
    first_exam = Exam()
    first_exam.writing_grade = 82
    first_exam.science_grade = 99
    print(f'{first_exam.writing_grade=}')
    print(f'{first_exam.science_grade=}')

    second_exam = Exam()
    second_exam.writing_grade = 75
    print(f'{second_exam.writing_grade=}')
    print(f'{first_exam.writing_grade=}')
