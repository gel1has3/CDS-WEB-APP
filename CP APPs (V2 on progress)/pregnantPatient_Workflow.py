
# This dashboard is designed by Geletaw Sahle
# The project is suprevised by
#

import pandas as pd
import streamlit as st

# import the defn. CG based indicators used as gold standard
import showCG_Indicators


# import CP processing module
import cp_Processing

# import cp prunning module
import cp_pruning

# import modlue for processing measure sysmptoms
import processing_Measured_Symptoms

# import CG urgent attention MS indicators
import urgent_attention_MS_indicators

# import filter and merge module
import cp_tools

# import anc care workflow and CP processing
import anc_care_workflow

# import managment and suggestions
import Mgmt_and_Suggestions

# import cp endrosment module
import cp_endrosment

# import streamlit graph processing module
from streamlit_agraph import agraph, Node, Edge, Config


# intialize the generated CP list
Generated_CP_LIST = pd.DataFrame({'Measured_Symptoms': [],
                                  'Urgent_Attention': '',
                                  'Generated_CP': [],
                                  'Finding': [],
                                  'Mgmt_and_Suggestions': [],
                                  })


def get_the_pregnant_patient_evidence(MS_Checklist):
    evdOptionList = []
    # get evidence if there is any
    current_directory = cp_tools.get_current_working_diretory()
    filename = "/ThePregnantPatient_EndrosedCPs.pkl"
    # merge the file name to get the full paths
    ThePregnantPatient_Endrosed_Path = current_directory + filename
    # ThePregnantPatient_Endrosed_Path = "/Users/geletawsahle/Desktop/CP_WorkFlow_DP_2022/ThePregnantPatient_EndrosedCPs.pkl"
    getPregnantPatient_evidence_and_factors = cp_tools.read_endrosed_cps(
        ThePregnantPatient_Endrosed_Path)

    viewPregnancy_evidence_and_factors = cp_tools.access_evidence(
        "PNC CPs", getPregnantPatient_evidence_and_factors)
    evidencelist = viewPregnancy_evidence_and_factors.columns.tolist()
    # getting evidence as a default values
    for evdValue in evidencelist:
        v = evdValue
        if v in MS_Checklist:
            evdOptionList.append(v)
    return evdOptionList


def PregnancyEntry():
    # potential list of measured symptoms
    symptomsList = [
        "status_or_numberofWeeks",
        "Fever",
        "BP",
        "bleeding",
        "convulsion",
        "headache",
        "blurredvision",
        "abdominalPain",
        "proteinuria",
        "temprature",
        "weakeness",
        "backpain",
        "breathingDifficulty",
        "swollenPainfulCalf",
        "vaginalBleeding",
        "decrease_or_absentof_fetalMovement",
        "painfulContractionLessthan37wks",
        "suddenGushofClear_or_pale",
        "cervical",
        "chorioamnionitis",
        "pain",
        "vaginaldischarge",
        "rh_negative",
        "pulse"]
    with st.expander(label="Prerequisite:  Check the age of the pregnant women. Only valid for women aged 15 to 49."):
        age = st.number_input("Enter Age:", min_value=15,
                              max_value=49, value=25, step=1)
    return age, symptomsList


