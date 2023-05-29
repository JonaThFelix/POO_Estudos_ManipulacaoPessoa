from Pessoa import Pessoa
def i():
  print('-'*65)
  
p1 = Pessoa('Jorge',24,'Masculino')

#01 - apresentação, dormindo e sem fome
p1.apresentar()

i()

#02 - acordei, está acordado e com fome
p1.acordar()

i()

#03 - validei se realmente acordou
p1.apresentar()

i()

#04 - dormiu e está sem fome
p1.dormir()

i()

#05 - validando se realmente dormiu
p1.apresentar()

i()

#06 - alimentando o obj, porém botei ele pra dormir no 04, tenho que acordar
p1.comer()

i()

#07 - acordando e alimentando
p1.acordar()
p1.comer()
