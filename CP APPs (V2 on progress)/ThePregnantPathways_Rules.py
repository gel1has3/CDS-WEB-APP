def ThePregnantPathways_Rules():
    # Knowledge based rules for clinical pathways
    rules = {
        # "PROM": {},
        "unsurePregnancy": {},

        "Urgent_attention": {
            # Urgent attention
            0: ('P_TP1', 'Give urgent attention'),
            1: ('P_TP2', 'Treat as severe pre-eclampsia'),
            2: ('P_TP3', 'Treat as severe hypertension'),
            3: ('P_TP4', 'Consider Path 114'),
            4: ('P_TP5', 'Preterm labour likely'),
            5: ('P_TP6', 'Premature rupture of membranes (PROM) likely'),
            6: ('P_RP7', 'Give face mask oxygen and refer urgently'),
            7: ('P_TP8', 'Give normal saline 1L IV rapidly, repeat until systolic BP > 90. Continue 1L 6 hourly. Stop if breathing worsens.'),
            8: ('P_TP9', 'Give ceftriaxone1 1g IM/IV or ampicillin1 2g IV/IM and gentamicin 80mg IM and refer urgently'),
        },
        "Convulsion": {
            # Convulsion or just convulsion
            0: ('P_TP10', 'Consideration path 15'),
            1: ('P_TP11', 'Treat for eclampsia: Lie patient in left lateral position'),
            2: ('P_TP12', 'Treat for eclampsia:Avoid placing anything in mouth'),
            3: ('P_TP13', 'Treat for eclampsia:Give 100% face mask oxygen'),
            4: ('P_TP14', 'Treat for eclampsia: Give magnesium sulphate'),

            # For convulsion or severe pre_eclampsia
            5: ('P_TP15', 'Give magnesium sulphate 4g in 200mL normal saline IV over 20 minutes. Also give 5g IM mixed with 1mL of lidocaine 2% in each buttock, and then 5g IM 4 hourly'),
            6: ('P_TP16', 'Continue 1L normal saline IV 12 hourly'),
            7: ('P_TP17', 'Insert urethral catheter and record urine output every 4 hours'),
            8: ('P_TP18', 'Stop magnesium sulphate if urine output < 100mL in 4 hours or respiratory rate < 162 or knee re exes disappear'),
            9: ('P_TP19', 'If convulsion recurs or does not respond, refer urgently to hospital'),

            # For convulsion or severe pre_eclampsia or severe hypertension
            10: ('P_TP20', 'Give hydralazine 5mg IV over 4 minutes. Also give 200mL normal saline IV. If BP still ≥ 150/100, repeat hydralazine 5mg every 30 minutes to a total maximum of 20mg'),
            11: ('P_TP21', 'Arrange urgent referral after giving the  first doses of medications'),

        },
        ################################################
        # "Convulsion": {},
        "severe_Pre_eclampsia": {
            # For convulsion or severe pre_eclampsia
            0: ('P_TP15', 'Give magnesium sulphate 4g in 200mL normal saline IV over 20 minutes. Also give 5g IM mixed with 1mL of lidocaine 2% in each buttock, and then 5g IM 4 hourly'),
            1: ('P_TP16', 'Continue 1L normal saline IV 12 hourly'),
            2: ('P_TP17', 'Insert urethral catheter and record urine output every 4 hours'),
            3: ('P_TP18', 'Stop magnesium sulphate if urine output < 100mL in 4 hours or respiratory rate < 162 or knee re exes disappear'),
            4: ('P_TP19', 'If convulsion recurs or does not respond, refer urgently to hospital'),

            # For convulsion or severe pre_eclampsia or severe hypertension
            5: ('P_TP20', 'Give hydralazine 5mg IV over 4 minutes. Also give 200mL normal saline IV. If BP still ≥ 150/100, repeat hydralazine 5mg every 30 minutes to a total maximum of 20mg'),
            6: ('P_TP21', 'Arrange urgent referral after giving the  first doses of medications'),

        },
        "severe_hypertension": {
            # For convulsion or severe pre_eclampsia or severe hypertension
            0: ('P_TP20', 'Give hydralazine 5mg IV over 4 minutes. Also give 200mL normal saline IV. If BP still ≥ 150/100, repeat hydralazine 5mg every 30 minutes to a total maximum of 20mg'),
            1: ('P_TP21', 'Arrange urgent referral after giving the  first doses of medications'),

        },
        "vaginalBleeding": {
            # vaginal bleeding  and <24 weeks and No cervical.....
            0: ('P_TP22', 'Threatened or complete miscarriage likely'),
            1: ('P_RP23', 'Refer same day to exclude ectopic pregnancy'),

            # vaginal bleeding  and <24 weeks and Yes cervical.....
            2: ('P_RP24', 'Refer same day'),
            3: ('P_TP25', 'Do MVA'),
            4: ('P_TP26',  'Give ibuprofen 400mg PO TID'),
            5: ('P_TP27',  'Give IV  fluids as above'),
            6: ('P_TP28', 'Give single dose misoprostol 800mcg intravaginally 800mcg intravaginally'),

            # rh negative for vaginalBleeding or late preganacy
            7: ('P_TP30',  'Give anti-D immunoglobulin 250mcg IM'),

        },
        "pretermLabour": {
            # preterm labour
            0: ('P_TP33', 'Give dexamethasone 6mg IM, record time given in referral letter'),
            1: ('P_TP34', 'Give nifedipine 30mg PO,then 10mg 4 hourly until transferred'),
            2: ('P_TP35', 'Check BP every 30 minutes. If BP < 90/60, give IV  fluids as above'),

        },
        "greater_than_34weeks": {
            # greater than 34 weeks
            0: ('P_TP36', 'Allow labour to continue.'),

        },
        "PROM": {
            # PROM
            0: ('P_TP37', 'Confirm amniotic fluid with sterile speculum: examination'),
            1: ('P_TP38', 'Give ceftriaxone1 1g IV/IM or ampicillin1 2g IV/IM and gentamicin 80mg IM'),
            2: ('P_RP39', 'Give ampicillin1 1g IV/IM and refer urgently.'),
            3: ('P_RP40', 'Give erythromycin 250mg 6 hourly. If 24-34 weeks, also give dexamethasone 6mg IM, record time given in referral letter. Refer same day'),

        },
        ################################################

        "convulsion_or_severe_pre_eclampsia": {
            # For convulsion or severe pre_eclampsia
            0: ('P_TP15', 'Give magnesium sulphate 4g in 200mL normal saline IV over 20 minutes. Also give 5g IM mixed with 1mL of lidocaine 2% in each buttock, and then 5g IM 4 hourly'),
            1: ('P_TP16', 'Continue 1L normal saline IV 12 hourly'),
            2: ('P_TP17', 'Insert urethral catheter and record urine output every 4 hours'),
            3: ('P_TP18', 'Stop magnesium sulphate if urine output < 100mL in 4 hours or respiratory rate < 162 or knee re exes disappear'),
            4: ('P_TP19', 'If convulsion recurs or does not respond, refer urgently to hospital'),

        },
        "convulsion_or_severe_pre_eclampsia_or_severe_hypertension": {
            # For convulsion or severe pre_eclampsia or severe hypertension
            0: ('P_TP20', 'Give hydralazine 5mg IV over 4 minutes. Also give 200mL normal saline IV. If BP still ≥ 150/100, repeat hydralazine 5mg every 30 minutes to a total maximum of 20mg'),
            1: ('P_TP21', 'Arrange urgent referral after giving the  first doses of medications'),

        },
        "vaginalBleeding_and_<24_weeks_and_Nocervical": {
            # vaginal bleeding  and <24 weeks and No cervical.....
            0: ('P_TP22', 'Threatened or complete miscarriage likely'),
            1: ('P_RP23', 'Refer same day to exclude ectopic pregnancy'),

        },
        "vaginalBleeding_and_<24_weeks_and_cervical": {
            # vaginal bleeding  and <24 weeks and Yes cervical.....
            0: ('P_RP24', 'Refer same day'),
            1: ('P_TP25', 'Do MVA'),
            2: ('P_TP26',  'Give ibuprofen 400mg PO TID'),
            3: ('P_TP27',  'Give IV  fluids as above'),
            4: ('P_TP28', 'Give single dose misoprostol 800mcg intravaginally 800mcg intravaginally'),

        },
        "tempraturre>38_and_pulse>100_and_smellyVagnalDischarge": {
            # tempraturre>38, pulse>100 of smelly vagnal discharge
            0: ('P_TP29', 'Give ceftriaxone1 1g IM/IV or ampicillin1 2g IV/IM and gentamicin 80mg IM'),

        },
        "rhnegative_vaginalBleeding_or_latepreganacy": {
            # rh negative for vaginalBleeding or late preganacy
            0: ('P_TP30',  'Give anti-D immunoglobulin 250mcg IM'),

        },
        "late_pregannancy": {
            # late pregannancy
            0: ('P_TP31', 'Avoid digital vaginal examination'),
            1: ('P_TP32', 'Give IV  uids as above'),

        },

        "preganctPatient_not_needing_urgent_attention": {

            # approaches for preganct patient not needing urgent attention
            0: ('P_RP41',  'Discuss the options around continuing with pregnancy, choosing adoption or abortion. Refer to social worker'),
            1: ('P_RP42',  'Determine gestational age by dates and on examination. If unable to determine gestational age, arrange ultrasound'),
            2: ('P_RP43',  'Do MVA or provide medical abortion.'),
            3: ('P_RP44',  'Discuss future contraception and consider path 110'),
            4: ('P_RP45',  'Abortion is not an option.'),
            5: ('P_RP46',  'Discuss possibility of adoption'),
            6: ('P_RP47',  'Give routine antenatal care'),
            7: ('P_RP48',  'Current medical problems: diabetes, heart/kidney disease, asthma, epilepsy, on TB treatment, substance use/abuse, hypertension, HIV stage 3 or 4'),
            8: ('P_RP49',  'Current pregnancy problems: rhesus negative with antibodies, multiple pregnancy, < 18 years old, vaginal bleeding or pelvic mass'),
            9: ('P_RP50',  'Previous pregnancy problems: stillbirth or neonatal loss, ≥ 3 consecutive miscarriages, birth weight < 2500g or > 4500g, admission for hypertension or pre-eclampsia, congenital abnormality'),
            10: ('P_RP52',  'Previous reproductive tract surgery (including caesarean section)'),


        },

    }
    return rules
