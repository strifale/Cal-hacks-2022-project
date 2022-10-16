import cohere
# co = cohere.Client("9RM5xpZbANQVLhq1nBzhgwtTmN9u5K1tGwIodxDK")
from source_files import utils
from cohere.classify import Example


def get_samples(file_name):
    """
    Returns the examples for the NLP model
    :param file_name: name of the example file
    :return: a list of Example class
    """
    samples = utils.read_files(file_name, True)
    examples = []
    for s in samples:
        cat_index = s.rfind(' ')
        category_type = s[cat_index + 1:]
        item = s[:cat_index - 1]
        examples.append(Example(item.rstrip(), category_type.rstrip()))
    return examples


def get_inputs(file_name):
    """
    Returns the inputs based on a .txt file
    :param file_name: Name of input file
    :return: Returns the list of inputs
    """
    file_read = utils.read_files(file_name, False)
    inputs = []
    for i in file_read:
        inputs.append(i.rstrip())
    return inputs

