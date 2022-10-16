from source_files import utils


def basic_read_file_test():
    test = utils.read_files("examplesText1.txt", True)
    expected = ['The order came 5 days early, positive\n',
                'The item exceeded my expectations, positive\n',
                'I ordered more for my friends, positive\n',
                'I would buy this again, positive\n',
                'I would recommend this to others, positive\n',
                'The package was damaged, negative\n',
                'The order is 5 days late, negative\n',
                'The order was incorrect, negative\n',
                'I want to return my item, negative\n',
                "The item\\'s material feels low quality, negative\n",
                'The product was okay, neutral\n',
                'I received five items in total, neutral\n',
                'I bought it from the website, neutral\n',
                'I used the product this morning, neutral\n',
                'The product arrived yesterday, neutral\n']

    assert (len(test) == len(expected))
    for i in range(len(test)):
        assert (test[i] == expected[i])


basic_read_file_test()
