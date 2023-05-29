class Pessoa:
  
  def __init__(self,nome,idade,sexo,acordado=False,fome=False):
    self.nome = nome
    self.idade = idade
    self.sexo = sexo
    self.acordado = acordado
    self.fome = fome

  def apresentar(self):
    print(f'O nome da pessoa é {self.nome} !')
    if self.acordado == False:
      print(f'{self.nome} está dormindo.')
    else:
      print(f'{self.nome} está acordado.')

  def acordar(self):
    self.acordado = True
    print(f'Agora {self.nome} está acordado')
    self.fome = True
    print(f'{self.nome} está com fome !!!')

  def dormir(self):
    self.acordado = False
    print(f'{self.nome} foi dormir, volte amanhã.')
    self.fome = False
    print(f'{self.nome} não está com fome, pois está dormindo.')

  def comer(self):
    self.fome = True
    if self.acordado == True:
      print(f'{self.nome} está com fome e está comendo')
    else:
      print(f'{self.nome} não tem como comer, pois está dormindo')
