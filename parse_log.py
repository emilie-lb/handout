import datetime
import logging
logging.basicConfig(level=logging.DEBUG)


logging.info("vérification si le pays demandé existe")


def open_log_file(path):
    liste_logs = []
    with open(path, "r") as log_file:
        for line in log_file.readlines():
            if line != "\n":
                liste_logs += [line.strip()]
    return liste_logs


def delai_min(line):
    date_time1 = datetime.datetime.strptime(line[0:5], '%H:%M')
    date_time2 = datetime.datetime.strptime(line[6:11], '%H:%M')
    timedelta= date_time2-date_time1
    return int(timedelta.total_seconds() / 60)

def create_delai_list(log):
    delai = delai_min(log)
    activity = log.strip().split(" ", 1)[1]
    return [delai, activity]


def temps_total(dico):
    total=0
    for min in dico.values():
        total += min
    return total


def write_file(liste):
    f = open("expected_output.txt", "w")
    for ligne in liste:
        f.write(ligne + "\n")

def liste_lignes_export(dico, total):
    liste_lignes=[]
    for key in sorted(dico.keys()):
        percent = dico[key]*100//total
        str_ok=f"{key:<20}{dico[key]:>9} minutes{percent:>5}%"
        # print(str_ok)
        # print(len(str_ok))
        liste_lignes.append(str_ok)
    return liste_lignes

def main(path):
    liste_logs = open_log_file(path)
    liste_delai=[]
    dico_delai = {}
    for log in liste_logs:
        liste_delai.append(create_delai_list(log))
    for ligne in liste_delai:
        if ligne[1] in dico_delai:
            dico_delai[ligne[1]] += ligne[0]
        else:
            dico_delai[ligne[1]]=ligne[0]
    total = temps_total(dico_delai)
    liste_lignes = liste_lignes_export(dico_delai, total)

    
    write_file(liste_lignes)

    


# print(main("planning.log"))
main("planning.log")
