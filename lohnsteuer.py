# globals 
username = 'user'
brutto = 0
lohnsteuer = 0
soli = 0
kirche = 0
kv = 0
pv = 0
rv = 0
av = 0

pro_soli = 0
pro_kirche = 0
glaube_ja_nein = 'Ja'
pro_kv = 0
pro_pv = 0
pro_rv = 0
pro_av = 0

fin_pro_soli = 0
fin_pro_kirche = 0
fin_pro_kv = 0
fin_pro_pv = 0
fin_pro_rv = 0
fin_pro_av = 0

def get_username():
    global username
    username = input('Bitte geben Sie ihren Nutzernamen ein: ')
    print(f'Hallo {username}, in den folgenden Schritten werden wir Sie nach Informationen fragen und im Anschluss erhalten Sie ihre Lohnsteuer. Viel Spaß')

def get_informations():
    global brutto, lohnsteuer, soli, kirche, kv, pv, rv, av, pro_soli, pro_kirche, pro_kv, pro_pv, pro_rv, pro_av

    brutto = float(input('Geben Sie Ihr Brutto-Gehalt ein: '))

    lohnsteuer = float(input('Geben Sie Ihr Lohnsteuer Betrag ein: '))
    
    soli = float(input('Geben Sie den Prozentsatz für den Solidaritätszuschlag ein: '))

    print('Sind Sie dem Christentum zugewandt?')
    glaube_ja_nein = str(input('Falls Ja schreiben Sie "Ja", sollte dies nicht der Fall sein so schreiben Sie "Nein": '))
    if glaube_ja_nein == 'Ja':
        print('Wohnen Sie in Badem-Württemberg oder Bayern?')
        bundesland_bb = str(input('Falls Ja schreiben Sie "Ja", sollte dies nicht der Fall sein so schreiben Sie "Nein": '))
        if bundesland_bb == 'Ja':
            kirche = 8
        elif bundesland_bb == 'Nein':
            kirche = 9
    elif glaube_ja_nein == 'Nein':
        kirche = 0

    kv = float(input('Geben Sie den Prozentsatz für Ihre Krankenversicherung an: '))
    pv = float(input('Geben Sie den Prozentsatz für Ihre Pflegeversicherung an: '))
    rv = float(input('Geben Sie den Prozentsatz für Ihre Rentenversicherung an: '))
    av = float(input('Geben Sie den Prozentsatz für Ihre Arbeitslosenversicherung an: '))

    pro_soli = soli/100
    pro_kirche = kirche/100
    pro_kv = kv/100
    pro_pv = pv/100
    pro_rv = rv/100
    pro_av = av/100

    print('Vielen Dank für das Eingeben Ihrer Informationen')


def convert_informations():
    global fin_pro_soli, fin_pro_kirche, fin_pro_kv, fin_pro_pv, fin_pro_rv, fin_pro_av
    global brutto, pro_soli, pro_kirche, pro_kv, pro_pv, pro_rv, pro_av

    fin_pro_soli = brutto * pro_soli
    fin_pro_kirche = lohnsteuer * pro_kirche
    fin_pro_kv = brutto * pro_kv
    fin_pro_pv = brutto * pro_pv
    fin_pro_rv = brutto * pro_rv
    fin_pro_av = brutto * pro_av



def generate_lohnsteuer():
    print('Hier ist Ihre fertige Lohnsteuer:')
    
    print(f'Brutto: {brutto}')

    print(f'Brutto gesamt: {brutto}')

    print(f'Lohnsteuer: {lohnsteuer}')

    print(f'Solidaritaetszuschlag: {fin_pro_soli}')

    print(f'Kirchensteuer: {fin_pro_kirche}')
    
    print(f'Krankenversicherung: {fin_pro_kv}')
    
    print(f'Pflegeversicherung: {fin_pro_pv}')

    print(f'Rentenversicherung: {fin_pro_rv}')

    print(f'Arbeitslosenversicherung: {fin_pro_av}')


def user_wants_again():
    print('Hello World')

def create_lohnsteuer():
    get_username()
    get_informations()
    convert_informations()
    generate_lohnsteuer()
    user_wants_again()

create_lohnsteuer()
