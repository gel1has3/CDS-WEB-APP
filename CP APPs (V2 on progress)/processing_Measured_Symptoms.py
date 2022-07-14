import streamlit as st
from itertools import combinations


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


def processing_Measured_Symptoms(MS):
    Possiblecombinations = []
    nestedList = {}
    nestedList = possible_SignsandSymptoms_Combinations(MS, Possiblecombinations)
    possibleComb = {}
    Measured_Symptoms_List = comibnationofParam(MS, nestedList, possibleComb)
    workflowInput = st.select_slider(
        "Input: Measured Symptoms", ["MS",
                                     "Processed MS",
                                     "MS Output"])

    if workflowInput == "MS":
        # processing_Measured_Symptoms(filteringListValues)
        st.write(MS)

    elif workflowInput == "Processed MS":
        st.write("A total of ",
                 len(MS),
                 "measured symptoms,and ",
                 len(Measured_Symptoms_List),
                 "possible combinations for exploring CPs")
        # st.write("Based on:", filteringListValues)
    else:
        hide = st.checkbox("Show Details")
        if hide:
            st.write(Measured_Symptoms_List)

    return Measured_Symptoms_List
