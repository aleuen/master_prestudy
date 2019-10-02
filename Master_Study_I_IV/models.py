from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from decimal import Decimal
import random
import itertools
from otree.db.models import Model, ForeignKey


author = 'Adrian Leuenberger'

doc = """
An implementation of a lottery task after Imas, 2016 (based on Gneezy & Potters, 1997).
Study 2, Robustness Check:
https://static1.squarespace.com/static/57967bc7cd0f68048126361d/t/57ba6b82893fc01e071b5d7c/1471835012022/Realization+Effect.pdf

"""


class Constants(BaseConstants):
    name_in_url = 'Master_Study_I_IV'
    players_per_group = None
    num_rounds = 1
    win_prob = 1/6  # The probability of winning each lottery
    multiplier = 7 # How many times the invested amount can be won in the lottery?

class Subsession(BaseSubsession):
    ##########################################################
    ##########      Iteration over Treatments       ##########
    ##########################################################
    def creating_session(self):
        # iterate over treatments
        treatment_group = itertools.cycle([1, 2, 3, 4])
        endowment = itertools.cycle([25, 25, 100, 100])
        endowment_tot = itertools.cycle([100, 75, 400, 300])
        treatment = itertools.cycle(['paper', 'realization', 'paper', 'realization'])
        # group 1 = 25 points paper treatment
        # group 2 = 25 points realization treatment
        # group 3 = 100 points paper treatment
        # group 4 = 100 points realization treatment
        if self.round_number == 1:
            for p in self.get_players():
                p.treatment_group = next(treatment_group)
                p.endowment = next(endowment)
                p.treatment = next(treatment)
                p.endowment_tot = next(endowment_tot)
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    ################################################################
    ##########            Treatments and Groups           ##########
    ################################################################
    treatment_group = models.IntegerField()
    endowment = models.CurrencyField()
    endowment_tot = models.CurrencyField()
    treatment = models.StringField()

    ################################################################
    ##########          Consent and Instructions          ##########
    ################################################################
    consent = models.IntegerField(
        label='Consent declaration:',
        initial=None,
        choices=[
            [1, 'I read and understood the stated terms. I had enough time to make a decision. Herewith, I consent to participate in this study.'],
            [0, 'I choose not to participate in this study.']
            ],
        widget=widgets.RadioSelect
        )

    # demographic start questionnaire
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

    # participant id
    code = models.StringField(label='personal identity code:',
                              blank=False,
                              max_length=6,)

    # control variables
    control_1 = models.IntegerField(
        label="1. How many points can you use for each round?",
        widget=widgets.RadioSelect
    )

    def control_1_choices(self):
        if self.endowment == 100:
            choices = [
                [0, '10 points'],
                [0, '25 points'],
                [1, '100 points'],
                [0, '400 points']
            ]
        else:
            choices = [
                [0, '10 points'],
                [1, '25 points'],
                [0, '100 points'],
                [0, '400 points']
            ]
        #random.shuffle(choices)
        return choices


    control_2 = models.IntegerField(
        label="2. How many points do you receive at the beginning in total?",
        widget=widgets.RadioSelect
    )

    def control_2_choices(self):
        if self.endowment == 100:
            choices = [
                [0, '10 points'],
                [0, '25 points'],
                [0, '100 points'],
                [1, '400 points']
            ]
        else:
            choices = [
                [0, '10 points'],
                [0, '25 points'],
                [1, '100 points'],
                [0, '400 points']
            ]
        #random.shuffle(choices)
        return choices

    control_3 = models.IntegerField(
        label="3. Imagine you invested some of your points in the lottery and lost. How many points do you receive in this round?",
        widget=widgets.RadioSelect
    )

    def control_3_choices(self):
        if self.endowment == 100:
            choices = [
                [0, '0 points'],
                [1, '100 points minus the points invested'],
                [0, '100 points']
            ]
        else:
            choices = [
                [0, '0 points'],
                [1, '25 points minus the points invested'],
                [0, '25 points']
            ]
        #random.shuffle(choices)
        return choices

    control_4 = models.IntegerField(
            label="4. Imagine you invested some of your points in the lottery and won. How many points do you receive in this round?",
            choices=[
                [0, '4 times the amount invested'],
                [0, '4 times the amount invested plus the unused points'],
                [0, '7 times the amount invested'],
                [1, '7 times the amount invested plus the unused points']
            ],
            widget=widgets.RadioSelect
        )

    ################################################################
    ##########                 Main Task                  ##########
    ################################################################
    success_number = models.IntegerField(initial=random.randint(1,6))

    random_draw = models.IntegerField()

    # Investments
    investment_1 = models.CurrencyField(
        label='',
        initial=None,
        min=0)

    def investment_1_max(self):
        return self.endowment

    investment_2 = models.CurrencyField(
        label='',
        initial=None,
        min=0)

    def investment_2_max(self):
        return self.endowment

    investment_3 = models.CurrencyField(
        label='',
        initial=None,
        min=0)

    def investment_3_max(self):
        return self.endowment

    investment_4 = models.CurrencyField(
        label='',
        initial=None,
        min=0)

    def investment_4_max(self):
        return self.endowment

    # Results / Payoffs
    lot_1_p = models.CurrencyField(initial=None)
    lot_2_p = models.CurrencyField(initial=None)
    lot_3_p = models.CurrencyField(initial=None)
    lot_4_p = models.CurrencyField(initial=None)

    lot_1_s = models.BooleanField(initial=None)
    lot_2_s = models.BooleanField(initial=None)
    lot_3_s = models.BooleanField(initial=None)
    lot_4_s = models.BooleanField(initial=None)

    sum_lot_t3 = models.CurrencyField(initial=None)

    sum_lot_p = models.CurrencyField(initial=None)
    sum_lot = models.DecimalField(max_digits=5, decimal_places=0)
    sum_lot_chf = models.DecimalField(max_digits=5, decimal_places=2)
    part_id = models.StringField(initial=None)

    realization = models.StringField(initial=None,
                                     label='')

    ################################################################
    ##########              Aspect Listing                ##########
    ################################################################
    # reasons
    reason_1 = models.StringField(initial=None,
                                  label='')
    reason_2 = models.StringField(initial=None,
                                  label='',
                                  blank=True)
    reason_3 = models.StringField(initial=None,
                                  label='',
                                  blank=True)
    reason_4 = models.StringField(initial=None,
                                  label='',
                                  blank=True)
    reason_5 = models.StringField(initial=None,
                                  label='',
                                  blank=True)

    last_reason = models.BooleanField(initial=None)

    # rate reasons
    def make_scale_1():
        return models.IntegerField(
            min=-50,
            max=50,
            label='How strongly does your description above support that you would invest more vs. less into the lottery?',
            initial=None
        )

    supp_r1 = make_scale_1()
    supp_r2 = make_scale_1()
    supp_r3 = make_scale_1()
    supp_r4 = make_scale_1()
    supp_r5 = make_scale_1()

    def make_scale_pr():
        return models.IntegerField(
            choices=[
                [1, 'Yes, it includes experience from the previous rounds'],
                [2, 'No, it does not include experience from the previous rounds']
            ],
            label='',
            initial=None,
        )

    exp_pr_r1 = make_scale_pr()
    exp_pr_r2 = make_scale_pr()
    exp_pr_r3 = make_scale_pr()
    exp_pr_r4 = make_scale_pr()
    exp_pr_r5 = make_scale_pr()

    # further questions
    sim_perc = models.IntegerField(
        choices=[
                [1, '1'],
                [2, '2'],
                [3, '3'],
                [4, '4'],
                [5, '5'],
                [6, '6'],
                [7, '7'],
            ],
        label='',
        initial=None,
        widget=widgets.RadioSelectHorizontal
    )

    manipulation_check = models.IntegerField(
        label='Did the task changein the last round? If yes, how?',
        initial=None,
        choices=[
            [1, 'no change'],
            [2, 'restart numbering of the round'],
            [3, 'other background color'],
            [4, 'time delay between round 3 and round 4'],
            [5, 'other currency to invest with'],
            [6, 'other size of the font']
        ],
        widget=widgets.RadioSelect
    )

    def manipulation_check_choices(self):
        import random
        choice_1 = [
            [1, 'no change']
        ]
        choices_shuffle = [
            [2, 'restart numbering of the round'],
            [3, 'other background color'],
            [4, 'time delay between round 3 and round 4'],
            [5, 'other currency to invest with'],
            [6, 'other size of the font']
        ]
        random.shuffle(choices_shuffle)
        choices = choice_1 + choices_shuffle
        print(choices)
        return choices


    ################################################################
    ##########                   Varia                    ##########
    ################################################################
    UserAgent = models.StringField()
    device = models.StringField()

    pass

