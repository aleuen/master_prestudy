from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
from decimal import Decimal


    ################################################################
    ##########          Consent and Instructions          ##########
    ################################################################
class Info_Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    def before_next_page(self):
        self.player.UserAgent = self.request.META.get('HTTP_USER_AGENT')



class Start_Questionnaire(Page):
    form_model = 'player'
    form_fields = ['sex', 'age', 'code']

    def before_next_page(self):
        self.player.participant.vars['code'] = self.player.code

    pass

class Prolog(Page):
    form_model = 'player'
    pass

class Instruction(Page):
    form_model = 'player'
    pass

class Control_Items(Page):
    form_model = 'player'
    form_fields = ['control_1', 'control_2', 'control_3', 'control_4']
    pass

class Feedback(Page):
    form_model = 'player'
    pass


    ################################################################
    ##########                 Main Task                  ##########
    ################################################################
class Lottery_Decision_1(Page):
    form_model = 'player'
    form_fields = ['investment_1']

    def vars_for_template(self):
        self.player.success_number = random.randint(1,6)

    def before_next_page(self):
        self.player.random_draw = random.randint(1,6)

        self.player.lot_1_s = self.player.random_draw == self.player.success_number
        self.player.lot_1_p = (self.player.lot_1_s * Constants.multiplier * self.player.investment_1) + \
                              (self.player.endowment - self.player.investment_1)

        self.player.participant.vars['investment_1'] = self.player.investment_1
        self.player.participant.vars['lot_1_s'] = self.player.lot_1_s
        self.player.participant.vars['lot_1_p'] = self.player.lot_1_p

        self.player.lot_1_p /= self.session.config['real_world_currency_per_point']
        self.player.participant.vars['payoff_investment'] = self.player.payoff#.to_real_world_currency(self.session)
    pass

class Lottery_Decision_2(Page):
    form_model = 'player'
    form_fields = ['investment_2']

    def vars_for_template(self):
        self.player.success_number = random.randint(1,6)

    def before_next_page(self):
        self.player.random_draw = random.randint(1,6)

        self.player.lot_2_s = self.player.random_draw == self.player.success_number
        self.player.lot_2_p = (self.player.lot_2_s * Constants.multiplier * self.player.investment_2) + \
                              (self.player.endowment - self.player.investment_2)

        self.player.participant.vars['investment_2'] = self.player.investment_2
        self.player.participant.vars['lot_2_s'] = self.player.lot_2_s
        self.player.participant.vars['lot_2_p'] = self.player.lot_2_p

        self.player.lot_2_p /= self.session.config['real_world_currency_per_point']
        self.player.participant.vars['payoff_investment'] = self.player.payoff#.to_real_world_currency(self.session)
    pass

class Lottery_Decision_3(Page):
    form_model = 'player'
    form_fields = ['investment_3']

    def vars_for_template(self):
        self.player.success_number = random.randint(1,6)

    def before_next_page(self):
        self.player.random_draw = random.randint(1,6)

        self.player.lot_3_s = self.player.random_draw == self.player.success_number
        self.player.lot_3_p = (self.player.lot_3_s * Constants.multiplier * self.player.investment_3) + \
                              (self.player.endowment - self.player.investment_3)
        self.player.sum_lot_t3 = self.player.lot_1_p + self.player.lot_2_p + self.player.lot_3_p

        self.player.participant.vars['investment_3'] = self.player.investment_3
        self.player.participant.vars['lot_3_s'] = self.player.lot_3_s
        self.player.participant.vars['lot_3_p'] = self.player.lot_3_p

        self.player.lot_3_p /= self.session.config['real_world_currency_per_point']
        self.player.participant.vars['payoff_investment'] = self.player.payoff#.to_real_world_currency(self.session)
    pass

class Lottery_Decision_4(Page):
    form_model = 'player'
    form_fields = ['investment_4']

    def vars_for_template(self):
        self.player.success_number = random.randint(1,6)

    def before_next_page(self):
        self.player.random_draw = random.randint(1,6)

        self.player.lot_4_s = self.player.random_draw == self.player.success_number
        self.player.lot_4_p = (self.player.lot_4_s * Constants.multiplier * self.player.investment_4) + \
                              (self.player.endowment - self.player.investment_4)

        self.player.participant.vars['investment_4'] = self.player.investment_4
        self.player.participant.vars['lot_4_s'] = self.player.lot_4_s
        self.player.participant.vars['lot_4_p'] = self.player.lot_4_p

        self.player.lot_4_p /= self.session.config['real_world_currency_per_point']
        self.player.participant.vars['payoff_investment'] = self.player.payoff#.to_real_world_currency(self.session)
    pass

class Rolling_dice(Page):
    form_model = 'player'
    timeout_seconds = .5
    pass

