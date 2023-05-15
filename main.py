from datetime import date, timedelta
import holidays


def dia_util(ano, mes, dia_util):
    feriados = holidays.BR(), holidays.US()

    dia = 1
    dia_semana = date(ano, mes, dia).weekday()
    contador_dia_util = 0

    while contador_dia_util < dia_util:
        if dia_semana != 5 and dia_semana != 6 and date(ano, mes, dia) not in feriados:
            contador_dia_util += 1
        if contador_dia_util == dia_util:
            break
        dia += 1
        dia_semana = date(ano, mes, dia).weekday()

    return dia


if __name__ == '__main__':
    print(dia_util())  # passe ano, mes, dia-util que deseja retornar
