from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from decimal import Decimal
import random
import itertools





author = 'Adrian Leuenberger'

doc = """
Informed consent and instructions for main task (implementation of a lottery task after Imas, 2016 (based on Gneezy & Potters, 1997)).
"""


class Constants(BaseConstants):
    name_in_url = 'Consent_Instructions'
    players_per_group = None
    num_rounds = 1
    compensation = 0.50
    endowment = 100 # points per round; must match endowment in the main task!
    endowment_tot = 400
    multiplier = 7 # How many times the invested amount can be won in the lottery?

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    UserAgent = models.StringField()
    device = models.StringField()

    consent = models.IntegerField(
        label='Consent declaration:',
        initial=None,
        choices=[
            [1, 'I read and understood the stated terms. I had enough time to make a decision. Herewith, I consent to participate in this study.'],
            [0, 'I choose not to participate in this study.']
            ],
        widget=widgets.RadioSelect
        )

    # demographic questionnaire
    sex = models.IntegerField(
        label='What is your gender?',
        choices=[
            [1, 'male'],
            [2, 'female'],
            [3, 'other / prefer not to say']],
        widget=widgets.RadioSelect,
        )

    age = models.IntegerField(
        label='Please enter your age:',
        min=18,
        max=99)

    # control variables
    if Constants.endowment == 100:
        control_1 = models.IntegerField(
            label="1. How many points can you use for each round?",
            choices=[
                [0, '10 points'],
                [0, '25 points'],
                [1, '100 points'],
                [0, '400 points']
            ],
            widget=widgets.RadioSelect
        )
    else:
        control_1 = models.IntegerField(
            label="1. How many points can you use for each round?",
            choices=[
                [0, '10 points'],
                [1, '25 points'],
                [0, '100 points'],
                [0, '400 points']
            ],
            widget=widgets.RadioSelect
        )

    if Constants.endowment == 100:
        control_2 = models.IntegerField(
            label="2. How many points do you have in total (over all rounds)?",
            choices=[
                [0, '10 points'],
                [0, '25 points'],
                [0, '100 points'],
                [1, '400 points']
            ],
            widget=widgets.RadioSelect
        )
    else:
        control_2 = models.IntegerField(
            label="2. How many points do you have in total (over all rounds)?",
            choices=[
                [0, '10 points'],
                [0, '25 points'],
                [1, '100 points'],
                [0, '400 points']
            ],
            widget=widgets.RadioSelect
        )

    if Constants.endowment == 100:
        control_3 = models.IntegerField(
            label="3. If you have invested 20 points and lost, how much is your outcome in this round?",
            choices=[
                [0, '- 20 points'],
                [0, '0 points'],
                [0, '20 points'],
                [1, '80 points']
            ],
            widget=widgets.RadioSelect
        )
    else:
        control_3 = models.IntegerField(
            label="3. If you have invested 20 points and lost, how much is your outcome in this round?",
            choices=[
                [0, '- 20 points'],
                [0, '0 points'],
                [1, '5 points'],
                [0, '20 points']
            ],
            widget=widgets.RadioSelect
        )

    control_4 = models.IntegerField(
        label="4. If you win the lottery, how much will you earn?",
        choices=[
            [0, '4 times the amount invested'],
            [0, '4 times the amount invested plus the unused points'],
            [0, '7 times the amount invested'],
            [1, '7 times the amount invested plus the unused points']
        ],
        widget=widgets.RadioSelect
        )

    # Kontrollfrage
    Kontrollfrage = models.IntegerField(
        label="Welche Farbe hatte der Hintergrund in der vierten Investitionsrunde?",
        choices=[
            [1, 'weiss'],
            [2, 'grau'],
            [3, 'weiss nicht']
        ],
        widget=widgets.RadioSelect
    )

    # feedback questionnaire
    check_goal = models.StringField(
        label='Was denken Sie, ist der Zweck dieser Studie?',
        blank=True
    )

    comment = models.LongStringField(
        label='Do you have any further comments?',
        blank=True
    )
    pass
