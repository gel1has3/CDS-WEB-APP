import streamlit as st

# import the defn. CG based indicators
import CG_rulesets_and_indicators

# import  managment and sugession
import Mgmt_and_Suggestions

# assign the imported indicator to a python dictionary
indicator = CG_rulesets_and_indicators.CG_rulesets()


class clinicalPathways_Indicator:
    """
        A function for acessing and signaling urgent attention pathways
    """
    def get_urgentAttention_indicators(*args):
        urgentAttention_indicator = indicator['referralIndicator']['urgentAttention']
        return urgentAttention_indicator
        # return cp_tools.create_interactive_df(urgentAttention_indicator)

    """
    A Function for acessing the referral Clinical Pathways indicators
    """
    def get_Convulsion_R_indicator(*args):
        convulision_indicator = indicator['referralIndicator']['convulsion']
        return convulision_indicator

    def get_severe_Pre_eclampsia_R_indicator(*args):
        pre_eclampsia_indicator = indicator['referralIndicator']['severe_pre_eclampsia']
        return pre_eclampsia_indicator

    def get_severe_hypertension_R_indicator(*args):
        severe_hypertension_indicator = indicator['referralIndicator']['severe_hypertension']
        return severe_hypertension_indicator

    def get_vaginalBleeding_R_indicator(*args):
        vaginalBleeding_indicator = indicator['referralIndicator']['vaginalBleeding']
        return vaginalBleeding_indicator

    def get_pretermLabour_R_indicator(*args):
        pretermLabour_indicator = indicator['referralIndicator']['pretermLabour']
        return pretermLabour_indicator

    def get_PROM_R_indicator(*args):
        PROM_indicator = indicator['referralIndicator']['PROM']
        return PROM_indicator

    def get_unsurePregnancy_R_indicator(*args):
        unsurePregnancy_indicator = indicator['referralIndicator']['unsurePregnancy']
        return unsurePregnancy_indicator

    """
    A Function for acessing the treatable CLinical Pathways indicators
    """
    def get_Convulsion_T_indicator(*args):
        convulision_indicator = indicator['treatableIndicator']['convulsion']
        return convulision_indicator

    def get_vaginalBleeding_T_indicator(*args):
        vaginalBleeding_indicator = indicator['treatableIndicator']['vaginalBleeding']
        return vaginalBleeding_indicator

    def get_pretermLabour_T_indicator(*args):
        pretermLabour_indicator = indicator['treatableIndicator']['pretermLabour']
        return pretermLabour_indicator

    def get_notUrgentAttention_T_indicator(*args):
        notUrgentAttention_indicator = indicator['treatableIndicator']['notUrgentAttention']
        return notUrgentAttention_indicator

    def get_unsurePregnancy_T_indicator(*args):
        unsurePregnancy_indicator = indicator['treatableIndicator']['unsurePregnancy']
        return unsurePregnancy_indicator

    """
    A Function for acessing the consideration Clinical Pathway indicators
    """
    def get_unsurePregnancy_C_indicator(*args):
        unsurePregnancy_indicator = indicator['considerationIndicator']['unsurePregnancy']
        return unsurePregnancy_indicator

    def get_notUrgentAttention_C_currentMedicalProblems_indicator(*args):
        #        'currentMedicalProblems',
        notUrgentAttention_indicator = indicator['considerationIndicator']['notUrgentAttention']['currentMedicalProblems']
        return notUrgentAttention_indicator

    def get_notUrgentAttention_C_currentPregnancyProblems_indicator(*args):
        # 'currentPregnancyProblems',
        notUrgentAttention_indicator = indicator['considerationIndicator']['notUrgentAttention']['currentPregnancyProblems']
        return notUrgentAttention_indicator

    def get_notUrgentAttention_C_previousPregnancyProblems_indicator(*args):
        # 'previousPregnancyProblems',
        notUrgentAttention_indicator = indicator['considerationIndicator']['notUrgentAttention']['previousPregnancyProblems']
        return notUrgentAttention_indicator

    def get_notUrgentAttention_C_previousReproductiveTractSurgery_indicator(*args):
        # 'previousReproductiveTractSurgery',
        notUrgentAttention_indicator = indicator['considerationIndicator']['notUrgentAttention']['previousReproductiveTractSurgery']
        return notUrgentAttention_indicator


def showIndicator():
    # acessing the indicators
    CPIndicator = clinicalPathways_Indicator()

    # check and display
    showIndicator = st.selectbox("",
                                 [" ",
                                  "Urgent Attention",
                                  "Referral",
                                  "Treatable at the health center",
                                  "Consideration",
                                  ])
    if showIndicator == "All":
        # over all
        st.write('CG Based CP Indicators: Used as Gold Standard and Exit Criteria',
                 indicator)
    elif showIndicator == "Urgent Attention":
        st.warning('Please be cautious and pay careful attention if any of the following signs and symptoms are seen in accordance with clinical guidelines')
        st.write("Urgent CP Attention Indicators",
                 CPIndicator.get_urgentAttention_indicators())
    elif showIndicator == "Referral":
        referral_filtering_choice = st.selectbox("Your are looking indicator for ",
                                                 ['', 'convulsion',
                                                  'severe pre_eclampsia',
                                                  'severe hypertension',
                                                  'vaginal bleeding',
                                                  'preterm labour',
                                                  'PROM', 'unsure pregnancy'])
        if referral_filtering_choice == 'convulsion':
            st.write("Referral CP Indicators: Convulsion",
                     CPIndicator.get_Convulsion_R_indicator())
            # will be dynamic here
            st.write("Mgmt_and_Suggestions",
                     Mgmt_and_Suggestions.convulsion_managmenet(
                         {'status_or_numberofWeeks': 'between 20 and 1 week postpartum'}))
        elif referral_filtering_choice == 'severe pre_eclampsia':
            st.write("Referral CP Indicators: Severe severe-eclampsia ",
                     CPIndicator.get_severe_Pre_eclampsia_R_indicator())
        elif referral_filtering_choice == 'severe hypertension':
            st.write("Referral CP Indicators: Severe Hypertension",
                     CPIndicator.get_severe_hypertension_R_indicator())
        elif referral_filtering_choice == 'vaginal bleeding':
            st.write("Referral CP Indicators: Vaginal Bleeding",
                     CPIndicator.get_vaginalBleeding_R_indicator())
        elif referral_filtering_choice == 'preterm labour':
            st.write("Referral CP Indicators: Preterm Labour",
                     CPIndicator.get_pretermLabour_R_indicator())
        elif referral_filtering_choice == 'PROM':
            st.write("Referral CP Indicators: PROM",
                     CPIndicator.get_PROM_R_indicator())
        elif referral_filtering_choice == 'unsure pregnancy':
            st.write("Referral CP Indicators: Unsure Pregnancy",
                     CPIndicator.get_unsurePregnancy_R_indicator())
        else:
            st.write("Enter your choice for viewing referral indicators")

    elif showIndicator == "Treatable at the health center":
        treatable_filtering_choice = st.selectbox("Your are looking indicator for ",
                                                  ['', 'convulsion',
                                                   'vaginal bleeding',
                                                   'preterm labour',
                                                   'Not urgent attention',
                                                   'unsure pregnancy'])

        if treatable_filtering_choice == 'convulsion':
            st.write("Treatable CP Indicators: Convulsion",
                     CPIndicator.get_Convulsion_T_indicator())
        elif treatable_filtering_choice == 'vaginal bleeding':
            st.write("Treatable CP Indicators: Vaginal Bleeding",
                     CPIndicator.get_vaginalBleeding_T_indicator())
        elif treatable_filtering_choice == 'preterm labour':
            st.write("Treatable CP Indicators: Preterm Labour",
                     CPIndicator.get_pretermLabour_T_indicator())
        elif treatable_filtering_choice == 'Not urgent attention':
            st.write("Treatable CP Indicators: Not urgent attention",
                     CPIndicator.get_notUrgentAttention_T_indicator())
        elif treatable_filtering_choice == 'unsure pregnancy':
            st.write("Treatable CP Indicators: Unsure Pregnancy",
                     CPIndicator.get_unsurePregnancy_T_indicator())
        else:
            st.write("Enter your choice for viewing treatble indicators")
    elif showIndicator == "Consideration":
        consideration_filtering_choice = st.selectbox("Your are looking indicator for ",
                                                      ['Unsure Pregnancy',
                                                       'Not urgent attention'])

        if consideration_filtering_choice == 'Unsure Pregnancy':
            st.write("Consideration CP Indicators: Unsure Pregnancy",
                     CPIndicator.get_unsurePregnancy_C_indicator())
        elif consideration_filtering_choice == 'Not urgent attention':
            notUrgentAttention_choice = st.selectbox("Your are looking specific indicator for ",
                                                     ['current medical problems',
                                                      'current pregnancy problems',
                                                      'previous pregnancy problems',
                                                      'previous reproductive tract surgery',
                                                      ])
            if notUrgentAttention_choice == 'current medical problems':
                st.write("Consideration CP Indicators:  current medical problems not urgent attention",
                         CPIndicator.get_notUrgentAttention_C_currentMedicalProblems_indicator())
            elif notUrgentAttention_choice == 'current pregnancy problems':
                st.write("Consideration CP Indicators:current pregnancy problems not urgent attention",
                         CPIndicator.get_notUrgentAttention_C_currentPregnancyProblems_indicator())
            elif notUrgentAttention_choice == 'previous pregnancy problems':
                st.write("Consideration CP Indicators: previous pregnancy problems not urgent attention",
                         CPIndicator.get_notUrgentAttention_C_previousPregnancyProblems_indicator())
            elif notUrgentAttention_choice == 'previous reproductive tract surgery':
                st.write("Consideration CP Indicators: previous reproductive tract surgery not urgent attention",
                         CPIndicator.get_notUrgentAttention_C_previousReproductiveTractSurgery_indicator())
            else:
                st.write("Enter your choice for viewing consideration indicators")
        else:
            st.write("Enter your choice for viewing consideration indicators")
    else:
        st.warning("Choosing is required to visualize the CG based CP indicators")
