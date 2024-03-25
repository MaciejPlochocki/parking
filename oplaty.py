from datetime import datetime

def oblicz_oplate(czas_wjazdu, czas_wyjazdu, stawka):
    format_czasu = "%H:%M"
    wjazd = datetime.strptime(czas_wjazdu, format_czasu)
    wyjazd = datetime.strptime(czas_wyjazdu, format_czasu)
    roznica = wyjazd - wjazd
    ilosc_godzin = roznica.seconds // 3600
    return ilosc_godzin * stawka