class Results_Round_1(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {
            'earnings': self.player.lot_1_p#.to_real_world_currency(self.session)
        }
    pass

class Results_Round_2(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {
            'earnings': self.player.lot_2_p  # .to_real_world_currency(self.session)
        }

    pass

class Results_Round_3(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {
            'earnings': self.player.lot_3_p  # .to_real_world_currency(self.session)
        }
    pass

class Results_Round_4(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {
            'earnings': self.player.lot_3_p  # .to_real_world_currency(self.session)
        }

    def before_next_page(self):
        self.player.sum_lot_p = self.player.lot_1_p + self.player.lot_2_p + self.player.lot_3_p + self.player.lot_4_p
        self.player.sum_lot = self.player.sum_lot_p
        # self.player.sum_lot_chf = round(Decimal(self.player.sum_lot) * 2 / self.player.endowment / 4, 1) / 2
        self.player.sum_lot_chf = Decimal(self.player.sum_lot * 2)
        self.player.sum_lot_chf = self.player.sum_lot_chf / Decimal(self.player.endowment)
        self.player.sum_lot_chf = Decimal(self.player.sum_lot_chf)/ 4
        self.player.sum_lot_chf = round(Decimal(self.player.sum_lot_chf), 1)
        self.player.sum_lot_chf = Decimal(self.player.sum_lot_chf / 2)

        self.player.participant.vars['sum_lot_chf'] = self.player.sum_lot_chf
        self.player.participant.vars['sum_lot'] = self.player.sum_lot

    pass

class Results_3_Rounds_Paper(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {
            'earnings': self.player.payoff#.to_real_world_currency(self.session)
        }

    def is_displayed(self):
        return self.player.treatment == 'paper'
    pass

class Results_3_Rounds_Realization(Page):
    form_model = 'player'
    form_fields = ['realization']
    def vars_for_template(self):
        return {
            'earnings': self.player.payoff#.to_real_world_currency(self.session)
        }

    def is_displayed(self):
        return self.player.treatment == 'realization'

    def realization_error_message(self, value):
        print('value is', value)
        if value != 'Closed':
                if value != 'closed':
                    if value !='"Closed"':
                        if value != '"closed"':
                            if value != 'Close':
                                if value != 'close':
                                    if value != '"Close"':
                                        if value != '"close"':
                                            return 'Please type "closed" in the field below to realize your earnings'
    pass


class Results_Final(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {
            'earnings': self.player.payoff#.to_real_world_currency(self.session)
        }
    pass

    ################################################################
    ##########              Aspect Listing                ##########
    ################################################################

class Aspect_Listing_1(Page):
    form_model = 'player'
    form_fields = ['reason_1']
    pass

class Aspect_Listing_2(Page):
    form_model = 'player'
    form_fields = ['reason_2', 'last_reason']

    def is_displayed(self):
        return self.player.last_reason != True
    pass

class Aspect_Listing_3(Page):
    form_model = 'player'
    form_fields = ['reason_3', 'last_reason']

    def is_displayed(self):
        return self.player.last_reason != True
    pass

class Aspect_Listing_4(Page):
    form_model = 'player'
    form_fields = ['reason_4', 'last_reason']

    def is_displayed(self):
        return self.player.last_reason != True

    pass

class Aspect_Listing_5(Page):
    form_model = 'player'
    form_fields = ['reason_5', 'last_reason']

    def is_displayed(self):
        return self.player.last_reason != True

    pass

class Aspect_Rating_1(Page):
    form_model = 'player'
    form_fields = ['supp_r1', 'exp_pr_r1']
    pass

class Aspect_Rating_2(Page):
    form_model = 'player'
    form_fields = ['supp_r2', 'exp_pr_r2']

    def is_displayed(self):
        return self.player.reason_2 != None
    pass

class Aspect_Rating_3(Page):
    form_model = 'player'
    form_fields = ['supp_r3', 'exp_pr_r3']

    def is_displayed(self):
        return self.player.reason_3 != None
    pass

class Aspect_Rating_4(Page):
    form_model = 'player'
    form_fields = ['supp_r4', 'exp_pr_r4']

    def is_displayed(self):
        return self.player.reason_4 != None
    pass

class Aspect_Rating_5(Page):
    form_model = 'player'
    form_fields = ['supp_r5', 'exp_pr_r5']

    def is_displayed(self):
        return self.player.reason_5 != None
    pass

class Similarity(Page):
    form_model = 'player'
    form_fields = ['sim_perc']
    pass

class Manipulation_Check(Page):
    form_model = 'player'
    form_fields = ['manipulation_check']
    pass

class Info_btt(Page):
    form_model = 'player'
    pass

    ################################################################
    ##########                Page Sequence               ##########
    ################################################################

page_sequence = [Info_Consent,
                 Start_Questionnaire,
                 Prolog,
                 Instruction,
                 Control_Items,
                 Feedback,
                 Lottery_Decision_1,
                 Rolling_dice,
                 Results_Round_1,
                 Lottery_Decision_2,
                 Rolling_dice,
                 Results_Round_2,
                 Lottery_Decision_3,
                 Rolling_dice,
                 Results_Round_3,
                 Results_3_Rounds_Paper,
                 Results_3_Rounds_Realization,
                 Lottery_Decision_4,
                 Aspect_Listing_1,
                 Aspect_Listing_2,
                 Aspect_Listing_3,
                 Aspect_Listing_4,
                 Aspect_Listing_5,
                 Aspect_Rating_1,
                 Aspect_Rating_2,
                 Aspect_Rating_3,
                 Aspect_Rating_4,
                 Aspect_Rating_5,
                 Similarity,
                 Manipulation_Check,
                 Info_btt,
                 Rolling_dice,
                 Results_Round_4
                 #Results_Final
                 ]
