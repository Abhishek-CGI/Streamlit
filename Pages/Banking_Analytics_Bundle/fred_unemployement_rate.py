import streamlit as st

def show():
    # Create two columns
    # col1, col2 = st.columns([1, 5])

# Add the logo to the first column
    # col1.image("pages\image\Insights by CG Infinity 1.png", width=100)

# Add the text to the second column
    st.write("# FRED - Unemployment Rate")


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

The dataset consolidates economic and financial data related to the unemployment rate from various sources. It includes data on interest rates, consumer price indices (seasonally adjusted and not seasonally adjusted), federal funds rate, M2 money supply (seasonally adjusted and not seasonally adjusted), treasury securities yields, and unemployment rates (seasonally adjusted and not seasonally adjusted).

**Scale:**

- Temporal: Covers data from multiple FRED series, potentially spanning decades depending on the chosen series.
- Granularity: Data points are provided at the daily level, offering detailed insights into short-term economic fluctuations.

**Value:**

- Macroeconomic insights: Consumers can analyse the relationship between various economic factors like Treasury yields, inflation, money supply, and federal funds rate with the unemployment rate.
- Timely market analysis: By monitoring daily updates, users can stay informed about evolving economic conditions and their potential impact on unemployment trends.
- Research and forecasting: The comprehensive data allows for quantitative analysis and model building to predict future unemployment patterns.
- Comprehensive Unemployment Indicators: Provides a comprehensive set of indicators related to unemployment and its economic determinants.

**Consumer Use:**

