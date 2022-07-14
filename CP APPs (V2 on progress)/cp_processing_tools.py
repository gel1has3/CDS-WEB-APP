import cp_tools
import streamlit as st
import cp_pruning


def cp_processing_tools(Generated_CP_LIST):
    """
    A function to proceed the prunning, merging and reterving uniques CPS
    """
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

    return prunedCP_DF, df2
