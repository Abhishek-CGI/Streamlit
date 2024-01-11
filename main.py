import streamlit as st
from Pages.Home import Home
from Pages.Bank_Marketing import Bank_Churn_Customers,Bank_Marketing
from Pages.Banking_Analytics_Bundle import FDIC, Fred_Financial_Labor_Performance, Fred_Interest_rate_data, fred_unemployement_rate
from Pages.Consumer_Financial_Protection_Bureau_Analysis import Consumer_Financial_Protection_Bureau_Analysis
from Pages.Demographics_Data_Bundle import Demographics_Statistics_By_Zip_Code
from Pages.Electric_Vehicle_Trends import Electric_Vehicle_Trends
from Pages.Federal_Exchange_Rates import Federal_Exchange_Rates
from Pages.Federal_Financial_Institutions_Package import Federal_Deposit_Insurance_Corporation
from Pages.Global_Landslide_Catalog_Export import Nasa_Landslide_Data
from Pages.Indicators_of_Health_Insurance_Coverage_at_the_Time_of_Interview import Indicators_of_Health_Insurance_Coverage
from Pages.Layoff_Data import Warn_Layoff_Data
from Pages.Lottery_Mega_Millions_Winning_Numbers import Lottery_Mega_millions_winning_numbers,Lottery_NY_Lotto_Winning_Numbers,Lottery_powerball_Winning_Numbers
from Pages.National_Credit_Union_Administration import Credit_Union_Information
from Pages.SEC_Analytics import sec

# Main Streamlit app
def main():
    # Create two columns
    col1, col2 = st.sidebar.columns([1, 5])

# Add the logo to the first column
    col2.image("Pages/image/Insights by CG Infinity 1.png", width=150)

# Add the text to the second column
    col1.write(" ")
    # st.sidebar.title("Home")
    selected_page = st.sidebar.selectbox("Search for the Listing", ["Home",
                                                    "Bank Marketing",
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
                                                   ])



    if selected_page == "Home":
        selected_dataset = st.sidebar.selectbox("Go To", ["Home"])
        if selected_dataset == "Home":
            Home.show()
    elif selected_page == "Bank Marketing":
        selected_dataset = st.sidebar.selectbox("Select Bank Marketing Dataset", ["Bank_Churn_Customers","Bank_Marketing"])
        if selected_dataset == "Bank_Churn_Customers":
            Bank_Churn_Customers.show()
        elif selected_dataset == "Bank_Marketing":
            Bank_Marketing.show()
    elif selected_page == "Banking Analytics Bundle":
        selected_dataset = st.sidebar.selectbox("Select Banking Analytics Bundle Dataset", ["FDIC", "Fred_Financial_Labor_Performance", "Fred_Interest_rate_data", "fred_unemployement_rate"])
        if selected_dataset == "FDIC":
            FDIC.show()
        elif selected_dataset == "Fred_Financial_Labor_Performance":
            Fred_Financial_Labor_Performance.show()
        elif selected_dataset == "Fred_Interest_rate_data":
            Fred_Interest_rate_data.show()
        elif selected_dataset == "fred_unemployement_rate":
            fred_unemployement_rate.show()
    elif selected_page == "Consumer Financial Protection Bureau Analysis":
        selected_dataset = st.sidebar.selectbox("Select Consumer Financial Protection Bureau Analysis Dataset", ["Consumer_Financial_Protection_Bureau_Analysis"])
        if selected_dataset == "Consumer_Financial_Protection_Bureau_Analysis":
            Consumer_Financial_Protection_Bureau_Analysis.show()
    elif selected_page == "Demographics Data Bundle":
        selected_dataset = st.sidebar.selectbox("Select Demographics Data Bundle", ["Demographics_Statistics_By_Zip_Code"])
        if selected_dataset == "Demographics_Statistics_By_Zip_Code":
            Demographics_Statistics_By_Zip_Code.show()
    elif selected_page == "Electric Vehicle Trends":
        selected_dataset = st.sidebar.selectbox("Select Electric Vehicle Trends", ["Electric_Vehicle_Trends"])
        if selected_dataset == "Electric_Vehicle_Trends":
            Electric_Vehicle_Trends.show()
    elif selected_page == "Federal Exchange Rates":
        selected_dataset = st.sidebar.selectbox("Select Federal Exchange Rates", ["Federal_Exchange_Rates"])
        if selected_dataset == "Federal_Exchange_Rates":
            Federal_Exchange_Rates.show()
    elif selected_page == "Federal Financial Institutions Package":
        selected_dataset = st.sidebar.selectbox("Select Federal Financial Institutions Package", ["Federal_Deposit_Insurance_Corporation"])
        if selected_dataset == "Federal_Deposit_Insurance_Corporation":
            Federal_Deposit_Insurance_Corporation.show()
    elif selected_page == "Global Landslide Catalog Export":
        selected_dataset = st.sidebar.selectbox("Select Global Landslide Catalog Export", ["Nasa_Landslide_Data"])
        if selected_dataset == "Nasa_Landslide_Data":
            Nasa_Landslide_Data.show()
    elif selected_page == "Indicators of Health Insurance Coverage at the Time of Interview":
        selected_dataset = st.sidebar.selectbox("Select Indicators of Health Insurance Coverage at the Time of Interview", ["Indicators_of_Health_Insurance_Coverage"])
        if selected_dataset == "Indicators_of_Health_Insurance_Coverage":
            Indicators_of_Health_Insurance_Coverage.show()
    elif selected_page == "Layoff Data":
        selected_dataset = st.sidebar.selectbox("Select Layoff Data", ["Warn_Layoff_Data"])
        if selected_dataset == "Warn_Layoff_Data":
            Warn_Layoff_Data.show()
    elif selected_page == "Lottery Mega Millions Winning Numbers":
        selected_dataset = st.sidebar.selectbox("Select Lottery Mega Millions Winning Numbers", ["Lottery_Mega_millions_winning_numbers","Lottery_NY_Lotto_Winning_Numbers","Lottery_powerball_Winning_Numbers"])
        if selected_dataset == "Lottery_Mega_millions_winning_numbers":
            Lottery_Mega_millions_winning_numbers.show()
        elif selected_dataset == "Lottery_NY_Lotto_Winning_Numbers":
            Lottery_NY_Lotto_Winning_Numbers.show()
        elif selected_dataset == "Lottery_powerball_Winning_Numbers":
            Lottery_powerball_Winning_Numbers.show()
    elif selected_page == "National Credit Union Administration":
        selected_dataset = st.sidebar.selectbox("Select National Credit Union Administration", ["Credit_Union_Information"])
        if selected_dataset == "Credit_Union_Information":
            Credit_Union_Information.show()
    elif selected_page == "SEC Analytics":
        selected_dataset = st.sidebar.selectbox("Select SEC Analytics", ["sec"])
        if selected_dataset == "sec":
            sec.show()


if __name__ == "__main__":
    main()
