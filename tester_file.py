from potato import POTATO

STATO = POTATO.STATO('.\\test.stato')
HTATO = POTATO.HTATO('.\\test.htato')

print(STATO.PLANT(['wee', 'weee', 'weeee']))
print(STATO.INJECT(data={'dsadsad': 43}))
print(STATO.STAIN())

print(HTATO.PLANT(['wee', 'weee', 'weeee']))
print(HTATO.INJECT(data={'wee': 43}))
print(HTATO.STAIN())