def Quantize_MeasuredSymptoms(age, measuredSymptoms):
    # List of measured symptoms and values
    numbeofWeeks = [
        '<12', '>=12 and <24', '<20', '<24',
        '>=24', '24-34', '>34', '>=37',
        'between 20 and 1 week postpartum', 'Other']
    Choices = ['Yes', 'No']
    three_Choices = ['Yes', 'Persistent', 'No', 'Other']
    numbeofWeeks = [
        '<12', '>=12 and <24', '<20', '<24',
        '>=24', '24-34', '>34', '>=37',
        'between 20 and 1 week postpartum', 'Other']
    BP_Choices = ['<90/60', '>90', '>=140/90', '>=160/110', 'Other']
    abdominalPain_Choices = ['Yes', 'No', 'Severe', 'Other']
    proteinuria_Choices = ['>1+', 'No proteinuria', '<1', 'Other']
    Temp_Choices = ['>=38°C', '<38°C ', 'Other']
    vaginalBleeding_Choices = ['Yes', 'Abnormal', 'Heavy', 'No', 'Other']
    vaginaldischarge_Choices = ['Normal', 'Smelly', 'No', 'Other']
    Pulse_Choices = ['>=100', '<100', 'Other']

    filteringListValues = {}
    # filteringListValues["Age"] = age
    for i in range(0, len(measuredSymptoms)):
        if measuredSymptoms[i] == "status_or_numberofWeeks":
            MsValue = st.selectbox(measuredSymptoms[i], numbeofWeeks)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "Fever":
            MsValue = st.selectbox(measuredSymptoms[i], Choices)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "BP":
            MsValue = st.selectbox(measuredSymptoms[i], BP_Choices)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "bleeding":
            MsValue = st.selectbox(measuredSymptoms[i], Choices)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "convulsion":
            MsValue = st.selectbox(measuredSymptoms[i], Choices)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "headache":
            MsValue = st.selectbox(measuredSymptoms[i], three_Choices)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "blurredvision":
            MsValue = st.selectbox(measuredSymptoms[i], Choices)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "abdominalPain":
            MsValue = st.selectbox(measuredSymptoms[i], abdominalPain_Choices)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "proteinuria":
            MsValue = st.selectbox(measuredSymptoms[i], proteinuria_Choices)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "temprature":
            MsValue = st.selectbox(measuredSymptoms[i], Temp_Choices)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "weakeness":
            MsValue = st.selectbox(measuredSymptoms[i], numbeofWeeks)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "backpain":
            MsValue = st.selectbox(measuredSymptoms[i], Choices)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "breathingDifficulty":
            MsValue = st.selectbox(measuredSymptoms[i], numbeofWeeks)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "swollenPainfulCalf":
            MsValue = st.selectbox(measuredSymptoms[i], numbeofWeeks)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "vaginalBleeding":
            MsValue = st.selectbox(measuredSymptoms[i], vaginalBleeding_Choices)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "decrease_or_absentof_fetalMovement":
            MsValue = st.selectbox(measuredSymptoms[i], numbeofWeeks)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "painfulContractionLessthan37wks":
            MsValue = st.selectbox(measuredSymptoms[i], numbeofWeeks)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "suddenGushofClear_or_pale":
            MsValue = st.selectbox(measuredSymptoms[i], numbeofWeeks)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "cervical":
            MsValue = st.selectbox(measuredSymptoms[i], numbeofWeeks)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "chorioamnionitis":
            MsValue = st.selectbox(measuredSymptoms[i], numbeofWeeks)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "pain":
            MsValue = st.selectbox(measuredSymptoms[i], numbeofWeeks)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "vaginaldischarge":
            MsValue = st.selectbox(measuredSymptoms[i], vaginaldischarge_Choices)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "rh_negative":
            MsValue = st.selectbox(measuredSymptoms[i], numbeofWeeks)
            filteringListValues[measuredSymptoms[i]] = MsValue
        elif measuredSymptoms[i] == "pulse":
            MsValue = st.selectbox(measuredSymptoms[i], Pulse_Choices)
            filteringListValues[measuredSymptoms[i]] = MsValue
        else:
            st.warning("A valid measured symptoms must be selected")
    # st.write("Measured Symptom Value:", filteringListValues)

    return filteringListValues


