import streamlit as st
import pandas as pd
########################################################################


########################################################################
# A feature that allows you to investigate management and provide recommendations
# based on conditions such as measured signs and symptoms.
########################################################################


class explore_managmenet_and_recommendations:
    def urgentAttention_Mgmt(val, *args):
        if val == 'breathingDifficulty' and breathingDifficulty == 'Yes':
            Suggestions = 'Give face mask oxygen and refer urgently.'
            return Suggestions
        elif BP == '<90/60':
            BPKB_Rules = 'Give normal saline 1L IV rapidly, repeat until systolic BP > 90. Continue 1L 6 hourly. Stop if breathing worsens'
            return BPKB_Rules
        elif temprature == '>=38':
            tempKB_Rules = 'Give ceftriaxone1 1g IM/IV or ampicillin1 2g IV/IM and gentamicin 80mg IM and refer urgently.'
            return tempKB_Rules
        else:
            return ""

    def PROM_Mgmt(*args):
        if suddenGushofClear_or_pale == 'Yes':
            PROM_TP1 = 'Premature rupture of membranes (PROM) likely'
            PROM_TP2 = 'Confirm amniotic  uid with sterile speculum: examination.'
            PROM_TP3 = 'Avoid digital vaginal examination.'
            return PROM_TP1 + PROM_TP2 + PROM_TP3
        elif suddenGushofClear_or_pale == 'Yes' and chorioamnionitis == 'Yes' and status_or_numberofWeeks == '>37':
            PROM_RP1 = 'If not in active labour 8 hours after PROM, give ampicillin1 1g IV/IM and refer urgently.'
            return PROM_RP1
        elif suddenGushofClear_or_pale == 'Yes' and chorioamnionitis == 'No' and status_or_numberofWeeks == '<37':
            PROM_TP3 = 'Give erythromycin 250mg 6 hourly'
            return PROM_TP3
        elif suddenGushofClear_or_pale == 'Yes' and chorioamnionitis == 'No' and status_or_numberofWeeks == '24-34':
            PROM_RP2 = 'Give dexamethasone 6mg IM, record time given in referral letter. Refer same day.'
            return PROM_RP2
        else:
            PROM_TP4 = 'Path is not available'
            return PROM_TP4

    def preterm_labour_managmenet(*args):
        if painfulContractionLessthan37wks == 'Yes' and status_or_numberofWeeks == '<24':
            PreTerm_RP1 = 'Refer'
            return PreTerm_RP1
        elif painfulContractionLessthan37wks == 'Yes' and status_or_numberofWeeks == '24-34':
            PreTerm_TR2 = 'Give dexamethasone 6mg IM, record time given in referral letter'
            PreTerm_TP1 = 'Give nifedipine 30mg PO,then 10mg 4 hourly until transferred'
            return PreTerm_TR2 + "; " + PreTerm_TP1
        elif painfulContractionLessthan37wks == 'Yes' and status_or_numberofWeeks == '24-34' and BP == '<90/60':
            PreTerm_TP2 = 'Give IV  fluids as above.'
            return PreTerm_TP2
        elif painfulContractionLessthan37wks == 'Yes' and status_or_numberofWeeks == '>34':
            PreTerm_TP3 = 'Allow labour to continue'
            return PreTerm_TP3
        else:
            V_RP3 = 'Refer'
            return V_RP3

    def vaginalBleeding_managmenet(*args):
        if status_or_numberofWeeks == '<24' and cervical == 'Yes':
            V_TP1 = 'Threatened or complete miscarriage likely'
            V_RP1 = 'Refer same day to exclude ectopic pregnancy'
            return V_TP1 + '; ' + V_RP1
        elif status_or_numberofWeeks == '>=12 and <24' and cervical == 'Yes':
            V_RP2 = 'Refer same day'
            return V_RP2
        elif status_or_numberofWeeks == '<12'and cervical == 'Yes':
            V_TP2 = 'Do MVA'
            return V_TP2
        elif status_or_numberofWeeks == '<24' and cervical == 'Yes' and pain == 'Yes':
            V_TP3 = 'Give ibuprofen 400mg PO TID'
            return V_TP3
        elif status_or_numberofWeeks == '<24' and cervical == 'Yes' and vaginalBleeding == 'Heavy':
            V_TP4 = 'Give IV fluid as above'
            V_TP5 = 'Give single dose misoprostol 800mcg intravaginally'
            V_RP3 = 'Refer the same day'
            return V_TP4 + "; " + V_TP5 + "; " + V_RP3
        elif status_or_numberofWeeks == '<24' and cervical == 'Yes' and temprature == '>=38' or pulse == '>=100' or vaginaldischarge == 'Smelly':
            V_TP6 = 'Give ceftriaxone1 1g IM/IV or ampicillin1 2g IV/IM and gentamicin 80mg IM'
            return V_TP6
        elif status_or_numberofWeeks == '<24' and cervical == 'Yes' and rh_negative == 'Yes':
            V_TP7 = 'Give anti-D immunoglobulin 250mcg IM'
            return V_TP7
        else:
            V_TP8 = 'Path is not available'
            return V_TP8

    def severe_hypertension_managmenet(*args):
        if severe_hypertension == 'Yes' and BP == '≥ 160/110':
            Hyp_TP1 = 'Give hydralazine 5mg IV over 4 minutes. Also give 200mL normal saline IV and Arrange urgent referral after giving the  rst doses of medications'
            return Hyp_TP1
        elif severe_hypertension == 'Yes' and BP == '≥ 150/110':
            Hyp_TP2 = 'repeat hydralazine 5mg every 30 minutes to a total maximum of 20mg and Arrange urgent referral after giving the  rst doses of medications'
            return Hyp_TP2
        else:
            Hyp_TP3 = 'Path is not available'
            return Hyp_TP3

    def pre_eclampsia_managmenet(*args):
        if BP == 'BP ≥ 140/90 ' and headache == 'Persistent' or blurredvision == 'Yes' or abdominalPain == 'Yes':
            Pre_TP0 = 'Give urgent attention to the pregnant patient and treat as severe pre-eclampsia'
            Pre_TP1 = 'Give magnesium sulphate 4g in 200mL normal saline IV over 20 minutes. Also give 5g IM mixed with 1mL of lidocaine 2% in each buttock, and then 5g IM 4 hourly'
            Pre_TP2 = 'Continue 1L normal saline IV 12 hourly'
            Pre_TP3 = 'Insert urethral catheter and record urine output every 4 hours'
            Pre_TP4 = 'Stop magnesium sulphate if urine output < 100mL in 4 hours or respiratory rate < 162 or knee re exes disappear'
            Pre_RP1 = 'If convulsion recurs or does not respond, refer urgently to hospital'
            return Pre_TP0 + "; " + Pre_TP1 + "; " + Pre_TP2 + "; " + Pre_TP3 + "; " + Pre_TP4 + "; " + Pre_RP1
        elif BP == 'BP ≥ 160/110 ' and proteinuria == '≥ 1+':
            Pre_TP5 = 'Give urgent attention to the pregnant patient  and treat as severe pre-eclampsia'
            return Pre_TP5
        elif BP == 'BP ≥ 160/110 ' and proteinuria == 'without proteinuria':
            Pre_TP6 = 'Give urgent attention to the pregnant patient and treat as severe hypertension'
            return Pre_TP6
        elif temprature == '≥ 38°C' and headache == 'Yes' or weakeness == 'Yes' or backpain == 'Yes' or abdominalPain == 'Yes':
            Pre_TP7 = 'Give urgent attention to the pregnant patient'
            return Pre_TP7
        elif breathingDifficulty == 'Yes' or swollenPainfulCalf == 'Yes' or vaginalBleeding == 'Yes' or decrease_or_absentof_fetalMovement == 'Yes' or painfulContractionLessthan37wks == 'Yes' or suddenGushofClear_or_pale == 'Yes':
            Pre_TP8 = 'Give urgent attention to the pregnant patient'
            return Pre_TP8
        elif pre_eclampsia == 'Yes' and BP == '≥ 160/110':
            Pre_TP9 = 'Give hydralazine 5mg IV over 4 minutes. Also give 200mL normal saline IV and Arrange urgent referral after giving the  rst doses of medications'
            return Pre_TP9
        elif pre_eclampsia == 'Yes' and BP == '≥ 150/110':
            Pre_TP10 = 'repeat hydralazine 5mg every 30 minutes to a total maximum of 20mg and Arrange urgent referral after giving the  rst doses of medications'
            return Pre_TP10
        else:
            Pre_TP11 = 'Path is not available'
            return Pre_TP11

    def convulsion_managmenet(*args):
        if convulsion == 'Yes' and status_or_numberofWeeks == '<20':
            CP1 = 'Consider path 15'
            return CP1
        elif convulsion == 'Yes' and status_or_numberofWeeks == 'between 20 and 1 week postpartum':
            C_TP1 = 'Treat for eclampsia: Lie patient in left lateral position'
            C_TP2 = 'Treat for eclampsia: Avoid placing anything in mouth'
            C_TP3 = 'Treat for eclampsia: Give 100% face mask oxygen'
            C_TP4 = 'Treat for eclampsia:: Give magnesium sulphate'
            return C_TP1 + "; " + C_TP2 + "; " + C_TP3 + "; " + C_TP4
        elif convulsion == 'Yes' and BP == '≥ 160/110':
            C_TP5 = 'give hydralazine 5mg IV over 4 minutes. Also give 200mL normal saline IV and Arrange urgent referral after giving the  rst doses of medications'
            return C_TP5
        elif convulsion == 'Yes' and BP == '≥ 150/110':
            C_TP6 = 'repeat hydralazine 5mg every 30 minutes to a total maximum of 20mg and Arrange urgent referral after giving the  rst doses of medications'
            return C_TP6
        else:
            C_TP7 = 'Give magnesium sulphate 4g in 200mL normal saline IV over 20 minutes. Also give 5g IM mixed with 1mL of lidocaine 2% in each buttock, and then 5g IM 4 hourly'
            C_TP8 = 'Continue 1L normal saline IV 12 hourly'
            C_TP9 = 'Insert urethral catheter and record urine output every 4 hours'
            C_TP10 = 'Stop magnesium sulphate if urine output < 100mL in 4 hours or respiratory rate < 162 or knee re exes disappear'
            C_RP1 = 'If convulsion recurs or does not respond, refer urgently to hospital'
            return C_TP7 + "; " + C_TP8 + "; " + C_TP9 + "; " + C_TP10 + "; " + C_RP1


