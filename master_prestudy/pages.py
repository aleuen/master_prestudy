from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
from decimal import Decimal

class Info_Consent(Page):
    form_model = 'player'
    form_fields = ['consent']
    def is_displayed(self):
        return self.round_number == 1
    pass

class Start_Questionnaire(Page):
    form_model = 'player'
    form_fields = ['sex', 'age', 'code']

    def is_displayed(self):
        return self.round_number == 1
    # def before_next_page(self):
    #     self.player.in_all_rounds().code = self.player.code
    pass

class Instruction_1(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number ==1
    def vars_for_template(self):
        self.player.success_number = random.randint(1,6)
    pass

class Instruction_2(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number ==1
    def vars_for_template(self):
        self.player.success_number = random.randint(1,6)
        self.player.success_number2 = random.randint(1, 6)
        self.player.fail_number = random.randint(1,6)
        if self.player.success_number2 == self.player.fail_number:
            self.player.fail_number = random.randint(1, 6)
pass

class Control_Item1(Page):
    form_model = 'player'
    form_fields = ['control_1']
    def is_displayed(self):
        return self.round_number == 1

    def control_1_error_message(self, value):
        print('value is', value)
        if value == 0:
            return 'Ihre Antwort ist nicht korrekt. Bitte versuchen Sie es erneut.'
    pass

class Control_Item2(Page):
    form_model = 'player'
    form_fields = ['control_2']
    def is_displayed(self):
        return self.round_number == 1

    def control_2_error_message(self, value):
        print('value is', value)
        if value == 0:
            return 'Ihre Antwort ist nicht korrekt. Bitte versuchen Sie es erneut.'
    pass

class Instruction_3(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number ==1
    def vars_for_template(self):
        self.player.success_number = random.randint(1,6)
    pass

class Lottery_Decision(Page):
    form_model = 'player'
    form_fields = ['investment']

    def is_displayed(self):
        if self.round_number != 4:
            return True
        elif self.player.in_round(1).background != 'grey':
            return True
        else:
            return False

    def vars_for_template(self):
        self.player.success_number = random.randint(1,6)

    def before_next_page(self):
        self.player.random_draw = random.randint(1,6)

        self.player.success = self.player.random_draw == self.player.success_number
        self.player.payoff = (self.player.success * Constants.multiplier * self.player.investment) + (Constants.endowment - self.player.investment)

        self.player.payoff /= self.session.config['real_world_currency_per_point']
        self.player.participant.vars['payoff_investment'] = self.player.payoff#.to_real_world_currency(self.session)

    pass

class Lottery_Decision_grey(Page):
    form_model = 'player'
    form_fields = ['investment']

    def is_displayed(self):
        if self.round_number != 4:
            return False
        elif self.player.in_round(1).background == 'grey':
            return True
        else:
            return False

    def vars_for_template(self):
        self.player.success_number = random.randint(1,6)

    def before_next_page(self):
        self.player.random_draw = random.randint(1,6)

        self.player.success = self.player.random_draw == self.player.success_number
        self.player.payoff = (self.player.success * Constants.multiplier * self.player.investment) + (Constants.endowment - self.player.investment)

        self.player.payoff /= self.session.config['real_world_currency_per_point']
        self.player.participant.vars['payoff_investment'] = self.player.payoff#.to_real_world_currency(self.session)

    pass

class Rolling_dice(Page):
    form_model = 'player'
    timeout_seconds = 1
    pass

class Results_Round(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {
            'earnings': self.player.payoff#.to_real_world_currency(self.session)
        }

    def before_next_page(self):
        if self.round_number == 4:
            self.player.lot_1_p = self.player.in_round(1).payoff
            self.player.lot_2_p = self.player.in_round(2).payoff
            self.player.lot_3_p = self.player.in_round(3).payoff
            self.player.lot_4_p = self.player.in_round(4).payoff
            self.player.lot_1_s = self.player.in_round(1).success
            self.player.lot_2_s = self.player.in_round(2).success
            self.player.lot_3_s = self.player.in_round(3).success
            self.player.lot_4_s = self.player.in_round(4).success
            self.player.investment_1 = self.player.in_round(1).investment
            self.player.investment_2 = self.player.in_round(2).investment
            self.player.investment_3 = self.player.in_round(3).investment
            self.player.investment_4 = self.player.in_round(4).investment
            self.player.part_id = self.player.in_round(1).code
            self.player.sum_lot_p = self.player.lot_1_p + self.player.lot_2_p + self.player.lot_3_p + self.player.lot_4_p
            self.player.sum_lot = self.player.sum_lot_p
            self.player.sum_lot_chf = round(Decimal(self.player.sum_lot) * 2 / 400, 1) / 2
    pass

class Results_3_Rounds(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == 3
    pass

    def vars_for_template(self):
        return {
            'earnings': self.player.payoff#.to_real_world_currency(self.session)
        }
    pass

class Results_Final(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    pass

    def vars_for_template(self):
        return {
            'earnings': self.player.payoff#.to_real_world_currency(self.session)
        }

    pass

class Intro_SOEP(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    pass

class SOEP_gen(Page):
    form_model = 'player'
    form_fields = ['SOEP_gen']
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    pass

class SOEP_fin(Page):
    form_model = 'player'
    form_fields = ['SOEP_fin']
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    pass

class Final_Questionnaire(Page):
    form_model = 'player'
    form_fields = ['check_instructions', 'comment_instructions', 'check_goal', 'comment']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    pass

class Administrative(Page):
    form_model = 'player'
    form_fields = ['code']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    pass


page_sequence = [Info_Consent,
                 Start_Questionnaire,
                 Instruction_1,
                 Instruction_2,
                 Control_Item1,
                 Control_Item2,
                 Instruction_3,
                 Lottery_Decision,
                 Lottery_Decision_grey,
                 Rolling_dice,
                 Results_Round,
                 Results_3_Rounds,
                 Results_Final,
                 Intro_SOEP,
                 SOEP_gen,
                 SOEP_fin,
                 Final_Questionnaire,
                 Administrative]
