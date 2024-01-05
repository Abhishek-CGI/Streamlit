import streamlit as st
from Pages import Bank_Marketing,Banking_Analytics_Bundle,Consumer_Financial_Protection_Bureau_Analysis,Demographics_Data_Bundle,Electric_Vehicle_Trends,Federal_Exchange_Rates,Federal_Financial_Institutions_Package,Global_Landslide_Catalog_Export,Indicators_of_Health_Insurance_Coverage_at_the_Time_of_Interview,Layoff_Data,Lottery_Mega_Millions_Winning_Numbers,National_Credit_Union_Administration,SEC_Analytics

# Main Streamlit app
def main():
    st.sidebar.title("Home")
    selected_page = st.sidebar.selectbox("Select", ["Bank Marketing",
                                                   "Banking Analytics Bundle",
                                                   "Consumer Financial Protection Bureau Analysis",
                                                   "Demographics Data Bundle",
                                                   "Electric Vehicle Trends",
                                                   "Federal Exchange Rates",
                                                   "Federal Financial Institutions Package",
                                                   "Global Landslide Catalog Export",
                                                   "Indicators of Health Insurance Coverage at the Time of Interview",
                                                   "Layoff Data",
                                                   "Lottery Mega Millions Winning Numbers",
                                                   "National Credit Union Administration",
                                                   "SEC Analytics",
                                                   "Home"])

    if selected_page == "Home":
        Home.show()
    elif selected_page == "Bank Marketing":
        selected_dataset = st.sidebar.selectbox("Select Bank Marketing Dataset", ["Bank_Churn_Customers"])
        Bank_Marketing.show(selected_dataset)
    elif selected_page == "Banking Analytics Bundle":
        selected_dataset = st.sidebar.selectbox("Select Banking Analytics Bundle Dataset", ["FDIC", "Fred_Financial_Labor_Performance", "Fred_Interest_rate_data", "Fred_unemployement_rate"])
        Banking_Analytics_Bundle.show(selected_dataset)
    elif selected_page == "Consumer Financial Protection Bureau Analysis":
        selected_dataset = st.sidebar.selectbox("Select Consumer Financial Protection Bureau Analysis Dataset", ["sec"])
        sec.show(selected_dataset)
    elif selected_page == "Demographics Data Bundle":
        selected_dataset = st.sidebar.selectbox("Select Demographics Data Bundle", ["Demographics_Statistics_By_Zip_Code"])
        sec.show(selected_dataset)
    elif selected_page == "Electric Vehicle Trends":
        selected_dataset = st.sidebar.selectbox("Select Electric Vehicle Trends", ["sec"])
        sec.show(selected_dataset)
    elif selected_page == "Federal Exchange Rates":
        selected_dataset = st.sidebar.selectbox("Select Federal Exchange Rates", ["sec"])
        sec.show(selected_dataset)
    elif selected_page == "Federal Financial Institutions Package":
        selected_dataset = st.sidebar.selectbox("Select Federal Financial Institutions Package", ["Federal_Deposit_Insurance_Corporation"])
        sec.show(selected_dataset)
    elif selected_page == "Indicators of Health Insurance Coverage at the Time of Interview":
        selected_dataset = st.sidebar.selectbox("Select Indicators of Health Insurance Coverage at the Time of Interview", ["Indicators_of_Health_Insurance_Coverage"])
        sec.show(selected_dataset)
    elif selected_page == "Layoff Data":
        selected_dataset = st.sidebar.selectbox("Select Layoff Data", ["Warn_Layoff_Data"])
        sec.show(selected_dataset)
    elif selected_page == "Lottery Mega Millions Winning Numbers":
        selected_dataset = st.sidebar.selectbox("Select Lottery Mega Millions Winning Numbers", ["Lottery_Mega_millions_winning_numbers","Lottery_NY_Lotto_Winning_Numbers","Lottery_powerball_Winning_Numbers"])
        sec.show(selected_dataset)
    elif selected_page == "National Credit Union Administration":
        selected_dataset = st.sidebar.selectbox("Select National Credit Union Administration", ["Credit_Union_Information"])
        sec.show(selected_dataset)
    elif selected_page == "SEC Analytics":
        selected_dataset = st.sidebar.selectbox("Select SEC Analytics", ["Sec"])
        sec.show(selected_dataset)


if __name__ == "__main__":
    main()
