# coding: utf-8

# Copyright (c) 2012, Machinalis S.R.L.
# This file is part of quepy and is distributed under the Modified BSD License.
# You should have received a copy of license in the LICENSE file.
#
# Authors: Rafael Carrascosa <rcarrascosa@machinalis.com>
#          Gonzalo Garcia Berrotaran <ggarcia@machinalis.com>

"""
People related regex
"""

from refo import Plus, Question
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Lemmas, Pos, QuestionTemplate, Particle
from dsl import IsPerson, LabelOf, DefinitionOf, BirthDateOf, BirthPlaceOf, HeightOf


class Thing(Particle):
    regex = Question(Pos("JJ")) + (Pos("NN") | Pos("NNP") | Pos("NNS")) |\
            Pos("VBN")

    def interpret(self, match):
        return HasKeyword(match.words.tokens)


class HowHighIsQuestion(QuestionTemplate):
    """
    Ex: "What is height of Burj Khalifa?"
    """
    regex = Lemma("what") +Lemma("be") + Question(POS("DT")) +Lemma("height") + POS("IN") + Thing() + Question(Pos("."))

    def interpret(self, match):
        label = HeightOf(match.thing)
        return label, "enum"
