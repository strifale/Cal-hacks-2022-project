from source_files import analysis
from source_files import utils


def read_sample_test():
    expected = ['The order came 5 days early', 'positive',
              'The item exceeded my expectations', 'positive',
              'I ordered more for my friends', 'positive',
              'I would buy this again', 'positive',
              'I would recommend this to others', 'positive',
              'The package was damaged', 'negative',
              'The order is 5 days late', 'negative',
              'The order was incorrect', 'negative',
              'I want to return my item', 'negative',
              "The item\\'s material feels low quality", 'negative',
              'The product was okay', 'neutral',
              'I received five items in total', 'neutral',
              'I bought it from the website', 'neutral',
              'I used the product this morning', 'neutral',
              'The product arrived yesterday', 'neutral']
    test = analysis.get_samples("examplesText1.txt")
    assert(len(expected) == 2 * len(test))
    test_index = 0
    expected_index = 0
    while test_index < len(test):
        assert(test[test_index].text == expected[expected_index])
        assert(test[test_index].label == expected[expected_index + 1])
        test_index += 1
        expected_index += 2

    
read_sample_test()
