
import streamlit as st
import cp_tools
import generate_cp_graph


def cp_endrosement_and_exit(prunedCP_DF, df2, *args):

    selected_indices = st.multiselect(
        'Select Endrosed Paths:', prunedCP_DF.index)
    selected_rows = df2.loc[selected_indices]
    # drop columns with all empty or nan values
    # st.write(selected_rows.columns)
    selected_rows = selected_rows.dropna(axis=1, how='all', inplace=False)
    st.write("Endrosed CPs for the measured symptoms:")
    st.write(selected_rows.style.apply(cp_tools.highlight_generated_CPs, axis=1))

    # downloadTable = cp_tools.get_table_download_link(selected_rows)

    # selected_rows.to_csv("/Users/geletawsahle/Desktop/CP_WorkFlow_DP_2022/EndrosedCPs.csv")

    # generate graph
    viewinGraph = st.checkbox("CPGraph: Visualize endrosed CPs")
    if viewinGraph:
        generate_cp_graph.generate_cp_graph(selected_rows)
    if not selected_indices:
        st.warning("Please choose the suitable evidence and CPs from the evidence/concordance table.")
    else:
        st.success("You are successully finalized and endrose {} generated CPs.".format(
            len(selected_rows)))

    return selected_rows
