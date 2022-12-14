import cohere
from cohere.classify import Example

from source_files import utils

co = cohere.Client("9RM5xpZbANQVLhq1nBzhgwtTmN9u5K1tGwIodxDK")


def get_inputs(samples):
    """
        Takes in the data that we want to classify and return a list of tuples where the first is the input, and the second is the label
        :param samples: data that we want to classify
        :return: List of tuples
        """
    response = co.classify(
        model='large',
        inputs=samples,
        examples=[Example("Jesus is alive.", "Spam"),
                  Example("Hell!", "Spam"),
                  Example("Yahoo is the best.", "Not spam"),
                  Example("Yes Ok", "Spam"),
                  Example("Most south Americans have MSN.", "Not spam"),
                  Example("Google is cool indeed, but it\'s just starting sucking ball with all competitive softwares "
                          "etc... There\'s a limit to everything", "Not spam"),
                  Example("u ppl hardly even get to the point of this vid sheesh lol", "Not spam"),
                  Example("the internet is gettin more and more scary.", "Spam"),
                  Example("No but I am", "Spam"),
                  Example(
                      "SURE! I\'m new to all this so bear with the new commer please.  My name is Brittanie.  I am "
                      "from "
                      "N.Y.C. in Utah now, going to school to become a paralegal.  Tell me about you.", "Spam"),
                  Example("Doug saga", "Spam"),
                  Example("2020....", "Spam"),
                  Example("I !!!!", "Spam"),
                  Example("God, GOOGLE OWNS THE NET!!!", "Not spam"),
                  Example("Wrong.\nNot *everyone* uses MSN.", "Not spam"),
                  Example("Google has 1001 videos ;)", "Not spam"),
                  Example("The start of the internet?", "Not spam"),
                  Example("for a 2007 video the audio quality is better", "Not spam"),
                  Example("whats the difference between yahoo widgets and AIM? O_o", "Not spam"),
                  Example("google should buy a continent, i need a vacation to google land", "Not spam"),
                  Example("Hallloooo coronavirus", "Spam"), Example("?????????google?????????????????????", "Not spam"),
                  Example("???????????????????????????????????????????????????", "Not spam"),
                  Example("??????????????????????????????????????????????????????????????????????????????????????????", "Not spam"),
                  Example("?????????????????????????????????????????????", "Not spam"), Example("???????????????", "Spam"),
                  Example("Shitty shanqi shitty Marvel shudianwangzu", "Spam"),
                  Example("????????????????????????????????????????????????", "Not spam"),
                  Example("??????????????????", "Not spam"), Example("???????????????", "Spam"),
                  Example("Blue: You want one?\nRed: spits on both of them.", "Not spam"),
                  Example("I\'m not really sure what I just watched but it was really interesting, more than my normal "
                          "classes. It has a pleasing visual graphics and animation, also the narrator has a calming "
                          "voice "
                          "and explains very well-", "Not spam"),
                  Example("Game theory", "Spam")])

    result = []
    for i in response.iterator:
        result.append((i.input, i.prediction))
    return result


def writefilesfrominput(inputs):
    """
        Directly write to files based on inputs
        :param inputs: The data that we want to classify
        :return: None
        """
    result = get_inputs(inputs)
    spam = []
    for i in result:
        if i[1] == "spam":
            spam.append(i[0])
    utils.write_files("spam.txt", spam)
