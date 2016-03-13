from django import forms
from .models import Question,Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    def clean_message(self):
        message = self.cleaned_data['message']
        return message
    def save(self):
        if self._user is not None:
            self.cleaned_data['author']=self._user
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
        if self._user is not None:
            self.cleaned_data['author']=self._user
        qid=self.cleaned_data['question']
        question=Question.objects.get(pk=qid)
        self.cleaned_data['question']=question
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

class SignupForm(forms.Form):
    username=forms.CharField(max_length=100)
    email=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)
    def clean_message(self):
        message = self.cleaned_data['message']
        return message
    def save(self):
        user=User.objects.create_user(username=self.cleaned_data['username'],
                                 email=self.cleaned_data['email'],
                                 password=self.cleaned_data['password'])

        #user=User(**self.cleaned_data)
        user.save()
        return user
    def get_username(self):
        return self.cleaned_data['username']
    def get_password(self):
        return self.cleaned_data['password']

class SigninForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)
    def clean_message(self):
        message = self.cleaned_data['message']
        return message
    def get_username(self):
        return self.cleaned_data['username']
    def get_password(self):
        return self.cleaned_data['password']