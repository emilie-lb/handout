import datetime
import logging
import argparse

logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument(dest='path', type=str, help='chemin vers fichier .log')
args = parser.parse_args()
# print(args)


def open_log_file(path):
    logging.debug(f"fonction open_log_file, fichier à ouvrir {path}")
    liste_logs = []
    with open(path, "r") as log_file:
        logging.debug(f"entrée dans fichier{path}")
        for line in log_file.readlines():
            if line != "\n":
                liste_logs += [line.strip()]
    logging.debug(f"ligne 1 de la liste de logs => {liste_logs[0]}")
    return liste_logs


def delai_min(line):
    date_time1 = datetime.datetime.strptime(line[0:5], '%H:%M')
    date_time2 = datetime.datetime.strptime(line[6:11], '%H:%M')
    timedelta = date_time2-date_time1
    return int(timedelta.total_seconds() / 60)


def create_delai_list(log):
    delai = delai_min(log)
    activity = log.strip().split(" ", 1)[1]
    return [delai, activity]


def temps_total(dico):
    total = 0
    for min in dico.values():
        total += min
    return total


def write_file(liste):
    logging.debug("entrée dans fonction write_file")
    f = open("expected_output.txt", "w")
    for ligne in liste:
        f.write(ligne + "\n")


def liste_lignes_export(dico, total):
    logging.debug("entrée dans fonction liste_lignes_export")
    liste_lignes = []
    for key in sorted(dico.keys()):
        percent = dico[key]*100//total
        str_ok = f"{key:<20}{dico[key]:>9} minutes{percent:>5}%"
        liste_lignes.append(str_ok)
    logging.debug(f"ligne 1 de liste_lignes =>\n{liste_lignes[0]}")
    logging.debug(f"longueur de la 1ere ligne => {len(liste_lignes[0])}")
    return liste_lignes


def create_dico_delai(liste):
    dico_delai = {}
    for ligne in liste:
        if ligne[1] in dico_delai:
            dico_delai[ligne[1]] += ligne[0]
        else:
            dico_delai[ligne[1]] = ligne[0]
    return dico_delai


def main(path):
    liste_logs = open_log_file(path)
    liste_delai = []
    for log in liste_logs:
        liste_delai.append(create_delai_list(log))
    dico_delai = create_dico_delai(liste_delai)
    total = temps_total(dico_delai)
    liste_lignes = liste_lignes_export(dico_delai, total)
    write_file(liste_lignes)


if __name__ == '__main__':
    main(args.path)

# print(main("planning.log"))
# main("planning.log")
