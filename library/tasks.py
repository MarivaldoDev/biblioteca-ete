from celery import shared_task
from .models import Emprestimo
from django.core.mail import send_mail


@shared_task
def enviar():
    emprestimos = Emprestimo.objects.all()
    for emprestimo in emprestimos:
        contato = Emprestimo.objects.get(id=emprestimo.id)
        if emprestimo.fim_emprestimo:
            send_mail(
                subject='Hora de devolver!', 
                message=f'Olá {emprestimo.portador}!\nVocê precisa devolver ou renovar o empréstimo do livro "{emprestimo.livro.upper()}" à biblioteca.',            
                from_email='testesdepython2@gmail.com',
                recipient_list=[contato.portador.email]
            )

            emprestimo.delete(id=emprestimo.id)