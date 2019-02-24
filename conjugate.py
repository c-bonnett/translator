import nltk
from nltk import *



verbos_irregs = ['errar', 'entender', 'pedir', 'construir', 'saber', 'decir', 'erguir', 'dormir', 'oír', 'tener', 'leer', 'caber', 'adquirir',
                 'venir', 'poner', 'jugar', 'agradecer', 'poder', 'hacer', 'sonreír', 'caer', 'roer', 'estar', 'oler', 'traer', 'querer', 'sentir',
                 'asir', 'tañer', 'dar', 'valer', 'ver', 'haber', 'acertar', 'ceñir', 'mover', 'ir', 'mullir', 'ser', 'contar', 'andar', 'conducir',
                 'pudrir', 'yacer', 'podrir', 'salir', 'discernir', 'lucir','conocer','saber']

formas_verbales = ['PSI', 'PII', 'PTI', 'FS', 'CS', 'PSS', 'PTS', 'GR', 'PAR', 'IMA', 'IMN']

formas_clave = ['PSI -> presente indicativo', 'PII -> pretérito imperfecto indicativo/copretérito','PTI -> pretérito perfecto simple/pretérito indicativo'
                  'FS -> futuro simple','CS -> condicional simple','PSS -> presente subjuntivo', 'PTS -> pretérito subjuntivo/pretérito imperfecto subjuntivo',
                  'GR -> gerundio', 'PAR -> participio','IMA -> imperativo afirmativo', 'IMN -> imperitivo negativo']

psi1_ends = ['o','as','a','amos','áis','an']
psi2_ends = ['o','es','e','emos','éis','en']
psi3_ends = ['o','es','e','imos','ís','en']
pii1_ends = ['aba','abas','aba','ábamos','abais','aban']
pii2_ends = ['ía','ías','ía','íamos','íais','ían']
pti1_ends = ['é','aste','ó','amos','asteis','aron']
pti2_ends = ['í','iste','ió','imos','isteis','ieron']
fs_ends = ['é','ás','á','emos','éis','án']
cs_ends = pii2_ends
pss1_ends = ['e','es','e','emos','éis','en']
pss2_ends = ['a','as','a','amos','áis','an']
pts_ends = ['ra','ras','ra','ramos','rais','ran']
###ima1_ends = ['a','e','ad']
###ima2_ends = ['e','a','ed']
###ima3_ends = ['e','a','id']
###imn1_ends = ['es','e','éis']
###imn2_ends = ['as','a','áis']


###gr_ends
###par_ends


def verb_stem(verb,form):   
    if verb[-2:] in ('ar', 'er', 'ir'):
        #verb_type = verb[-2:]
        if form in ['cs','fs']:
            verb_stem = verb
            return verb_stem
        elif form == 'pts':
            if verb_type in ['ar']:
                first_stem = verb[:-2]+pti1_ends[5]
                verb_stem = first_stem[:-3]
                return verb_stem
            elif verb_type in ['er','ir']:
                first_stem = verb[:-2]+pti2_ends[5]
                verb_stem = first_stem[:-3]
                return verb_stem
        else:
            verb_stem = verb[:-2]
            return verb_stem
    else:
        print('Please input a regular Spanish verb in the infinitive.')

def verb_type(verb):
     if verb[-2:] in ('ar', 'er', 'ir'):
        v_end = verb[-2:]
        return v_end
     else:
         print('verb form error')
    

def verb_accidents(word):
    verb_form = None
    while verb_form == None:
        track = input('Enter D for direct conjugation; enter A to individually input verb accidents: ')
        if track.lower() == 'd':
            response = input('Enter the verb form you would like. For a list of symbols, enter X. For a symbol key, enter Y: ')
            if response.lower() == 'x':
                print(formas_verbales)
            elif response.lower() == 'y':
                print(formas_clave)
            elif response.upper() in formas_verbales:
                verb_form = response.upper()
                return verb_form
            else:
                print("Please enter a supported verb form.")                
    else:
        print(word)

def clave():
    print(formas_clave)
        
###verb and form as strings; person as int
def simple_conjugate(verb,form,person):    
    stem = verb_stem(verb,form)
    v_end = verb_type(verb)
    print(stem)
    print(v_end)
    if form == 'psi':
        if v_end == 'ar':
            return stem + psi1_ends[person-1]
        elif v_end == 'er':
            return stem + psi2_ends[person-1]
        elif v_end == 'ir':
            return stem + psi3_ends[person-1]
    elif form == 'pii':
        if v_end == 'ar':
            return stem + pii1_ends[person-1]
        elif v_end in ['er','ir']:
            return stem + pii2_ends[person-1]
    elif form == 'pti':
        if v_end == 'ar':
            return stem + pti1_ends[person-1]
        elif v_end in ['er','ir']:
            return stem + pti2_ends[person-1]
    elif form == 'fs':
        return stem + fs_ends[person-1]
    elif form == 'cs':
        return stem + cs_ends[person-1]
    elif form == 'pss':
        if v_end == 'ar':
            return stem + pss1_ends[person-1]
        elif v_end in ['er','ir']:
            return stem + pii2_ends[person-1]
    elif form == 'pts':
        return stem + pts_ends[person-1]
    else:
        print('null')
    
    
