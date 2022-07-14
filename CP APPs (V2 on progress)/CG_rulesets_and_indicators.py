#!/usr/bin/env python
# coding: utf-8

# ### Indicator (or Exit Criteria)

# We extracted the indicator (or Exit critieria) from the Clinical Guideline (CGs) used as a Gold Standard - through indvidual measured symptoms and combinations of measured symptoms. The indicator is arranged in python nested dictionray structure.


def KBRules_for_pregnantManagment_recommendation():
    pregnanancyManagmentSuggestions = {
        # Avalilabel treatment sugesstion for The Pregnant Patient
        # Urgent attention
        'Urgent_attention': {
            'P_TP1': 'Give urgent attention',
            'P_TP2': 'Treat as severe pre-eclampsia',
            'P_TP3': 'Treat as severe hypertension',
            'P_TP4': 'Consider Path 114',
            'P_TP5': 'Preterm labour likely',
            'P_TP6': 'Premature rupture of membranes likely',
            'P_RP7': 'Give face mask oxygen and refer urgently',
            'P_TP8': 'Give normal saline 1L IV rapidly, repeat until systolic BP > 90. Continue 1L 6 hourly. Stop if breathing worsens.',
            'P_TP9': 'Give ceftriaxone1 1g IM/IV or ampicillin1 2g IV/IM and gentamicin 80mg IM and refer urgently',
        },
        'Convulsion': {
            # Convulsion or just convulsion
            'P_TP10': 'Consideration path 15',
            'P_TP11': 'Treat for eclampsia: Lie patient in left lateral position',
            'P_TP12': 'Treat for eclampsia:Avoid placing anything in mouth',
            'P_TP13': 'Treat for eclampsia:Give 100% face mask oxygen',
            'P_TP14': 'Treat for eclampsia: Give magnesium sulphate',
        },
        'convulsion_or_severePre_eclampsia': {
            # For convulsion or severe pre_eclampsia
            'P_TP15': 'Give magnesium sulphate 4g in 200mL normal saline IV over 20 minutes. Also give 5g IM mixed with 1mL of lidocaine 2% in each buttock, and then 5g IM 4 hourly',
            'P_TP16': 'Continue 1L normal saline IV 12 hourly',
            'P_TP17': 'Insert urethral catheter and record urine output every 4 hours',
            'P_TP18': 'Stop magnesium sulphate if urine output < 100mL in 4 hours or respiratory rate < 162 or knee re exes disappear',
            'P_TP19': 'If convulsion recurs or does not respond, refer urgently to hospital',
        },
        'convulsion_or_severePre_eclampsia_or_severeHypertension': {
            # For convulsion or severe pre_eclampsia or severe hypertension
            'P_TP20': 'Give hydralazine 5mg IV over 4 minutes. Also give 200mL normal saline IV. If BP still ≥ 150/100, repeat hydralazine 5mg every 30 minutes to a total maximum of 20mg',
            'P_TP21': 'Arrange urgent referral after giving the  first doses of medications',
        },
        'vaginalBleeding_and<24weeks_and_Nocervical': {
            # vaginal bleeding  and <24 weeks and No cervical.....
            'P_TP22': 'Threatened or complete miscarriage likely',
            'P_RP23': 'Refer same day to exclude ectopic pregnancy',

        },
        'vaginalBleeding_and<24weeksandCervical': {
            # vaginal bleeding  and <24 weeks and Yes cervical.....
            'P_RP24': 'Refer same day',
            'P_TP25': 'Do MVA',
            'P_TP26': 'Give ibuprofen 400mg PO TID',
            'P_TP27': 'Give IV  fluids as above',
            'P_TP28': 'Give single dose misoprostol 800mcg intravaginally 800mcg intravaginally',

        },
        'tempraturre>38_Pulse>100withSmellyVagnalDischarge': {
            # tempraturre>38, pulse>100 of smelly vagnal discharge
            'P_TP29': 'Give ceftriaxone1 1g IM/IV or ampicillin1 2g IV/IM and gentamicin 80mg IM',

        },
        'rhNegativeVaginalBleeding_or_latePreganacy': {
            # rh negative for vaginalBleeding or late preganacy
            'P_TP30': 'Give anti-D immunoglobulin 250mcg IM',
        },
        'latePregannancy': {
            # late pregannancy
            'P_TP31': 'Avoid digital vaginal examination',
            'P_TP32': 'Give IV  uids as above',
        },
        'pretermLabour': {
            # preterm labour
            'P_TP33': 'Give dexamethasone 6mg IM, record time given in referral letter',
            'P_TP34': 'Give nifedipine 30mg PO,then 10mg 4 hourly until transferred',
            'P_TP35': 'Check BP every 30 minutes. If BP < 90/60, give IV  fluids as above',
        },
        # greater than 34 weeks
        'P_TP36': 'Allow labour to continue.',
        'PROM': {        # PROM
            'P_TP37': 'Confirm amniotic fluid with sterile speculum: examination',
            'P_TP38': 'Give ceftriaxone1 1g IV/IM or ampicillin1 2g IV/IM and gentamicin 80mg IM',
            'P_RP39': 'Give ampicillin1 1g IV/IM and refer urgently.',
            'P_RP40': 'Give erythromycin 250mg 6 hourly. If 24-34 weeks, also give dexamethasone 6mg IM, record time given in referral letter. Refer same day',
        },
        'NotNeeding_UrgentAttention': {
            # approaches for preganct patient not needing urgent attention
            'P_RP41': 'Discuss the options around continuing with pregnancy, choosing adoption or abortion. Refer to social worker',
            'P_RP42': 'Determine gestational age by dates and on examination. If unable to determine gestational age, arrange ultrasound',
            'P_RP43': 'Do MVA or provide medical abortion.',
            'P_RP44': 'Discuss future contraception and consider path 110',
            'P_RP45': 'Abortion is not an option.',
            'P_RP46': 'Discuss possibility of adoption',
            'P_RP47': 'Give routine antenatal care',
            'P_RP48': 'Current medical problems: diabetes, heart/kidney disease, asthma, epilepsy, on TB treatment, substance use/abuse, hypertension, HIV stage 3 or 4',
            'P_RP49': 'Current pregnancy problems: rhesus negative with antibodies, multiple pregnancy, < 18 years old, vaginal bleeding or pelvic mass',
            'P_RP50': 'Previous pregnancy problems-stillbirth or neonatal loss ≥ 3 consecutive miscarriages birth weight < 2500g or > 4500g admission for hypertension or pre-eclampsia congenital abnormality',
            'P_RP52': 'Previous reproductive tract surgery including caesarean section',
        }

    }
    return pregnanancyManagmentSuggestions


