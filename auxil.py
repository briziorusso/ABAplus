

def sets_to_str(sets, contr_map={}):
    """
    :param sets: set of sets of Sentences to format
    :param contr_map: dictionary mapping symbols of contraries to symbols of assumptions (default empty)
    :return: formatted string representation of sets
    """
    str = ""

    it = iter(sets)
    first_set = next(it, None)
    if first_set is not None:
        str += set_to_str(first_set, contr_map)
    for set in it:
        str += ", "
        str += set_to_str(set, contr_map)

    return str


def set_to_str(set, contr_map={}):
    """
    :param set: set of Sentences to format
    :param contr_map: dictionary mapping symbols of contraries to symbols of assumptions (default empty)
    :return: formatted string representation of sets
    """
    str = "{"

    it = iter(set)
    first_sentence = next(it, None)
    if first_sentence is not None:
        str += sentence_to_str(first_sentence, contr_map)
    for sentence in it:
        str += ", "
        str += sentence_to_str(sentence, contr_map)

    str += "}"

    return str


def sentence_to_str(sentence, contr_map={}):
    """
    :param sentence: Sentence to format
    :param contr_map: dictionary mapping symbols of contraries to symbols of assumptions (default empty)
    :return: formatted string representation of sentence
    """
    if sentence.is_contrary:
        if sentence.symbol in contr_map:
            return contr_map[sentence.symbol]
        return '¬'.format(sentence.symbol)
    else:
        return sentence.symbol


def arguments_extensions_to_str_list(extensions_dict, contr_map={}):
    """
    :param extensions_dict: dictionary mapping sets to their conclusions
    :param contr_map: dictionary mapping symbols of contraries to symbols of assumptions (default empty)
    :return: list of formatted arguments(deductions)
    """
    res = []

    for extension, conclusions in extensions_dict.items():
        res.append(argument_to_str(extension, conclusions, contr_map))

    return res


def argument_to_str(premise, conclusion, contr_map={}):
    """
    :param premise: set of Sentences representing the premise
    :param conclusion: set of Sentences representing the conclusion
    :param contr_map: dictionary mapping symbols of contraries to symbols of assumptions (default empty)
    :return: formatted argument(deduction)
    """
    str = ""
    str += set_to_str(premise)
    str += " HAS CONCLUSIONS "
    str += set_to_str(conclusion, contr_map)

    return str

