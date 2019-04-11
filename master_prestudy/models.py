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
    name_in_url = 'master_prestudy'
    players_per_group = None
    num_rounds = 4 # How many lotteries?
    endowment = 100  # How many points are given during each lottery?
    win_prob = 1/6  # The probability of winning each lottery
    multiplier = 7 # How many times the invested amount can be won in the lottery?

class Subsession(BaseSubsession):
    def creating_session(self):
        # iterate over treatments
        background = itertools.cycle(['grey', 'white'])
        if self.round_number == 1:
            for p in self.get_players():
                p.background = next(background)
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    background = models.StringField()
    UserAgent = models.StringField()
    device = models.StringField()
    # browser = models.StringField()
    # user_agent = models.StringField
    #
    # def my_view(request):
    #     device = self.request.user_agent.device.family
    #     self.player.browser = self.request.user_agent.browser.family
    #     pass

    consent = models.IntegerField(
        label='Einwilligungserklärung:',
        initial=None,
        choices=[
            [1, 'Ja, ich habe die oben aufgeführten Bedingungen gelesen und verstanden. Ich hatte genügend Zeit, eine Entscheidung zu treffen. Hiermit bestätige ich mein Einverständnis zur Teilnahme an dieser Studie.'],
            [0, 'Nein, ich möchte nicht an dieser Studie teilnehmen.']
            ],
        widget=widgets.RadioSelect
        )

    success_number = models.IntegerField(initial=0)
    success_number2 = models.IntegerField(initial=0)
    fail_number = models.IntegerField(initial=0)

    investment = models.IntegerField(
        label='Investition:',
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


    # demographic questionnaire
    sex = models.IntegerField(
        label='Bitte wählen Sie Ihr Geschlecht aus:',
        choices=[
            [1, 'männlich'],
            [2, 'weiblich']],
        widget=widgets.RadioSelect,
        )
    age = models.IntegerField(
        label='Bitte geben Sie Ihr Alter an:',
        min=18,
        max=99)

    # participant id
    code = models.StringField(label='persönlicher Identitätscode:',
                              blank=False,
                              max_length=6,)

    # control variables
    control_1 = models.IntegerField(
        label="",
        choices=[
            [0, '0 Punkte'],
            [0, '200 Punkte'],
            [1, '300 Punkte'],
            [0, '400 Punkte']
        ],
        widget=widgets.RadioSelect
        )

    control_2 = models.IntegerField(
        label="",
        choices=[
            [0, '1400 Punkte'],
            [1, '1450 Punkte'],
            [0, '1650 Punkte'],
            [0, '1850 Punkte']
        ],
        widget=widgets.RadioSelect
        )

    control_3 = models.IntegerField(
        label="Sie haben 80 Punkte investiert. Ihre Gewinnzahl ist 5 und es wurde eine 2 gewürfelt. "
              "Wieviele Punkte erhalten Sie für diese Periode?",
        choices=[
            [0, '0 Punkte'],
            [1, '20 Punkte'],
            [0, '80 Punkte'],
            [0, '140 Punkte']
        ],
        widget=widgets.RadioSelect
        )

    control_4 = models.IntegerField(
        label="Sie haben 50 Punkte investiert. Ihre Gewinnzahl ist 2 und es wurde eine 2 gewürfelt. " \
              "Wieviele Punkte erhalten für diese Periode?",
        choices=[
            [0, '50 Punkte'],
            [0, '350 Punkte'],
            [1, '400 Punkte'],
            [0, '450 Punkte']
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

    # SOEP5-Fragen (generell und finanzdomäne)
    SOEP_gen = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden?',
        widget=widgets.RadioSelectHorizontal,
    )

    SOEP_fin = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='Wie würden Sie Ihre Risikobereitschaft bei Geldanlagen einschätzen?',
        widget=widgets.RadioSelectHorizontal,
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

    comment_instructions = models.StringField(
        label='Wie könnten die Instruktionen verbessert werden?',
        blank=True
    )

    check_goal = models.StringField(
        label='Was denken Sie, ist der Zweck dieser Studie?',
        blank=True
    )

    comment = models.LongStringField(
        label='Haben Sie einen Kommentar zu der Lotterie-Aufgabe bzw. der Studie?',
        blank=True
    )
    pass
