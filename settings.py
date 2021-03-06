from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.50,
    'doc': "",
}

SESSION_CONFIGS = [
    #{
    #    'name': 'public_goods',
    #    'display_name': "Public Goods",
    #    'num_demo_participants': 3,
    #    'app_sequence': ['public_goods', 'payment_info'],
    #},

    {
        'name': 'Master_Study_I_IV',
        'num_demo_participants': 16,
        'app_sequence': ['Master_Study_I_IV', 'SOEP5', 'Exit_Questionnaire'],
    }
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = '$'
USE_POINTS = True

ROOM_DEFAULTS = {}

ROOMS = [
    {
        'name': 'prestudy',
        'display_name': 'master_prestudy',
        'participant_label_file': '_rooms/econ101.txt',
    }
]
# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '#!=0$7h!%=$%g*6@k50azm@$&(jmf(k6cj)p4*f+y95+ioybg6'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree', 'otree_tools']
EXTENSION_APPS = ['otree_tools']



