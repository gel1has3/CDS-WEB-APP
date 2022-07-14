

class pnc_Managament_and_Suggestions:
    # CG PNC managment and sugession
    def urgentAttention_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'feeling unwell': "Yes"}.items():
            PNC_CP = 'Refer urgently.'
        elif Measured_Symptoms_Dict.items() <= {'temprature': ">38"}.items():
            PNC_CP = 'Refer urgently.'
        elif Measured_Symptoms_Dict.items() <= {'feeling unwell': "Yes", 'temprature': ">38"}.items():
            PNC_CP = 'give ceftriaxone1 1g IM/IV or amoxicillin1 1g PO with metronidazole 1g PO.'
            PNC_CP1 = 'Refer urgently.'
        elif Measured_Symptoms_Dict.items() <= {'BP': "<90/60"}.items():
            PNC_CP = 'give normal saline 1L IV rapidly, repeat until systolic BP > 90. Continue 1L 6 hourly. Stop if breathing worsens.'
        elif Measured_Symptoms_Dict.items() <= {'pulse': "≥100"}.items():
            PNC_CP = 'Refer urgently.'
        elif Measured_Symptoms_Dict.items() <= {'Heavy bleeding': "Yes", 'pulse': "≥100"}.items():
            PNC_CP = 'give normal saline 1L IV rapidly, repeat until systolic BP > 90. Continue 1L 6 hourly. Stop if breathing worsens.'
            PNC_CP1 = 'Refer urgently.'
            return PNC_CP + PNC_CP1
        elif Measured_Symptoms_Dict.items() <= {'Tear extending to anuse or rectum': "Yes"}.items():
            PNC_CP = 'Refer urgently.'
        elif Measured_Symptoms_Dict.items() <= {'pallor': "Yes", 'respiratoryRate': ">30"}.items():
            PNC_CP = 'Refer urgently.'
        elif Measured_Symptoms_Dict.items() <= {'dizziness/faintness': "Yes"}.items():
            PNC_CP = 'Refer urgently.'
        elif Measured_Symptoms_Dict.items() <= {'chest pain': "Yes"}.items():
            PNC_CP = 'Refer urgently.'
        elif Measured_Symptoms_Dict.items() <= {'pallor': "Yes", 'Haemoglobin': '< 7g/dL'}.items():
            PNC_CP = 'Refer urgently.'
        else:
            PNC_CP = "The FHR is normal"
            return PNC_CP

    def postpartumHaemorrhage_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'Heavy bleeding': "Yes"}.items():
            PNC_CP = 'Look for and repair any perineal tears.'
            PNC_CP1 = 'Massage uterus and empty bladder (with catheter if needed).'
            PNC_CP2 = 'Give oxytocin 10IU IM, then 30IU in 1L normal saline at 40 drops/minute IV.'
            PNC_CP3 = 'If uterus still soft after this, give ergometrine2 0.2mg IM/IV or misoprostol 400mcg sublingual and continue massaging uterus.'
            PNC_CP4 = 'If still bleeding heavily, apply bimanual3 or external aortic compression4 or non-pneumatic anti-shock garments (if available) during referral.'
            PNC_CP5 = 'Refer urgently.'
            return PNC_CP + PNC_CP1 + PNC_CP2 + PNC_CP3 + PNC_CP4 + PNC_CP5

    def convulsion_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'convulsion': "Yes"}.items():
            PNC_CP = 'Refer urgently.'
            return PNC_CP

    def severePre_eclampsia_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'BP': "≥140/90", 'headache': "Persistent"}.items():
            PNC_CP = 'Refer urgently.'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'BP': "≥140/90", 'blurredvision': "Yes"}.items():
            PNC_CP = 'Refer urgently.'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'BP': "≥140/90", 'abdominalPain': "Yes"}.items():
            PNC_CP = 'Refer urgently.'
            return PNC_CP
        PNC_CP = ''
        return PNC_CP

    def depression_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'patient not interacting with baby': 'Yes'}.items():
            PNC_CP = 'Consider path 99'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'a difficult life event in the last year': 'Yes'}.items():
            PNC_CP = 'Consider path 99'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'unhappy about pregnancy': 'Yes'}.items():
            PNC_CP = 'Consider path 99'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'absent or unsupportive partner': 'Yes'}.items():
            PNC_CP = 'Consider path 99'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'previous depression': 'Yes'}.items():
            PNC_CP = 'Consider path 99'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'anxiety, violence at home': 'Yes'}.items():
            PNC_CP = 'Consider path 99'
            return PNC_CP

    def substance_use_and_abuse_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'drunk ≥ 4 drinks5/session': 'Yes'}.items():
            PNC_CP = 'consider path 103'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'used khat or illegal drug': 'Yes'}.items():
            PNC_CP = 'consider path 103'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'misused prescription or over-the-counter medication': 'Yes'}.items():
            PNC_CP = 'consider path 103'
            return PNC_CP

    def famliyPlanning_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'assess patient’s contraception needs': 'Yes'}.items():
            PNC_CP = 'consider path 110'
            return PNC_CP

    def BabyFeeding_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'breastfeeding problem': 'Yes'}.items():
            PNC_CP = 'consider path 31.  Check that baby latches well and is not mixed feeding.'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'formula feeding': 'Yes'}.items():
            PNC_CP = ' ensure correct mixing of formula and water and that it is affordable, feasible, acceptable, safe and sustainable.'
            return PNC_CP

    def Baby_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'ensure baby received immunisations at birth': 'Yes'}.items():
            PNC_CP = 'Assess and manage the baby according to the IMNCI guide. Ensure baby received immunisations at birth and ensure baby is immunised at 6 week visit.'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'ensure baby is immunised at 6 week visit': 'Yes'}.items():
            PNC_CP = 'Assess and manage the baby according to the IMNCI guide. Ensure baby received immunisations at birth and ensure baby is immunised at 6 week visit.'
            return PNC_CP

    def abdomen_and_perineum_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'perineal': 'Yes'}.items():
            PNC_CP = 'check healing.'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'abdominal wound': 'Yes'}.items():
            PNC_CP = 'check healing.'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'painful abdomen': 'Yes'}.items():
            PNC_CP = 'check temperature and refer.'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'smelly discharge': 'Yes'}.items():
            PNC_CP = 'check temperature and refer.'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'poorly contracted uterus': 'Yes'}.items():
            PNC_CP = 'check temperature and refer.'
            return PNC_CP

    def BP_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'BP': '≥ 140/90'}.items():
            PNC_CP = 'recheck after 1 hour rest. If BP still ≥ 140/90 and ≤ 1 week postpartum, refer urgently.'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'BP': '≥ 140/90', 'checked at (or status)': 'after 1 hour rest'}.items():
            PNC_CP = 'refer urgently.'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'BP': '≥ 140/90', 'checked at (or status)': '≤ 1 week postpartum'}.items():
            PNC_CP = 'refer urgently.'
            return PNC_CP

    def HIV_test_in_mother_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'mother diagnosed with HIV': '+ve'}.items():
            PNC_CP = 'consider path 75 and give ANC Care 76'
            PNC_CP = 'do HIV PCR on baby same day and start post-exposure prophylaxis in baby while waiting for PCR result and consider path 118.'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'mother diagnosed with HIV': '+ve', 'on ART': 'No'}.items():
            PNC_CP = 'consider path 79 and start ART'
            PNC_CP = 'do HIV PCR on baby same day and start post-exposure prophylaxis in baby while waiting for PCR result and consider path 118.'
            return PNC_CP

    def HIV_test_in_HIV_exposed_baby_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'baby diagnosed with HIV': '+ve', 'Age of the baby': '<9 months'}.items():
            PNC_CP = 'start ART and confirm result with 2nd PCR.'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'baby diagnosed with HIV': '+ve', 'Age of the baby': '9-17 months'}.items():
            PNC_CP = 'do rapid test. If positive, do PCR. If PCR positive, start ART and confirm result with 2nd PCR.'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'baby diagnosed with HIV': '+ve', 'Age of the baby': '≥ 18 months'}.items():
            PNC_CP = 'consider path 75'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'baby diagnosed with HIV': '+ve', 'mother diagnosed with HIV': 'Yes', 'breastfeeding': 'Yes', 'baby unwell': 'Yes'}.items():
            PNC_CP = 'If mother diagnosed with HIV while breastfeeding or baby unwell, do HIV test same day.'
            return PNC_CP

    def Haemoglobin_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'pale': 'Yes', 'Haemoglobin': '<7g/dL'}.items():
            PNC_CP = ' refer same day'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'pale': 'Yes', 'Haemoglobin': '7-11g/d'}.items():
            PNC_CP = 'treat at the health center'
            return PNC_CP

    def Syphilis_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'Syphilis': '+ve'}.items():
            PNC_CP = 'consider path 41 and  treat mother and baby'
            return PNC_CP

    def cervicalScreen_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'mother diagnosed with HIV': '-ve'}.items():
            PNC_CP = 'screen every 5 years if patient between 30-49 years.'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'mother diagnosed with HIV': '+ve'}.items():
            PNC_CP = 'screen at HIV diagnosis (regardless of age) then 5 yearly'
            return PNC_CP
        elif Measured_Symptoms_Dict.items() <= {'cervicalScreen': 'Abnormal'}.items():
            PNC_CP = 'consider path 40'
            return PNC_CP


