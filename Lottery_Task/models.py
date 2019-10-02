from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from decimal import Decimal
import random
import itertools





author = 'Adrian Leuenberger'

doc = """
An implementation of a lottery task after Imas, 2016 (based on Gneezy & Potters, 1997).
Study 2, Robustness Check:
https://static1.squarespace.com/static/57967bc7cd0f68048126361d/t/57ba6b82893fc01e071b5d7c/1471835012022/Realization+Effect.pdf

"""


class Constants(BaseConstants):
    name_in_url = 'Lottery_Task'
    players_per_group = None
    num_rounds = 4 # How many lotteries?
    endowment = 100  # How many points are given during each lottery?
    endowment_2 = 25
    win_prob = 1/6  # The probability of winning each lottery
    multiplier = 7 # How many times the invested amount can be won in the lottery?

class Subsession(BaseSubsession):
    def creating_session(self):
        # iterate over treatments
        group = itertools.cycle([1, 2, 3, 4])
        if self.round_number == 1:
            for p in self.get_players():
                p.group = next(group)
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    group = models.IntegerField()
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

    success_number = models.IntegerField(initial=random.randint(1,6))
    success_number2 = models.IntegerField(initial=0)
    fail_number = models.IntegerField(initial=0)

    investment = models.IntegerField(
        label='',
        initial=None,
        min=0,
        max=Constants.endowment)

    lottery = models.BooleanField()
        # initial=None,
        # label='Möchten Sie CHF 0.25 in die Lotterie investieren?',
        # choices=[
        #     [25, 'Ja, ich will in die Lotterie investieren.'],
        #     [0, 'Nein, ich steige aus den Lotterien aus.']
        # ]

    success = models.BooleanField()
    random_draw = models.IntegerField()
    exit = models.IntegerField(initial=0)

    # results / payoffs
    investment_1 = models.IntegerField(initial=None)
    investment_2 = models.IntegerField(initial=None)
    investment_3 = models.IntegerField(initial=None)
    investment_4 = models.IntegerField(initial=None)

    lot_1_p = models.CurrencyField(initial=None)
    lot_2_p = models.CurrencyField(initial=None)
    lot_3_p = models.CurrencyField(initial=None)
    lot_4_p = models.CurrencyField(initial=None)

    lot_1_s = models.BooleanField(initial=None)
    lot_2_s = models.BooleanField(initial=None)
    lot_3_s = models.BooleanField(initial=None)
    lot_4_s = models.BooleanField(initial=None)

    sum_lot_p = models.CurrencyField(initial=None)
    sum_lot = models.DecimalField(max_digits=5, decimal_places=0)
    sum_lot_chf = models.DecimalField(max_digits=5, decimal_places=2)
    part_id = models.StringField(initial=None)

    #Aspect Listing
    reason_1 = models.LongStringField(initial=None,
                                      label='Reason # 1')
    reason_2 = models.LongStringField(initial=None,
                                      label='Reason # 2')
    reason_3 = models.LongStringField(initial=None,
                                      label='Reason # 3')
    reason_4 = models.LongStringField(initial=None,
                                      label='Reason # 4')
    reason_5 = models.LongStringField(initial=None,
                                      label='Reason # 5')

