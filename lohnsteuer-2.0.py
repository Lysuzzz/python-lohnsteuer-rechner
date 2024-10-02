# Konstanten für die Kirchensteuer
KIRCHE_BW_BAYERN = 0.08  # 8% für Baden-Württemberg und Bayern
KIRCHE_ANDERE = 0.09      # 9% für alle anderen Bundesländer
KIRCHE_NULL = 0.0         # Keine Kirchensteuer

def get_username():
    username = input('Bitte geben Sie ihren Nutzernamen ein: ')
    print(f'Hallo {username}, in den folgenden Schritten werden wir Sie nach Informationen fragen und im Anschluss erhalten Sie ihre Lohnsteuer. Viel Spaß')
    return username

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Bitte geben Sie eine gültige Zahl ein.")

def get_informations():
    brutto = get_float_input('Geben Sie Ihr Brutto-Gehalt ein: ')
    lohnsteuer = get_float_input('Geben Sie Ihr Lohnsteuer Betrag ein: ')
    soli = get_float_input('Geben Sie den Prozentsatz für den Solidaritätszuschlag ein: ')
    
    glaube = input('Sind Sie dem Christentum zugewandt? (Ja/Nein): ').strip().capitalize()
    kirche = KIRCHE_NULL
    if glaube == 'Ja':
        bundesland = input('Wohnen Sie in Baden-Württemberg oder Bayern? (Ja/Nein): ').strip().capitalize()
        if bundesland == 'Ja':
            kirche = KIRCHE_BW_BAYERN
        else:
            kirche = KIRCHE_ANDERE
    
    kv = get_float_input('Geben Sie den Prozentsatz für Ihre Krankenversicherung an: ')
    pv = get_float_input('Geben Sie den Prozentsatz für Ihre Pflegeversicherung an: ')
    rv = get_float_input('Geben Sie den Prozentsatz für Ihre Rentenversicherung an: ')
    av = get_float_input('Geben Sie den Prozentsatz für Ihre Arbeitslosenversicherung an: ')
    
    return brutto, lohnsteuer, soli, kirche, kv, pv, rv, av

def calculate_deductions(brutto, lohnsteuer, soli, kirche, kv, pv, rv, av):
    pro_soli = soli / 100
    pro_kirche = kirche
    pro_kv = kv / 100
    pro_pv = pv / 100
    pro_rv = rv / 100
    pro_av = av / 100

    fin_pro_soli = brutto * pro_soli
    fin_pro_kirche = lohnsteuer * pro_kirche
    fin_pro_kv = brutto * pro_kv
    fin_pro_pv = brutto * pro_pv
    fin_pro_rv = brutto * pro_rv
    fin_pro_av = brutto * pro_av

    return fin_pro_soli, fin_pro_kirche, fin_pro_kv, fin_pro_pv, fin_pro_rv, fin_pro_av

def generate_lohnsteuer(brutto, lohnsteuer, deductions):
    print('Hier ist Ihre fertige Lohnsteuer:')
    
    # Erstellen einer Liste mit Labels und den zugehörigen Werten
    labels = ['Brutto', 'Lohnsteuer', 'Solidaritätszuschlag', 'Kirchensteuer', 
              'Krankenversicherung', 'Pflegeversicherung', 'Rentenversicherung', 
              'Arbeitslosenversicherung', 'Nettobetrag']
    
    values = [brutto, lohnsteuer] + list(deductions)
    
    # Berechnung des Nettobetrags
    nettobetrag = brutto - sum(deductions) - lohnsteuer
    values.append(nettobetrag)
    
    # Ausgabe in zwei Spalten
    for label, value in zip(labels, values):
        print(f'{label:>25}: {value:>15.2f}')

def user_wants_again():
    again = input('Wenn Sie eine neue Lohnsteuer machen möchten, dann schreiben Sie "Ja": ').strip().capitalize()
    return again == "Ja"

def create_lohnsteuer():
    username = get_username()
    brutto, lohnsteuer, soli, kirche, kv, pv, rv, av = get_informations()
    deductions = calculate_deductions(brutto, lohnsteuer, soli, kirche, kv, pv, rv, av)
    generate_lohnsteuer(brutto, lohnsteuer, deductions)
    
    if user_wants_again():
        create_lohnsteuer()

create_lohnsteuer()