if __name__ == "__main__":
    getRecommendations = explore_managmenet_and_recommendations()
    findingChoice = [
        'urgentAttention',
        'convulsion',
        'severe_pre_eclampsia',
        'vaginalBleeding',
        'pretermLabour',
        'PROM',
        'unsurePregnancy',
        'notUrgentAttention',
    ]
    finding = st.selectbox("Finding:", findingChoice)
    if finding == "urgentAttention":
        Suggestions = getRecommendations.urgentAttention_Mgmt()
    elif finding == "severe_hypertension":
        Suggestions = getRecommendations.severe_hypertension_managmenet()
    elif finding == "convulsion":
        Suggestions = getRecommendations.convulsion_managmenet()
    elif finding == "severe_pre_eclampsia":
        Suggestions = getRecommendations.pre_eclampsia_managmenet()
    elif finding == "vaginalBleeding":
        Suggestions = getRecommendations.PROM_Mgmt()
    elif finding == "pretermLabour":
        Suggestions = getRecommendations.preterm_labour_managmenet()
    elif finding == "PROM":
        suddenGushofClear_or_pale = 'Yes'
        Factors = "breathingDifficulty"
        Suggestions = getRecommendations.PROM_Mgmt()
    elif finding == "unsurePregnancy":
        Suggestions = getRecommendations.PROM_Mgmt()
    elif finding == "notUrgentAttention":
        Suggestions = getRecommendations.PROM_Mgmt()
    else:
        recommendations = "Consult the nearest specialists: According to the guidelines, there are no available recommendations."
