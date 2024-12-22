from celery import shared_task
from django.core.mail import send_mail
from .models import Emprestimo


@shared_task
def checar_emprestimo():
    # emprestimos = Emprestimo.objects.all()

    # for emprestimo in emprestimos:
    #     if emprestimo.fim_emprestimo:
    #         enviar_email(emprestimo.portador, emprestimo.livro, emprestimo.portador.email)
    #         print('\033]1;33m E-mail enviado!\033[m')
    
    return 'Tarefa concluída!'

def enviar_email(portador, livro, email):
    send_mail(
        subject='Hora de devolver!', 
        message=f'Olá {portador}!\nVocê precisa devolver ou renovar o empréstimo do livro "{livro.upper()}" à biblioteca.',            
        from_email='testesdepython2@gmail.com',
        recipient_list=[email]
    )


if __name__ == "__main__":
    checar_emprestimo()