class anc_Managament_and_Suggestions:
    # CG ANC managment and susgession
    def EDD_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'status_or_numberofWeeks': '≥ 41 weeks'}.items():
            ANC_CP = 'Confirm EDD and refer for fetal evaluation and possible induction of labour.'
        return ANC_CP

    def FetalMovements_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {"Decreased or Absent fetal movements": "Yes"}.items():
            ANC_CP = 'Assessed fetal heart rate (FHR)'
            return ANC_CP
        elif Measured_Symptoms_Dict.items() <= {"FHR": "> 160"}.items():
            ANCP = 'FHR = {}. and refer to hospital'.format("> 160")
            return ANCP
        elif Measured_Symptoms_Dict.items() <= {"FHR": "< 110"}.items():
            ANCP = ' FHR = {}. and refer to hospital'.format("< 110")
            return ANCP
        elif Measured_Symptoms_Dict.items() <= {"FHR": "Absent"}.items():
            ANCP = 'FHR = {}. and refer to hospital'.format("Absent")
            return ANCP
        elif Measured_Symptoms_Dict.items() <= {"Decreased or Absent fetal movements": "Yes", "FHR": "Absent"}.items():
            ANCP = 'refer to hospital'
            return ANCP
        else:
            ANCP = "The FHR is normal"
            return ANCP

    def TB_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {"cough": "> 2 weeks", "nightSweats": "Yes", "weightLoss": "Yes", "Fever": "Yes"}.items():
            ANC_CP = 'exclude TB and consider path 71.'
        return ANC_CP

    def MentalHealth_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {"Felt depressed": "Yes", "Hopeless": "Yes", "irritable or worrying a lot": "Yes", "Sad": "Yes", "Had multiple physical complaints": "Yes", "Felt little interest or pleasure in doing things": "Yes"}.items():
            ANC_CP = 'Consider path 99.'
            return ANC_CP
        if Measured_Symptoms_Dict.items() <= {"Taking ≥ 14 units of alcohol/week or misusing illicit or prescription drugs": "Yes"}.items():
            ANC_CP1 = 'refer for secondary hospital antenatal care.'
            return ANC_CP1

    def Weight_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {"ExpecedWeightGain": "1-2kg at each visit"}.items():
            ANC_CP = 'refer to hospital.'
        return ANC_CP

    def BMI_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {"BMI": "< 18.5"}.items():
            ANC_CP = 'Exclude TB  71 and give routine malnutrition care  70.'
        elif Measured_Symptoms_Dict.items() <= {"BMI": ">30"}.items():
            ANC_CP = 'Refer to hospital for CVD risk assessment and management'
        else:
            ANC_CP = "Normal"
        return ANC_CP

    def MUAC_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {"MiddleUperArmCircumference": "<23cm"}.items():
            ANC_CP = 'Exclude TB  71, HIV  75 and give routine malnutrition care  70.'
        return ANC_CP

    def AbdominalExamination_managment(Measured_Symptoms_Dict):
        ANC_CP, ANC_CP1, ANC_CP2 = '', '', ''
        if Measured_Symptoms_Dict.items() <= {"Mass other than uterus in abdomen or pelvis": "Yes"}.items():
            ANC_CP = 'If mass other than uterus in abdomen or pelvis, refer for assessment.'
        if Measured_Symptoms_Dict.items() <= {"Plot symphysis-fundal height(SFH) is not within 3cm from expected gestational age": "Yes"}.items():
            ANC_CP1 = 'Plot symphysis-fundal height (SFH) on, antenatal card: measurement in centimeters is roughly gestational age in weeks. If SFH is not within 3cm from expected gestational age, refer to hospital.'
        if Measured_Symptoms_Dict.items() <= {"Breech or non-cephalic presentation": "Yes"}.items():
            ANC_CP2 = 'If breech or non-cephalic presentation at 37 weeks, refer to hospital.'
        return ANC_CP + ANC_CP1 + ANC_CP2

    def VaginalDischarge_managment(Measured_Symptoms_Dict):
        ANC_CP, ANC_CP1 = '', ''
        if Measured_Symptoms_Dict.items() <= {"VaginalDischarge": "Yes"}.items():
            ANC_CP = 'If abnormal discharge, treat for STI  36.'
        if Measured_Symptoms_Dict.items() <= {"Smallamountsofclear/palefluid": "Yes"}.items():
            ANC_CP1 = 'Premature rupture of membranes likely and consider path 112.If small amounts of clear/pale fluid,refer.Avoid digital examination.'
        return ANC_CP + ANC_CP1

    def BP_managment(Measured_Symptoms_Dict):
        ANC_CP, ANC_CP1, ANC_CP2, ANC_CP3 = '', '', '', ''
        if Measured_Symptoms_Dict.items() <= {"BP": "≥140/90"}.items():
            ANC_CP = 'If BP ≥ 140/90, repeat after 1 hour lying on left side. If 2nd BP normal, repeat after 2 days. If 2nd BP still raised, check urine dipstick for protein:'
        if Measured_Symptoms_Dict.items() <= {"proteinuria": "No proteinuria", "BP": "≥140/90"}.items():
            ANC_CP1 = 'No proteinuria: start methyldopa 250mg PO TID and refer to hospital.'
        if Measured_Symptoms_Dict.items() <= {"proteinuria": "≥1+", "BP": "≥140/90"}.items():
            ANC_CP2 = 'Refer to hospital.'
        if Measured_Symptoms_Dict.items() <= {"BP": "≥140/90", "BP": "≥160/110"}.items():
            ANC_CP3 = ' If BP ≥ 140/90 and symptoms or BP ≥ 160/110, manage as severe pre-eclampsia 112.'
        return ANC_CP + ANC_CP1 + ANC_CP2 + ANC_CP3

    def UrineDipstick_managment(Measured_Symptoms_Dict):
        ANC_CP, ANC_CP1, ANC_CP2, ANC_CP3 = '', '', '', ''
        if Measured_Symptoms_Dict.items() <= {'dipstick': 'normal with dysuria (burning urine)'}.items() or Measured_Symptoms_Dict.items() <= {'dipstick': 'leucocytes or nitrites present'}.items():
            ANC_CP = 'Treat for complicated urinary tract infection  44.'
        if Measured_Symptoms_Dict.items() <= {'BP': '<140/90', 'proteinuria': '<2+'}.items():
            ANC_CP1 = 'refer to hospital to exclude kidney disease. If BP < 140/90 and < 2+ proteinuria, reassess at next antenatal visit.'
        if Measured_Symptoms_Dict.items() <= {'Glucose in the urine': 'Yes'}.items():
            ANC_CP2 = 'check random blood sugar  86.'
        if Measured_Symptoms_Dict.items() <= {'BP': '≥160/110', 'proteinuria': '>1+'}.items():
            ANC_CP3 = 'Manage as severe pre-eclampsia  112.'
        return ANC_CP + ANC_CP1 + ANC_CP2 + ANC_CP3

    def DiabetesScreen_managment(Measured_Symptoms_Dict):
        ANC_CP, ANC_CP1, ANC_CP2 = '', '', ''
        if Measured_Symptoms_Dict.items() <= {"diabetes": "Yes", "status_or_numberofWeeks": "26 weeks"}.items():
            ANC_CP = 'Do oral glucose tolerance test4'
        if Measured_Symptoms_Dict.items() <= {"diabetes": "Yes", "glucose level": "75gm oral glucose lose"}.items() or {"diabetes": "Yes", "glucose level": "1-hour > 180mg/dl lose"}.items() or {"diabetes": "Yes", "glucose level": "2-hour ≥ 140mg/dl lose"}.items():
            ANC_CP1 = 'if fasting glucose ≥ 120mg/dl or following a 75gm oral glucose lose, 1-hour > 180mg/dl or 2-hour ≥ 140mg/dl, refer to hospital.'
        if Measured_Symptoms_Dict.items() <= {"diabetes": "Yes", "risk level": "High"}.items():
            ANC_CP2 = 'If high risk at first visit, check blood glucose  86. If diabetes, refer to hospital.'
        return ANC_CP + ANC_CP1 + ANC_CP2

    def Haemoglobin_managment(Measured_Symptoms_Dict):
        ANC_CP, ANC_CP1, ANC_CP2, ANC_CP3, ANC_CP4 = '', '', '', '', ''
        if Measured_Symptoms_Dict.items() <= {"Haemoglobin": "< 8g/dL", "status_or_numberofWeeks": "< 34 weeks"}.items():
            ANC_CP = 'refer to hospital same day.'
        elif Measured_Symptoms_Dict.items() <= {"Haemoglobin": "< 10g/dL", "status_or_numberofWeeks": "< 34 weeks"}.items():
            ANC_CP1 = 'refer to hospital same day.'
        elif Measured_Symptoms_Dict.items() <= {"Pallor": "Yes", "respiratoryRate": ">30"}.items():
            ANC_CP2 = 'refer to hospital same day.'
        elif Measured_Symptoms_Dict.items() <= {"Dizziness/faintness": "Yes", "Chest pain": "Yes"}.items():
            ANC_CP3 = 'refer to hospital same day.'
        elif Measured_Symptoms_Dict.items() <= {"Haemoglobin": "8-10g/dL"}.items():
            ANC_CP4 = 'Treat  115 and repeat Hb monthly until Hb > 10g/dL.'
        return ANC_CP + ANC_CP1 + ANC_CP2 + ANC_CP3 + ANC_CP4

    def RhStatus_managmenet(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {"RhStatus": "+ve"}.items():
            ANC_CP = 'Continue routine care.'
        elif Measured_Symptoms_Dict.items() <= {"RhStatus": "-ve", "status_or_numberofWeeks": "28 weeks"}.items():
            ANC_CP = 'Give anti-D immunoglobulin 250mcg IM at 28 weeks and immediately after delivery. Also give if miscarriage, ectopic or abdominal trauma.'
        return ANC_CP

    def Syphilis_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {"Syphilis": "+ve"}.items():
            ANC_CP = 'If positive  41.'
        return ANC_CP

    def HIV_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {"HIV": "+ve"}.items():
            ANC_CP = 'Test for HIV  75. If patient refuses, offer test at each visit, even in early labour.'
            ANC_CP1 = 'If HIV positive give routine care 76 and start ART same week 115.'
        return ANC_CP + ANC_CP1

    def HIVViralLoad_managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {"ViralLoad": ">1000copies/mL", "Assessment Time and Status": "During Firsit Visit HIV Positive"}.items():
            ANC_CP = 'If viral load > 1000copies/mL for 1st time, give increased adherence support  78 and repeat viral load after 3 months.'
        elif Measured_Symptoms_Dict.items() <= {"ViralLoad": ">1000copies/mL", "Assessment Time and Status": "During on ART 6 months"}.items():
            ANC_CP = 'If viral load > 1000copies/mL for 2nd time, patient has virological failure: refer to hospital.'
        elif Measured_Symptoms_Dict.items() <= {"ViralLoad": ">1000copies/mL"}.items():
            ANC_CP = 'If viral load > 1000copies/mL for 2nd time, patient has virological failure: refer to hospital.'
        elif Measured_Symptoms_Dict.items() <= {"ViralLoad": ">1000copies/mL", "Assessment Time and Status": "During on ART 12 months"}.items():
            ANC_CP = 'If viral load > 1000copies/mL for 2nd time, patient has virological failure: refer to hospital.'
        elif Measured_Symptoms_Dict.items() <= {"ViralLoad": ">1000copies/mL", "Assessment Time and Status": "During on ART Yearly"}.items():
            ANC_CP = 'If viral load > 1000copies/mL for 2nd time, patient has virological failure: refer to hospital.'
        return ANC_CP


class CG_Managament_and_Suggestions:
    # The pregant patient managment and susgession based on the CGs
    # The managment and suggestions  for the finding cases
    def convulsion_managmenet(Measured_Symptoms_Dict):
        """
        Input: A dictionary items measured symptoms together with their values are passed
        Process: The managment and sugession based on the guidelines
        Return: The return management and suggestions
        """
        # dict1 = {'status': '<0'}
        # st.write(dict1.items() <= {'convulsion': 'Yes', 'status': '<20'}.items())
        if Measured_Symptoms_Dict.items() <= {'convulsion': 'Yes', 'status_or_numberofWeeks': '<20'}.items():
            CP1 = 'Consider path 15'
            return CP1
        elif Measured_Symptoms_Dict.items() <= {'convulsion': 'Yes', 'status_or_numberofWeeks': 'between 20 and 1 week postpartum'}.items():
            C_TP1 = 'Treat for eclampsia: Lie patient in left lateral position'
            C_TP2 = 'Treat for eclampsia: Avoid placing anything in mouth'
            C_TP3 = 'Treat for eclampsia: Give 100% face mask oxygen'
            C_TP4 = 'Treat for eclampsia:: Give magnesium sulphate'
            return C_TP1+C_TP2+C_TP3+C_TP4
        elif Measured_Symptoms_Dict.items() <= {'convulsion': 'Yes', 'BP': '≥ 160/110'}.items():
            C_TP5 = 'give hydralazine 5mg IV over 4 minutes. Also give 200mL normal saline IV and Arrange urgent referral after giving the  rst doses of medications.'
            return C_TP5
        elif Measured_Symptoms_Dict.items() <= {'convulsion': 'Yes', 'BP': '≥ 150/100'}.items():
            C_TP6 = 'repeat hydralazine 5mg every 30 minutes to a total maximum of 20mg and Arrange urgent referral after giving the  rst doses of medications.'
            return C_TP6
        else:
            C_TP7 = 'Give magnesium sulphate 4g in 200mL normal saline IV over 20 minutes. Also give 5g IM mixed with 1mL of lidocaine 2% in each buttock, and then 5g IM 4 hourly.'
            C_TP8 = 'Continue 1L normal saline IV 12 hourly.'
            C_TP9 = 'Insert urethral catheter and record urine output every 4 hours.'
            C_TP10 = 'Stop magnesium sulphate if urine output < 100mL in 4 hours or respiratory rate < 162 or knee re exes disappear.'
            C_RP1 = 'If convulsion recurs or does not respond, refer urgently to hospital.'
            return C_TP7+C_TP8+C_TP9+C_TP10+C_RP1

    def pregnancyManagment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'breathingDifficulty': 'Yes'}.items():
            breathingDifficultyKB_Rules = 'Give face mask oxygen and refer urgently.'
            return breathingDifficultyKB_Rules
        if Measured_Symptoms_Dict.items() <= {'BP': '<90/60'}.items():
            BPKB_Rules = 'Give normal saline 1L IV rapidly, repeat until systolic BP > 90. Continue 1L 6 hourly. Stop if breathing worsens'
            return BPKB_Rules
        if Measured_Symptoms_Dict.items() <= {'temprature': '>=38'}.items():
            tempKB_Rules = 'Give ceftriaxone1 1g IM/IV or ampicillin1 2g IV/IM and gentamicin 80mg IM and refer urgently.'
            return tempKB_Rules

    def PROM_Managment(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'suddenGushofClear_or_pale': 'Yes'}.items():
            PROM_TP1 = 'Premature rupture of membranes (PROM) likely'
            PROM_TP2 = 'Confirm amniotic  uid with sterile speculum: examination.'
            PROM_TP3 = 'Avoid digital vaginal examination.'
            return PROM_TP1 + PROM_TP2 + PROM_TP3
        elif Measured_Symptoms_Dict.items() <= {'suddenGushofClear_or_pale': 'Yes', 'chorioamnionitis': 'Yes', 'status_or_numberofWeeks': '>37'}.items():
            PROM_RP1 = 'If not in active labour 8 hours after PROM, give ampicillin1 1g IV/IM and refer urgently.'
            return PROM_RP1
        elif Measured_Symptoms_Dict.items() <= {'suddenGushofClear_or_pale': 'Yes', 'chorioamnionitis': 'No', 'status_or_numberofWeeks': '<37'}.items():
            PROM_TP3 = 'Give erythromycin 250mg 6 hourly'
            return PROM_TP3
        elif Measured_Symptoms_Dict.items() <= {'suddenGushofClear_or_pale': 'Yes', 'chorioamnionitis': 'No', 'status_or_numberofWeeks': '24-34'}.items():
            PROM_RP2 = 'Give dexamethasone 6mg IM, record time given in referral letter. Refer same day.'
            return PROM_RP2
        else:
            PROM_TP4 = 'Path is not available'
            return PROM_TP4

    def preterm_labour_managmenet(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'painfulContractionLessthan37wks': 'Yes', 'status_or_numberofWeeks': '<24'}.items():
            PreTerm_RP1 = 'Refer'
            return PreTerm_RP1
        elif Measured_Symptoms_Dict.items() <= {'painfulContractionLessthan37wks': 'Yes', 'status_or_numberofWeeks': '24-34'}.items():
            PreTerm_TR2 = 'Give dexamethasone 6mg IM, record time given in referral letter'
            PreTerm_TP1 = 'Give nifedipine 30mg PO,then 10mg 4 hourly until transferred'
            return PreTerm_TR2 + PreTerm_TP1
        elif Measured_Symptoms_Dict.items() <= {'painfulContractionLessthan37wks': 'Yes', 'status_or_numberofWeeks': '24-34', 'BP': '<90/60'}.items():
            PreTerm_TP2 = 'Give IV  fluids as above.'
            return PreTerm_TP2
        elif Measured_Symptoms_Dict.items() <= {'painfulContractionLessthan37wks': 'Yes',  'status_or_numberofWeeks': '>34'}.items():
            PreTerm_TP3 = 'Allow labour to continue'
            return PreTerm_TP3
        else:
            V_RP3 = 'Refer'
            return V_RP3

    def vaginalBleeding_managmenet(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'status_or_numberofWeeks': '<24', 'cervical': 'Yes'}.items():
            V_TP1 = 'Threatened or complete miscarriage likely'
            V_RP1 = 'Refer same day to exclude ectopic pregnancy'
            return V_TP1 + V_RP1
        elif Measured_Symptoms_Dict.items() <= {'status_or_numberofWeeks': '>=12 and <24', 'cervical': 'Yes'}.items():
            V_RP2 = 'Refer same day'
            return V_RP2
        elif Measured_Symptoms_Dict.items() <= {'status_or_numberofWeeks': '<12', 'cervical': 'Yes'}.items():
            V_TP2 = 'Do MVA'
            return V_TP2
        elif Measured_Symptoms_Dict.items() <= {'status_or_numberofWeeks': '<24', 'cervical': 'Yes', 'pain': 'Yes'}.items():
            V_TP3 = 'Give ibuprofen 400mg PO TID'
            return V_TP3
        elif Measured_Symptoms_Dict.items() <= {'status_or_numberofWeeks': '<24', 'cervical': 'Yes', 'vaginalBleeding': 'Heavy'}.items():
            V_TP4 = 'Give IV fluid as above'
            V_TP5 = 'Give single dose misoprostol 800mcg intravaginally'
            V_RP3 = 'Refer the same day'
            return V_TP4 + V_TP5 + V_RP3
        elif Measured_Symptoms_Dict.items() <= {'status_or_numberofWeeks': '<24', 'cervical': 'Yes', 'temprature': '>=38', 'pulse': '>=100', 'vaginaldischarge': 'Smelly'}.items():
            V_TP6 = 'Give ceftriaxone1 1g IM/IV or ampicillin1 2g IV/IM and gentamicin 80mg IM'
            return V_TP6
        elif Measured_Symptoms_Dict.items() <= {'status_or_numberofWeeks': '<24', 'cervical': 'Yes', 'rh_negative': 'Yes'}.items():
            V_TP7 = 'Give anti-D immunoglobulin 250mcg IM'
            return V_TP7
        else:
            V_TP8 = 'Path is not available'
            return V_TP8

    def severe_hypertension_managmenet(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'severe_hypertension': 'Yes', 'BP': '>=160/110'}.items():
            Hyp_TP1 = 'Give hydralazine 5mg IV over 4 minutes. Also give 200mL normal saline IV and Arrange urgent referral after giving the  rst doses of medications'
            return Hyp_TP1
        elif Measured_Symptoms_Dict.items() <= {'severe_hypertension': 'Yes', 'BP': '≥150/110'}.items():
            Hyp_TP2 = 'repeat hydralazine 5mg every 30 minutes to a total maximum of 20mg and Arrange urgent referral after giving the  rst doses of medications'
            return Hyp_TP2
        else:
            Hyp_TP3 = 'Path is not available'
            return Hyp_TP3

    def pre_eclampsia_managmenet(Measured_Symptoms_Dict):
        if Measured_Symptoms_Dict.items() <= {'BP': '≥140/90', 'headache': 'Persistent', 'blurredvision': 'Yes', 'abdominalPain': 'Yes'}.items():
            Pre_TP0 = 'Give urgent attention to the pregnant patient and treat as severe pre-eclampsia'
            Pre_TP1 = 'Give magnesium sulphate 4g in 200mL normal saline IV over 20 minutes. Also give 5g IM mixed with 1mL of lidocaine 2% in each buttock, and then 5g IM 4 hourly'
            Pre_TP2 = 'Continue 1L normal saline IV 12 hourly'
            Pre_TP3 = 'Insert urethral catheter and record urine output every 4 hours'
            Pre_TP4 = 'Stop magnesium sulphate if urine output < 100mL in 4 hours or respiratory rate < 162 or knee re exes disappear'
            Pre_RP1 = 'If convulsion recurs or does not respond, refer urgently to hospital'
            return Pre_TP0 + Pre_TP1 + Pre_TP2 + Pre_TP3 + Pre_TP4 + Pre_RP1
        elif Measured_Symptoms_Dict.items() <= {'BP': '≥160/110', 'proteinuria': '≥ 1+'}.items():
            Pre_TP5 = 'Give urgent attention to the pregnant patient  and treat as severe pre-eclampsia'
            return Pre_TP5
        elif Measured_Symptoms_Dict.items() <= {'BP': '≥160/110 ', 'proteinuria': 'without proteinuria'}.items():
            Pre_TP6 = 'Give urgent attention to the pregnant patient and treat as severe hypertension'
            return Pre_TP6
        elif Measured_Symptoms_Dict.items() <= {'temprature': '≥38°C', 'headache': 'Yes', 'weakeness': 'Yes', 'backpain': 'Yes', 'abdominalPain': 'Yes'}.items():
            Pre_TP7 = 'Give urgent attention to the pregnant patient'
            return Pre_TP7
        elif Measured_Symptoms_Dict.items() <= {'breathingDifficulty': 'Yes', 'swollenPainfulCalf': 'Yes', 'vaginalBleeding': 'Yes', 'decrease_or_absentof_fetalMovement': 'Yes', 'painfulContractionLessthan37wks': 'Yes', 'suddenGushofClear_or_pale': 'Yes'}.items():
            Pre_TP8 = 'Give urgent attention to the pregnant patient'
            return Pre_TP8
        elif Measured_Symptoms_Dict.items() <= {'pre_eclampsia': 'Yes', 'BP': '>=160/110'}.items():
            Pre_TP9 = 'Give hydralazine 5mg IV over 4 minutes. Also give 200mL normal saline IV and Arrange urgent referral after giving the  rst doses of medications'
            return Pre_TP9
        elif Measured_Symptoms_Dict.items() <= {'pre_eclampsia': 'Yes', 'BP': '≥150/100'}.items():
            Pre_TP10 = 'repeat hydralazine 5mg every 30 minutes to a total maximum of 20mg and Arrange urgent referral after giving the  rst doses of medications'
            return Pre_TP10
        else:
            Pre_TP11 = 'Path is not available'
            return Pre_TP11

    def unsurePregnancy(*args):
        BP == 'BP ≥ 140/90 '


