import streamlit as st

from itertools import combinations

import pandas as pd

# import the defn. CG based indicators
import showCG_Indicators

# import managment and sugession for the finding
import Mgmt_and_Suggestions

# Import pickle Package, to reterive the saved CP model
import pickle
import os.path

# importing label encoder libraries
from sklearn.preprocessing import LabelEncoder


# import libraries for the data-driven applications
from imblearn.combine import SMOTETomek
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB

from collections import Counter

# sugesstions and recommendations
import pregnantPatientRecommendations
getRecommendations = pregnantPatientRecommendations.explore_managmenet_and_recommendations()

# Input - List of the presented signs and symptoms
Measured_Signs_and_Symptoms_List = {}


#    Potential list of signs and symptoms hasextracted from the CGs (Endorsed by WHO,
#    Ministry of Health and a group of experts)
Potential_List_of_Signs_and_Symptoms = {}

#     An indicator (or criteria) extracted from the CGs (Expert Opinion).
#     Its used to check whether the measured symptoms satisfy the condition or not.
#     Also, used as an EXIT criteria
Indicator = {}


#    Output -  A list of generated CP

Generated_CP_LIST = {}

#  A list of parameters for ranking CP """
RankingParameters = {'Probability', 'Severity', 'Cost', 'Weight', 'Evidence'}

# A list of pruning parameters """
PruningParameters = {'Probability', 'Severity', 'Cost', 'Weight', 'Evidence'}

Flag = False


# A function to generate possible combinations of signs and symptoms: the function will return both indvidual
#        measured sysmptoms and possible combinations of measrued Symptoms
Possiblecombinations = []
nestedList = {}


def possible_SignsandSymptoms_Combinations(value, Possiblecombinations):
    # the value is the list of measured symptoms
    noOFmeasuredSymptoms = len(value)
    for j in range(1, noOFmeasuredSymptoms+1):
        comb = combinations(value, j)
        for i in list(comb):
            Possiblecombinations.append(i)
    return Possiblecombinations


#    iterate over the generated combination of measured parameters nested list for indexing and validating
#    the value of each combination of measured parameters for CP generation


def comibnationofParam(MS, nestedList, possibleComb):
    # iterate the generated combination of possible parameters and generate CP
    i = 0  # used for indexing the dictionary
    for subList in nestedList:
        res = {i: {k: MS[k]
                   for k in subList}}
        # res = {i: {k: Measured_Signs_and_Symptoms_List['BPs']
        #           if k == 'BPz' else 'yes' for k in subList}}
        possibleComb.update(res)
        i = i+1
    return possibleComb  # return possible combination in Dictionary format


# Call, showindicator() function to visualize the indicators
clinicalPathways_Indicator = showCG_Indicators.clinicalPathways_Indicator()
# Call all the knowledge based CG indicators
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


# A Function for generating Clinical Pathways
def clinicalPathway_generator(Generated_CP_LIST, presentedMeasuredSymptoms, indicators, Urgent_Attention, CP, finding, Mgmt_and_Suggestions):
    #    Generate the clinical pathway based on the measured symptoms
    #    The indicators used for validating the measured symptoms and an exit criteria
    # presentedMeasuredSymptoms: list of measured and combination of measured symptoms
    for index in range(0, len(presentedMeasuredSymptoms)):
        # a dictionray list of indicators (used a gold standard for evalutation)
        for j in range(0, len(indicators)):
            # check exact matching, Exit Criteria
            if dict(indicators[j], **presentedMeasuredSymptoms[index]) == indicators[j]:
                # if presentedMeasuredSymptoms[index] == indicators[j]:

                # print(presentedMeasuredSymptoms[index])
                temp = presentedMeasuredSymptoms[index]

                # Trace the evidence from hisotry for the presentedMeasuredSymptoms[index]

                # generatedResult.append(presentedMeasuredSymptoms[index])
                result = pd.Series(data={'Measured_Symptoms': presentedMeasuredSymptoms[index],
                                         'Urgent_Attention': Urgent_Attention,
                                         'Generated_CP': CP,
                                         'Finding': finding,
                                         'Mgmt_and_Suggestions': Mgmt_and_Suggestions,
                                         'Evidence': '',
                                         'Prior_Prob': '',
                                         'Accuracy': '',
                                         'Pred_CP': '',
                                         'Severity': '', 'Cost': '', 'Weight': ''}, name=len(Generated_CP_LIST))
                Generated_CP_LIST = Generated_CP_LIST.append(result)
    return Generated_CP_LIST


