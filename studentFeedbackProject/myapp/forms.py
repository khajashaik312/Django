from django import forms
class FeedBackForm(forms.Form):
    sid=forms.IntegerField()
    sname=forms.CharField()
    smarks=forms.FloatField()
    splace=forms.CharField(widget=forms.Textarea)