def CG_rulesets():
    indicator = {
        'referralIndicator': {
            # Clinical referral indicator

            # indicator based on indivdual symptoms
            'urgentAttention': {
                0: {'convulsion': "Yes"},
                1: {'BP': '>=140/90'},
                2: {'BP': '>=160/110'},
                3: {'BP': '>=140/90', 'headache': 'Yes'},
                4: {'BP': '>=140/90', 'blurredVision': 'Yes'},
                5: {'BP': '>=140/90', 'abdominalPain': 'Yes'},
                6: {'BP': '>=160/110', 'proteinuria': 'Yes'},
                7: {'headache': 'Yes'},
                8: {'blurredVision': 'Yes'},
                9: {'abdominalPain': 'Yes'},
                10: {'temprature': '>=38°C'},
                11: {'diffcultyBreathing': 'Yes'},
                12: {'swollenPainfulCalf': 'Yes'},
                13: {'vaginalBleeding': 'Yes'},
                14: {'decreased_absent_FetalMovements': 'Yes'},
                15: {'painful_contractions_lessthan_37weeks': 'Yes'},
                16: {'sudden_GushOFclear_or_pale_fluid': 'Yes'},
                17: {'temprature': '>=38°C', 'headache': 'Yes'},
                18: {'temprature': '>=38°C', 'weakness': 'Yes'},
                19: {'temprature': '>=38°C', 'backPain': 'Yes'},
                20: {'temprature': '>=38°C', 'abdominalPain': 'Yes'},
            },
            'convulsion': {
                0: {'convulsion': "Yes"},
                1: {'convulsion': 'Yes', 'status': '<20weeks'},
                2: {'convulsion': 'Yes', 'status': 'between 20 weeks and 1 week'},
                3: {'convulsion': 'Yes', 'patientCondition': 'recurs or didnt respond'},
                4: {'convulsion': 'Yes', 'BP': '>=160/110'},
            },
            'severe_pre_eclampsia': {
                0: {'BP': '>=140/90', 'headache': 'Yes'},
                1: {'BP': '>=140/90', 'blurredVision': 'Yes'},
                2: {'BP': '>=140/90', 'abdominalPain': 'Yes'},
                3: {'BP': '>=160/110', 'proteinuria': 'Yes'},
            },
            'severe_hypertension': {
                0: {'BP': '>=160/110', 'proteinuria': 'Yes'}
            },
            # vaginal bleeding referral pathways
            'vaginalBleeding': {
                0: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'No'},
                1: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'No', 'temperature': '>=38°C'},
                2: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'No', 'pulse': '>=100'},
                3: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'No', 'smellyVaginalDischarge': 'Yes'},
                # when there is Cervical os open/dilated or products of conception in cervical os/vagina?
                4: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes'},
                5: {'vaginalBleeding': 'Yes', 'status': '>12weeks', 'cervicalDilated_ConceptioninCervical': 'Yes'},
                6: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'bleeding': 'Yes'},

                7: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'temperature': '>=38°C'},
                8: {'vaginalBleeding': 'Yes', 'status': '>12weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'temperature': '>=38°C'},
                9: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'bleeding': 'Yes', 'temperature': '>=38°C'},

                10: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'pulse': '>=100'},
                11: {'vaginalBleeding': 'Yes', 'status': '>12weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'pulse': '>=100'},
                12: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'bleeding': 'Yes', 'pulse': '>=100'},

                13: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'smellyVaginalDischarge': 'Yes'},
                14: {'vaginalBleeding': 'Yes', 'status': '>12weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'smellyVaginalDischarge': 'Yes'},
                15: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'bleeding': 'Yes', 'smellyVaginalDischarge': 'Yes'},

                16: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'No', 'temperature': '>=38', 'RH+Ve': 'Yes'},
                17: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'No', 'pulse': '>=100', 'RH+Ve': 'Yes'},
                18: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'No', 'smellyVaginalDischarge': 'Yes', 'RH+Ve': 'Yes'},
                19: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'RH+Ve': 'Yes'},
                20: {'vaginalBleeding': 'Yes', 'status': '>12weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'RH+Ve': 'Yes'},
                21: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'bleeding': 'Yes', 'RH+Ve': 'Yes'},

                22: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'temperature': '>=38', 'RH+Ve': 'Yes'},
                23: {'vaginalBleeding': 'Yes', 'status': '>12weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'temperature': '>=38', 'RH+Ve': 'Yes'},
                24: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'bleeding': 'Yes', 'temperature': '>=38', 'RH+Ve': 'Yes'},

                25: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'pulse': '>=100', 'RH+Ve': 'Yes'},
                26: {'vaginalBleeding': 'Yes', 'status': '>12weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'pulse': '>=100', 'RH+Ve': 'Yes'},
                27: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'bleeding': 'Yes', 'pulse': '>=100', 'RH+Ve': 'Yes'},

                28: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'smellyVaginalDischarge': 'Yes', 'RH+Ve': 'Yes'},
                29: {'vaginalBleeding': 'Yes', 'status': '>12weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'smellyVaginalDischarge': 'Yes', 'RH+Ve': 'Yes'},
                30: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'bleeding': 'Yes', 'smellyVaginalDischarge': 'Yes', 'RH+Ve': 'Yes'},
                31: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'No', 'RH+Ve': 'Yes'},
                32: {'vaginalBleeding': 'Yes', 'status': '>24weeks'},
                33: {'vaginalBleeding': 'Yes', 'status': '>24weeks', 'RH+Ve': 'Yes'},
            },
            # pre-term labour
            'pretermLabour': {
                0: {'painful_contractions_lessthan_37weeks': 'Yes'},
                1: {'painful_contractions_lessthan_37weeks': 'Yes', 'status': '<24weeks'},
                2: {'painful_contractions_lessthan_37weeks': 'Yes', 'status': '>34 weeks'},
                3: {'painful_contractions_lessthan_37weeks': 'Yes'},
                4: {'painful_contractions_lessthan_37weeks': 'Yes'},
            },
            'PROM': {
                0: {'sudden_GushOFclear_or_pale_fluid': 'Yes'},
                1: {'sudden_GushOFclear_or_pale_fluid': 'Yes', 'chorioamnionits': 'Yes'},
                2: {'sudden_GushOFclear_or_pale_fluid': 'Yes', 'chorioamnionits': 'No'},
                3: {'sudden_GushOFclear_or_pale_fluid': 'Yes', 'chorioamnionits': 'No', 'status': '<37weeks'},
                4: {'sudden_GushOFclear_or_pale_fluid': 'Yes', 'chorioamnionits': 'No', 'status': '>37weeks'},
            },
            'unsurePregnancy': {
                0: {'pregnancyIntent': 'No', 'requestAborition': 'Yes', 'age>18': 'Yes', 'status': '>12 weeks'},
            },
        },

        # treatable clinical pathway indicators
        'treatableIndicator': {
            'convulsion': {
                0: {'convulsion': 'Yes'},
                1: {'BP': '<90/60'},
            },
            # vaginal bleeding tretable pathways
            'vaginalBleeding': {
                0: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'No', 'temperature': '>=38'},
                1: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'No', 'pulse': '>=100'},
                2: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'No', 'smellyVaginalDischarge': 'Yes'},
                3: {'vaginalBleeding': 'Yes', 'status': '<12weeks', 'cervicalDilated_ConceptioninCervical': 'Yes'},
                4: {'vaginalBleeding': 'Yes', 'status': '<12weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'temperature': '>=38'},
                5: {'vaginalBleeding': 'Yes', 'status': '<12weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'pulse': '>=100'},
                6: {'vaginalBleeding': 'Yes', 'status': '<12weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'smellyVaginalDischarge': 'Yes'},
                7: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'pain': 'Yes'},
                8: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'pain': 'Yes', 'temperature': '>=38'},
                9: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'pain': 'Yes', 'pulse': '>=100'},
                10: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'pain': 'Yes', 'smellyVaginalDischarge': 'Yes'},

                11: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'No', 'temperature': '>=38', 'RH+Ve': 'Yes'},
                12: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'No', 'pulse': '>=100', 'RH+Ve': 'Yes'},
                13: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'No', 'smellyVaginalDischarge': 'Yes', 'RH+Ve': 'Yes'},
                14: {'vaginalBleeding': 'Yes', 'status': '<12weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'RH+Ve': 'Yes'},
                15: {'vaginalBleeding': 'Yes', 'status': '<12weeks', 'cervicalOSdilated': 'Yes', 'temperature': '>=38', 'RH+Ve': 'Yes'},
                16: {'vaginalBleeding': 'Yes', 'status': '<12weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'pulse': '>=100', 'RH+Ve': 'Yes'},
                17: {'vaginalBleeding': 'Yes', 'status': '<12weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'smellyVaginalDischarge': 'Yes', 'RH+Ve': 'Yes'},
                18: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'pain': 'Yes', 'RH+Ve': 'Yes'},
                19: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'pain': 'Yes', 'temperature': '>=38', 'RH+Ve': 'Yes'},
                20: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'pain': 'Yes', 'pulse': '>=100', 'RH+Ve': 'Yes'},
                21: {'vaginalBleeding': 'Yes', 'status': '<24weeks', 'cervicalDilated_ConceptioninCervical': 'Yes', 'pain': 'Yes', 'smellyVaginalDischarge': 'Yes', 'RH+Ve': 'Yes'},
            },
            # pre-term labour treatable pathways
            'pretermLabour': {
                0: {'painful_contractions_lessthan_37weeks': 'Yes', 'status': 'between 24 and 34 weeks'},
                1: {'painful_contractions_lessthan_37weeks': 'Yes', 'status': '<between 24 and 34 weeks', 'BP': '<90/60'},
            },
            'notUrgentAttention': {
                'currentMedicalProblems': {
                    0: {'pregnancyIntent': 'Yes'},
                },
                'currentPregnancyProblems': {
                    0: {'pregnancyIntent': 'Yes'},
                },
                'previousPregnancyProblems': {
                    0: {'pregnancyIntent': 'Yes'},
                },
                'previousReproductiveTractSurgery': {
                    0: {'pregnancyIntent': 'Yes'},
                },
            },
            'unsurePregnancy': {
                0: {'pregnancyIntent': 'No', 'requestAborition': 'Yes'},
                1: {'pregnancyIntent': 'No', 'requestAborition': 'Yes', 'age>18': 'Yes'},
                2: {'pregnancyIntent': 'No', 'requestAborition': 'Yes', 'age>18': 'Yes', 'status': '<12 weeks'},
                3: {'pregnancyIntent': 'No', 'requestAborition': 'Yes', 'age>18': 'Yes'},
                4: {'pregnancyIntent': 'No', 'requestAborition': 'Yes', 'age>18': 'No'},
            },
        },
        # conisderation path: multi disease clinical pathways indicators
        'considerationIndicator': {
            'unsurePregnancy': {
                0: {'pregnancyIntent': 'No', 'requestAborition': 'Yes', 'age>18': 'Yes', 'contraception': 'Yes'},
            },
            'notUrgentAttention': {
                'currentMedicalProblems': {
                    0: {'pregnancyIntent': 'Yes', 'diabetes': 'Yes'},
                    1: {'pregnancyIntent': 'Yes', 'heart/kidney disease': 'Yes'},
                    2: {'pregnancyIntent': 'Yes', 'asthma': 'Yes'},
                    3: {'pregnancyIntent': 'Yes', 'epilepsy': 'Yes'},
                    4: {'pregnancyIntent': 'Yes', 'TB_Treatment': 'Yes'},
                    5: {'pregnancyIntent': 'Yes', 'substance_use_and_abuse': 'Yes'},
                    6: {'pregnancyIntent': 'Yes', 'hypertension': 'Yes'},
                    7: {'pregnancyIntent': 'Yes', 'HIVStage_3_or_4': 'Yes'},
                },
                'currentPregnancyProblems': {
                    0: {'pregnancyIntent': 'Yes', 'RH+Ve': 'Yes'},
                    1: {'pregnancyIntent': 'Yes', 'multiplePregnancy': 'Yes'},
                    2: {'pregnancyIntent': 'Yes', '<18yrsOld': 'Yes'},
                    3: {'pregnancyIntent': 'Yes', 'vaginalBleeding': 'Yes'},
                },
                'previousPregnancyProblems': {
                    0: {'pregnancyIntent': 'Yes', 'stillbirth': 'Yes'},
                    1: {'pregnancyIntent': 'Yes', 'neonatalLoss': 'Yes'},
                    2: {'pregnancyIntent': 'Yes', '>=3consecutiveMiscarriages': 'Yes'},
                    3: {'pregnancyIntent': 'Yes', 'birth weight < 2500g or > 4500g': 'Yes'},
                    4: {'pregnancyIntent': 'Yes', 'hypertension': 'Yes'},
                    5: {'pregnancyIntent': 'Yes', 'pre-eclampsia': 'Yes'},
                    6: {'pregnancyIntent': 'Yes', 'congenitalAbNormality': 'Yes'},
                },
                'previousReproductiveTractSurgery': {
                    0: {'pregnancyIntent': 'Yes', 'caesareanSection': 'Yes'},
                    1: {'pregnancyIntent': 'Yes', 'reproductiveTractSurgery': 'Yes'},
                },
            },

        },
    }
    return indicator


