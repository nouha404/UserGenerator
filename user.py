"""Module qui genere des données aléatoires"""
from faker import Faker
from pathlib import Path
import logging

fake = Faker(locale='fr_Fr')
ROOT_FOLDER = Path(__file__).resolve().parent
user_log = ROOT_FOLDER / 'user.log'


logging.basicConfig(filename= user_log,filemode='a' ,level=logging.INFO)

if not Path.exists(user_log):
    user_log.touch()

def get_user():
    """get_user

    Returns:
        str: _cette fonction retourne un nom et prenom aleatoire_
    """
    logging.info('Generer les donner aleatoires')
    return f'{fake.name()} {fake.first_name()}'
    
def get_users(nombre_user : int = 1):
    """get_users

    Args:
        nombre_user (int, optional): _description_. Defaults to 1.

    Returns:
        list: _Retourne une liste de {nombre_user}_
    """
    user_liste = []
    i = 0
    while i < nombre_user:
        i += 1
        user_liste.append(get_user())
          
    logging.info(f'Generation de {nombre_user} liste de données aleatoires' )
    return user_liste

if __name__ == '__main__':
    user = get_users()
    print(user)
    """ Explication
        __name__ == '__main__' :
    pour que quand on va importer le module
    que le script ne s'execute pas directement car name sera != de main
    """



