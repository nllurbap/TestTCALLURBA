import json
dades ={
        'nom':'',
        'edat':0,
        'alçada':1.00,
        'pes':0,
        'imc':0.00
        }

categories = {
        "AS":{
            'value':0,
            'bool':False,
            'limit':16
            },
        "AP":{
            'value':0,
            'bool':False,
            'limit':10
            },
        "SC":{
            'value':0,
            'bool':False,
            'limit':8
            },
        "SD":{
            'value':0,
            'bool':False,
            'limit':8
            },
        "CS":{
            'value':0,
            'bool':False,
            'limit':5
            },
        "P":{
            'value':0,
            'bool':False,
            'limit':12
            },
        "F":{
            'value':0,
            'bool':False,
            'limit':10
            },
        "RM":{
            'value':0,
            'bool':False,
            'limit':13
            },
        "R":{
            'value':0,
            'bool':False,
            'limit':2
            },
        "D":{
            'value':0,
            'bool':False,
            'limit':16
            },
        "EF":{
            'value':0,
            'bool':False,
            'limit':13,
            },    
        "CM":{
            'value':0,
            'bool':False,
            'limit':11,
            },
        
        "V":{
            'value':0,
            'bool':False,
            'limit':16,
            },
        "SOAA":{
            'value':0,
            'bool':False,
            'limit':8,
            },
        "CSNN":{
            'value':0,
            'bool':False,
            'limit':15,
            },
        "FG":{
            'value':0,
            'bool':False,
            'limit':13,
            },
        "FC":{
            'value':0,
            'bool':False,
            'limit':10,
            },
        "X":{
            'value':0,
            'bool':False,
            'limit':5,
            },
        }

def calculate_imc(pes,alzada):
    imc = pes / pow(alzada,2)
    return imc

def is_acord(pregunta):
    if pregunta == 3 or pregunta == 4:
        return True
    else:
        return False

def is_desacord(pregunta):
    if pregunta == 1 or pregunta == 0:
        return True
    else: 
        return False

def eval_mateixa_resposta(resposta1,resposta2):
    if ((is_acord(resposta1) and is_acord(resposta2)) or (is_desacord(resposta1) and is_desacord(resposta2)) or resposta1 == resposta2):
        return True
    else:
        return False

def eval_resposta_oposada(resposta1,resposta2):
    if ((is_acord(resposta1) and is_desacord(resposta2)) or (is_desacord(resposta1) and is_acord(resposta2)) or (resposta1 == 2 and resposta2 == 2)):
        return True
    else:
        return False

def make_inverter(value):
    result = 0
    if value == 4:
        result = 0
    elif value == 3:
        result = 1
    elif value == 1:
        result = 3
    elif value == 0:
        result = 4
    else:
        result = value
    return result

def is_inverter(value1,value2):
    if value1 == 1 and value2 == 3:
        return true
    elif value1 == 3 and value2 == 1:
        return true
    elif value1 == 0 and value2 == 4:
        return true
    elif value1 == 4 and value2 == 0:
        return true
    else:
        return false

def eval_items_infrequencia(respostes_llista):
    #Pregunta 20
    if respostes_llista[19] < 3:
        return False
    #Pregunta 13
    elif respostes_llista[12] < 3:
        return False
    #Pregunta 65
    elif respostes_llista[64] > 1:
        return False
    #Pregunta 72
    elif respostes_llista[71] < 3:
        return False
    #Pregunta 85
    elif respostes_llista[84] < 3:
        return False
    else:
        return True

