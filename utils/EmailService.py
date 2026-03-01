from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

class EmailService:

    @staticmethod
    def send_email(subject, template_name, context, recipient_list):
        try:
            html_content = render_to_string(template_name, context)
            print('-----------------------------------')
            print(html_content)
            email = EmailMultiAlternatives(
                subject=subject,
                body='',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=recipient_list
            )

            email.attach_alternative(html_content, "text/html")
            email.send()
            print("Email sent")
            return True
        except Exception as e:
            print("Email Error:", e)
            return False