def ANC_CG_rulesets():
    ANC_indicators = {
        'ANC_referralIndicator':
        {
            'currentMedicalProblems': {
                0: {'diabetes': 'Yes'},
                1: {'heart/kidney disease': 'Yes'},
                2: {'asthma': 'Yes'},
                3: {'epilepsy': 'Yes'},
                4: {'on TB treatment': 'Yes'},
                5: {'substance use/abuse': 'Yes'},
                6: {'hypertension': 'Yes'},
                7: {'HIV stage 3 or 4': 'Yes'},
                8: {'diabetes': 'Yes', 'heart/kidney disease': 'Yes', 'asthma': 'Yes',
                    'epilepsy': 'Yes', 'on TB treatment': 'Yes', 'on TB treatment': 'Yes',
                    'on TB treatment': 'Yes', 'substance use/abuse': 'Yes', 'hypertension': 'Yes', 'HIV stage 3 or 4': 'Yes'},
            },
            'currentPregnancyProblems': {
                0: {'rhesus negative with antibodies': 'Yes'},
                1: {'multiple pregnancy': 'Yes'},
                2: {'< 18 years old': 'Yes'},
                3: {'vaginal bleeding or pelvic mass': 'Yes'},
            },
            'previousPregnancyProblems': {
                0: {'stillbirth or neonatal loss': 'Yes'},
                1: {' ≥ 3 consecutive miscarriages': 'Yes'},
                2: {'birth weight < 2500g or > 4500g': 'Yes'},
                3: {'admission for hypertension or pre-eclampsia': 'Yes'},
                4: {'congenital abnormality': 'Yes'},
            },
            'previousReproductiveTractSurgery': {
                0: {'Previous reproductive tract surgery(including caesarean section)': 'Yes'},
            },
            'EstimatedDeliveryDate': {
                0: {'status_or_numberofWeeks': '≥ 41 weeks'},  # EDD - estimated delivery dates
            },
            'FetalMovements': {
                0: {'Decreased or Absent fetal movements': 'Yes', "FHR": '> 160'},
                1: {'Decreased or Absent fetal movements': 'Yes', "FHR": '< 110'},
                2: {'Decreased or Absent fetal movements': 'Yes', "FHR": 'Absent'},
            },
            'MentalHealth': {
                0: {'Taking ≥ 14 units of alcohol/week': 'Yes'},
                1: {'Misusing illicit': 'Yes'},
                2: {'Prescription drugs': 'Yes'},
            },
            'Weight': {
                0: {'ExpecedWeightGain': '1-2kg at each visit'},
                1: {'ExpecedWeightGain': '< 1kg gain over 2 visits'},
            },
            'MiddleUperArmCircumference': {},
            'BMI': {
                0: {'BMI': '>30'},
            },
            'AbdominalExamination': {
                0: {'Mass other than uterus in abdomen or pelvis': 'Yes'},
                1: {'Plot symphysis-fundal height(SFH) is not within 3cm from expected gestational age': 'Yes'},
                2: {'Breech or non-cephalic presentation': 'Yes'}
            },
            'VaginalDischarge': {
                0: {'Smallamountsofclear/palefluid': 'Yes'},
                1: {'VaginalDischarge': 'Yes'},
            },
            'BP': {
                0: {'BP': '≥140/90', 'proteinuria': 'No proteinuria'},
                1: {'BP': '≥160/110', 'proteinuria': '≥1+'},
                2: {'BP': '≥140/90'},
                3: {'BP': '≥160/110'},
            },
            'UrineDipStick': {
                0: {'BP': '≥160/110', 'risk level': 'High'},
                1: {'BP': '<140/90', 'proteinuria': '≥2+'},
                2: {'dipstick': 'normal with dysuria (burning urine)'},
                3: {'dipstick': 'leucocytes or nitrites present'},
                4: {'Glucose in the urine': 'Yes'},
                5: {'BP': '<140/90', 'proteinuria': '<2+'},
                6: {'BP': '≥160/110', 'proteinuria': '>1+'},

            },
            'DiabetesScreen': {
                0: {'diabetes': 'Yes'},
                1: {'glucose level': '≥ 120mg/dl'},
                2: {'glucose level': '75gm oral glucose lose'},
                3: {'glucose level': '1-hour > 180mg/dl lose'},
                4: {'glucose level': '2-hour ≥ 140mg/dl lose'},
                5: {"diabetes": "Yes", "status_or_numberofWeeks": "26 weeks"},
                6: {"diabetes": "Yes", "glucose level": "1-hour > 180mg/dl lose"},
                7: {"diabetes": "Yes", "glucose level": "2-hour ≥ 140mg/dl lose"},
                8: {'diabetes': 'Yes', "risk level": "High"}
            },
            'Haemoglobin': {
                0: {'Haemoglobin': '< 8g/dL',  'status_or_numberofWeeks': '< 34 weeks'},
                1: {'Haemoglobin': '< 10g/dL', 'status_or_numberofWeeks': '> 34 weeks'},
                2: {'Pallor': 'Yes', 'respiratoryRate': '>30'},
                3: {'Haemoglobin': '< 8g/dL',  'status_or_numberofWeeks': '< 34 weeks', 'Dizziness/faintness': 'Yes', 'Chest pain': 'Yes'},
                4: {'Haemoglobin': '< 10g/dL',  'status_or_numberofWeeks': '> 34 weeks', 'Dizziness/faintness': 'Yes', 'Chest pain': 'Yes'},
                5: {'Pallor': 'Yes', 'respiratoryRate': '>30', 'Dizziness/faintness': 'Yes', 'Chest pain': 'Yes'},
                6: {'Dizziness/faintness': 'Yes'},
                7: {'Chest pain': 'Yes'},
            },
            'HIVViralLoad': {
                0: {'ViralLoad': '>1000copies/mL', 'WhentwoAssesment_Status': '2nd time'},
                1: {"ViralLoad": ">1000copies/mL", "Assessment Time and Status": "During Firsit Visit HIV Positive"},
                2: {"ViralLoad": ">1000copies/mL", "Assessment Time and Status": "During on ART 6 months"},
                3: {"ViralLoad": ">1000copies/mL"},
                4: {"ViralLoad": ">1000copies/mL", "Assessment Time and Status": "During on ART 12 months"},
                5: {"ViralLoad": ">1000copies/mL", "Assessment Time and Status": "During on ART Yearly"},
            },
        },
        'ANC_treatableIndicator':
        {
            'TB': {
                0: {'cough': '> 2 weeks'},
                1: {'weightLoss': 'Yes'},
                2: {'nightSweats': 'Yes'},
                3: {'Fever': 'Yes'},
                4: {'cough > 2 weeks': 'Yes', 'weightLoss': 'Yes', 'nightSweats': 'Yes', 'Fever': 'Yes'},
            },
            'MiddleUperArmCircumference': {
                0: {'MiddleUperArmCircumference': '<23cm'},
            },
            'BMI': {
                0: {'BMI': '>18.5'},
            },

            'VaginalDischarge': {
                0: {'VaginalDischarge': 'Abnormal'},
            },

            'UrineDipStick': {
                0: {'BP': '<140/90', 'proteinuria': '<2+'},
                1: {'Glucose in the urine': 'Yes'},
                2: {'dipstick': 'normal with dysuria (burning urine)'},
                3: {'dipstick': 'leucocytes or nitrites present'},
                4: {'BP': '≥160/110', 'proteinuria': '>1+'},
            },
            'DiabetesScreen': {
                0: {'status_or_numberofWeeks': '26 weeks'},
            },
            'Haemoglobin': {
                0: {'Haemoglobin': '8-10g/dl'},
            },
            'RhStatus': {
                0: {'RhStatus': '+ve'},
                0: {'RhStatus': '-ve', 'status_or_numberofWeeks': '28 weeks'},
            },
            'Syphilis': {
                0: {'Syphilis': '+ve'},
            },
            'HIV': {
                0: {'HIV': '+ve'},
            },
            'HIVViralLoad': {
                0: {'ViralLoad': '>1000copies/mL', 'WhentwoAssesment_Status': '1st time'},
            },
        },
        'ANC_considerationIndicator': {
            'MentalHealth': {
                0: {'Felt depressed': 'Yes'},
                1: {'Sad': 'Yes'},
                2: {'Hopeless': 'Yes'},
                3: {'irritable or worrying a lot': 'Yes'},
                4: {'Had multiple physical complaints': 'Yes'},
                5: {'Felt little interest or pleasure in doing things': 'Yes'},
                6: {'Taking ≥ 14 units of alcohol/week or misusing illicit or prescription drugs': 'Yes'},
            },
            'Syphilis': {
                0: {'Syphilis': '+ve'},
            },
            'HIV': {
                0: {'HIV': '+ve'},
            },
            'HIVViralLoad': {
                0: {'ViralLoad': '>1000copies/mL', 'WhentwoAssesment_Status': '1st time'},
            },

        },
    }
    return ANC_indicators


