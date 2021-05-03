from dictapi import Dict
from os import getcwd

import pandas as pd
import re
import csv

from progressbar import printProgressBar

translator = Dict()
translated = list()

word_count = 0
current_word = 0

def makeexcel(csvfile):
    read = pd.read_csv(csvfile)
    read.to_excel("translated.xlsx",index = None, header=True, encoding='utf8')

def translate(word):
    global current_word
    # Progress Bar
    current_word = current_word + 1
    printProgressBar(current_word, word_count, prefix="Progress:", suffix="Done", length=50)

    # Translate Word
    global translated
    result = translator.translate(word, from_language="de", to_language="en")
    try:
        returned = result.translation_tuples[:1][0]
        translated = translated + [(word, re.sub(r'\s<.+>', '',
                                                re.sub(r'\s{\w+}', '',returned[1].capitalize())))]
    except:
        translated = translated + [(word, "Not Found")]
    result.translation_tuples = []

def translate_bulk(data):
    global translated
    for item in data:
        translate(item)
    with open("translated.csv", "w", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['German', 'English'])
        for translated_word in translated:
            writer.writerow(translated_word)
    makeexcel("translated.csv")
        
words = list()
with open("words.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter='\n', quotechar="|")
    for word in reader:
        word_count = word_count + 1
        new_word = word[0]
        words.append(new_word)

translate_bulk(words)