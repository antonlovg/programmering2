import json

# Läser language_code.json så som vi lärt oss i programmering 1
def sprakkod(filnamn):
    try:
        with open(filnamn, 'r') as fil:
            data_dictionary = json.load(fil)
        return data_dictionary
    except FileNotFoundError:
        return {}

