CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["utils"],0)


creneaux = CoreLibs.utils.creneaux


def deleteTuteur(name, surname, groupid):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    delete_rq="DELETE FROM 'tuteur' WHERE name = '"+name+"' AND surname = '"+surname+"' AND groupid = "+str(groupid)
    cursor.execute(delete_rq)
    MainDB.commit()
    cursor.close()
    return 


def addTuteur(name, surname, groupid,parsedFreetime,parsedSubjects):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""INSERT INTO tuteur (name,surname,group,freeon,subject) VALUES (?,?,?,?,?)""",(name,surname,groupid,parsedFreetime,parsedSubjects))
    MainDB.commit()
    return cursor.close()


def findTuteur(groupLVL,parsedFreetime,parsedSubjects):
    results = []
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    for i in parsedFreetime:
        for j in parsedSubjects:
            cursor.execute("""SELECT name, surname FROM 'tuteur' INNER JOIN 'group' ON tuteur.groupid = 'group'.id WHERE 'group'.level <= ? AND freeon LIKE ? AND subject LIKE ?""",(groupLVL,i,j))
            results.append((i,j,cursor.fetchall()))
    cursor.close()
    return results