def get_ANC_CG_Managament_and_Suggestions(Generated_CP_LIST):
    # Get ANC managment and sugesstions based on the clincal guidelines
    for col in range(0, len(Generated_CP_LIST)):
        getMS = Generated_CP_LIST.at[col, 'Measured_Symptoms']
        if Generated_CP_LIST.at[col, 'Finding'] == 'current medical problems':
            getMgt = CG_Managament_and_Suggestions.convulsion_managmenet(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'current pregnancy problems':
            getMgt = CG_Managament_and_Suggestions.convulsion_managmenet(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'previous pregnancy problems':
            getMgt = CG_Managament_and_Suggestions.convulsion_managmenet(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'previous reproductive tract surgery':
            getMgt = CG_Managament_and_Suggestions.convulsion_managmenet(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'TB':
            getMgt = anc_Managament_and_Suggestions.TB_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'Late estimated delivery date':
            getMgt = anc_Managament_and_Suggestions.EDD_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'Decreased or absent fetal movements':
            getMgt = anc_Managament_and_Suggestions.FetalMovements_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'Mental health':
            getMgt = anc_Managament_and_Suggestions.MentalHealth_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'BMI High - CVD Risk':
            getMgt = anc_Managament_and_Suggestions.BMI_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'Urine dipstick test':
            getMgt = anc_Managament_and_Suggestions.UrineDipstick_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'Haemoglobin':
            getMgt = anc_Managament_and_Suggestions.Haemoglobin_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'HIV Viral Load (patient may have virological failure)':
            getMgt = anc_Managament_and_Suggestions.HIVViralLoad_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'Abdominal Examination':
            getMgt = anc_Managament_and_Suggestions.AbdominalExamination_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'Middle Uper Arm Circumference':
            getMgt = anc_Managament_and_Suggestions.MUAC_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'BMI':
            getMgt = anc_Managament_and_Suggestions.BMI_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'Vaginal discharge (Abnormal or suddenGushofClear_or_pale)':
            getMgt = anc_Managament_and_Suggestions.VaginalDischarge_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'Diabetes Screen':
            getMgt = anc_Managament_and_Suggestions.DiabetesScreen_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'Haemoglobin':
            getMgt = anc_Managament_and_Suggestions.Haemoglobin_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'RH Status':
            getMgt = anc_Managament_and_Suggestions.RhStatus_managmenet(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'Syphilis':
            getMgt = anc_Managament_and_Suggestions.Syphilis_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'Expected weight gain of 1-2kg at each visit or < 1kg gain over 2 visits':
            getMgt = anc_Managament_and_Suggestions.Weight_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'HIV':
            getMgt = anc_Managament_and_Suggestions.HIV_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'HIV Viral Load':
            getMgt = anc_Managament_and_Suggestions.HIVViralLoad_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'BP is high or low (not normal)':
            getMgt = anc_Managament_and_Suggestions.BP_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
    return Generated_CP_LIST


def get_CG_Managament_and_Suggestions(Generated_CP_LIST):
    # The managment and suggestions  for the finding cases
    # assign the mangment and sugession based on the measured symptoms and finding
    # st.write("Columns:", Generated_CP_LIST.columns)
    # getMS = {"convulsion": "Yes", 'BP': '≥ 160/110'}
    # getMS = {"BP": ">=160/110", "convulsion": "Yes"}
    # MS_mgmt_and_suggestions = Mgmt_and_Suggestions.convulsion_managmenet(xMS)
    # st.write("The mant and sugession for ".format(xMS), MS_mgmt_and_suggestions)
    for col in range(0, len(Generated_CP_LIST)):
        getMS = Generated_CP_LIST.at[col, 'Measured_Symptoms']
        # get the Mgmt_and_Suggestions based on the findings
        if Generated_CP_LIST.at[col, 'Finding'] == 'Convulsion':
            getMgt = CG_Managament_and_Suggestions.convulsion_managmenet(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'severe_Pre_eclampsia':
            getMgt = CG_Managament_and_Suggestions.pre_eclampsia_managmenet(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'severe_hypertension':
            getMgt = CG_Managament_and_Suggestions.severe_hypertension_managmenet(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'vaginalBleeding':
            getMgt = CG_Managament_and_Suggestions.vaginalBleeding_managmenet(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'pretermLabour':
            getMgt = CG_Managament_and_Suggestions.preterm_labour_managmenet(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'PROM':
            getMgt = CG_Managament_and_Suggestions.PROM_Managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'unsurePregnancy':
            getMgt = CG_Managament_and_Suggestions.unsurePregnancy(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
    return Generated_CP_LIST


def get_PNC_CG_Managament_and_Suggestions(Generated_CP_LIST):
    # Get ANC managment and sugesstions based on the clincal guidelines
    for col in range(0, len(Generated_CP_LIST)):
        getMS = Generated_CP_LIST.at[col, 'Measured_Symptoms']
        if Generated_CP_LIST.at[col, 'Finding'] == 'urgent attention':
            getMgt = pnc_Managament_and_Suggestions.urgentAttention_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'postpartum haemorrhage':
            getMgt = pnc_Managament_and_Suggestions.postpartumHaemorrhage_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'convulsion':
            getMgt = pnc_Managament_and_Suggestions.convulsion_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'severe pre_eclampsia':
            getMgt = pnc_Managament_and_Suggestions.severePre_eclampsia_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'depression':
            getMgt = pnc_Managament_and_Suggestions.depression_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'substance use and abuse':
            getMgt = pnc_Managament_and_Suggestions.substance_use_and_abuse_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'famliy planning':
            getMgt = pnc_Managament_and_Suggestions.famliyPlanning_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'Baby feeding':
            getMgt = pnc_Managament_and_Suggestions.BabyFeeding_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'Baby (immunization)':
            getMgt = pnc_Managament_and_Suggestions.Baby_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'abdomen and perineum':
            getMgt = pnc_Managament_and_Suggestions.abdomen_and_perineum_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'BP':
            getMgt = pnc_Managament_and_Suggestions.BP_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'HIV test in mother':
            getMgt = pnc_Managament_and_Suggestions.HIV_test_in_mother_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'HIV test in HIV exposed baby':
            getMgt = pnc_Managament_and_Suggestions.HIV_test_in_HIV_exposed_baby_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'Haemoglobin':
            getMgt = pnc_Managament_and_Suggestions.Haemoglobin_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'Syphilis':
            getMgt = pnc_Managament_and_Suggestions.Syphilis_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
        elif Generated_CP_LIST.at[col, 'Finding'] == 'cervical screen':
            getMgt = pnc_Managament_and_Suggestions.cervicalScreen_managment(getMS)
            Generated_CP_LIST.at[col, 'Mgmt_and_Suggestions'] = getMgt
    return Generated_CP_LIST
