<h1>dictionarysnek</h1>

## Table of contents
* [General info](#general-info)
* [Dependencies](#dependencies)
* [Setup](#setup)
* [Usage](#usage)

## General info
A Dictionary API Wrapper for Python.
	
## Dependencies
Project is created with:
* Requests Version: 2.26.0
* Dictionary API: dictionaryapi.dev
	
## Setup
Python-pip:
```
$ pip install dictionarysnek
```
Poetry:
```
$poetry add dictionarysnek
```

## Usage
* Import the module: ```from dictionarysnek import dictionarysnek```
* Get the data: ```data = dictionarysnek.getdata("mundane")```
* Pass it to the desired function to get the output: ```synonyms = dictionarysnek.getsyn(data)```

## Functions
* Get Synonyms -> Returns an array of Synonyms -> ```dictionarysnek.getsyn(json: list)```
* Get Antonyms -> Returns an array of Antonyms -> ```dictionarysnek.getant(json: list)```
* Get Definition -> Returns the definition of the given word -> ```dictionarysnek.getdefi(json: list)```
* Get Word -> Returns the given word -> ```dictionarysnek.getword(json: list)```
* Get Phonetic -> Returns the phonetic of the given word -> ```dictionarysnek.getphonetic(json: list)```
* Get Part of Speech -> Returns the Part of Speech of the given word -> ```dictionarysnek.getpos(json: list)```
* Get Example -> Gives an usage of the given word -> ```dictionarysnek.getex(json: list)```
* Get Origin -> Gives information about the origin of the given word -> ```dictionarysnek.getorigin(json: list)```
