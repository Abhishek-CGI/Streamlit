import streamlit as st

def show():
    # Create two columns
    # col1, col2 = st.columns([1, 5])

# Add the logo to the first column
    # col1.image("pages\image\Insights by CG Infinity 1.png", width=100)

# Add the text to the second column
    st.write("# FRED - Interest Rate Data")


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

**Scope:**

The dataset consolidates data related to various interest rates, including treasury yield curve rates, treasury bill rates, long-term rates, and real long-term rates. It encompasses a range of durations, from short-term bills to long-term treasury bonds, providing a comprehensive overview of interest rate movements over time.

**Scale:**

- Temporal: Covers a broad timespan, depending on the underlying FRED series, potentially spanning decades.
- Granularity: Data is provided at the daily level, enabling detailed analysis of short-term interest rate fluctuations.
- Comprehensiveness: Encompasses rates for maturities ranging from 1 month to 30 years, as well as short-term Treasury bills and long-term composite rates.

**Value:**

- Unified access: Streamlines access to a diverse set of interest rate data within a single view, simplifying analysis.
- In-depth analysis: Facilitates comprehensive studies of interest rate trends, yield curve shapes, and the relationship between nominal and real rates.
- Economic insights: Enables insights into economic conditions, inflation expectations, monetary policy, and financial market dynamics.
- Versatile applications: Supports a wide range of use cases across finance, economics, research, and investment decision-making.

**Consumer Use:**

