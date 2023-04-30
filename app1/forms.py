from .models import CourseEvaluation
from django import forms
# from .models import SurveyRating


# class SurveyRatingForm(forms.ModelForm):
#     class Meta:
#         model = SurveyRating
#         fields = ['course_objectives', 'delivering_material', 'engaging_students',
#                   'responding_questions', 'providing_feedback', 'inclusive_environment',
#                   'using_technology', 'promoting_critical_thinking', 'challenging_students',
#                   'overall_satisfaction']


class CourseEvaluationForm(forms.ModelForm):
    communication = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    delivery = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    engagement = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    responsiveness = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    feedback = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    inclusiveness = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    technology = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    critical_thinking = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    motivation = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    satisfaction = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )

    class Meta:
        model = CourseEvaluation
        fields = ['faculty_member', 'course_title', 'semester', 'year', 'evaluator', 'communication', 'delivery', 'engagement', 'responsiveness',
                  'feedback', 'inclusiveness', 'technology', 'critical_thinking', 'motivation', 'satisfaction', 'comments']
