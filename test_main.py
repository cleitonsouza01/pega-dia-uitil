# Testes
# second business day
# 20230103
# 20230202
# 20230302
# 20230404
# 20230503
# 20230602
# 20230705
# 20230802
# 20230905
# 20231003
# 20231103
# 20231204
import datetime

from pytest import mark

from main import dia_util


def test_retorna_segundo_dia_util():
    data = '20230701'
    entrada = datetime.datetime.strptime(data, '%Y%m%d')
    saida = datetime.datetime.strptime('20230705', '%Y%m%d')
    assert dia_util(entrada.year, entrada.month, 2) == saida


def test_retorna_segundo_dia_util2():
    data = '20231101'
    entrada = datetime.datetime.strptime(data, '%Y%m%d')
    saida = datetime.datetime.strptime('20231103', '%Y%m%d')
    assert dia_util(entrada.year, entrada.month, 2) == saida

def test_retorna_segundo_dia_util3():
    data = '20231201'
    entrada = datetime.datetime.strptime(data, '%Y%m%d')
    saida = datetime.datetime.strptime('20231204', '%Y%m%d')
    assert dia_util(entrada.year, entrada.month, 2) == saida


def test_retorna_segundo_dia_util4():
    data = '20230101'
    entrada = datetime.datetime.strptime(data, '%Y%m%d')
    saida = datetime.datetime.strptime('20230103', '%Y%m%d')
    assert dia_util(entrada.year, entrada.month, 2) == saida


def test_retorna_segundo_dia_util5():
    data = '20230801'
    entrada = datetime.datetime.strptime(data, '%Y%m%d')
    saida = datetime.datetime.strptime('20230802', '%Y%m%d')
    assert dia_util(entrada.year, entrada.month, 2) == saida
