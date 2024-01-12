import streamlit as st

def show():
    # Create two columns
    # col1, col2 = st.columns([1, 5])

# Add the logo to the first column
    # col1.image("pages\image\Insights by CG Infinity 1.png", width=100)

# Add the text to the second column
    st.write("# Federal Exchange Rates")


# # Text to be displayed in the blue box
# info_text = """
# The Federal Deposit Insurance Corporation (FDIC) is a vital government agency in the United States established to safeguard and stabilize the nation's banking system. Formed in response to the economic challenges of the Great Depression in the 1930s, the FDIC primarily operates as a guarantor of deposits held in U.S. banks and thrifts. Its fundamental purpose is to instill confidence in the financial system by offering insurance coverage for deposits, with the standard amount currently set at $250,000 per depositor, per bank. Beyond deposit insurance, the FDIC assumes a critical regulatory role, overseeing and examining banks to ensure their safety and soundness. In cases of bank failures, the FDIC takes charge of resolving the institution, either through the sale of its assets or by facilitating the transfer of operations to another financial entity. This regulatory body extends its influence across a spectrum of financial institutions, ranging from large national banks to smaller community banks. By diligently assessing risks, promoting sound banking practices, and wielding resolution authority when necessary, the FDIC contributes significantly to the stability and confidence in the U.S. financial landscape. Its proactive measures in risk management, coupled with its role in maintaining the integrity of the banking sector, underscore the FDIC's crucial position in protecting depositors and ensuring the resilience of the country's financial system.
# """

# # Add an image in the same row
# st.image("pages/image/fdic.png", width=100) 
# # Display the text in a blue box with custom styling
# st.markdown(
#     f'<div style="background-color: #D9EAF8; padding: 20px; border-radius: 10px;">{info_text}</div>',
#     unsafe_allow_html=True,
# )



# Image
# st.image("pages/image/fdic.png", width=700)

# Text to be displayed in the blue box
    info_text = """
    Foreign exchange rates represent the price of one currency in terms of another. They indicate how much of one currency you would need to exchange to obtain a certain amount of another currency. Exchange rates are typically expressed as ratios, where one unit of the first currency is equivalent to a certain amount of the second currency.
    """


# Display the text in a blue box with custom styling
    st.markdown(
    f'<div style="background-color: #D3D3D3; padding: 20px; border-radius: 10px;">{info_text}</div>',
    unsafe_allow_html=True,
    )

    st.markdown("""
    **Key Elements of Exchange Rates:**

    - **Base Currency:** This is the currency you are converting from. Its value is always 1 in the exchange rate calculation. For example, if you're in the United States, the U.S. Dollar (USD) might be your base currency.

    - **Quote Currency:** This is the currency you are converting to. Its value is given in the exchange rate. For example, if you're converting from USD to Euro (EUR), the Euro would be the quote currency.
    """)
# SQL Queries section
    st.subheader('SQL Queries')

# Query 1
    st.markdown("""
    **Filtering Complaints from a Specific Company:**
    ```sql
    SELECT *
    FROM cfpb_data
    WHERE company = 'ABC Bank';
    """)

# Query 2
    st.markdown("""
    **Calculating the average response time to complaints:**
    ```sql
    SELECT company, AVG(response_time_days) AS COMPANY_RESPONSE_TO_CONSUMER
    FROM cfpb_data
    GROUP BY company
    ORDER BY COMPANY_RESPONSE_TO_CONSUMER;
    """)

# Query 3
    st.markdown("""
    **Counting the number of complaints per product:**
    ```sql
    SELECT product, COUNT(*) AS complaint_ID
    FROM cfpb_data
    GROUP BY product
    ORDER BY complaint_ID DESC;
    """)

# Query 4
    st.markdown("""
    **Analyzing Complaints Overtime:**
    ```sql
    SELECT EXTRACT(YEAR FROM date_received) AS year,
    EXTRACT(MONTH FROM date_received) AS month,
    COUNT(*) AS complaint_ID
    FROM cfpb_data
    GROUP BY year, month
    ORDER BY year, month;
    """)


    st.subheader('Business Needs')


    # Display the text in a blue box with custom styling
    st.markdown("""

    Foreign exchange rates represent the price of one currency in terms of another. They indicate how much of one currency you would need to exchange to obtain a certain amount of another currency. Exchange rates are typically expressed as ratios, where one unit of the first currency is equivalent to a certain amount of the second currency.

    **Currency Conversion and Comparison**:  

    - Businesses that deal with international transactions can use the exchange rate data to convert and compare different currency values. For example, an e-commerce platform might display prices in multiple currencies based on the exchange rates to help customers make informed purchasing decisions.

    **Financial Analysis and Reporting**:  

    - Financial institutions and investment firms can analyze historical exchange rate data to assess currency trends and make informed investment decisions. They can generate reports to track the performance of different currencies against a base currency over time.

    **Regulatory Compliance**: 

    -	Some industries, such as finance and international trade, are subject to regulatory requirements related to currency reporting and compliance. Accurate exchange rate data is essential for meeting these obligations.  

    **Tourism and Travel Planning**:  

    - Companies in the travel and tourism industry can use exchange rate data to provide travelers with up-to-date currency conversion rates for various destinationS.

    """)


    st.subheader('Tables Included')
    st.markdown("""
    - Foreign_Exchange_Rates
    """)

    # Fields included section
    st.subheader('Fields Included')
    st.markdown("""
        -   S_NO
        -	BASE 
        -	TIME 
        -	AUSTRALIAN_DOLLAR 
        -	EURO_AREA_EURO 
        -	NEW_ZELAND_DOLLAR 
        -	UNITED_KINGDOM_POUND 
        -	BRAZIL_REAL 
        -	CANADIAN_DOLLAR 
        -	CHINA_YUAN 
        -	HONG_KONG_DOLLAR 
        -	INDIAN_RUPEE 
        -	KOREA_WON 
        -	MEXICAN_PESO 
        -	SOUTH_AFRICA_RAND 
        -	SINGAPORE_DOLLAR 
        -	DENMARK_DANISH_KRONE 
        -	JAPAN_YEN
        -	MALAYSIA_RINGGIT 
        -	NORWAY_NORWEGIAN_KRONE 
        -	SWEDEN_KRONA 
        -	SRI_LANKAN_RUPEE 
        -	SWITZERLAND_FRANC
        -	TAIWAN_NEW_TAIWAN_DOLLAR 
        -	THAILAND_BAHT

    """)

    # Closing section
    st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")
