# globals 
username = 'user'
brutto = 0
lohnsteuer = 0
pro_soli = 0
pro_kirche = 0
glauben = True
pro_kv = 0
pro_pv = 0
pro_rv = 0
pro_av = 0


def get_username():
    username = input('Bitte geben Sie ihren Nutzernamen ein: ')
    print(f'Hallo {username}, in den folgenden Schritten werden wir Sie nach Informationen fragen und im Anschluss erhalten Sie ihre Lohnsteuer. Viel Spaß')

def get_informations():
    brutto = float(input('Geben Sie Ihr Brutto-Gehalt ein: '))

    lohnsteuer = float(input('Geben Sie Ihr Lohnsteuer Betrag ein: '))
    
    pro_soli = float(input('Geben Sie den Prozentsatz für den Solidaritätszuschlag ein: '))

    print('Sind Sie dem Christentum zugewandt?')
    glauben = str(input('Falls Ja schreiben Sie "Ja", sollte dies nicht der Fall sein so schreiben Sie "Nein"'))
    print('Wohnen Sie in Badem-Württemberg oder Bayern?')
    


def generate_lohnsteuer():
    print('Hello World')

def user_wants_again():
    print('Hello World')

def create_lohnsteuer():
    get_username()
    get_informations()
    generate_lohnsteuer()
    user_wants_again()

create_lohnsteuer()
