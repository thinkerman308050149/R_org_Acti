import pytest
from tiempo import tiempo

def test_initialization():
    t = tiempo()
    assert t.minuto == 0
    assert t.hora == 0
    assert t.dia == 6
    assert t.fecha == 1
    assert t.mes == 1
    assert t.year == 2000

def test_custom_initialization():
    t = tiempo(minuto=30, hora=12, dia=3, fecha=15, mes=5, year=2024)
    assert t.minuto == 30
    assert t.hora == 12
    assert t.dia == 3
    assert t.fecha == 15
    assert t.mes == 5
    assert t.year == 2024

def test_invalid_minute():
    with pytest.raises(ValueError):
        tiempo(minuto=60)
    with pytest.raises(ValueError):
        tiempo(minuto=-1)

def test_invalid_hour():
    with pytest.raises(ValueError):
        tiempo(hora=24)
    with pytest.raises(ValueError):
        tiempo(hora=-1)

def test_invalid_day():
    with pytest.raises(ValueError):
        tiempo(dia=8)
    with pytest.raises(ValueError):
        tiempo(dia=0)

def test_invalid_month():
    with pytest.raises(ValueError):
        tiempo(mes=13)
    with pytest.raises(ValueError):
        tiempo(mes=0)

def test_invalid_year():
    with pytest.raises(ValueError):
        tiempo(year=1999)
    with pytest.raises(ValueError):
        tiempo(year=2100)

def test_invalid_date():
    with pytest.raises(ValueError):
        tiempo(fecha=32, mes=1)
    with pytest.raises(ValueError):
        tiempo(fecha=31, mes=4)
    with pytest.raises(ValueError):
        tiempo(fecha=29, mes=2, year=2023) # Not a leap year
    with pytest.raises(ValueError):
        tiempo(fecha=30, mes=2, year=2024) # Leap year

def test_avancetime_minuto():
    t = tiempo(minuto=59, hora=23, dia=7, fecha=31, mes=12, year=2023)
    t.avancetime_minuto()
    assert t.minuto == 0
    assert t.hora == 0
    assert t.dia == 1
    assert t.fecha == 1
    assert t.mes == 1
    assert t.year == 2024

def test_avancetime_hora():
    t = tiempo(hora=23, dia=7, fecha=31, mes=12, year=2023)
    t.avancetime_hora()
    assert t.hora == 0
    assert t.dia == 1
    assert t.fecha == 1
    assert t.mes == 1
    assert t.year == 2024

def test_avancetime_fecha():
    t = tiempo(dia=7, fecha=31, mes=12, year=2023)
    t.avancetime_fecha()
    assert t.dia == 1
    assert t.fecha == 1
    assert t.mes == 1
    assert t.year == 2024

def test_avancetime_mes():
    t = tiempo(mes=12, year=2023, fecha=31)
    t.avancetime_mes()
    assert t.mes == 1
    assert t.year == 2024
    assert t.fecha == 31

def test_avancetime_year():
    t = tiempo(year=2023)
    t.avancetime_year()
    assert t.year == 2024

def test_backtime_minuto():
    t = tiempo(minuto=0, hora=0, dia=1, fecha=1, mes=1, year=2024)
    t.backtime_minuto()
    assert t.minuto == 59
    assert t.hora == 23
    assert t.dia == 7
    assert t.fecha == 31
    assert t.mes == 12
    assert t.year == 2023

def test_backtime_hora():
    t = tiempo(hora=0, dia=1, fecha=1, mes=1, year=2024)
    t.backtime_hora()
    assert t.hora == 23
    assert t.dia == 7
    assert t.fecha == 31
    assert t.mes == 12
    assert t.year == 2023

def test_backtime_fecha():
    t = tiempo(dia=1, fecha=1, mes=1, year=2024)
    t.backtime_fecha()
    assert t.dia == 7
    assert t.fecha == 31
    assert t.mes == 12
    assert t.year == 2023

def test_backtime_mes():
    t = tiempo(mes=1, year=2024, fecha=31)
    t.backtime_mes()
    assert t.mes == 12
    assert t.year == 2023
    assert t.fecha == 31

def test_backtime_year():
    t = tiempo(year=2024)
    t.backtime_year()
    assert t.year == 2023

def test_yearbisiesto():
    t_leap = tiempo(year=2024)
    t_not_leap = tiempo(year=2023)
    assert t_leap.yearbisiesto() is True
    assert t_not_leap.yearbisiesto() is False

def test_finalmes():
    t_31 = tiempo(mes=1)
    t_30 = tiempo(mes=4)
    t_29 = tiempo(mes=2, year=2024)
    t_28 = tiempo(mes=2, year=2023)
    assert t_31.finalmes() == 31
    assert t_30.finalmes() == 30
    assert t_29.finalmes() == 29
    assert t_28.finalmes() == 28

def test_name_day():
    t = tiempo(dia=1)
    assert t.name_day() == "Lunes"
    t = tiempo(dia=7)
    assert t.name_day() == "Domingo"

def test_name_mes():
    t = tiempo(mes=1)
    assert t.name_mes() == "Enero"
    t = tiempo(mes=12)
    assert t.name_mes() == "Diciembre"

def test_str():
    t = tiempo(minuto=30, hora=12, dia=3, fecha=15, mes=5, year=2024)
    assert str(t) == "Fecha:Miércoles 15 de Mayo del 2024 - Hora: 12:30"