def eval_items_correlacionats(respostes_llista):
    valor = 7
    #Pregunta 15 respota oposada Pregunta 78
    if  eval_resposta_oposada(respostes_llista[14],respostes_llista[77]):
        valor -= 1
    #Pregunta 1 mateixa resposta Pregunta 46
    if eval_mateixa_resposta(respostes_llista[0],respostes_llista[45]):
        valor -= 1
    #Pregunta 47 mateixa resposta Pregunta 77
    if eval_mateixa_resposta(respostes_llista[46],respostes_llista[76]):
        valor -= 1
    #Pregunta 34 resposta oposada Pregunta 66
    if eval_resposta_oposada(respostes_llista[33],respostes_llista[65]):
        valor -= 1
    #Pregutna 45 resposta oposada Pregunta 9
    if eval_resposta_oposada(respostes_llista[44],respostes_llista[8]):
        valor -= 1
    #Pregunta 84 resposta oposada Pregunta 40
    if eval_resposta_oposada(respostes_llista[83],respostes_llista[39]):
        valor -= 1
    # Pregunta 33 mateixa resposta Pregunta 80
    if eval_mateixa_resposta(respostes_llista[32],respostes_llista[79]):
        valor -= 1
    if valor < 5:
        print(f"El valor correlacional es {valor}")
        return False
    else:
        return True

def eval_patro_repetitiu(list_respostes):
    #S'avalua si una resposta s'ha donat en el 90% del test
    if list_respostes.count(0) > 78:
        return False
    elif list_respostes.count(1) > 78:
        return False
    elif list_respostes.count(2) > 78:
        return False    
    elif list_respostes.count(3) > 78:
        return False
    elif list_respostes.count(4) > 78:
        return False
    else:
        return True

def eval_patro_repetitiu_2(list_respostes):
    #S'avalua si totes les respostes del test s'han respost de manera 0 1 2 3 4 
    #Es a dir Totalment desacord, desacord, indiferent, acord, totalment acord 
    #De forma ciclica
    string_list = ''
    for value in list_respostes:
        string_list += str(value)
    string_patro = '01234'
    if string_list.count(string_patro) == 17:
        return False
    else:
        return True


def eval_anorexia_nerviosa(values_cat):
    # IMC + AS + AP + P + F
    return (imc_an and values_cat['AS']['bool'] and values_cat['P']['bool'] and values_cat['F']['bool'] and values_cat['AP']['bool'])

def eval_an_fartaneres(values_cat):
    # FG + FC 
    return (values_cat['FG']['bool'] and values_cat['FC']['bool'])

def eval_an_purges_medicament(values_cat):
    # CM
    return values_cat['CM']['bool']

def eval_an_purges_vomit(values_cat):
    # V
    return values_cat['V']['bool']

def eval_an_restrictiu_dieta(values_cat):
    #D
    return values_cat['D']['bool']

def eval_an_restrictiu_exercici(values_cat):
    #EF
    return values_cat['EF']['bool']

def eval_bulimia_nerviosa(values_cat):
    #IMC + FG + FC + AS + AP
    return (imc_bn and values_cat['FG']['bool'] and values_cat['FC']['bool'] and values_cat['AS']['bool'] and values_cat['AP']['bool'])

def eval_bn_vomit(values_cat):
    # V
    return values_cat['V']['bool']

def eval_bn_execici_fisic(values_cat):
    #EF
    return values_cat['EF']['bool']

def eval_bn_medicaments(values_cat):
    # CM
    return values_cat['CM']['bool']

def eval_trastorn_fartaneres(values_cat):
    # FG + FC
    return (values_cat['FG']['bool'] and values_cat['FC']['bool'])

def eval_teria(values_cat):
    # RM + (CS or SOAA or IMC)
    return (values_cat['RM']['bool'] and (values_cat['CS']['bool'] or values_cat['SOAA']['bool'] or imc_an))

def eval_ruminacio(values_cat):
    return values_cat['R']['bool']

def eval_pica(values_cat):
    return values_cat['CSNN']['bool']

f = open('data.json')
pepe = json.load(f)
preguntes = pepe['pepito']

list_respostes = []


print("Quin nom tens: ")
y = input()
dades['nom'] = y
print("Quina edat tens: ")
y = input()
y = int(y)
dades['edat'] = y
print("Quin alçada fas: ")
y = input()
y = float(y)
dades['alçada'] = y
print("Quin pes tens: ")
y = input()
y = float(y)
dades['pes'] = y

