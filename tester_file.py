from hytato import *

STATO = POTATO.STATO('.\\test.stato')
HTATO = POTATO.HTATO('.\\test.htato')

def test_stato_plant():
    print(STATO.PLANT(['wee', 'weee', 'weeee']))
def test_stato_inject():
    print(STATO.INJECT(data={'dsadsad': 43}))
def test_stato_inject_no_potato():
    print(POTATO.STATO('.\\test2.stato').INJECT(data={'dsadsad': 43}))
def test_stato_stain():
    print(STATO.STAIN())

def test_htato_plant():
    print(HTATO.PLANT(['wee', 'weee', 'weeee']))
def test_htato_inject():
    print(HTATO.INJECT(data={'wee': 43}))
def test_htato_stain():
    print(HTATO.STAIN())

print('ALL GOOD, or so it seems')