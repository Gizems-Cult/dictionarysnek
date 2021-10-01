import requests


def getdata(word: str):
    request = requests.get(
        f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

    return request.json()


def getword(json: list):
    word = json[0]["word"]
    return word


def getphonetic(json: list):
    phonetic = json[0]["phonetic"]
    return phonetic


def getorigin(json: list):
    origin = json[0]["origin"]
    return origin


def getpos(json: list):
    pos = json[0]["meanings"][0]["partOfSpeech"]
    return pos


def getsyn(json: list):
    syn = json[0]["meanings"][0]["definitions"][0]["synonyms"]
    return syn


def getant(json: list):
    ant = json[0]["meanings"][0]["definitions"][0]["antonyms"]
    return ant


def getdefi(json: list):
    defi = json[0]["meanings"][0]["definitions"][0]["definition"]
    return defi


def getex(json: list):
    ex = json[0]["meanings"][0]["definitions"][0]["example"]
