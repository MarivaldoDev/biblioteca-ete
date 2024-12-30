from celery import shared_task
from django.core.mail import send_mail


@shared_task
def enviar_email(portador, livro, email):
    send_mail(
        subject='Hora de devolver!', 
        message=f'Olá {portador}!\nVocê precisa devolver ou renovar o empréstimo do livro "{livro.upper()}" à biblioteca.',            
        from_email='testesdepython2@gmail.com',
        recipient_list=[email]
    )
    
    return None