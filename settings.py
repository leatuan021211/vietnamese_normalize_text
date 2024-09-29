import json


def sort_by_key(dictionary: dict):
    return dict(sorted(dictionary))


# Define work bank file paths
BASE_NUMBERS_FILEPATH = "bank/base_numbers.json"
NUMBER_LEVEL_FILEPATH = "bank/number_levels.json"
DATE_PREFIXS_FILEPATH = "bank/date_prefixs.json"
VOWELS_FILEPATH = "bank/vowels.json"
FINAL_CONSONANTS_FILEPATH = "bank/final_consonants.json"
HEAD_CONSONANTS_FILEPATH = "bank/head_consonants.json"
TONES_FILEPATH = "bank/tones.json"
UNITS_FILEPATH = "bank/units.json"
ACRONYMS_FILEPATH = "bank/acronyms.json"
LETTERS_FILEPATH = "bank/letters.json"
SYMBOLS_FILEPATH = "bank/symbols.json"
SAME_PHONEMES_FILEPATH = "bank/same_phonemes.json"

BREAKS = {
    ".": " chấm ",
    ",": " phẩy ",
}

ACCENTS = ['1', '2', '3', '4', '5'] # 1: sắc, 2: huyền, 3: hỏi, 4: ngã, 5: nặng

# Load word banks
with open(TONES_FILEPATH, "r") as file:
    TONES = json.load(file)

with open(BASE_NUMBERS_FILEPATH, "r") as file:
    BASE_NUMBERS = {int(key): value for key, value in json.load(file).items()}

with open(NUMBER_LEVEL_FILEPATH, "r") as file:
    NUMBER_LEVELS = {int(key): value for key, value in json.load(file).items()}

with open(DATE_PREFIXS_FILEPATH, "r", encoding="utf-8") as file:
    DATE_PREFIXS = sorted(json.load(file), key=len, reverse=True)

with open(UNITS_FILEPATH, "r", encoding="utf-8") as file:
    UNITS = sort_by_key(json.load(file).items())

with open(ACRONYMS_FILEPATH, "r", encoding="utf-8") as file:
    ACRONYMS = sort_by_key(json.load(file).items())

with open(LETTERS_FILEPATH, "r", encoding="utf-8") as file:
    LETTERS = sort_by_key(json.load(file).items())

with open(SYMBOLS_FILEPATH, "r", encoding="utf-8") as file:
    SYMBOLS = sort_by_key(json.load(file).items())

with open(SAME_PHONEMES_FILEPATH, "r", encoding="utf-8") as file:
    SAME_PHONEMES = sort_by_key(json.load(file).items())

with open(VOWELS_FILEPATH, "r", encoding="utf-8") as file:
    VOWELS = sorted(json.load(file), key=len, reverse=True)
    
with open(HEAD_CONSONANTS_FILEPATH, "r", encoding="utf-8") as file:
    HEAD_CONSONANTS = sorted(json.load(file), key=len, reverse=True)
    
with open(FINAL_CONSONANTS_FILEPATH, "r", encoding="utf-8") as file:
    FINAL_CONSONANTS = sorted(json.load(file), key=len, reverse=True)
    
PHONEMES = sorted(VOWELS + HEAD_CONSONANTS + FINAL_CONSONANTS + ACCENTS + list(BREAKS.keys()), key=len, reverse=True)
