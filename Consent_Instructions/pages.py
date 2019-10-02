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

    def before_next_page(self):
        self.player.UserAgent = self.request.META.get('HTTP_USER_AGENT')



class Start_Questionnaire(Page):
    form_model = 'player'
    form_fields = ['sex', 'age']

    def is_displayed(self):
        return self.round_number == 1
    # def before_next_page(self):
    #     self.player.in_all_rounds().code = self.player.code
    pass

class Instruction(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number ==1
    pass

class Control_Items(Page):
    form_model = 'player'
    form_fields = ['control_1', 'control_2', 'control_3', 'control_4']
    def is_displayed(self):
        return self.round_number == 1
    pass

class Feedback(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number == 1
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
                 Instruction,
                 Control_Items,
                 Feedback]