def clinicalPathway_processing_wizard():
    # intialize the generated CP list
    Generated_CP_LIST = pd.DataFrame(
        {'Measured_Symptoms': [],
         'Urgent_Attention': '',
         'Generated_CP': [],
         'Finding': [],
         'Mgmt_and_Suggestions': [],
         'Evidence': []})
    ###
    # Call, showindicator() function to visualize the indicators
    clinicalPathways_Indicator = showCG_Indicators.clinicalPathways_Indicator()
    # Call all the knowledge based indicators
    indicators = {
        'urgentIndicators': {0: clinicalPathways_Indicator.get_urgentAttention_indicators()},
        'referralIndicators': {
            0: clinicalPathways_Indicator.get_Convulsion_R_indicator(),
            1: clinicalPathways_Indicator.get_severe_Pre_eclampsia_R_indicator(),
            2: clinicalPathways_Indicator.get_severe_hypertension_R_indicator(),
            3: clinicalPathways_Indicator.get_vaginalBleeding_R_indicator(),
            4: clinicalPathways_Indicator.get_pretermLabour_R_indicator(),
            5: clinicalPathways_Indicator.get_PROM_R_indicator(),
            6: clinicalPathways_Indicator.get_unsurePregnancy_R_indicator(),
        },
        'treatableIndicators': {
            0: clinicalPathways_Indicator.get_Convulsion_T_indicator(),
            1: clinicalPathways_Indicator.get_vaginalBleeding_T_indicator(),
            2: clinicalPathways_Indicator.get_pretermLabour_T_indicator(),
            # 3:clinicalPathways_Indicator.get_notUrgentAttention_T_indicator(),
            3: clinicalPathways_Indicator.get_unsurePregnancy_T_indicator(),
        }
    }

    ####
    age, symptomsList = PregnancyEntry()
    Next = st.checkbox("Next")

    if Next and age >= 15 and age <= 49:
        recordNumber = st.text_input("Enter the medical record number", max_chars=10)
        with st.expander(label="Step - I: Accept the pregnant patient measured signs and symptoms"):
            # get evidence for the pregant patient
            evdOptionList = get_the_pregnant_patient_evidence(symptomsList)
            # get evidence for the pregant patient
            measuredSymptoms = st.multiselect("Select measured symptoms from the list:",
                                              symptomsList, default=evdOptionList)
            st.write("Measured Symptoms:", measuredSymptoms)

        with st.expander(label="Step - II: Checking and validating the value of measured symptoms"):
            filteringListValues = Quantize_MeasuredSymptoms(age, measuredSymptoms)

        # Check urgent attention is required based on the measuredSymptoms sysmptoms
        urgentMS, UrgentBP = urgent_attention_MS_indicators.CG_urgent_attention_MS_indicators()

        if len(filteringListValues) == 0:
            st.info("Fill out the above measured symptoms to proceed with the pregnant patient's clinical pathways or provide normal antenatal care to the pregnant patient who does not necessitate attention.")

        elif len(filteringListValues) != 0 and filteringListValues.items() <= urgentMS.items() or UrgentBP.items() <= filteringListValues.items():
            # A path for urgent attention is fullfilled
            with st.expander(label="Step - III: The Pregnant Patient Generated Clinical Pathways. Give urgent attention to the pregnant patient, one or more of the following measured symptoms appear. "):
                presentedMeasuredSymptoms = processing_Measured_Symptoms.processing_Measured_Symptoms(
                    filteringListValues)
                # execute if there is any urgent conditions
                Generated_CP_LIST = cp_Processing.execute_clincalPathways(
                    Generated_CP_LIST, presentedMeasuredSymptoms)

                st.success("Generated CPs")
                st.write("Number of Generated CPs: ", len(Generated_CP_LIST))

                ###############################################################
                # Call and Get managment and sugession module to retreview the mangament and susgession based on the finding and measured symptoms
                Generated_CP_LIST = Mgmt_and_Suggestions.get_CG_Managament_and_Suggestions(
                    Generated_CP_LIST)

                ###############################################################

                showGCPS = st.checkbox("Generated CPs Details")
                if showGCPS:
                    st.write(Generated_CP_LIST)

                st.success("Process and Prune the Generated CPs")
                msdf = cp_tools.Transform_DictValue_to_df(Generated_CP_LIST)
                # st.write("msdf", msdf)
                cpdf = cp_tools.filiter_proceed_cpdf(Generated_CP_LIST)
                # st.write("cpdf", cpdf)
                generatedCP_dataframe = cp_tools.mergeProceed_msDF_and_cpDF(msdf, cpdf)
                showALL = st.checkbox("Show All Generated CPs")
                if showALL:
                    # st.write("Processed Generated CPs", generatedCP_dataframe.sort_values(
                    #    'Generated_CP', ascending='True'))
                    generatedCP_dataframe = generatedCP_dataframe.sort_values(
                        'Generated_CP', ascending='True')
                    st.write(generatedCP_dataframe.style.apply(
                        cp_tools.highlight_generated_CPs, axis=1))

                # find duplicate rows
                # Selecting duplicate rows except first
                # occurrence based on all columns
                # duplicate = generatedCP_dataframe[~generatedCP_dataframe.duplicated()]
                df2 = cp_tools.reterive_unquie_CPs(generatedCP_dataframe)
                # Print the resultant Dataframe
                st.write("A total of ", len(generatedCP_dataframe),
                         "CPs are generated", len(df2), "unique CPs")
                st.write("Summarize CPs ")
                df2 = df2.sort_values('Generated_CP', ascending='False')
                st.write(df2.style.apply(cp_tools.highlight_generated_CPs, axis=1))
                st.info("Prune the generated CPs")
                prunedCP_DF = cp_pruning.cp_pruning(df2)

            # Endrose and Save the Clinical Pathways based on GP/Nurse Prefernce
            with st.expander(label="Step - IV: Select and endrose the pregnant patient clinical pathways"):
                # Sample
                ThePregnantPatient_Endrosed_Path = "/Users/geletawsahle/Desktop/CP_WorkFlow_DP_2022/ThePregnantPatient_EndrosedCPs.pkl"

                endrosed_CPs = cp_endrosment.cp_endrosement_and_exit(prunedCP_DF, df2)
                if 'Finding' not in endrosed_CPs.columns or len(endrosed_CPs) == 0:
                    endrosed_CPs['Finding'] = ''
                    st.error("The selection or endorsement of CPs has not yet happened.")

                    # if len(endrosed_CPs) == 0:
                    #    st.warning("There is no endrosed or selected CPs")
                else:
                    # automatically plot and fill the ANC routine card
                    # st.write(endrosed_CPs)
                    if st.button('Save Endrosed CPs'):
                        cp_tools.save_endrosed_cps(
                            ThePregnantPatient_Endrosed_Path, endrosed_CPs, "Saved_Endrosed_CPS")
                        st.success("The endrosed CP is saved for future reference. Thank you for making use of the CP POC instrument. For pregnancy/ANC/PNC routine support, I,  CP POC-INSTRUMENT feel you get the finest evidence and support.")

        else:
            # path for non urgent attention basd on the clinical guidelines
            with st.expander(label="Step - III: Approach to the newly diagnosed pregnant patient not needing urgent attention"):
                pregResponse = st.selectbox("Does the patient want the pregnancy?", [
                    "No or unsure", "Yes"])
                if pregResponse == "No or unsure":
                    result = st.checkbox(
                        "Discuss the options around continuing with pregnancy, choosing adoption or abortion. Refer to social worker.")
                    ga = st.checkbox(
                        "Determine gestational age by dates and on examination. If unable to determine gestational age, arrange ultrasound.")
                    if ga:
                        weeks = st.selectbox("GA", ['< 12 weeks', '≥ 12 weeks'])
                    if ga and result:
                        dResult = st.selectbox("Discussion result", [
                            'Patient requests abortion', 'Patient decides to continue with pregnancy'])
                        if dResult == 'Patient requests abortion':
                            ask_further_info = st.selectbox(
                                "Any one of < 18 years old, pregnant following incest or rape, severe mental illness or congenital malformation?", ['Yes', 'No'])
                            if ask_further_info == 'Yes':
                                if weeks == '< 12 weeks':
                                    st.checkbox("Do MVA or provide medical abortion")
                                elif weeks == '≥ 12 weeks':
                                    st.checkbox("Refer to hospital for TOP")
                                else:
                                    st.checkbox("Discuss future contraception  110")
                            elif ask_further_info == 'No':
                                st.info("Based on the information, here is the options")
                                st.checkbox("Abortion is not an option")
                                st.checkbox("Discuss possibility of adoption")
                                st.checkbox("Give routine antenatal care.")
                            else:
                                st.write("Please choice appropirate information")
                        elif dResult == 'Patient decides to continue with pregnancy':
                            st.write("")
                else:
                    st.info(
                        "Give routine antenatal care in health centre 114. Since,not needing referral level antenatal care")
            if pregResponse == "Yes":
                anc_care_workflow.anc_main()
