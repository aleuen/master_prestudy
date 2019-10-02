from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
from decimal import Decimal


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

class Rolling_dice(Page):
    form_model = 'player'
    timeout_seconds = .5
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
            self.player.sum_lot_p = self.player.lot_1_p + self.player.lot_2_p + self.player.lot_3_p + self.player.lot_4_p
            self.player.sum_lot = self.player.sum_lot_p
            self.player.sum_lot_chf = round(Decimal(self.player.sum_lot) * 2 / Constants.endowment / 4, 1) / 2
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


page_sequence = [Lottery_Decision,
                 Rolling_dice,
                 Results_Round,
                 Results_3_Rounds,
                 Results_Final]