dades['imc'] = calculate_imc(dades['pes'],dades['alçada'])

if dades['imc'] > 17:
    imc_an = True
    imc_bn = False
else:
    imc_an = False
    imc_bn = True

for pregunta in preguntes:
    print(f"{pregunta['id']}. {pregunta['text']}")
    print(f"0. {pregunta['options'][0]['text']}")
    print(f"1. {pregunta['options'][1]['text']}")
    print(f"2. {pregunta['options'][2]['text']}")
    print(f"3. {pregunta['options'][3]['text']}")
    print(f"4. {pregunta['options'][4]['text']}")
    print("Introdueix la teva resposta: ")
    x = input()
    x = int(x)
    list_respostes.append(x)
    if pregunta['inverted'] == True:
        x = make_inverter(x)
    categories[pregunta['categoria']]['value'] += x
    if categories[pregunta['categoria']]['value'] > categories[pregunta['categoria']]['limit']:
        categories[pregunta['categoria']]['bool'] = True
    print("")

## Abans de evaluar el tiquet es fan les comprobacions pertinents de que el test sigui valid.
if not eval_items_infrequencia(list_respostes):
    print("El test no es pot evaluar pels items infrequents")
    eval = False
if not eval_items_correlacionats(list_respostes):
    print("El test no es pot evaluar pels items correlacionats")
    eval = False
if not eval_patro_repetitiu(list_respostes):
    print("El 90% de les preguntes s'ha respos el mateix, queda invalidat")
    eval = False
if not eval_patro_repetitiu_2(list_respostes):
    print("Hi ha un patro repetitiu clar")
    eval = False

#En cas que no pasi cap de les evaluacions es denega la evaluació del test
if not eval:
    print("TESTING---------------------- ")
    cat_key = categories.keys()
    for cat in cat_key:
        print(f"{cat} /// {categories[cat]['bool']} /// {categories[cat]['value']}")
    print("")
    print(list_respostes)
    exit(0)

t = open('responses_bo.json')

pepe2 = json.load(t)
respostes = pepe2['pepito']

#Es recorre el fitxer de responses per mostrar el missatge corresponent segons el rang de valor de cada categoria.
for resposta in respostes:
    for value in resposta['values']:
        if categories[resposta['name']]['value'] >= value['min'] and categories[resposta['name']]['value'] <= value['max']:
            print(value['response'])
            print("")

## Finalment es fa el diagnostic final amb els valors obtinguts
frase = "El diagnostic final es "
if eval_anorexia_nerviosa(categories):
    frase += "anorexia nerviosa "
    if eval_an_purges_vomit(categories) or eval_an_purges_medicament(categories):
        frase += " purgativa "
        if eval_an_purges_vomit(categories):
            frase += "vomits " 
        if eval_an_purges_medicament(categories):
            frase += "medicaments"
        if eval_an_fartaneres(categories):
            frase += " i fartaneres"
    if eval_an_restrictiu_dieta(categories) or eval_an_restrictiu_exercici(categories):
        frase += "restrictiva "
        if eval_an_restrictiu_exercici(categories):
            frase += "exercici "
        if eval_an_restrictiu_dieta(categories):
            frase += "dieta "
elif eval_bulimia_nerviosa(categories):
    frase += "bulimia nerviosa "
    if eval_bn_vomit(categories):
        frase += "vomit "
    if eval_bn_medicaments(categories):
        frase += "medicament "
    if eval_bn_execici_fisic(categories):
        frase += "exercici "
elif eval_trastorn_fartaneres(categories):
    frase += "trastorn fartaneres"
elif eval_teria(categories):
    frase += "trastorn evitacio/restriccio de la ingesta d'aliments"
elif eval_pica(categories):
    frase += "pica"
else:
    frase += "no compatible amb cap TCA "

print(frase)
print("\n")

print("TESTING---------------------- ")
cat_key = categories.keys()
for cat in cat_key:
    print(f"{cat} /// {categories[cat]['bool']} /// {categories[cat]['value']}")

f.close()
t.close()