- Economists and financial analysts: Analyse interest rate trends, assess economic outlook, evaluate investment opportunities, and model economic behaviour.
- Fixed income traders and portfolio managers: Track interest rate movements, make informed trading decisions, and manage interest rate risk in portfolios.
- Risk managers: Assess interest rate exposure and potential impacts on financial institutions and corporate investments.
- Policymakers and central bankers: Monitor financial markets, inform monetary policy decisions, and assess the impact of policy actions on interest rates.
- Academic researchers: Conduct empirical studies on interest rate behaviour, macroeconomic relationships, and financial market dynamics.
"""


# Display the text in a blue box with custom styling
    st.markdown(
    f'<div style="background-color: #D9EAF8; padding: 20px; border-radius: 10px;">{info_text}</div>',
    unsafe_allow_html=True,
    )







# Datasets section
    st.subheader('Datasets')


    # Display the text in a blue box with custom styling
    st.markdown("""
        -  **DTYCR (Daily Treasury Yield Curve Rates):**  These columns represent the Daily Treasury Par Yield Curve Rates for different maturities, such as 1-month, 2-month, 3-month, 4-month, 6-month, 1-year, 2-year, 3-year, 5-year, 7-year, 10-year, 20-year, and 30-year.
        -  **DTRYCR (Daily Treasury Real Yield Curve Rates):**  These columns represent the Daily Treasury Par Real Yield Curve Rates for different maturities, such as 5-year, 7-year, 10-year, 20-year, and 30-year.
        -  **DTBR (Daily Treasury Bill Rates):**  These columns represent the Treasury Bill Rates for different maturities, such as 4-weeks bank discount, 4-weeks coupon equivalent, 8-weeks bank discount, 8-weeks coupon equivalent, 13-weeks bank discount, 13-weeks coupon equivalent, 17-weeks bank discount, 17-weeks coupon equivalent, 26-weeks bank discount, 26-weeks coupon equivalent, 52-weeks bank discount, and 52-weeks coupon equivalent.
        -  **DTLTR (Daily Treasury Long-Term Rates):**  These columns represent Long-Term Treasury Rates, such as the Long-Term Composite Rate (>10 years) , the Treasury 20-Year Constant Maturity Rate and Extrapolation Factor.
        -  **DTRLTR (Daily Treasury Real Long-Term Rates):**  These columns represent Long-Term Real Rates, such as the Long-Term Real Composite Rate (>10 years).
        """
    )

# SQL Queries section
    st.subheader('SQL Queries')

# Query 1
    st.markdown("""
    **Average rate for different maturities (average yield curve rate for 1-year)**
    ```sql
    SELECT AVG(DTYCR_1_Yr) AS Avg_1_Year_Rate FROM FRED_MARKETPLACE;""")

# Query 2
    st.markdown("""
    **Minimum and Maximum Rates (minimum and maximum 30-year yield curve rates)**
    ```sql
    SELECT MIN(DTYCR_30_Yr) AS Min_30_Year_Rate, MAX(DTYCR_30_Yr) AS Max_30_Year_Rate FROM FRED_MARKETPLACE;""")

# Query 3
    st.markdown("""
    **Trend Analysis – Comparing rates over different time periods (trend for 1-year yield curve rates)**
    ```sql
    SELECT
        Date,
        DTYCR_1_Yr,
        LAG(DTYCR_1_Yr) OVER (ORDER BY Date) AS Previous_1_Year_Rate
    FROM FRED_MARKETPLACE;

    SELECT
        Date,
        DTYCR_1_Yr,
        LEAD(DTYCR_1_Yr) OVER (ORDER BY Date) AS Previous_1_Year_Rate
    FROM FRED_MARKETPLACE;""")

# Query 4
    st.markdown("""
    **Identifying Dates with an Inverted Treasury Bill Curve (3-Month Rate Higher than 6-Month Rate)**
    ```sql
    SELECT
        Date,
        DTBR_13_WEEKS_BANK_DISCOUNT AS Yield_3_Month,
        DTBR_26_WEEKS_BANK_DISCOUNT AS Yield_6_Month
    FROM FRED_MARKETPLACE
    WHERE [DTBR_13_WEEKS_BANK_DISCOUNT] > [DTBR_26_WEEKS_BANK_DISCOUNT];""")

# Query 5
    st.markdown("""
    **Average Long-Term Treasury Rate**
    ```sql
    SELECT
        AVG(DTLTR_LT_COMPOSITE_GREATER_THAN_10_Yrs) AS Avg_Long_Term_Treasury_Rate
    FROM FRED_MARKETPLACE;""")

# Query 6
    st.markdown("""
    **Identifying the date with the largest change in the 5-year Daily Treasury Yield Curve rate**
    ```sql
    SELECT TOP 5
        Date,
        DTRYCR_5_YR AS Yield_5_Year,
        DTRYCR_5_YR - LAG(DTRYCR_5_YR) OVER (ORDER BY Date) AS Rate_Change
    FROM FRED_MARKETPLACE
    ORDER BY ABS(DTRYCR_5_YR - LAG(DTRYCR_5_YR) OVER (ORDER BY Date)) DESC;""")

    

    st.subheader('Business Needs')


    # Display the text in a blue box with custom styling
    st.markdown("""
        -  **Interest Rate Forecasting:**  Businesses may need to analyze historical interest rate trends across different maturities (e.g., 1-month, 1-year, 10-year) to forecast future interest rates. This analysis can help in making informed decisions about financial planning, investment strategies, and risk management.
        -  **Risk Management:**  Understanding the yield curve and the spread between short-term and long-term rates can help businesses assess interest rate risks and manage exposure to fluctuations in interest rates. This is particularly important for businesses with significant debt or financial investments.
        -  **Investment Analysis:**  Companies may use the interest rate data to evaluate various investment opportunities, such as government bonds, treasury bills, or other fixed-income securities. The analysis can include comparing different maturities to identify the most attractive investment options.
        -  **Monetary Policy Impact:**  Businesses operating in sectors sensitive to monetary policy changes may track the Treasury Bill rates and yield curve data to assess how changes in interest rates by central banks can impact borrowing costs, consumer spending, and overall economic conditions.
        -  **Benchmarking:**  Companies can compare their own interest rates (e.g., on loans or deposits) against the Treasury Bill and Treasury Yield Curve rates to assess competitiveness and market positioning.
        -  **Economic Analysis:**  Businesses may use interest rate data as an economic indicator to understand macroeconomic conditions, assess inflation expectations, and evaluate potential impacts on their operations and revenue streams.
        -  **Financial Reporting:**  Companies, especially financial institutions, may need interest rate data for financial reporting purposes, regulatory compliance, and disclosures to stakeholders.
        -  **Interest Rate Hedging:**  Businesses with exposure to interest rate fluctuations may use interest rate data to implement hedging strategies, such as interest rate swaps or derivatives, to mitigate risks.
        """
    )


    st.subheader('Tables Included')
    st.markdown("""
    - FRED_MARKETPLACE_DATA

    """)

    # Fields included section
    st.subheader('Fields Included')
    st.markdown("""
    - Date 
    - DTYCR_1_Mo	
    - DTYCR_2_Mo 
    - DTYCR_3_Mo	
    - DTYCR_4_Mo 
    - DTYCR_6_Mo 
    - DTYCR_1_Yr 
    - DTYCR_2_Yr 
    - DTYCR_3_Yr 
    - DTYCR_5_Yr 
    - DTYCR_7_Yr 
    - DTYCR_10_Yr 
    - DTYCR_20_Yr 
    - DTYCR_30_Yr 
    - DTRYCR_5_YR 
    - DTRYCR_7_YR 
    - DTRYCR_10_YR 
    - DTRYCR_20_YR 
    - DTRYCR_30_YR 
    - DTBR_4_WEEKS_BANK_DISCOUNT 
    - DTBR_4_WEEKS_COUPON_EQUIVALENT 
    - DTBR_8_WEEKS_BANK_DISCOUNT 
    - DTBR_8_WEEKS_COUPON_EQUIVALENT 
    - DTBR_13_WEEKS_BANK_DISCOUNT 
    - DTBR_13_WEEKS_COUPON_EQUIVALENT 
    - DTBR_17_WEEKS_BANK_DISCOUNT 
    - DTBR_17_WEEKS_COUPON_EQUIVALENT 
    - DTBR_26_WEEKS_BANK_DISCOUNT 
    - DTBR_26_WEEKS_COUPON_EQUIVALENT 
    - DTBR_52_WEEKS_BANK_DISCOUNT 
    - DTBR_52_WEEKS_COUPON_EQUIVALENT 
    - DTLTR_LT_COMPOSITE_GREATER_THAN_10_Yrs 
    - DTLTR_TREASURY_20_Yr_CMT 
    - DTLTR_EXTRAPOLATION_FACTOR 
    - DTRLTR_LT_Real_Average_10_GREATER_THAN_Yrs 


    """)

    # Closing section
    st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")
