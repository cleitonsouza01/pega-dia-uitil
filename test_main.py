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

import pytest
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


@pytest.mark.parametrize("test_input,expected", [("20200101", "20200103"), ("20200201", "20200204"), ("20200301", "20200303"), ("20200401", "20200402"), ("20200501", "20200505"), ("20200601", "20200602"), ("20200701", "20200702"), ("20200801", "20200804"), ("20200901", "20200902"), ("20201001", "20201002"), ("20201101", "20201103"), ("20201201", "20201202") ])
def test_retorna_segundo_dia_util_2020(test_input, expected):
    entrada = datetime.datetime.strptime(test_input, '%Y%m%d')
    expected = datetime.datetime.strptime(expected, '%Y%m%d')
    assert dia_util(entrada.year, entrada.month, 2) == expected

@pytest.mark.parametrize("test_input,expected", [("20320101", "20320105"), ("20320201", "20320203"), ("20320301", "20320302"), ("20320401", "20320402"), ("20320501", "20320504"), ("20320601", "20320602"), ("20320701", "20320702"), ("20320801", "20320803"), ("20320901", "20320902"), ("20321001", "20321004"), ("20321101", "20321103"), ("20321201", "20321202") ])
def test_retorna_segundo_dia_util_2032(test_input, expected):
    entrada = datetime.datetime.strptime(test_input, '%Y%m%d')
    expected = datetime.datetime.strptime(expected, '%Y%m%d')
    assert dia_util(entrada.year, entrada.month, 2) == expected


@pytest.mark.parametrize("test_input,expected", [("20080101", "20080103"), ("20080201", "20080204"), ("20080301", "20080304"), ("20080401", "20080402"), ("20080501", "20080505"), ("20080601", "20080603"), ("20080701", "20080702"), ("20080801", "20080804"), ("20080901", "20080903"), ("20081001", "20081002"), ("20081101", "20081104"), ("20081201", "20081202") ])
def test_retorna_segundo_dia_util_2008(test_input, expected):
    entrada = datetime.datetime.strptime(test_input, '%Y%m%d')
    expected = datetime.datetime.strptime(expected, '%Y%m%d')
    assert dia_util(entrada.year, entrada.month, 2) == expected


@pytest.mark.parametrize("test_input,expected", [("19980101", "19980105"), ("19980201", "19980203"), ("19980301", "19980303"), ("19980401", "19980402"), ("19980501", "19980505"), ("19980601", "19980602"), ("19980701", "19980702"), ("19980801", "19980804"), ("19980901", "19980902"), ("19981001", "19981002"), ("19981101", "19981103"), ("19981201", "19981202") ])
def test_retorna_segundo_dia_util_1998(test_input, expected):
    entrada = datetime.datetime.strptime(test_input, '%Y%m%d')
    expected = datetime.datetime.strptime(expected, '%Y%m%d')
    assert dia_util(entrada.year, entrada.month, 2) == expected
