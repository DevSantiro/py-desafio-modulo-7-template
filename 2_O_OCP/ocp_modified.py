'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''

from abc import ABC, abstractmethod

# Interfaces
class ExameInterface(ABC):
    @abstractmethod
    def verifica_condicoes_exame() -> bool: pass


class AprovadorInterface(ABC):
    @abstractmethod
    def aprovar_solicitacao_exame() -> bool: pass


# Classes
class Aprovador(AprovadorInterface):
    def aprovar_solicitacao_exame(self, exame: ExameInterface) -> bool: 
        if exame.verifica_condicoes_exame():
            print("Exame aprovado!")

class ExameSangue(ExameInterface):
    def verifica_condicoes_exame(self) -> bool:
        print("Verificando condições do exame de Sangue!")
        return True

class ExameRaioX(ExameInterface):
    def verifica_condicoes_exame(self) -> bool:
        print("Verificando condições do exame de RaioX!")
        return True


exame_sangue = ExameSangue()
exame_raio_x = ExameRaioX()
aprovador    = Aprovador()

aprovador.aprovar_solicitacao_exame(exame_sangue)
aprovador.aprovar_solicitacao_exame(exame_raio_x)

