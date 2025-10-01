from django import forms

ROLES = [
    ('student', 'Student'),
    ('teacher', 'Teacher'),
]

SUBJECTS = [
    ('math', 'Mathematics'),
    ('science', 'Science'),
]

TOPICS = {
    'math': [('algebra', 'Algebra'), ('geometry', 'Geometry')],
    'science': [('physics', 'Physics'), ('chemistry', 'Chemistry')],
}

class RoleForm(forms.Form):
    role = forms.ChoiceField(choices=ROLES, label="Select Role")

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    student_id = forms.CharField(max_length=20)

class TeacherForm(forms.Form):
    name = forms.CharField(max_length=100)
    subject = forms.ChoiceField(choices=SUBJECTS, label="Select Subject")

class TopicForm(forms.Form):
    topic = forms.ChoiceField(choices=[], label="Select Topic")

    def __init__(self, subject=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if subject and subject in TOPICS:
            self.fields['topic'].choices = TOPICS[subject]
        else:
            self.fields['topic'].choices = []
