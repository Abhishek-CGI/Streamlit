import streamlit as st
from Pages import Home,Bank_Marketing,Banking_Analytics_Bundle,Consumer_Financial_Protection_Bureau_Analysis,Demographics_Data_Bundle,Electric_Vehicle_Trends,Federal_Exchange_Rates,Federal_Financial_Institutions_Package,Global_Landslide_Catalog_Export,Indicators_of_Health_Insurance_Coverage_at_the_Time_of_Interview,Layoff_Data,Lottery_Mega_Millions_Winning_Numbers,National_Credit_Union_Administration,SEC_Analytics

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
        selected_friend = st.sidebar.selectbox("Select Bank Marketing Dataset", ["FDIC", "Fred_Financial_Labor_Performance", "Fred_Interest_rate_data", "fred_unemployement_rate"])
        Bank_Marketing.show(selected_friend)
    elif selected_page == "Banking Analytics Bundle":
        selected_friend = st.sidebar.selectbox("Select Banking Analytics Bundle Dataset", ["FDIC", "Fred_Financial_Labor_Performance", "Fred_Interest_rate_data", "fred_unemployement_rate"])
        Banking_Analytics_Bundle.show(selected_friend)
    elif selected_page == "Consumer Financial Protection Bureau Analysis":
        selected_pet = st.sidebar.selectbox("Select Consumer Financial Protection Bureau Analysis Dataset", ["sec"])
        sec.show(selected_pet)
    elif selected_page == "Demographics Data Bundle":
        selected_pet = st.sidebar.selectbox("Select Demographics Data Bundle", ["sec"])
        sec.show(selected_pet)
    elif selected_page == "Electric Vehicle Trends":
        selected_pet = st.sidebar.selectbox("Select Electric Vehicle Trends", ["sec"])
        sec.show(selected_pet)
    elif selected_page == "Federal Exchange Rates":
        selected_pet = st.sidebar.selectbox("Select Federal Exchange Rates", ["sec"])
        sec.show(selected_pet)
    elif selected_page == "Federal Financial Institutions Package":
        selected_pet = st.sidebar.selectbox("Select Federal Financial Institutions Package", ["sec"])
        sec.show(selected_pet)
    elif selected_page == "Indicators of Health Insurance Coverage at the Time of Interview":
        selected_pet = st.sidebar.selectbox("Select Indicators of Health Insurance Coverage at the Time of Interview", ["sec"])
        sec.show(selected_pet)
    elif selected_page == "Layoff Data":
        selected_pet = st.sidebar.selectbox("Select Layoff Data", ["sec"])
        sec.show(selected_pet)
    elif selected_page == "Lottery Mega Millions Winning Numbers":
        selected_pet = st.sidebar.selectbox("Select Lottery Mega Millions Winning Numbers", ["sec"])
        sec.show(selected_pet)
    elif selected_page == "National Credit Union Administration":
        selected_pet = st.sidebar.selectbox("Select National Credit Union Administration", ["sec"])
        sec.show(selected_pet)
    elif selected_page == "SEC Analytics":
        selected_pet = st.sidebar.selectbox("Select SEC Analytics", ["sec"])
        sec.show(selected_pet)


if __name__ == "__main__":
    main()
