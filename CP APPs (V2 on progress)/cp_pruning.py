import streamlit as st
import cp_tools


def cp_pruning(data):
    prunningParameters = ['Generated_CP', 'Urgent_Attention', 'Finding', "Generated_CP_Freq"]
    filteringList = st.multiselect("Prunning Parameters", prunningParameters)
    st.write("No. of Prunning Parameters:", len(filteringList))
    st.write("Details:", filteringList)

    # Values for flitering
    filteringListValues = {}
    for i in range(0, len(filteringList)):
        MsValue = st.selectbox(filteringList[i], data[filteringList[i]].unique())
        filteringListValues[filteringList[i]] = MsValue
    st.write("Chose prunning parameter /cut-off value:", filteringListValues)

    # Create your filtering function:

    def filter_dict(data, dic):
        return data.loc[data[list(filteringListValues.keys())].isin(list(filteringListValues.values())).all(axis=1), :]

    # Use it on your DataFrame:

    st.write("Prunned CPs...")
    prunnedDF = filter_dict(data, filteringListValues)
    st.write(prunnedDF.style.apply(cp_tools.highlight_generated_CPs, axis=1))
    return filter_dict(data, filteringListValues)
