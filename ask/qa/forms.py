from django import forms
from .models import Question,Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    def clean_message(self):
        message = self.cleaned_data['message']
        return message
    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):

    text = forms.CharField()
    question=forms.IntegerField()
    def clean_message(self):
        message = self.cleaned_data['message']
        return message
    def save(self):
        print(self.cleaned_data)
        qid=self.cleaned_data['question']
        question=Question.objects.get(pk=qid)
        self.cleaned_data['question']=question
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer