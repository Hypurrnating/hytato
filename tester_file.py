from hytato import *; import asyncio

STATO = POTATO.STATO('.\\test.stato')
HTATO = POTATO.HTATO('.\\test.htato')

def test_stato_plant():
    STATO.PLANT(['wee', 'weee', 'weeee'])
def test_stato_inject():
    STATO.INJECT(data={'dsadsad': 43})
def test_stato_inject_no_potato():
    POTATO.STATO('.\\test2.stato').INJECT(data={'dsadsad': 43})
def test_stato_stain():
    STATO.STAIN()

def test_htato_plant():
    HTATO.PLANT(['wee', 'weee', 'weeee'])
def test_htato_inject():
    HTATO.INJECT(data={'wee': 43})
def test_htato_stain():
    HTATO.STAIN()

def test_stato_inject_simultaneously():
    pass
def test_htato_inject_simultaneously():
    pass


print('ALL GOOD, or so it seems')