def PNC_CG_rulesets():
    PNC_indicators = {
        'PNC_referralIndicator':
        {
            'urgentAttention': {
                0: {'feeling unwell': "Yes"},
                1: {'temprature': ">38"},
                2: {'BP': "<90/60"},
                3: {'pulse': "≥100"},
                4: {'Tear extending to anuse or rectum': "Yes"},
                5: {'pallor': "Yes", 'respiratoryRate': ">30"},
                6: {'dizziness/faintness': "Yes"},
                7: {'chest pain': "Yes"},
                8: {'pallor': "Yes", 'Haemoglobin': '< 7g/dL'},
                9: {'Heavy bleeding': "Yes", 'pulse': "≥100"},
                10: {'feeling unwell': "Yes", 'temprature': ">38"},
            },
            'postpartumHaemorrhage': {
                0: {'Heavy bleeding': "Yes"},
            },
            'convulsion': {
                0: {'convulsion': "Yes"},
            },
            'severePre_eclampsia': {
                0: {'BP': "≥140/90", 'headache': "Persistent"},
                1: {'BP': "≥140/90", 'blurredvision': "Yes"},
                2: {'BP': "≥140/90", 'abdominalPain': "Yes"},
            },


        },
        'PNC_treatableIndicator':
        {
            'depression': {
                0: {'patient not interacting with baby': 'Yes'},
                1: {'a difficult life event in the last year': 'Yes'},
                2: {'unhappy about pregnancy': 'Yes'},
                3: {'absent or unsupportive partner': 'Yes'},
                4: {'previous depression': 'Yes'},
                5: {'anxiety, violence at home': 'Yes'},

            },
            'substance_use_and_abuse': {
                0: {'drunk ≥ 4 drinks5/session': 'Yes'},
                1: {'used khat or illegal drug': 'Yes'},
                2: {'misused prescription or over-the-counter medication': 'Yes'},
            },
            'famliyPlanning': {

                0: {'assess patient’s contraception needs': 'Yes'},
            },
            'BabyFeeding': {
                0: {'breastfeeding problem': 'Yes'},
                1: {'formula feeding': 'Yes'},
            },
            'Baby': {
                0: {'ensure baby received immunisations at birth': 'Yes'},
                1: {'ensure baby is immunised at 6 week visit': 'Yes'},

            },
            'abdomen_and_perineum': {
                0: {'perineal': 'Yes'},
                1: {'abdominal wound': 'Yes'},
                2: {'painful abdomen': 'Yes'},
                3: {'smelly discharge': 'Yes'},
                4: {'poorly contracted uterus': 'Yes'},
            },
            'BP': {
                0: {'BP': '≥ 140/90'},
                1: {'BP': '≥ 140/90', 'checked at (or status)': 'after 1 hour rest'},
                2: {'BP': '≥ 140/90', 'checked at (or status)': '≤ 1 week postpartum'},
            },
            'HIV_test_in_mother': {
                0: {'mother diagnosed with HIV': '+ve'},
                1: {'mother diagnosed with HIV': '+ve', 'on ART': 'No'},

            },
            'HIV_test_in_HIV_exposed_baby': {
                0: {'baby diagnosed with HIV': '+ve', 'Age of the baby': '<9 months'},
                1: {'baby diagnosed with HIV': '+ve', 'Age of the baby': '9-17 months'},
                2: {'baby diagnosed with HIV': '+ve', 'Age of the baby': '≥ 18 months'},
                3: {'baby diagnosed with HIV': '+ve', 'mother diagnosed with HIV': 'Yes', 'breastfeeding': 'Yes', 'baby unwell': 'Yes'},
            },
            'Haemoglobin': {
                0: {'pale': 'Yes', 'Haemoglobin': '<7g/dL'},
                1: {'pale': 'Yes', 'Haemoglobin': '7-11g/d'},
            },
            'Syphilis': {
                0: {'Syphilis': '+ve'},
            },
            'cervicalScreen': {
                0: {'mother diagnosed with HIV': '-ve'},
                1: {'mother diagnosed with HIV': '+ve'},
                2: {'cervicalScreen': 'Abnormal'},
            },

        },
    }
    return PNC_indicators
