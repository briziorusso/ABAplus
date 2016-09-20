from aba_plus_ import *
import re

ASSUMP_PREDICATE = "myAsm"
CONTR_PREDICATE = "contrary"
RULE_PREDICATE = "myRule"
# myPrefLT(a, b) represents a < b
LT_PREDICATE = "myPrefLT"
# myPrefLE(a, b) represents a <= b
LE_PREDICATE = "myPrefLE"

ASSUMP_REGEX = r"myAsm\((.+)\)"
CONTR_REGEX = r"contrary\((.+),(.+)\)"
RULE_REGEX = r"myRule\((.+),\[(.*)\]\)"
LT_REGEX = r"myPrefLT\((.+),(.+)\)"
LE_REGEX = r"myPrefLE\((.+),(.+)\)"

DUPLICATE_USE_FOUND = "_duplicate"

def generate_aba_plus_framework_from_file(filename):
    file = open(filename, 'r')
    input = file.read()
    file.close()
    return generate_aba_plus_framework(input)

def generate_aba_plus_framework(input_string):
    input = input_string.replace('\r', '')
    input = input.replace('\n', '')
    declarations = input.split(".")


    assump_declarations = [decl for decl in declarations if ASSUMP_PREDICATE in decl]
    assumptions = generate_assumptions(assump_declarations)

    contr_declarations = [decl for decl in declarations if CONTR_PREDICATE in decl]
    res = generate_contraries_map(contr_declarations, assumptions)
    contr_map = res[0]
    aux_rules = res[1]

    rule_declarations = [decl for decl in declarations if RULE_PREDICATE in decl]
    rules = generate_rules(rule_declarations, contr_map, aux_rules)

    pref_declarations = [decl for decl in declarations if (LT_PREDICATE in decl) or (LE_PREDICATE in decl)]
    preferences = generate_preferences(pref_declarations)

    return (ABA_Plus(assumptions, preferences, rules), contr_map)

def generate_assumptions(assump_decls):
    assumptions = set()

    for decl in assump_decls:
        # remove spaces
        cleaned_decl = decl.replace(" ", "")
        match = re.match(ASSUMP_REGEX, cleaned_decl)
        if match:
            symbol = match.group(1)
            assumptions.add(Sentence(symbol, False))

    return assumptions

def generate_contraries_map(contr_decls, assumptions):
    # maps symbols to contraries
    map = {}
    symbols_seen = set()
    assumption_symbols = [asm.symbol for asm in assumptions]

    for decl in contr_decls:
        cleaned_decl = decl.replace(" ", "")
        match = re.match(CONTR_REGEX, cleaned_decl)
        if match:
            sentence = match.group(1)
            contrary = match.group(2)

            if sentence not in assumption_symbols:
                raise InvalidContraryDeclarationException("Contraries cannot be declared for non-assumptions!")
            if contrary in assumption_symbols:
                raise InvalidContraryDeclarationException("The symbol of an assumption cannot be used as a contrary!")

            if sentence in symbols_seen:
                raise DuplicateSymbolException("The contrary of an assumption can only be mapped to a single symbol!")
            if contrary in symbols_seen:
                raise DuplicateSymbolException("A symbol can only be mapped to the contrary of one assumption!")

            map[contrary] = sentence
            symbols_seen.add(sentence)
            symbols_seen.add(contrary)

    return (map, set())

class InvalidContraryDeclarationException(Exception):
    def __init__(self, message):
        self.message = message

class DuplicateSymbolException(Exception):
    def __init__(self, message):
        self.message = message

def generate_rules(rule_decls, map, aux_rules):
    rules = aux_rules

    for decl in rule_decls:
        cleaned_decl = decl.replace(" ", "")
        match = re.match(RULE_REGEX, cleaned_decl)
        if match:
            consequent_symbol = match.group(1)
            consequent = translate_symbol(consequent_symbol, map)

            antecedent = set()
            if match.group(2) != "":
                antecedent_symbols = match.group(2).split(",")

                for ant in antecedent_symbols:
                    antecedent.add(translate_symbol(ant, map))

            rules.add(Rule(antecedent, consequent))

    return rules

# TODO: check if sentences are assumptions
def generate_preferences(pref_decls):
    preferences = set()

    for decl in pref_decls:
        cleaned_decl = decl.replace(" ", "")

        relation = NO_RELATION
        match = re.match(LT_REGEX, cleaned_decl)
        if match:
            relation = LESS_THAN
        else:
            match = re.match(LE_REGEX, cleaned_decl)
            if match:
                relation = LESS_EQUAL
        if relation != NO_RELATION:
            sentence_symbol1 = match.group(1)
            sentence1 = Sentence(sentence_symbol1, False)
            sentence_symbol2 = match.group(2)
            sentence2 = Sentence(sentence_symbol2, False)
            preferences.add(Preference(sentence1, sentence2, relation))

    return preferences

def translate_symbol(symbol, map):
    if (symbol in map) and (map[symbol] != DUPLICATE_USE_FOUND):
        return Sentence(map[symbol], True)
    else:
        return Sentence(symbol, False)