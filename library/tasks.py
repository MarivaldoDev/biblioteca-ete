import os
import django
from django.conf import settings
from datetime import datetime
from django.core.mail import send_mail
from library.models import Emprestimo


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ete.settings')
django.setup()

if not settings.configured:
    raise RuntimeError("As configurações do Django não foram carregadas corretamente.")


def checar_emprestimo():
    emprestimos = Emprestimo.objects.all()

    for emprestimo in emprestimos:
        if emprestimo.fim_emprestimo:
            enviar_email(emprestimo.portador, emprestimo.livro, emprestimo.portador.email)
            print('\033]1;33m E-mail enviado!\033[m')


def enviar_email(portador, livro, email):
    send_mail(
        subject='Hora de devolver!', 
        message=f'Olá {portador}!\nVocê precisa devolver ou renovar o empréstimo do livro "{livro.upper()}" à biblioteca.',            
        from_email='testesdepython2@gmail.com',
        recipient_list=[email]
    )

if __name__ == "__main__":
    checar_emprestimo()