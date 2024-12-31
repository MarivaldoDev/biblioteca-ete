from celery import shared_task
from django.core.mail import send_mail
from .models import Emprestimo


@shared_task
def enviar_email():
    emprestimos = Emprestimo.objects.all()
    
    for emprestimo in emprestimos:
        if emprestimo.fim_emprestimo:
            send_mail(
                subject='Hora de devolver!', 
                message=f'Olá {emprestimo.portador.nome}!\nVocê precisa devolver ou renovar o empréstimo do livro "{emprestimo.livro.upper()}" à biblioteca.',            
                from_email='testesdepython2@gmail.com',
                recipient_list=[emprestimo.portador.email]
            )
    
    return None