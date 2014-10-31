
# -*- coding: utf-8 -*-
from lettuce import step, world
import sys
sys.path.append('../')
from Triangle import Triangle

@step(u'Given: Un triangulo de lados "([^"]*)", "([^"]*)", "([^"]*)"')
def given_un_triangulo_de_lados_group1_group2_group1(step, a, b, c):
    world.parametros=[int(a), int(b), int(c)]

@step(u'When: realizo el calculo')
def when_realizo_el_calculo(step):
	trian = Triangle(world.parametros)
	world.tipo = trian.istriangle()
   

@step(u'Then: obtengo un triangulo de tipo "([^"]*)"')
def then_obtengo_un_triangulo_de_tipo_group1(step, tipo):
	assert world.tipo == tipo, "resultado obtenido {0}, resultado esperado {1}".format(world.tipo, tipo)
    
