import streamlit as st
import pandas as pd
import numpy as np
import sqlite3


# Security
# passlib,hashlib,bcrypt,scrypt
import hashlib

# import the defn. CG based indicators used as gold standard
import showCG_Indicators
import anc_CG_Indicators
import pnc_CG_Indicators

# import Knowledge based ruels
import getPregnantPatientRules

# import the pregnant patient workflow
import pregnantPatient_Workflow

# import anc workflow
import anc_care_workflow

# import pnc workflow
import pnc_care_workflow

# import CP tools module
import cp_tools


def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


# DB Management
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions


def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username, password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (username, password))
    conn.commit()


def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data


def show_CG_KB_Indicators():
        # KB rules for pregnancy
    with st.expander(label="The Pregnant Patient Indicators and Managment CG-KB rules"):
        showRules = ["Indicators", "CG-KB Managment & Rules"]
        showRulesandIndicators = st.radio("", showRules)
        st.write(
            '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        if showRulesandIndicators == "Indicators":
            showCG_Indicators.showIndicator()
        elif showRulesandIndicators == "CG-KB Managment & Rules":
            st.success("The Pregnant Patient Managment KB Rules")
            getPregnantPatientRules.Visualize_Preg_KB_rules()
        else:
            st.warning("Please select to visualize")

    with st.expander(label="ANC Indicators and Managment CG-KB rules"):
        st.success("The ANC Managment KB Rules and Indicators")
        anc_CG_Indicators.show_ANC_indicators()

    with st.expander(label="PNC Indicators and Managment CG-KB rules"):
        st.write("The PNC Managment KB Rules and Indicators")
        pnc_CG_Indicators.show_PNC_indicators()


def main():
    """CP Login App"""

    st.success("CP4LRS: Automated & interactive point of care CP workflow and data processing instrument")

    menu = ["Home", "Indicators", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        # st.success("CP-POC data processing")
        st.write("CP-POC instrument performance metrics")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Total referral", value="r %", delta="x.x %")
            st.metric(label="Total treatable at the HC", value="r %", delta="r %")
        with col2:
            st.metric(label="Reduce unncessary referal", value="ur %", delta="x.x %")
            st.metric(label="Reduce delay", value="d %", delta="r %")
        with col3:
            st.metric(label="Document completion rate", value="dc %", delta="dc %")
            st.metric(label="Promote evidence", value="e %", delta="e %")
        st.info("If you already have a user name, please login to evaluate and validate the system; otherwise, sign up and create a user name from the sidebar menu on the left.")
    elif choice == "Indicators":
        # pregnantPatient_Workflow.pregnant_Patient_Workflow_wizard()
        show_CG_KB_Indicators()

    elif choice == "Login":
        # st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("Login"):
            # if password == '12345':
            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(username, check_hashes(password, hashed_pswd))
            if result:

                # st.success("User: {}".format(username))

                task = st.selectbox("Welcom user: {} , please choose to continue.".format(username), [
                                    "The pregnant patient", "ANC", "PNC",
                                    "View CG Indicators",
                                    "View Endrosed CPs",
                                    "View Users"])
                if task == "The pregnant patient":
                    st.success(
                        "You are at {}  workflow and data processing".format(task))
                    # pregnantPatient_Workflow.PregnancyEntry()
                    pregnantPatient_Workflow.clinicalPathway_processing_wizard()

                elif task == "View CG Indicators":
                    options = ['The pregnant patient indicators',
                               'ANC indicators', 'PNC indicators']
                    # making the orientaiton horizontal
                    st.write(
                        '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                    selectOptions = st.radio(" ", options)
                    if selectOptions == 'ANC indicators':
                        anc_CG_Indicators.show_ANC_indicators()
                    elif selectOptions == 'PNC indicators':
                        pnc_CG_Indicators.show_PNC_indicators()
                    else:
                        showCG_Indicators.showIndicator()
                elif task == "ANC":
                    st.success(
                        "You are at {}  workflow and data processing".format(task))
                    anc_care_workflow.anc_main()

                elif task == "PNC":
                    st.success(
                        "You are at {}  workflow and data processing".format(task))
                    pnc_care_workflow.pnc_main()
                elif task == "View Users":
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(user_result, columns=["Username", "Password"])
                    st.dataframe(clean_db)
                elif task == "View Endrosed CPs":
                    viewCP_options = st.selectbox("Which CP is the historical record you're looking for ?",
                                                  ["", "The pregnant patient CPs", "ANC CPs", "PNC CPs"])
                    if viewCP_options == "The pregnant patient CPs":
                        # get the endrosed cp current directory
                        current_directory = cp_tools.get_current_working_diretory()
                        filename = "/ThePregnantPatient_EndrosedCPs.pkl"
                        # merge the file name to get the full paths
                        ThePregnantPatient_Endrosed_Path = current_directory + filename
                        # ThePregnantPatient_Endrosed_Path = "/Users/geletawsahle/Desktop/CP_WorkFlow_DP_2022/ThePregnantPatient_EndrosedCPs.pkl"
                        getPregnantPatient_evidence_and_factors = cp_tools.read_endrosed_cps(
                            ThePregnantPatient_Endrosed_Path)

                        # filter by frequency of occurrence
                        value = st.selectbox(
                            "Filtered by frequency of occurrence:", range(1, 20))
                        filtered_Result = cp_tools.fliter_evidence_or_factors(
                            getPregnantPatient_evidence_and_factors, value)
                        st.write("Reterived endrosed CPs", filtered_Result)

                        # view factors from pregnant patient endrosed tables
                        viewPregnantPatient_evidence_and_factors = cp_tools.access_evidence(
                            viewCP_options, filtered_Result)
                        viewPregEvidenFactors = st.checkbox(
                            "View the pregnant patient evidence and factors")
                        if viewPregEvidenFactors:
                            # reterive only selected elements
                            st.info("Evidence and Factors")
                            st.write(
                                "A list of factors that has been saved at least once in the endrosed CP databse")
                            st.write(viewPregnantPatient_evidence_and_factors.columns.tolist())

                    elif viewCP_options == "ANC CPs":
                        # get the endrosed cp current directory
                        current_directory = cp_tools.get_current_working_diretory()
                        filename = "/ANC_EndrosedCPs.pkl"
                        # merge the file name to get the full paths
                        ANC_Endrosed_Path = current_directory + filename
                        # ANC_Endrosed_Path = "/Users/geletawsahle/Desktop/CP_WorkFlow_DP_2022/ANC_EndrosedCPs.pkl"
                        getANC_evidence_and_factors = cp_tools.read_endrosed_cps(ANC_Endrosed_Path)

                        # filter by frequency of occurrence
                        value = st.selectbox(
                            "Filtered by frequency of occurrence:", range(1, 20))
                        filtered_Result = cp_tools.fliter_evidence_or_factors(
                            getANC_evidence_and_factors, value)
                        st.write("Reterived endrosed CPs", filtered_Result)

                        # view factors from pregnant patient endrosed tables
                        viewPregnantPatient_evidence_and_factors = cp_tools.access_evidence(
                            viewCP_options, filtered_Result)
                        # reterive only selected elements
                        viewANCEvidenFactors = st.checkbox(
                            "View the ANC evidence and factors")
                        if viewANCEvidenFactors:
                            st.info("Evidence and Factors")
                            st.write(
                                "A list of factors that has been saved at least once in the endrosed CP databse")
                            st.write(viewPregnantPatient_evidence_and_factors.columns.tolist())
                    elif viewCP_options == "PNC CPs":
                        # get the endrosed cp current directory
                        current_directory = cp_tools.get_current_working_diretory()
                        filename = "/PNC_EndrosedCPs.pkl"
                        # merge the file name to get the full paths
                        PNC_Endrosed_Path = current_directory + filename
                        # PNC_Endrosed_Path = "/Users/geletawsahle/Desktop/CP_WorkFlow_DP_2022/PNC_EndrosedCPs.pkl"
                        getPNC_evidence_and_factors = cp_tools.read_endrosed_cps(PNC_Endrosed_Path)
                        # view factors from PNC endrosed tables
                        # filter by frequency of occurrence
                        value = st.selectbox(
                            "Filtered by frequency of occurrence:", range(1, 20))
                        filtered_Result = cp_tools.fliter_evidence_or_factors(
                            getPNC_evidence_and_factors, value)
                        st.write("Reterived endrosed CPs", filtered_Result)

                        # view factors from pregnant patient endrosed tables
                        viewPregnantPatient_evidence_and_factors = cp_tools.access_evidence(
                            viewCP_options, filtered_Result)
                        # reterive only selected elements
                        viewPNCEvidenFactors = st.checkbox(
                            "View the PNC evidence and factors")
                        if viewPNCEvidenFactors:
                            st.info("Evidence and Factors")
                            st.write(
                                "A list of factors that has been saved at least once in the endrosed CP databse")
                            st.write(viewPregnantPatient_evidence_and_factors.columns.tolist())
            else:
                st.warning("Incorrect Username/Password")

    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user, make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")


if __name__ == '__main__':
    main()

    hide_streamlit_style = """
                <style>
                # MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                footer:after {
                    content:'Powered by ETRO-VUB, JU, and NASCERE';
    	            visibility: visible;
    	            display: block;
    	            position: relative;
    	            # background-color: red;
    	            padding: 5px;
    	            top: 2px;
                }

                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
