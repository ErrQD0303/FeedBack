from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     # By default the required field is True
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Please enter a shorter name!"
#     })
#     review_text = forms.CharField(
#         label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

# ModelForm enables you to save the data directly into the database
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'  # Select all fields in the Review Model
        # exclude = ['owner_comment']
        labels = {
            'user_name': "Your Name",
            'review_text': "Your Feedback",
            'rating': 'Your Rating'
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty",
                "max_length": "Please enter a shorter name!"
            }
        }
