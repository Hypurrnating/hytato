import pathlib; import ast; import os; import sys; from zipfile import ZipFile, ZipInfo

'''
HTATO stands for HARD POTATO. These files must be created by the HTATO class, and has fixed keys.
Meaning you can not easily add a new key to it. This makes it more suitable for files storing the 
permanent data like status or settings.

STATO stands for SOFT POTATO. These can have a variable number of keys. Making it more suitable
for files that might be used to store temporary data.

Apart from the number of keys, HTATO and STATO have other characteristics that make it suitable for their use

.potato files are for use by potato lib only (!)
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
    def func(*args, **kwargs):
        if args[0].potato.exists() == True:
            raise POTATOExists('Found existing potato file at path')
        return fn(*args, **kwargs)
    return func

def CheckPotatoNonExistant(fn):
    """must have self parameter and the potato path inside self parameter: self.potato"""
    def func(*args, **kwargs):
        if args[0].potato.exists() == False:
            raise POTATONonExists('Did not find existing potato file at path')
        return fn(*args, **kwargs)
    return func

# Return classes:

class potato_returns():
    class stato():
        class StatoPlantReturn():
            def __init__(self, complete, path, keys, version_history, encryption):
                self.complete = complete
                self.path = path
                self.keys = keys
                self.version_history = version_history
                self.encryption = encryption

        class StatoInjectReturn():
            def __init__(self, complete, update, all):
                self.complete = complete
                self.update = update
                self.all = all

    class htato():
        class HtatoPlantReturn():
            def __init__(self, complete, path, keys):
                self.complete = complete
                self.path = path
                self.keys = keys

        class HtatoInjectReturn():
            def __init__(self, complete, update, all):
                self.complete = complete
                self.update = update
                self.all = all

# All Hail Potato:

class POTATO():
    class STATO():
        def __init__(self, potato: pathlib.Path) -> None:
            """STATO stands for SOFT POTATO. These can have a variable number of keys. Making it more suitable for files that might be used to store temporary data."""

            self.potato = pathlib.Path(potato)
            split = self.potato.name.split('.')
            if split[len(split)-1] != 'stato':
                raise NotSTATO('Not an STATO file')

        @CheckPotatoExistant
        def PLANT(self, KEYS: list, version_history: bool = True, encryption: bool = False) -> potato_returns.stato.StatoPlantReturn:
            """Creates a STATO file at the path and adds None to all keys. Users must update the keys using INJECT method.\n
            returns a StatoPlantReturn class with parameters: complete, path, keys, version_history, encryption"""

            if encryption == True:
                print('Encryption is not currently fully supported')
            configfile_string = str()
            configfile_string += f'version_history: {version_history}' + '\n'
            configfile_string += f'encryption: {encryption}' + '\n'
            potatofile_string = str()
            for x in KEYS:
                potatofile_string += f'{x}: None' + '\n'
            ZipFile(self.potato, 'w').close()
            ZipFile(self.potato, 'a').writestr(data=configfile_string, zinfo_or_arcname='config.potato')
            ZipFile(self.potato, 'a').writestr(data=potatofile_string, zinfo_or_arcname='data.potato')
            ZipFile(self.potato, 'a').mkdir(zinfo_or_directory_name='version_history')

            return potato_returns().stato().StatoPlantReturn(complete=True, path=self.potato, keys=KEYS, version_history=version_history, encryption=encryption)

        @CheckPotatoNonExistant
        def STAIN(self, starch: str = 'data', decryption_key: str = None) -> dict:
            """Reads STATO file. Starch specifies what part you want to read.\n
            Type 'data' (default) for the simple dictionary stored inside, or 'config' for the preferences set during planting. 'history' is not yet supported\n
            returns a dictionary with keys and values of python objects"""

            match starch:
                case 'data':
                    starch = 'data.potato'
                case 'config':
                    starch = 'config.potato'
                case 'history':
                    return 'Not supported'

            read = ZipFile(self.potato, 'r').read(name=starch).decode().split('\n')
            parsed = dict()
            for x in read:
                if bool(x): #since its not .readlines() we need to make sure the string actually has something
                    x = x.replace("\n", "").split(':')  # unlikely to have "\n" in the string now but eh
                    key = x[0].strip()
                    value = ast.literal_eval(x[1].strip())
                    parsed[key] = value
            return parsed

        def INJECT(self, data: dict, starch: str = 'data') -> potato_returns.stato.StatoInjectReturn:
            """Update the data in the potato file at the path. Starch specifies the part you want to edit.\n
            Type 'data' (default) for the simple dictionary stored inside, or 'config' for the preferences set during planting. 'history' is not yet supported
            returns a StatoInjectReturn class with parameters: complete, update, all"""

            match starch:
                case 'data':
                    starch = 'data.potato'
                case 'config':
                    starch = 'config.potato'
                case 'history':
                    return 'Not supported'

            stained = self.STAIN(starch=starch)
            for x in data.keys():
                stained[x] = data[x]
            potatofile_string = str()
            for x in stained.keys():
                key = x
                value = stained[key]
                if type(value) == str:
                    value = f'"{value}"'
                potatofile_string += f'{key}: {value}' + '\n'

            # NEEDS ATTENTION!
            ZipFile(self.potato, 'a').writestr(data=potatofile_string, zinfo_or_arcname=starch)

            return potato_returns.stato.StatoInjectReturn(complete=True, update=data, all=stained)

    class HTATO():
        def __init__(self, potato: pathlib.Path) -> None:
            """HTATO stands for HARD POTATO. These files must be created by the HTATO class, and has fixed keys. Meaning you can not easily add a new key to it. This makes it more suitable for files storing the permanent data like status or settings."""

            self.potato = pathlib.Path(potato)
            split = self.potato.name.split('.')
            if split[len(split)-1] != 'htato':
                raise NotHTATO('Not an HTATO file')

        @CheckPotatoExistant
        def PLANT(self, KEYS: list) -> potato_returns.htato.HtatoPlantReturn:
            """Creates a HTATO file at the path and adds None to all keys. Users must update the keys using INJECT method.\n
            returns a HtatoPlantReturn class with parameters: complete, path, keys"""

            potatofile_string = str()
            for x in KEYS:
                potatofile_string += f'{x}: None' + '\n'        
            potatofile = open(self.potato, 'w')
            potatofile.write(potatofile_string)
            potatofile.close()

            return potato_returns().htato().HtatoPlantReturn(complete=True, path=self.potato, keys=KEYS)

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
        def INJECT(self, data: dict) -> potato_returns.htato.HtatoInjectReturn:
            """Update the data in the potato file at the path.\n
            returns a HtatoInjectReturn class with parameters: complete, update, all"""

            stained = self.STAIN()
            for x in data.keys():
                if bool(list(stained.keys()).count(x)) == False:
                    raise HTATOKey(f'The key: "{x}" is not in the original hard potato file.')
                stained[x] = data[x]
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

            return potato_returns().htato().HtatoInjectReturn(complete=True, update=data, all=stained)

POTATO = POTATO()
print(POTATO.STATO('.\\gugu.stato').INJECT(data={'oaoa': True}))
#print(POTATO.STATO('.\\gugu.stato').PLANT(['wee', 'weee', 'weeee']))