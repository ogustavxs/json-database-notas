from tinydb import TinyDB, Query
import os
db = TinyDB('database.json')
gradeq = Query()

def clear():
    """Clear the terminal"""
    os.system('cls')

def check(subjects:str, bimonthly:int):
    """Checks whether a subject and a bimonthly period are valid and exist in the database."""
    if db.contains(gradeq.subjects == subjects):
        if db.contains(gradeq.bimonthly == bimonthly):
            return True
        else:
            return False
    else:
        return False
    
def check_max_min(grade:float):
    """Checks if a school grade is within the valid range of 0 to 10."""
    if grade < 0 or grade > 10:
        return False
    else:
        return True
    
def add(subjects:str, bimonthly:int, grade:float):
    """Adds a grade to a specified bimonthly period of a subject."""
    if check(subjects, bimonthly) and check_max_min(grade):
        db.update({'grade': grade}, (gradeq.subjects == subjects) & (gradeq.bimonthly == bimonthly))

def get(subjects:str, bimonthly:int):
    """Retrieves the grade for a specified subject and bimonthly period."""
    if check(subjects, bimonthly):
        return db.search((gradeq.subjects == subjects) & (gradeq.bimonthly == bimonthly))[0]['grade']

def get_all(subjects:str):
    """Retrieves all grades for a specified subject."""
    if check(subjects, 1):
        a = db.search(gradeq.subjects == subjects)
        return a

def get_all_grades(subjects:str):
    """Retrieves all grades (only) for a specified subject."""
    if check(subjects, 1):
        notaslista = []
        for notas in get_all(subjects):
            notaslista.append(notas['grade'])
        return notaslista

def list_all():
    """Retrieves all entries in the database."""
    return db.all()

def list_all_names():
    """Retrieves a list of all subject names."""
    return ["portugues", "matematica", "biologia", "fisica", "quimica", "historia", "sociologia", "filosofia", "geografia", "ingles", "espanhol", "ed_fisica"]
