velib = [{'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE)\
 - 93170 BAGNOLET', 'zip': '93170', 'number': 31705, 'lati\
 tude': 48.8645278209514, 'city': 'BAGNOLET', 'name': 'CHAMPEAUX\
 (BAGNOLET)', 'longitude': 2.416170724425901}, {'address': "52\
 RUE D'ENGHIEN / ANGLE RUE DU FAUBOURG POISSONIERE -\
 75010 PARIS", 'zip': '75010', 'number': 10042, 'latit\
ude': 48.87242006305313, 'city': 'PARIS', 'name': 'ENGHIEN\
', 'longitude': 2.348395236282807}, {'address': '74\
 BOULEVARD DES BATIGNOLLES - 75008 PARIS', 'zip': '75008', 'n\
 umber': 8020, 'latitude': 48.882148945631904, 'city': '\
PARIS', 'name': 'METRO ROME', 'longitude': 2.319860054774211}, {'ad\
dress': '37 RUE CASANOVA - 75001 PARIS', 'zip': '75001', 'num\
ber': 1022, 'latitude': 48.8682170167744, 'city': 'PARIS', 'na\
me': 'RUE DE LA PAIX', 'longitude': 2.330493511399174}, {'a\
ddress': '139 AVENUE JEAN LOLIVE / MAIL CHARLES DE GAULLE \
- 93500 PANTIN', 'zip': '93500', 'number': 35014, 'latit\
ude': 48.893268664697416, 'city': 'PANTIN', 'name': 'DE GA\
ULLE (PANTIN)', 'longitude': 2.412715733388685}]

for s in velib:
    print(s['name'], s['zip'], s['city'])
