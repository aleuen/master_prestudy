# Similarity and Mental Account 
Study for masterthesis
Author: Adrian Leuenberger

## General Information
The purpose of this repository is to develop the measures
which will be used for the masterproject of Adrian Leuenberger.

The measures are programmed in [oTree](https://otree.readthedocs.io/en/latest/).
Each part of the study has its own App (and thus a folder in this repository) such
that in the end the study can be created by setting the `app_sequence`
in `settings.py`.

The parts are:
- `Consent_Instructions`: Informed Consent and Instructions (including comprehension questions)
- `Lottery_Task` lottery task after [Imas, 2016](https://static1.squarespace.com/static/57967bc7cd0f68048126361d/t/57ba6b82893fc01e071b5d7c/1471835012022/Realization+Effect.pdf
) (based on [Gneezy &
Potters 1997](https://academic.oup.com/qje/article/112/2/631/1870944)). Each Manipulation has its own App:
    - `Lottery_Task_1`: Baseline I: Replication Study 2 Imas (amount per round: 25 points)
    - `Lottery_Task_2`: Baseline II: Replication Study 2 Imas (amount per round: 100 points)
    - `Lottery_Task_3`: Realization: Replication Study 2 Imas
    - `Lottery_Task_4`: Framing: Replication Experiment 4 by MMW, 2019)
    - `Lottery_Task_5`: Layout wwwg: Background change in t4
    - `Lottery_Task_6`: Layout gggg: Reverse Baseline (amount per round: 100 points)
    - `Lottery_Task_7`: Layout gggw: Background change in t4 (Reverse Group 5)
    - `Lottery_Task_8`: Time delay between t3 and t4   
- `SOEP5`: The SOEP Scale for Risk Aversion (all 7 items)
- `Aspect Listing`: 2 qualitative questions for time preference / patience (Chapman et al., 2016 & Falk et al, 2018)
- `Exit Questionnaire`: Measures Overconfidence, Overprecision and Overplacement as in Chapman et al. (2016)
- `Administratives`: Implements the [Big Five Inventory 2](https://zis.gesis.org/skala/Danner-Rammstedt-Bluemke-Treiber-Berres-Soto-John-Die-deutsche-Version-des-Big-Five-Inventory-2-(BFI-2))


### General
- The code should be commented where something might be unclear.
Variable and function names should explain as much by themselves are possible while still remaining short.

- To randomize pages we implement [this](https://groups.google.com/forum/#!searchin/otree/randomize$20page$20sequence%7Csort:date/otree/G2YEdFul9y4/9HFrfsq7BQAJ) solution by Philipp Chapkovski.

- The payoff of the participants will be calculated using the oTree internal payoff variable.
Please do not use it for any other purpose than to store the money the participant should get
from completing your app.

- Input fields should be checked such that the format of answers is standardized.
A "year of birth" field should for example only allow for 4-digit numbers.
A field expecting percentage should only allow numbers between 0 and 100.

- There can be three levels of timers: Either there is *no timer* at all, a *soft* timer
that only reminds the participant that the time is up and a *hard* timer, where
the next page is loaded as soon as the time is up. Use each type where applicable.

## Style Guidelines

- The currency should be referred to as "points" in all apps. The average earning
in your app should be 50 points per minute.

- The instructions should be written in German and use the formal "Sie".
If there are already used translations for a measure, preferably use those.

- Questionnaire questions should be **bold**. If something needs to be emphasised in
the question it should additionally be underlined.

- If more than two options can be chosen and they are not in an ordinal scale, 
a dropdown widget should be used.

- Vertical radio buttons should only be used for binary and non-ordinal measures.

- Ordinal measures should be presented as horizontal radio buttons with anchors on the
extreme left and extreme right and numbers under the buttons. If each button would need a long text, you should use a
dropdown menu.

- Page footer should include web page, e-mail adress, SNF project number, Unibas, UZH and SNSF logo. This layout is stored in templates/global folder, as "Page1.html" (this is a clone of Page.html with only css elements added). To apply this layout to your app, replace {% extends "global/Page.html" %} with {% extends "global/Page1.html" %} at the beginning of your template.
