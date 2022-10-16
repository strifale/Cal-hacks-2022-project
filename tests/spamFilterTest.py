from source_files import spamFilter
from source_files import utils


def read_sample_test():
    samples = [
        "My sister is majoring in chinese in collage, (we\'re american) so I wanted to look up some songs bc I "
        "love "
        "music. I love kpop, but haven\'t listened to Chinese music, so I thought why not lol. I really like it!",
        "chinese music is cool"]
    result = spamFilter.get_inputs(samples)
    return result


s = read_sample_test()

for i in s:
    print("----------")
    print("our text: ", i[0])
    print("our label: ", i[1])