# A function for executing clinical pathways


def execute_clincalPathways(Generated_CP_LIST, Measured_Symptoms_List):
    # Getting the measured symptoms list
    presentedMeasuredSymptoms = Measured_Symptoms_List

    # execute if there is any urgent conditions
    Generated_CP_LIST = clinicalPathway_generator(Generated_CP_LIST, presentedMeasuredSymptoms,
                                                  indicators['urgentIndicators'][0], Urgent_Attention='Yes', CP='NC', finding='UrgentAttention', Mgmt_and_Suggestions='')

    # execute referral clincal pathways
    for i in range(0, len(indicators['referralIndicators'])):
        if i == 0:
            Generated_CP_LIST = clinicalPathway_generator(
                Generated_CP_LIST, presentedMeasuredSymptoms, indicators['referralIndicators'][i], Urgent_Attention='Yes', CP='R', finding='Convulsion', Mgmt_and_Suggestions='')
        elif i == 1:
            Generated_CP_LIST = clinicalPathway_generator(
                Generated_CP_LIST, presentedMeasuredSymptoms, indicators['referralIndicators'][i], Urgent_Attention='Yes', CP='R', finding='severe_Pre_eclampsia', Mgmt_and_Suggestions='')
        elif i == 2:
            Generated_CP_LIST = clinicalPathway_generator(
                Generated_CP_LIST, presentedMeasuredSymptoms, indicators['referralIndicators'][i], Urgent_Attention='Yes', CP='R', finding='severe_hypertension', Mgmt_and_Suggestions='')
        elif i == 3:
            Generated_CP_LIST = clinicalPathway_generator(
                Generated_CP_LIST, presentedMeasuredSymptoms, indicators['referralIndicators'][i], Urgent_Attention='Yes', CP='R', finding='vaginalBleeding', Mgmt_and_Suggestions='')
        elif i == 4:
            Generated_CP_LIST = clinicalPathway_generator(
                Generated_CP_LIST, presentedMeasuredSymptoms, indicators['referralIndicators'][i], Urgent_Attention='Yes', CP='R', finding='pretermLabour', Mgmt_and_Suggestions='')
        elif i == 5:
            Generated_CP_LIST = clinicalPathway_generator(
                Generated_CP_LIST, presentedMeasuredSymptoms, indicators['referralIndicators'][i], Urgent_Attention='Yes', CP='R', finding='PROM', Mgmt_and_Suggestions='')
        elif i == 6:
            Generated_CP_LIST = clinicalPathway_generator(
                Generated_CP_LIST, presentedMeasuredSymptoms, indicators['referralIndicators'][i], Urgent_Attention='Yes', CP='R', finding='unsurePregnancy', Mgmt_and_Suggestions='')
        else:
            st.info("Most likely a previously unseen case and a case treated at the health center.")

    # execute treatable clinical pathways
    for t in range(0, len(indicators['treatableIndicators'])):
        if t == 0:
            Generated_CP_LIST = clinicalPathway_generator(
                Generated_CP_LIST, presentedMeasuredSymptoms, indicators['treatableIndicators'][t], Urgent_Attention='No', CP='T', finding='Convulsion', Mgmt_and_Suggestions='')
        elif t == 1:
            Generated_CP_LIST = clinicalPathway_generator(
                Generated_CP_LIST, presentedMeasuredSymptoms, indicators['treatableIndicators'][t], Urgent_Attention='No', CP='T', finding='vaginalBleeding', Mgmt_and_Suggestions='')
        elif t == 2:
            Generated_CP_LIST = clinicalPathway_generator(
                Generated_CP_LIST, presentedMeasuredSymptoms, indicators['treatableIndicators'][t], Urgent_Attention='No', CP='T', finding='pretermLabour', Mgmt_and_Suggestions='')
        # elif t == 3:
        #   Finding='notUrgentAttention'
        #   Generated_CP_LIST = cp_processingTest(Generated_CP_LIST, presentedMeasuredSymptoms, indicators['treatableIndicators'][t], Urgent_Attention='No',CP='T',finding=finding)
        elif t == 3:
            Generated_CP_LIST = clinicalPathway_generator(
                Generated_CP_LIST, presentedMeasuredSymptoms, indicators['treatableIndicators'][t], Urgent_Attention='No', CP='T', finding='unsurePregnancy', Mgmt_and_Suggestions='')
        else:
            st.info("Most likely a previously unseen case and a case treated at the health center.")

    # execute conisderation clinical pathways i.e. multi-disease clincal pathways

    return Generated_CP_LIST


