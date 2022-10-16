import os


def read_files(file_name, is_sample: bool):
    """
    :param file_name: input file
    :param is_sample: true if the file is a sample file
    :return: a list of string from the file (Warning: This still includes newlines!)
    """
    curr_path = os.path.dirname(__file__)
    word = '/samples/'
    if not is_sample:
        word = '/inputs/'
    new_path = curr_path[:-12] + word + file_name

    with open(new_path, 'r') as f:
        return f.readlines()


def write_files(file_name, output):
    """
    Write output to output folder
    :param file_name: name of the file to write on
    :param output: what should fill the file
    :return: None
    """
    curr_path = os.path.dirname(__file__)
    word = '/outputs/'
    new_path = curr_path[:-12] + word + file_name
    file = open(new_path, "w")
    file.write(output)
    file.close()

from cohere.classify import Example


def get_samples(file_name):
    """
    Returns the examples for the NLP model
    :param file_name: name of the example file
    :return: a list of Example class
    """
    samples = read_files(file_name, True)
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
    file_read = read_files(file_name, False)
    inputs = []
    for i in file_read:
        inputs.append(i.rstrip())
    return inputs