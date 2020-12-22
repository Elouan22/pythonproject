# -*- coding: utf-8 -*-
"""
Code modifiable.
"""

from automate import Automate
from state import State
from transition import Transition
from parser import *

# Création de l'automate à l'aide de ses transistions : 
# création d'états 
# s0 state 
s0 = State(0,True,False)
# s1 state 
s1 = State(1,False,True)
# s2 state 
s2 = State(2,False,True)
#Création de transitions 
t1 = Transition(s0,"a",s0);
t2 = Transition(s0,"b",s1);
t3 = Transition(s1,"a",s2);
t4 = Transition(s1,"b",s2);
t5 = Transition(s2,"a",s0);
t6 = Transition(s2,"b",s1);
# affichage de l'automate 
auto = Automate([t1,t2,t3,t4,t5,t6])
print(auto)
auto.show("A_ListeTrans")

# Créations de l'automate à l'aide de ses transitions et états : 
auto1 = Automate([t1,t2,t3,t4,t5,t6], [s0,s1,s2])
print(auto1)
auto1.show("A_ListeEtats")
# Création de l'aitomate à partir d'un fichier texte : 
auto2 = Automate.creationAutomate("auto.txt")
print(auto2)
auto2.show("A_texte")
"""
# Premières manipulations
t = Transition(s0,"a",s0)
auto.removeTransition(t)
print(auto)
auto.removeTransition(t1)
print(auto)
auto.addTransition(t1)
print(auto)
auto.show("A_addtransition")
auto.removeState(s1)
print(auto)
auto.addState(s1)
print(auto)
s2 = State(0,True,False)
auto.addState(s2)
print(auto)
auto1.getListTransitionsFrom(s1)
print(auto1)
"""
# Exercices de base : tests et complétion
# test de la fonction succ
liste = auto.succ([s0,s1,s2],"a")
print(liste)

# test de la fonction accepte 
accepte(auto,"aba")





















