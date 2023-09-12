"""
This file contains all the common utilty functions to be used
"""
import re
from django.core.mail import EmailMessage



class StringUtils:
    """
    class represents the string util functions
    """
    @staticmethod
    def to_uppercase(string:str) -> str:
        result = string.upper() if string else None
        return result
    
    @staticmethod
    def to_lower(string:str) -> str:
        result = string.lower() if string else None
        return result
    

class AuthenticationUtils:

    @staticmethod
    def validate_email(email:str) -> bool:
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_pattern, email):
            return True
        else:
            return False
        
        




class SendEmailUtils:
    @staticmethod
    def send_email(data):
        """ method to send email """
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        email.send(fail_silently=False)

    # @staticmethod
    # def send_mass_email(data):
    #     """ method to send email """
    #     email = EmailMessage(
    #         subject=data['email_subject'], body=data['email_body'], to=data['to_email'])
    #     EmailThread(email).start()
