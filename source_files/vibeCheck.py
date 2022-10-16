import cohere
from cohere.classify import Example

from source_files import utils

co = cohere.Client('{apiKey}')


def get_inputs(samples):
    """
    Takes in the data that we want to classify and return a list of tuples where the first is the input, and the second is the label
    :param samples: data that we want to classify
    :return: List of tuples
    """
    response = co.classify(
        model='medium',
        inputs=samples,
        examples=[Example("your voice is beautiful, those who don\'t like it are jealous!", "positive"),
                  Example("Your voice just so soothing", "positive"),
                  Example("자신만의 창법으로 부르는것같으면서도 약간 모창하는게 느껴져서 너무 듣기 좋아요", "positive"),
                  Example("수스님의 차분한 음색이 돋보이는 곡이네요. 오늘도 정말 잘 들었습니다.", "positive"),
                  Example("this is not math class", "negative"), Example("Why am I watching math", "negative"),
                  Example("Soo this is how Karen’s were made hawks= karen", "negative"),
                  Example("unexpected but one of the explanations of game theory basics i’ve seen", "positive"),
                  Example(
                      "I think the result may have differed if hawks were given, say, 25% survival chance after fighting. But still a superb manifestation of how some animals developed altruism.",
                      "neutral"), Example("Doves. Hawks. Eat.", "neutral"), Example(
                "My way of describing the prisoner\'s dilemma is: Everyone prefers a maximum possibility of doing less badly (red) to a minimum possibility of doing much better (blue).\n\nMi forma de describir el dilema del prisionero es: Todos prefieren una posibilidad máxima de que les vaya menos mal (rojo) a una posibilidad minina de que les vaya mucho mejor (azul).",
                "neutral"), Example("Conclusion:\nIf only hawk: Fail\nIf only dove: Success\nBoth: Success", "neutral"),
                  Example("Don’t look", "negative"), Example(
                "The ones simulating us are propably getting their mind blown because we startet simulating stuff ourselfes now.",
                "positive"), Example("Those blobs look tasty", "neutral"),
                  Example("bro my ad got interrupted by an ad", "negative"),
                  Example("Could you use this to simulate the damage of invasive species?  That would be really cool.",
                          "positive"),
                  Example("A 10 minute video taught me more than a 1 month biology unit", "positive"), Example(
                "How did you create behaviors for the blobs ?\nWere they using Neural Networks with genetic algorithms ? or was it reinforcement learning?\nHow did you program them when to seek food and when to go home?",
                "positive"), Example("Simple simulation but informative. We can relate it to our society", "neutral"),
                  Example(
                      "Making a world-ending machine that can send the server into oblivion in the nether is rather oddly fitting.",
                      "neutral"), Example(
                "I think when you can pay to be unbanned, it’s a pretty good indication of how much the host really cares…",
                "neutral"), Example("These guys are the villains the world didnt know it needed", "positive"), Example(
                "Relative of cherrished trans individuals, here. Thank you so much for this calm, factual presentation of reality.",
                "positive"), Example(
                "I really like native approach to the LBGTQ communities. I think everyone\'s heard the term two spirit it\'s generally means you have male and female Spirit within you.\n\nThe Navajo believe that there are five genders that male and female are generally the polarities. The two spirit person got to find their place within that polarity. It\'s an interesting idea. Unfortunately trans people are honored by the Navajo people.",
                "positive"), Example(
                "I agree with your assessment and couldn’t have said it better myself I am very anti capital punishment",
                "positive"), Example("\"An eye for an eye makes the whole world blind\"", "neutral"), Example(
                "\"Many that live deserve death. Some that die deserve life. Can you give it to them, Frodo?\"",
                "neutral"), Example("Preach it bro.", "positive"),
                  Example("this shouldn’t have pissed me off so much but it did", "negative"),
                  Example("Omg I\'m so glad this video is out!! Tysm for the opportunity Jubilee", "positive"), Example(
                "this video sums up the toxicity of labeling someone’s sexuality based on if they cuff their jeans or not, etc",
                "neutral"), Example(
                "When the momma cat came back and the mom was like so much more understanding of her, I think it\'s cause she knew she was losing her baby too. That\'s why they wanted to pamper her suddenly.",
                "neutral"), Example("This is better than other youtubers", "positive"), Example(
                "didn’t think i’d cry going into this at all, but the story at the end pulled at my heartstrings in a major way",
                "positive"), Example("I\'ve been crying for 30 minutes. This was so powerful", "positive"),
                  Example("This is pretty insightful and inspiring. Also great progress! Keep it up!", "positive"),
                  Example(
                      "As someone that just started, even his beginner projects seem incredible to me, how did he do that in just a few months",
                      "positive"), Example(
                "Finally a tutorial that\'s straight to the point and doesn\'t leave me picking my nose and doubting "
                "my intelligence",
                "positive"), Example(
                "Блин, почти не зная английский, мне этот урок более понятен, чем большинство уроков на "
                "русском...\nСпасибо! Это супер!!!",
                "positive"),
                  Example("It\'s so weird that he mostly films at night but it\'s cool we\'re all antisocial",
                          "neutral"), Example("I have not laughed this hard in a while", "positive"), Example(
                "Spoiler:\n\n\n\n\n\nHe did a legitimately stellar job at hiding he was both people in this one.",
                "neutral")])

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
    pos = []
    neg = []
    neutral = []
    for i in result:
        if i[1] == "positive":
            pos.append(i[0])
        elif i[1] == "negative":
            neg.append(i[0])
        else:
            neutral.append(i[0])
    utils.write_files("positive.txt", pos)
    utils.write_files("negatives.txt", neg)
    utils.write_files("neutral.txt", neutral)
