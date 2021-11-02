from django import forms
from App_Board.models import Question, Answer

# 데이터베이스 모델 중 일부 속성만 사용


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']  # 사용할 모델의 속성
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }
