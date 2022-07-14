import streamlit as st
import ThePregnantPathways_Rules
import cp_tools

# to create interactive DataFrame

# assign the imported indicator to a python dictionary
rules = ThePregnantPathways_Rules.ThePregnantPathways_Rules()


# function to import getPregnantPatientRules

class KB_PregnantPathways_Rules:
    def get_urgentAttention_rules(*args):
        urgentAttention_rules = rules['Urgent_attention']
        return urgentAttention_rules

    def get_Convulsion_rules(*args):
        Convulsion_rules = rules['Convulsion']
        return Convulsion_rules

    def get_convulsion_or_severe_pre_eclampsia_rules(*args):
        convulsion_or_severe_pre_eclampsia_rules = rules['convulsion_or_severe_pre_eclampsia']
        return convulsion_or_severe_pre_eclampsia_rules

    def get_convulsion_or_severe_pre_eclampsia_or_severe_hypertension_rules(*args):
        convulsion_or_severe_pre_eclampsia_or_severe_hypertension_rules = rules[
            'convulsion_or_severe_pre_eclampsia_or_severe_hypertension']
        return convulsion_or_severe_pre_eclampsia_or_severe_hypertension_rules

    def get_vaginalBleeding_and_24weeks_and_Nocervical_rules(*args):
        vaginalBleeding_and_24weeks_and_Nocervical_rules = rules['vaginalBleeding_and_24weeks_and_Nocervical']
        return vaginalBleeding_and_24weeks_and_Nocervical_rules

    def get_vaginalBleeding_and_24weeks_and_cervical_rules(*args):
        vaginalBleeding_and_24weeks_and_cervical_rules = rules['vaginalBleeding_and_<24_weeks_and_cervical']
        return vaginalBleeding_and_24weeks_and_cervical_rules

    def get_tempraturre_and_pulse_and_smellyVagnalDischarge_rules(*args):
        tempraturre_and_pulse_and_smellyVagnalDischarge_rules = rules[
            'tempraturre>38_and_pulse>100_and_smellyVagnalDischarge']
        return tempraturre_and_pulse_and_smellyVagnalDischarge_rules

    def get_rhnegative_vaginalBleeding_or_latepreganacy_rules(*args):
        rhnegative_vaginalBleeding_or_latepreganacy_rules = rules['rhnegative_vaginalBleeding_or_late preganacy']
        return rhnegative_vaginalBleeding_or_latepreganacy_rules

    def get_late_pregannancy_rules(*args):
        late_pregannancy_rules = rules['late_pregannancy']
        return late_pregannancy_rules

    def severe_Pre_eclampsia_rules(*args):
        severe_Pre_eclampsia_rules = rules['severe_Pre_eclampsia']
        return severe_Pre_eclampsia_rules

    def severe_hypertension_rules(*args):
        severe_hypertension_rules = rules['severe_hypertension']
        return severe_hypertension_rules

    def vaginalBleeding_rules(*args):
        vaginalBleeding_rules = rules['vaginalBleeding']
        return vaginalBleeding_rules

    def pretermLabour_rules(*args):
        pretermLabour_rules = rules['pretermLabour']
        return pretermLabour_rules

    def PROM_rules(*args):
        PROM_rules = rules['PROM']
        return PROM_rules


def Visualize_Preg_KB_rules():
    PKB_rules = KB_PregnantPathways_Rules()

    # check and display
    showRules = st.selectbox("",
                             [" ",
                              "Urgent Attention",
                              "Convulsion",
                              "severe_Pre_eclampsia",
                              "severe_hypertension",
                              "vaginalBleeding",
                              "pretermLabour",
                              "PROM",
                              "unsurePregnancy",
                              "Convulsion or Severe Pre_eclampsia",
                              "Convulsion or Severe Pre_eclampsia or Severe Hypertension",
                              "vaginalBleeding_and_24weeks_and_Nocervical",
                              "vaginalBleeding_and_<24_weeks_and_cervical",
                              "tempraturre>38_and_pulse>100_and_smellyVagnalDischarge",
                              "rhnegative_vaginalBleeding_or_late preganacy",
                              "late_pregannancy",
                              ])
    if showRules == "All":
        # over all
        st.write('The Pregnant Patient KB Rules', rules)
        # return_rules_asTable(rules, finding="All")
    elif showRules == "Urgent Attention":
        # st.write('The Pregnant Patient: Urgent attention KB Rules',
        #         PKB_rules.get_urgentAttention_rules())
        cp_tools.return_rules_asTable(
            PKB_rules.get_urgentAttention_rules(), finding="Urgent Attention")

    elif showRules == "severe_Pre_eclampsia":
        st.write('The Pregnant Patient: Severe Pre eclampsia KB Rules')
        cp_tools.return_rules_asTable(PKB_rules.severe_Pre_eclampsia_rules(),
                                      finding="severe_Pre_eclampsia")

    elif showRules == "severe_hypertension":
        st.write('The Pregnant Patient: Severe hypertension KB Rules')
        cp_tools.return_rules_asTable(PKB_rules.severe_hypertension_rules(),
                                      finding="severe_hypertension")
    elif showRules == "vaginalBleeding":
        st.write('The Pregnant Patient: Vaginal bleeding KB Rules')
        cp_tools.return_rules_asTable(PKB_rules.vaginalBleeding_rules(),
                                      finding="vaginalBleeding")
    elif showRules == "pretermLabour":
        st.write('The Pregnant Patient: Pre-term labour KB Rules')
        cp_tools.return_rules_asTable(PKB_rules.pretermLabour_rules(),
                                      finding="pretermLabour")
    elif showRules == "PROM":
        st.write('The Pregnant Patient: PROM KB Rules')
        return_rules_asTable(PKB_rules.PROM_rules(),
                             finding="PROM")
    elif showRules == "Convulsion":
        st.write('The Pregnant Patient: Convulsion KB Rules')
        cp_tools.return_rules_asTable(PKB_rules.get_Convulsion_rules(),
                                      finding="Convulsion")

    elif showRules == "Convulsion or Severe Pre_eclampsia":
        st.write('The Pregnant Patient: Convulsion or Severe Pre_eclampsia KB Rules')
        cp_tools.return_rules_asTable(PKB_rules.get_convulsion_or_severe_pre_eclampsia_rules(),
                                      finding="Convulsion or Severe Pre_eclampsia")
    elif showRules == "Convulsion or Severe Pre_eclampsia or Severe Hypertension":
        st.write('The Pregnant Patient: Convulsion or Severe Pre_eclampsia or Severe Hypertension KB Rules')
        cp_tools.return_rules_asTable(PKB_rules.get_convulsion_or_severe_pre_eclampsia_or_severe_hypertension_rules(),
                                      finding="get_convulsion_or_severe_pre_eclampsia_or_severe_hypertension_rules")
    elif showRules == "vaginalBleeding_and_<24_weeks_and_cervical":
        st.write('The Pregnant Patient: Vaginal Bleeding and <24 weeks and cervical KB Rules')
        cp_tools.return_rules_asTable(PKB_rules.get_vaginalBleeding_and_24weeks_and_cervical_rules(),
                                      finding="late_pregannancy")
    elif showRules == "tempraturre>38_and_pulse>100_and_smellyVagnalDischarge":
        st.write('The Pregnant Patient: Tempraturre>38 and Pulse>100 and Smelly Vagnal Discharge KB Rules')
        cp_tools.return_rules_asTable(PKB_rules.get_tempraturre_and_pulse_and_smellyVagnalDischarge_rules(),
                                      finding="late_pregannancy")
    elif showRules == "rhnegative_vaginalBleeding_or_late":
        st.write('The Pregnant Patient: RH Negative Vaginal Bleeding or late pregnancy KB Rules')
        cp_tools.return_rules_asTable(PKB_rules.get_rhnegative_vaginalBleeding_or_latepreganacy_rules(),
                                      finding="late_pregannancy")
    elif showRules == "late_pregannancy":
        st.write('The Pregnant Patient: Late Preganancy KB Rules')
        cp_tools.return_rules_asTable(PKB_rules.get_late_pregannancy_rules(),
                                      finding="late_pregannancy")

    else:
        st.warning("Please Select the options from the menu")


if __name__ == '__main__':
    Visualize_Preg_KB_rules()
