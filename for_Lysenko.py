# -*- coding: utf-8 -*-
import numpy as np
import random

def saddle_point():
	global b, elements_in_rows, elements_in_columns
	b = np.random.randint(1,11, size=(4,4))
	print "    Зададим матрицу выигрышей:"
	print b
	elements_in_rows = list(np.amin(b, axis=1))
	elements_in_columns = list(np.amax(b, axis=0))
	print "    Найдем нижнюю границу alfa:" 
	print "Минимальный элемент в каждой строке: %s" %elements_in_rows
	print "Нижняя цена игры: %s" %max(elements_in_rows)
	print "    Найдем верхнюю границу beta:"
	print "Максимальный элемент в каждом столбце: %s" %elements_in_columns
	print "Верхняя граница игры: %s" %min(elements_in_columns)
	if max(elements_in_rows)!=max(elements_in_columns): print "Матрица не содержит седловой точки - переходим к критерию Байеса"
	else: print "Матрица содержит седловую точку"
	print "-"*80
	
def Bayes():
	print "    Определим наилучшую стратегию по критерию Байеса:"
	P = np.array([.1,.2,.3,.4])
	print "Зададим матрицу вероятностей: %s" %P
	matrix_average_gain = list(np.dot(P,np.transpose(b)))
	print "Найдем матрицу средних выигрышей: %s" %matrix_average_gain
	print "Выбираем максимальный средний выигрыш: %s, что соответствует %d стратегии" %(max(matrix_average_gain),matrix_average_gain.index(max(matrix_average_gain))+1)
	print "-"*80
	
def Vald():
	print "    Определим наилучшую стратегию по критерию Вальда:"
	print "Сформируем матрицу наихудших условий: %s " %elements_in_rows
	print "Максимальное значение в матрице наихудших условий: %s, что соответствует %d стратегии" %(max(elements_in_rows), elements_in_rows.index(max(elements_in_rows))+1)
	print "-"*80

def Sevidz():
	pass
	
def Gurvits():
	print "    Определим наилучшую стратегию по критерию Гурвица для коэффициента компромиса eta = 0.5:"
	eta = 0.5
	gurvits_list = 0.5*np.amax(b, axis=1)+0.5*np.amin(b, axis=1)
	print "Матрица Гурвица имеет вид: %s" %gurvits_list	
	print "-"*80
	
	
if __name__=='__main__':
    saddle_point()
    Bayes()
    Vald()
    Sevidz()
    Gurvits()
    
    