- Economists and financial analysts: Analyse the interplay between economic indicators and unemployment for research and investment decisions.
- Policymakers and government agencies: Track unemployment trends and inform policy initiatives addressing employment challenges.
- Businesses and investors: Evaluate economic conditions and their potential impact on business activities and investment strategies.
- Academic researchers: Conduct quantitative studies and develop models to understand unemployment dynamics.
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
        -  **OBSERVATION_DATE:**  This column represents the date for which the economic and financial data is recorded or reported. It serves as a time reference for each data point in the dataset.
        -  **TWO_YEAR_TREASURY_CONSTANT:**  This column likely contains the interest rate or yield associated with the Two-Year Treasury Constant Maturity. It represents the interest rate on U.S. government securities (bonds) with a two-year time-to-maturity.
        -  **CONSUMER_PRICE_INDEX_NOT_SEASONALLY_ADJUSTED:**  This column contains the Consumer Price Index (CPI) data, which measures the average price change of a basket of goods and services in the economy. The data in this column is likely not seasonally adjusted, meaning it does not include adjustments for regular seasonal fluctuations.
        -  **CONSUMER_PRICE_INDEX_SEASONALLY_ADJUSTED:**  This column also contains the Consumer Price Index (CPI) data, but in this case, the data is likely seasonally adjusted. Seasonal adjustments remove the effects of regular seasonal variations from the index, allowing for a more accurate representation of underlying price trends.
        -  **FEDERAL_FUNDS:**  This column contains data related to the Federal Funds Rate. The Federal Funds Rate is the interest rate at which depository institutions (banks) lend reserve balances to other depository institutions overnight on an uncollateralized basis. It is an important indicator of the central bank's monetary policy stance.
        -  **M2_NOT_SEASONALLY_ADJUSTED:**  This column likely contains data related to the M2 money supply, which represents a broad measure of the money supply that includes cash, checking deposits, savings deposits, and other liquid assets. The data in this column is likely not seasonally adjusted.
        -  **M2_SEASONALLY_ADJUSTED:**  This column contains data related to the seasonally adjusted M2 money supply. Seasonal adjustments are applied to remove regular seasonal fluctuations from the data.
        -  **TREASURY_SECURITIES:**  This column likely contains data related to various U.S. Treasury securities, such as government bonds and Treasury bills. It may represent their yields or interest rates.
        -  **UNEMPLOYMENT_RATE_NOT_SEASONALLY_ADJUSTED:**  This column contains data on the unemployment rate, which measures the percentage of the labor force that is unemployed and actively seeking employment. The data in this column is likely not seasonally adjusted.
        -  **UNEMPLOYMENT_RATE_SEASONALLY_ADJUSTED:**  This column contains data on the seasonally adjusted unemployment rate. Seasonal adjustments are applied to remove regular seasonal variations from the unemployment rate data.
        """
    )

# SQL Queries section
    st.subheader('SQL Queries')

# Query 1
    st.markdown("""
    **Average Consumer Price Index**
    ```sql
    SELECT 
        AVG(CONSUMER_PRICE_INDEX_NOT_SEASONALLY_ADJUSTED) AS Avg_CPI_Not_Adjusted,
        AVG(CONSUMER_PRICE_INDEX_SEASONALLY_ADJUSTED) AS Avg_CPI_Adjusted
    FROM FRED_MARKETPLACE_DATASET;""")

# Query 2
    st.markdown("""
    **Federal Funds Rate Trend**
    ```sql
    SELECT 
        OBSERVATION_DATE,
        FEDERAL_FUNDS
    FROM FRED_MARKETPLACE_DATASET
    ORDER BY OBSERVATION_DATE;""")

# Query 3
    st.markdown("""
    **Unemployment Rate Comparison**
    ```sql
    SELECT 
        OBSERVATION_DATE,
        UNEMPLOYMENT_RATE_NOT_SEASONALLY_ADJUSTED AS Unemployment_Not_Adjusted,
        UNEMPLOYMENT_RATE_SEASONALLY_ADJUSTED AS Unemployment_Adjusted
    FROM FRED_MARKETPLACE_DATASET;""")

# Query 4
    st.markdown("""
    **M2 Money Supply Analysis**
    ```sql
    SELECT 
        OBSERVATION_DATE,
        M2_NOT_SEASONALLY_ADJUSTED AS M2_Not_Adjusted,
        M2_SEASONALLY_ADJUSTED AS M2_Adjusted
    FROM FRED_MARKETPLACE_DATASET;""")

# Query 5
    st.markdown("""
    **Analyzing Treasury Securities Data**
    ```sql
    SELECT
        OBSERVATION_DATE,
        TREASURY_SECURITIES,
        TREASURY_SECURITIES - LAG(TREASURY_SECURITIES) OVER (ORDER BY OBSERVATION_DATE) AS Treasury_Securities_Change
    FROM FRED_MARKETPLACE_DATASET;""")

# Query 6
    st.markdown("""
    **Two-Year Treasury Constant Rate Trend**
    ```sql
    SELECT 
        OBSERVATION_DATE,
        TWO_YEAR_TREASURY_CONSTANT
    FROM FRED_MARKETPLACE_DATASET
    ORDER BY OBSERVATION_DATE;""")

# Query 7
    st.markdown("""
    **Calculating the Inflation Rate**
    ```sql
    SELECT
        OBSERVATION_DATE,
        (CONSUMER_PRICE_INDEX_SEASONALLY_ADJUSTED - LAG(CONSUMER_PRICE_INDEX_SEASONALLY_ADJUSTED) OVER (ORDER BY OBSERVATION_DATE)) / LAG(CONSUMER_PRICE_INDEX_SEASONALLY_ADJUSTED) OVER (ORDER BY OBSERVATION_DATE) * 100 AS Inflation_Rate_Adjusted,
        (CONSUMER_PRICE_INDEX_NOT_SEASONALLY_ADJUSTED - LAG(CONSUMER_PRICE_INDEX_NOT_SEASONALLY_ADJUSTED) OVER (ORDER BY OBSERVATION_DATE)) / LAG(CONSUMER_PRICE_INDEX_NOT_SEASONALLY_ADJUSTED) OVER (ORDER BY OBSERVATION_DATE) * 100 AS Inflation_Rate_Not_Adjusted
    FROM FRED_MARKETPLACE_DATASET;""")

# Query 8
    st.markdown("""
    **Analyzing Money Supply Growth**
    ```sql
    SELECT
        OBSERVATION_DATE,
        (M2_SEASONALLY_ADJUSTED - LAG(M2_SEASONALLY_ADJUSTED) OVER (ORDER BY OBSERVATION_DATE)) / LAG(M2_SEASONALLY_ADJUSTED) OVER (ORDER BY OBSERVATION_DATE) * 100 AS M2_Growth_Adjusted,
        (M2_NOT_SEASONALLY_ADJUSTED - LAG(M2_NOT_SEASONALLY_ADJUSTED) OVER (ORDER BY OBSERVATION_DATE)) / LAG(M2_NOT_SEASONALLY_ADJUSTED) OVER (ORDER BY OBSERVATION_DATE) * 100 AS M2_Growth_Not_Adjusted
    FROM FRED_MARKETPLACE_DATASET;""")     


    st.subheader('Business Needs')


    # Display the text in a blue box with custom styling
    st.markdown("""
        -  **Inflation Analysis:**  Businesses can use the Consumer Price Index (CPI) data to monitor inflation trends. Understanding inflation rates is crucial for pricing strategies, cost management, and forecasting financial performance.
        -  **Interest Rate Sensitivity:**  Companies can analyze the Federal Funds Rate and Treasury Securities data to assess their interest rate sensitivity. This analysis can help businesses manage interest rate risks, especially if they have significant debt or variable rate loans.
        -  **Economic Forecasting:**  The unemployment rate data can be utilized by businesses to assess labor market conditions and make informed decisions regarding hiring, capacity planning, and overall economic outlook.
        -  **Monetary Policy Impact:**  Businesses can monitor the Federal Funds Rate to understand how changes in monetary policy by the central bank may impact borrowing costs, consumer spending, and overall economic conditions.
        -  **Money Supply Analysis:**  Analyzing M2 money supply data can provide insights into overall liquidity in the economy. Businesses can use this information to assess the availability of credit and potential impacts on consumer spending and investment.
        -  **Investment Decision-Making:**  Companies can use the data on Treasury Securities and the Two-Year Treasury Constant rate to evaluate investment opportunities and make decisions about allocating capital to fixed-income instruments.
        -  **Economic Indicator Tracking:**  Businesses can use this data to track key economic indicators, such as inflation and unemployment, which can have significant implications for business performance and market conditions.
        -  **Business Forecasting:**  By understanding interest rate trends, businesses can forecast borrowing costs and plan for future financing needs, capital expenditures, and investments.
        -  **Competitor Analysis:**  Companies can compare their interest rate sensitivity, inflation expectations, and monetary policy assessments against their competitors to gauge their competitive position and market opportunities.
        -  **Economic Impact Assessments:**  The data can help businesses assess the potential impacts of economic changes on their revenue, expenses, and profitability.
        """
    )


    st.subheader('Tables Included')
    st.markdown("""
    - FRED_2Y_TREASURY_CONSTANT
    - FRED_CONSUMER_PRICE_INDEX_NOT_SEASONALLY_ADJUSTED
    - FRED_CONSUMER_PRICE_INDEX_SEASONALLY_ADJUSTED
    - FRED_FEDERAL_FUNDS
    - FRED_M2_NOT_SEASONALLY_ADJUSTED
    - FRED_M2_SEASONALLY_ADJUSTED
    - FRED_TREASURY_SECURITIES
    - FRED_UNEMPLOYMENT_RATE_NOT_SEASONALLY_ADJUSTED
    - FRED_UNEMPLOYMENT_RATE_SEASONALLY_ADJUSTED


    """)

    # Fields included section
    st.subheader('Fields Included')
    st.markdown("""
    - OBSERVATION_DATE 	
    - TWO_YEAR_TREASURY_CONSTANT  
    - CONSUMER_PRICE_INDEX_NOT_SEASONALLY_ADJUSTED 	
    - CONSUMER_PRICE_INDEX_SEASONALLY_ADJUSTED  
    - FEDERAL_FUNDS  
    - M2_NOT_SEASONALLY_ADJUSTED  
    - M2_SEASONALLY_ADJUSTED  
    - TREASURY_SECURITIES  
    - UNEMPLOYMENT_RATE_NOT_SEASONALLY_ADJUSTED  
    - UNEMPLOYMENT_RATE_SEASONALLY_ADJUSTED  
 


    """)

    # Closing section
    st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")
