from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import json



class Exit_Questionnaire(Page):
    form_model = 'player'
    form_fields = ['education', 'subject', 'statistics', 'stocks', 'gamble']

    def before_next_page(self):
        self.player.investment_1 = self.player.participant.vars['investment_1']
        self.player.investment_2 = self.player.participant.vars['investment_2']
        self.player.investment_3 = self.player.participant.vars['investment_3']
        self.player.investment_4 = self.player.participant.vars['investment_4']

        self.player.lot_1_s = self.player.participant.vars['lot_1_s']
        self.player.lot_2_s = self.player.participant.vars['lot_2_s']
        self.player.lot_3_s = self.player.participant.vars['lot_3_s']
        self.player.lot_4_s = self.player.participant.vars['lot_4_s']

        self.player.lot_1_p = self.player.participant.vars['lot_1_p']
        self.player.lot_2_p = self.player.participant.vars['lot_2_p']
        self.player.lot_3_p = self.player.participant.vars['lot_3_p']
        self.player.lot_4_p = self.player.participant.vars['lot_4_p']

        self.player.sum_lot = self.player.participant.vars['sum_lot']

        self.player.sum_lot_chf = self.player.participant.vars['sum_lot_chf']

        self.player.code = self.player.participant.vars['code']


    pass

class Comments(Page):
    form_model = 'player'
    form_fields = ['check_goal', 'comment']
    pass


class Results_Final(Page):
    form_model = 'player'
    pass


class Administrative(Page):
    form_model = 'player'
    pass


page_sequence = [Exit_Questionnaire,
                 Results_Final,
                 Comments,
                 Administrative]