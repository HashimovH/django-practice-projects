from django.forms import ModelForm, TextInput
from .models import Message

class MessageForm(ModelForm):
	class Meta:
		model = Message
		fields = '__all__'
		exclude = ['message_date']

		widgets = {
			'estate': TextInput(attrs={'type': 'hidden'})
		}

		labels = {
			'full_name': 'Full Name',
			'email': 'Your Email',
			'phone': 'Phone Number',
			'message': 'Your Message'
		}
		help_texts = {
            'phone': 'Please write with country code.',
        }