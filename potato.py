import asyncio; import os; import sys; import json; import pathlib; import ast; import traceback

'''
HTATO stands for HARD POTATO. These files must be created by the HTATO class, and has fixed keys.
Meaning you can not easily add a new key to it. This makes it more suitable for files storing the 
permanent data like status or settings.

STATO stands for SOFT POTATO. These can have a variable number of keys. Making it more suitable
for files that might be used to store temporary data.

Apart from the number of keys, HTATO and STATO have other characteristics that make it suitable for their use
'''

# Exceptions:

class POTATOExists(Exception):
    """Exception for when the specified potato file (whether hard or soft) already exists in the directory"""
class POTATONonExists(Exception):
    """Exception for when the specified potato file (whether hard of soft) doesn't exist in the directory"""
class NotHTATO(Exception):
    """Exception for when the path passed in class is not an HTATO file"""
class NotSTATO(Exception):
    """Exception for when the path passed in class is not an STATO file"""
class HTATOKey(KeyError):
    """Exception for when the key in data is not part of the original HTATO file"""

# Decorators:

def CheckPotatoExistant(fn):
    """must have self parameter and the potato path inside self parameter: self.potato"""
    def func(*args):
        if args[0].potato.exists() == True:
            raise POTATOExists('Found existing potato file at path')
        return fn(*args)
    return func

def CheckPotatoNonExistant(fn):
    """must have self parameter and the potato path inside self parameter: self.potato"""
    def func(*args):
        if args[0].potato.exists() == False:
            raise POTATONonExists('Did not find existing potato file at path')
        return fn(*args)
    return func


class POTATO():
    class STATO():
        def __init__(self, potato: pathlib.Path) -> None:
            """STATO stands for SOFT POTATO. These can have a variable number of keys. Making it more suitable for files that might be used to store temporary data."""

            self.potato = pathlib.Path(potato)
            split = self.potato.name.split('.')
            if split[len(split)-1] != 'stato':
                raise NotSTATO('Not an STATO file')

        @CheckPotatoExistant
        def PLANT(self, KEYS: list) -> list:
            """Creates a STATO file at the path and adds None to all keys. Users must update the keys using INJECT method.\n
            returns a list: [bool, potato path, keys in potato file]"""

            potatofile_string = str()
            for x in KEYS:
                potatofile_string += f'{x}: None' + '\n'
            potatofile = open(self.potato, 'w')
            potatofile.write(potatofile_string)
            potatofile.close()

            return [True, self.potato, KEYS]


    class HTATO():
        def __init__(self, potato: pathlib.Path) -> None:
            """HTATO stands for HARD POTATO. These files must be created by the HTATO class, and has fixed keys. Meaning you can not easily add a new key to it. This makes it more suitable for files storing the permanent data like status or settings."""

            self.potato = pathlib.Path(potato)
            split = self.potato.name.split('.')
            if split[len(split)-1] != 'htato':
                raise NotHTATO('Not an HTATO file')

        @CheckPotatoExistant
        def PLANT(self, KEYS: list) -> list:
            """Creates a HTATO file at the path and adds None to all keys. Users must update the keys using INJECT method.\n
            returns a list: [bool, potato path, keys in the potato file]"""

            potatofile_string = str()
            for x in KEYS:
                potatofile_string += f'{x}: None' + '\n'        
            potatofile = open(self.potato, 'w')
            potatofile.write(potatofile_string)
            potatofile.close()

            return [True, self.potato, KEYS]

        @CheckPotatoNonExistant
        def STAIN(self) -> dict:
            """Reads the potato file at the path. \n
            returns a dictionary with keys and values of python objects"""

            read = open(self.potato, 'r').readlines()
            parsed = dict()
            for x in read:
                # python still sometimes read the \n ending.
                x = x.replace("\n", "").split(':')
                key = x[0].strip()
                value = ast.literal_eval(x[1].strip())
                parsed[key] = value
            return parsed

        @CheckPotatoNonExistant
        def INJECT(self, DATA: dict) -> list:
            """Update the data in the potato file at the path.\n
            returns a list: [bool, dictionary of updated data, dictionary of all data]"""

            stained = self.STAIN()
            for x in DATA.keys():
                if bool(list(stained.keys()).count(x)) == False:
                    raise HTATOKey(f'The key: "{x}" is not in the original hard potato file.')
                stained[x] = DATA[x]
            potatofile_string = str()
            for x in stained.keys():
                key = x
                value = stained[key]
                if type(value) == str:
                    value = f'"{value}"'
                potatofile_string += f'{key}: {value}' + '\n'
            potatofile = open(self.potato, 'w')
            potatofile.write(potatofile_string)
            potatofile.close()
            return [True, DATA, stained]
        

potato = POTATO()