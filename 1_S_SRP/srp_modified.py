'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''

class ConnectAPI:
    def conect_api(): pass

class Notification:
    def send_notification(): pass

class Report:
    def generate_report(): pass

    def send_report(): pass

class TaskHandler:
    def create_task(): pass

    def update_task(): pass

    def remove_task(): pass
