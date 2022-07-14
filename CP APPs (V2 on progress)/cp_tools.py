import pandas as pd
import base64
import streamlit as st
import os
from st_aggrid import AgGrid
# for-  Columns can be pinned, grouped and aggregated
from st_aggrid.grid_options_builder import GridOptionsBuilder


def get_current_working_diretory():
    """
    Getting the current working directory
    """
    current_directory = os.getcwd()
    return current_directory


def fliter_evidence_or_factors(getfliteredDF, cut_off_value):
    """
    Filter the result using frequency from endrosed tables
    """
    filtered_result_DF = getfliteredDF[getfliteredDF['Generated_CP_Freq'] >= cut_off_value]
    # filtered_result_DF = filtered_result_DF[filtered_result_DF.isnull(how='all')]
    return filtered_result_DF


def access_evidence(category, endrosedDF):
    """
    A function to trace evidences from the table
    """
    if category == "The pregnant patient CPs":
        getEvidence = endrosedDF.loc[:, ~endrosedDF.columns.isin(
            ['Urgent_Attention', 'Generated_CP', 'Finding', 'Mgmt_and_Suggestions', 'Generated_CP_Freq'])]
        return getEvidence
    elif category == "ANC CPs":
        getEvidence = endrosedDF.loc[:, ~endrosedDF.columns.isin(
            ['Urgent_Attention', 'Generated_CP', 'Finding', 'Mgmt_and_Suggestions', 'Generated_CP_Freq'])]
        return getEvidence
    elif category == "PNC CPs":
        getEvidence = endrosedDF.loc[:, ~endrosedDF.columns.isin(
            ['Urgent_Attention', 'Generated_CP', 'Finding', 'Mgmt_and_Suggestions', 'Generated_CP_Freq'])]
        return getEvidence
    else:
        getEvidence = 'No evidence available'
        return getEvidence


def read_endrosed_cps(Endrosed_Path):
    Saved_PNC_Endrosed_CPS = pd.read_pickle(Endrosed_Path)
    if os.path.exists(Endrosed_Path):
        # st.write("Reterived endrosed CPs", Saved_PNC_Endrosed_CPS)
        return Saved_PNC_Endrosed_CPS
    else:
        st.error("There is no avilable endrosed pathways")


def save_endrosed_cps(Endrosed_File_Path, endrosed_CPs, Saved_Endrosed_CPS):
    """
    This function helps to save the endrosed CP in to file or databse
    """
    if os.path.exists(Endrosed_File_Path):
        # Saved_PNC_Endrosed_CPS = pd. read_pickle(PNC_Endrosed_Path)
        Saved_Endrosed_CPS = pd.read_pickle(Endrosed_File_Path)
        # overwrite
        Saved_Endrosed_CPS.append(endrosed_CPs).to_pickle(Endrosed_File_Path)

    else:
        endrosed_CPs.to_pickle(Endrosed_File_Path)
    return Saved_Endrosed_CPS


def filter_endrosed_CPs(endrosed_CPs, value):
    return endrosed_CPs.loc[endrosed_CPs['Finding'] == value]


def filiter_proceed_cpdf(Generated_CP_LIST):
    cpdf = Generated_CP_LIST.filter(
        ['Urgent_Attention', 'Generated_CP', 'Finding', 'Mgmt_and_Suggestions'], axis=1)
    return cpdf

# merge the ms data frames and proceess data frames


def mergeProceed_msDF_and_cpDF(msdf, cpdf):
    concat_result = pd.concat([msdf, cpdf], sort=False, axis=1)
    concat_result.fillna('', inplace=True)
    return concat_result

# reterive unquie CP columns


def reterive_unquie_CPs(df):
    cols = df.columns.tolist()
    df1 = df
    df1['Generated_CP_Freq'] = 1
    df2 = df1.groupby(cols).Generated_CP_Freq.count().reset_index()
    return df2
############################################################

############################################################


def highlight_generated_CPs(df):
    noofColumns = len(df)
    if df.Generated_CP == "R":
        return ['background-color: #FF6347']*noofColumns
    elif df.Generated_CP == "T":
        return ['background-color: lightgreen']*noofColumns
    else:
        return ['background-color: yellow']*noofColumns


def Transform_DictValue_to_df(Generated_CP_LIST):
    msdf = pd.DataFrame()
    for i in range(0, len(Generated_CP_LIST['Measured_Symptoms'])):
        xx = pd.DataFrame([Generated_CP_LIST['Measured_Symptoms'][i]])
        msdf = msdf.append(xx, 'sort=True')
    return msdf


def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(csv.encode()).decode()
    # href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    href = f'<a href="data:file/csv;base64,{b64}" download="endrosedCP.csv">Save CP: CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)


def return_rules_asTable(selectedRules, finding='finding'):
    """
    A function to retrun the managment and suggestions KB rules as  a table
    """
    # create run-time only managment and sugesstions data frame
    Mgmt_and_Suggestions_DF = pd.DataFrame(columns=['Path_ID', 'Finding', 'Mgmt_and_Suggestions'])

    for value in range(0, len(selectedRules)):
        Mgmt_and_Suggestions_DF = Mgmt_and_Suggestions_DF.append(
            {
                'Path_ID': selectedRules[value][0],
                'Finding': finding,
                'Mgmt_and_Suggestions': selectedRules[value][1],
            },
            ignore_index=True)
    # set option layout for display
    options = ["Table", "Interactive", "Selectable"]
    # making the orientaiton horizontal
    st.write(
        '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    selectedRadio = st.radio("", options)
    if selectedRadio == "Interactive":
        # AgGrid(Mgmt_and_Suggestions_DF)
        selected = create_interactive_df(Mgmt_and_Suggestions_DF)
        st.write(selected)
    elif selectedRadio == "Selectable":
        values = st.multiselect("Available managment & sugesstions for {}".format(finding),
                                Mgmt_and_Suggestions_DF['Mgmt_and_Suggestions'],
                                )
        st.write("Prescribed managment & sugesstions for {}".format(finding), values)
    else:
        Mgmt_and_Suggestions_DF = Mgmt_and_Suggestions_DF.style.set_properties(
            **{'text-align': 'left'})
        st.table(Mgmt_and_Suggestions_DF)


def create_interactive_df(data):
    """
    A function to create an interactive and seelectable dataframe
    """
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True)  # Add pagination
    gb.configure_side_bar()  # Add a sidebar
    gb.configure_selection('multiple', use_checkbox=True,
                           groupSelectsChildren="Group checkbox select children")  # Enable multi-row selection
    gridOptions = gb.build()

    grid_response = AgGrid(
        data,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT',
        update_mode='MODEL_CHANGED',
        fit_columns_on_grid_load=False,
        theme='blue',  # Add theme color to the table
        enable_enterprise_modules=True,
        height=350,
        # width='100%',
        reload_data=True
    )

    data = grid_response['data']
    selected = grid_response['selected_rows']
    df = pd.DataFrame(selected)  # Pass the selected rows to a new dataframe df
    return df
