from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
import itertools
import json



author = 'Adrian Leuenberger'

doc = """
Exit Questionnaire
"""

class Constants(BaseConstants):
    name_in_url = 'Exit_Questionnaire'
    players_per_group = None
    num_rounds = 1
    pass


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Results / Payoffs
    investment_1 = models.CurrencyField(initial=None)
    investment_2 = models.CurrencyField(initial=None)
    investment_3 = models.CurrencyField(initial=None)
    investment_4 = models.CurrencyField(initial=None)

    lot_1_p = models.CurrencyField(initial=None)
    lot_2_p = models.CurrencyField(initial=None)
    lot_3_p = models.CurrencyField(initial=None)
    lot_4_p = models.CurrencyField(initial=None)

    lot_1_s = models.BooleanField(initial=None)
    lot_2_s = models.BooleanField(initial=None)
    lot_3_s = models.BooleanField(initial=None)
    lot_4_s = models.BooleanField(initial=None)

    sum_lot_p = models.CurrencyField(initial=None)
    sum_lot = models.CurrencyField(initial=None)
    sum_lot_chf = models.DecimalField(max_digits=5, decimal_places=2)

    # participant id
    code = models.StringField(label='personal identity code:',
                              blank=False,
                              max_length=6,)

    # demographic questionnaire
    education = models.IntegerField(
        label='What is the highest level of school you have completed or the highest degree you have received?',
        choices=[
            [1, 'less than high school degree'],
            [2, 'high school degree or equivalent (e.g., GED)'],
            [3, 'Some college but no degree'],
            [4, 'Associate degree'],
            [5, 'Bachelor degree'],
            [6, 'Graduate degree'],
            [0, 'Prefer not to say']
        ],
        )

    subject = models.IntegerField(
        label='What subject did you study?'
        )

    def subject_choices(self):
        import random
        choices_end = [
            [99, 'other'],
            [0, 'Prefer not to say']
        ]
        choices_shuffle = [
            [1, 'Business'],
            [2, 'Medicine'],
            [3, 'Law'],
            [4, 'Arts'],
            [5, 'Social Science'],
            [6, 'Science']
        ]
        random.shuffle(choices_shuffle)
        choices = choices_shuffle + choices_end
        return choices

    statistics = models.IntegerField(
        label='Did you ever take a statistic course?',
        choices=[
            [1, 'Yes'],
            [0, 'No']
        ],
        widget=widgets.RadioSelect,
    )

    stocks = models.IntegerField(
        label='Have you ever traded stocks?',
        choices=[
            [1, 'Yes'],
            [0, 'No']
        ],
        widget=widgets.RadioSelect,
    )

    gamble = models.IntegerField(
        label='Have you played any games of chance in the last 12 months (e.g. online, at the casino)?',
        choices=[
            [1, 'Yes'],
            [0, 'No']
        ],
        widget=widgets.RadioSelect
        #alternativ: How often do you gamble (e.g. online, at the casino)?'
    )

    # feedback questionnaire
    check_instructions = models.IntegerField(
        label='Wie verständlich waren für Sie die Instruktionen?',
        choices=[
            [4, 'sehr verständlich'],
            [3, 'eher verständlich'],
            [2, 'eher unverständlich'],
            [1, 'unverständlich']
        ],
        widget=widgets.RadioSelectHorizontal
    )

    # open comments:
    check_goal = models.StringField(
        label='What do you think is the purpose of this study?',
        blank=True
    )

    comment = models.LongStringField(
        label='Do you have any further comments?',
        blank=True
    )

    pass


