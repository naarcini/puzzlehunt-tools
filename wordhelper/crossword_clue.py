import requests
import urllib.parse
from bs4 import BeautifulSoup

def crossword_clue(clue, pattern = ''):
    encoded_clue = urllib.parse.quote_plus(clue)
    encoded_pattern = urllib.parse.quote_plus(pattern)
    pattern_length = len(pattern)
    if pattern_length == 0:
        pattern_length = 'any'

    response = requests.get(f'http://www.dictionary.com/fun/crosswordsolver?query={encoded_clue}&pattern={encoded_pattern}&l={pattern_length}')
    soup = BeautifulSoup(response.text, 'html.parser')
    resultElements = soup.find_all('div', {'class': 'matching-answer'})

    results = []
    for resultElement in resultElements[1:]:
        results.append(resultElement.text.strip())

    return results

def crossword_clue_multi(clues, patterns = []):
    results = []
    if len(patterns) == 0:
        for i in range(len(clues)):
            results.append(crossword_clue(clues[i]))
    elif len(clues) == len(patterns):
        for i in range(len(clues)):
            results.append(crossword_clue(clues[i], patterns[i]))
    else:
        print('Mismatched number of clues and patterns')
    return results