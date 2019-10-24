from django.test import TestCase

# Create your tests here.
'''
l= ['copo','copos','copaiba','girafa','amor','copo','Copos','feliz']
s= []
if len(l) > 0:
	if len(s) == 0:
		s.append(l[0])
print(l)
for i in range(1,len(l)):
	cont= False
	for j in range(len(s)):
		if l[i].lower() == s[j].lower():
			cont= True
	if not cont:
		s.append(l[i])
print(s)
'''
import unicodedata
import re

"""
A remoção de acentos foi baseada em uma resposta no Stack Overflow.
http://stackoverflow.com/a/517974/3464573
"""
palavra= 'âncora,.)'
def removeCharEspecials(palavra):
	#Unicode normalize transforma um caracter em seu equivalente em latin.
	nfkd= unicodedata.normalize('NFKD', palavra)
	palavraSemAcento= u"".join([c for c in nfkd if not unicodedata.combining(c)])
	#Usa expressão regular para retornar a palavra apenas com números, letras e espaço
	return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)
print(removeCharEspecials(palavra))