
from refo import Plus, Question
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Pos, QuestionTemplate, Token, Particle, \
                          Lemmas
from dsl import IsCountry, ReligionOf, LabelOf

class Country(Particle):
    regex = Plus(Pos("DT") | Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS")) | Pos("IN")


    def interpret(self, match):
        name = match.words.tokens.title()
        return IsCountry() + HasKeyword(name)


class ReligionOfQuestion(QuestionTemplate):

    """
    Ex: "list of Religions"
    """
    regex = (Lemma("list")) + (Lemma("religion") | Lemma("religions")) + \
            Pos("IN") + Country()

    def interpret(self, match):
        religion = ReligionOf(match.country)
        label = LabelOf(religion)
        return label, "enum"

