from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
import itertools
import json



author = 'Adrian Leuenberger'

doc = """
SOEP 5 Risk Aversion
https://www.diw.de/documents/publikationen/73/diw_01.c.571151.de/diw_ssp0423.pdf (p. 59 - 61)
"""

class Constants(BaseConstants):
    name_in_url = 'SOEP5'
    players_per_group = None
    tasks = ['drive', 'finance', 'sport', 'career', 'health', 'trust']
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        from .pages import initial_page_sequence
        aaa = [i.__name__.split('_') for i in initial_page_sequence]
        page_blocks = [list(group) for key, group in itertools.groupby(aaa, key=lambda x: x[0])]
        for p in self.get_players():
            pb=page_blocks.copy()
            random.shuffle(pb)
            level1 = list(itertools.chain.from_iterable(pb))
            level2 = ['_'.join(i) for i in level1]
            p.page_sequence = json.dumps(level2)

class Group(BaseGroup):
    pass

def make_scale(label):
    return models.IntegerField(
        choices=[0,1,2,3,4,5,6,7,8,9,10],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )

class Player(BasePlayer):
    risk_soep_general = make_scale('')
    risk_soep_drive = make_scale('... while driving?')
    risk_soep_finance = make_scale('... in financial matters?')
    risk_soep_sport = make_scale('... during leisure and sport?')
    risk_soep_career = make_scale('... in your occupation?')
    risk_soep_health = make_scale('... with your health?')
    risk_soep_trust = make_scale('... your faith in other people?')
    page_sequence = models.StringField()
    pass


