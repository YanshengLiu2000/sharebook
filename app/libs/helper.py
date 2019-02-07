
def is_isbn_or_keyword(inputs):
    """
    This function is used by '/book/search/'
    it can check whether the inputs are keyword of a book or isbn
    :param inputs: user input words
    :return: checking result
    """
    isbn_or_keyword='keyword'
    if len(inputs)==13 and inputs.isdigit():
        isbn_or_keyword='isbn'
    short_inputs=inputs.strip('-')
    if '-' in inputs and short_inputs.isdigit() and len(short_inputs)==10:
        isbn_or_keyword='isbn'
    return isbn_or_keyword