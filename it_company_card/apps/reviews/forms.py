from django import forms

from .models import Reviews


class AddReviewForm(forms.ModelForm):
    """Форма нового комментария"""
    class Meta:
        model = Reviews
        fields = ('title', 'description')