########################################################################
"""
    Prunning based on different parameters
"""


def pruning(output):
    st.info("Preview Records")
    PruningParametersList = st.multiselect("Prunning with", output.columns)
    st.write("No. of Selected Prunning Criteria:", len(PruningParametersList))
    st.write("Details:", PruningParametersList)

    # Values for flitering
    PruningParametersListValues = {}
    for i in range(0, len(PruningParametersList)):
        MsValue = st.selectbox(PruningParametersList[i],
                               output[PruningParametersList[i]].unique())
        PruningParametersListValues[PruningParametersList[i]] = MsValue
    st.write("Flitering criteria with thier values:", PruningParametersListValues)
    return PruningParametersListValues


# filter the values based on the prunning parameters
def filter_dict(data, PruningParametersLValues, dic):
    return data.loc[data[list(PruningParametersLValues.keys())].isin(
        list(PruningParametersLValues.values())).all(axis=1), :]


########################################################################
"""
    The exact match between dynamically generated CP and data-driven CP and their variation.
"""


def viewCPwithEvidence(output):
    evdR = output.loc[(output['Evidence'] == 'Yes')]
    return evdR


def viewCPwithoutEvidence(output):
    evdR = output.loc[(output['Evidence'] != 'Yes')]
    return evdR


def variationAnalysis(output, KB_CP, DD_CP):
    evdR = output.loc[(output['Evidence'] >= 'Yes') & (
        output['Generated_CP'] == KB_CP) & (output['Pred_CP'] == DD_CP)]
    return evdR
########################################################################
########################################################################
# Tracing evidence from historical records


class TracingCP:

    def check_Evidence(pres, temp, *args):
        """

        """
        getColumnList = []
        """
            Retrieving the column name
        """
        for col in temp:
            getColumnList.append(col)
        """
            Check the retrieved column found in the existing record or not
        """
        if set(getColumnList).issubset(pres.columns):
            Flag = "Yes"
        else:
            Flag = "No"
        return Flag

    def load_clinicalPathways_model(*args):
        """
            Load the clinical pathway model back from file. The model was trained and saved in the file. The model is
            reterived for predciting and caculating the posterior probablity.
        """
        Pkl_Filename = "/Users/geletawsahle/Desktop/CP_2020_WEPAPP/Pickle_CP_Model.pkl"

        if os.path.exists(Pkl_Filename):
            try:
                with open(Pkl_Filename, 'rb') as file:
                    Pickled_CP_Model = pickle.load(file)
                return Pickled_CP_Model
            except EOFError:
                return "It's Empty Pickeled Model"

    def trace_and_predict_ProbabiliticCP(presented, *args):
        """
        """
        # Call the function to fill the missing values
        TracingCP.fill_missing_values(presented)

        # Encode the presented symptoms for calculating the probability and the target
        encoded_presented = presented.apply(LabelEncoder().fit_transform)
        # print(encoded_presented)

        # get the clinical pathway model
        ClinicalPathwayModel = TracingCP.load_clinicalPathways_model()

        # Predict using the
        y_pred = ClinicalPathwayModel.predict(encoded_presented)

        # Return the mean accuracy on the given test data and labels.
        # accuracy = ClinicalPathwayModel.score(X_test, y_test)
        accuracy = ClinicalPathwayModel.score(encoded_presented, y_pred)

        # get the priors
        priorClass = ClinicalPathwayModel.class_prior_

        # predictive probablities
        print("Pred_CP_Class:", y_pred,
              "Pred_Prob:", ClinicalPathwayModel.predict_proba(encoded_presented).mean(),
              "predict_log_proba:", ClinicalPathwayModel.predict_log_proba(
                  encoded_presented).mean(),
              "Accuracy:", accuracy)

        return y_pred, priorClass, accuracy

    def insert_unseen_measuredSymptoms(historicalRecords, *args):
        """
            This function aims to insert unseen measured symptoms into the healthcenter records.
            Append on the historical records for future tracing
        """
        historicalRecords = historicalRecords.append(
            Generated_CP_LIST['Measured_Symptoms'][i], ignore_index=True)

        # call, to update the save model using the new unseen records
        Update_CPModel.re_Train_CPModel(historicalRecords)

        return historicalRecords.shape

    def fill_missing_values(presented):
        # Fill the missing values
        for col in presented.columns:
            # replacing na values in college with No college
            presented[col].fillna("Notavailable", inplace=True)
        return presented
