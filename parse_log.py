import datetime
import logging
import argparse

logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument(dest='path', type=str, help='chemin vers fichier .log')
args = parser.parse_args()


def open_log_file(path):
    """ Cette fonction ouvre le fichier .log et enregistre les lignes
    dans une liste
    Parametre : chemin vers le fichier .log
    Return : liste contenant toutes les lignes du fichier .log en format
    """
    logging.info(f"fonction open_log_file, fichier à ouvrir {path}")
    liste_logs = []
    with open(path, "r") as log_file:
        logging.debug(f"entrée dans fichier{path}")
        for line in log_file.readlines():
            if line != "\n":
                liste_logs += [line.strip()]
    logging.debug(f"ligne 1 de la liste de logs => {liste_logs[0]}")
    return liste_logs


def delai_min(log):
    """ Cette fonction calcule le temps (ou délai) d'une activité donnée
    Parametre : une string contenant une ligne du fichier .log
    (ex: "09:20-11:00 Introduction")
    Return : temps de l'activité en minute (type integer)
    (ex: 100)
    """
    date_time1 = datetime.datetime.strptime(log[0:5], '%H:%M')
    date_time2 = datetime.datetime.strptime(log[6:11], '%H:%M')
    timedelta = date_time2-date_time1
    return int(timedelta.total_seconds() / 60)


def create_delai_list(log):
    """ Cette fonction extrait d'une line de log l'activité et calcule le
    délai de cette activité en min (en appelant la fonction delai_min(log))
    Parametre : une string contenant une ligne du fichier .log
    (ex: "09:20-11:00 Introduction")
    Return : une liste
    (ex: ["Exercises", 100])
    """
    delai = delai_min(log)
    activity = log.strip().split(" ", 1)[1]
    return [delai, activity]


def create_dico_delai(liste):
    """ Cette fonction crée un dictionnaire contenant les noms des
    activités (clés) et les temps cumulés pour chaque activité (valeurs)
    Parametre : une liste de de listes contenant 2 éléments,
    l'activité (string) et le délai en minutes (integer).
    (ex: [["Introduction", 40], ["Exercises", 100], ["Exercises", 105])
    Return : un dictionnaire contenant les activités (clés) et le temps cumulé
    des activités (valeurs)
    """
    dico_delai = {}
    for ligne in liste:
        if ligne[1] in dico_delai:
            dico_delai[ligne[1]] += ligne[0]
        else:
            dico_delai[ligne[1]] = ligne[0]
    return dico_delai


def temps_total(dico):
    """ Cette fonction calcule le temps total des activités en minutes
    Parametre : un dico contenant les activités (clés) et le temps cumulé
    des activités (valeurs)
    Return : integer représentant le temps total de toutes les activités
    en minutes.
    """
    total = 0
    for minutes in dico.values():
        total += minutes
    logging.debug(f"temps total de toutes les activités {total}")
    return total


def liste_lignes_export(dico, total):
    """ Cette fonction met en forme les lignes de texte que le fichier
    de sortie contiendra
    Parametre :
    - un dico contenant les activités (clés) et le temps cumulé
    des activités (valeurs)
    - un integer (le temps total cumulé de toutes les activités)
    Return : une liste contenant les lignes de texte que le fichier
    de sortie contiendra (avec une mise respectant les contraintes
    d'alignement et de longueur de texte)
    (ex: "Break                      65 minutes    6%")
    """
    logging.debug("entrée dans fonction liste_lignes_export")
    liste_lignes = []
    for key in sorted(dico.keys()):
        percent = dico[key]*100//total
        str_ok = f"{key:<20}{dico[key]:>9} minutes{percent:>5}%"
        liste_lignes.append(str_ok)
    logging.debug(f"ligne 1 de liste_lignes =>\n{liste_lignes[0]}")
    logging.debug(f"longueur de la 1ere ligne => {len(liste_lignes[0])}")
    return liste_lignes


def write_file(liste):
    """ Cette fonction crée un fichier puis elle écrit les lignes sous
    leur forme finale dans ce fichier.
    Parametre : une liste contenant les lignes à ajouter au fichier
    de sortie
    """
    logging.debug("entrée dans fonction write_file")
    f = open("output.txt", "w")
    for ligne in liste:
        f.write(ligne + "\n")


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
