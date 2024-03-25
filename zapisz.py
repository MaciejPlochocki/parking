import os
import csv


def zapisz(rejestracja, godzina_wjazdu, godzina_wyjazdu):
    """
    funkcja która dodaje dane samochodu do pliku parking.csv.
    :param rejestracja: str.
    :param godzina_wjazdu: str.
    :param godzina_wyjazdu: str.
    """
    with open("parking.csv", "w", newline='') as f:
        write = csv.writer(f, delimiter=",")
        write.writerow(["numer_rejestracji",
                        "godzina_wjazdu",
                        "godzina_wyjazdu",])

        write.writerow([rejestracja,
                        godzina_wjazdu,
                        godzina_wyjazdu,
                        ])

    with open("parking.csv", "r") as f:
        r = csv.reader(f, delimiter=",")
        for row in r:
            print(",".join(row))
