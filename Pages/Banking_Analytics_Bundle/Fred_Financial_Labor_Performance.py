import streamlit as st

def show():
    # Create two columns
    # col1, col2 = st.columns([1, 5])

# Add the logo to the first column
    # col1.image("pages\image\Insights by CG Infinity 1.png", width=100)

# Add the text to the second column
    st.write("# FRED - Financial Labor Performance")


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

The dataset consolidates economic and financial data from various sources, providing insights into labor force participation rates, personal saving rates, total nonfarm employment, and industrial production. The data is categorized into seasonally adjusted and not seasonally adjusted metrics.

**Scale:**

- Observation Date: Date for which economic and financial data is recorded or reported.
- Labor Force Participation Rate (Seasonally Adjusted): Metric reflecting the percentage of the working-age population that is actively engaged in the labor market, seasonally adjusted.
- Labor Force Participation Rate (Not Seasonally Adjusted): Metric reflecting the percentage of the working-age population that is actively engaged in the labor market, not seasonally adjusted.
- Personal Saving Rate: Proportion of disposable income that individuals save rather than spend.
- Total Nonfarm Employment (Seasonally Adjusted): Data on total nonfarm employment, capturing the number of individuals employed across various industries, seasonally adjusted.
- Total Nonfarm Employment (Not Seasonally Adjusted): Data on total nonfarm employment, capturing the number of individuals employed across various industries, not seasonally adjusted.
- Industrial Production (Seasonally Adjusted): Data on industrial production, gauging the output and performance of the industrial sector, seasonally adjusted.
- Industrial Production (Not Seasonally Adjusted): Data on industrial production, gauging the output and performance of the industrial sector, not seasonally adjusted.

**Value:**

- Comprehensive Economic Indicators: Provides a comprehensive set of economic indicators related to labor force, personal saving, employment, and industrial production.
- Temporal Analysis: Allows for the analysis of economic trends and changes over time through seasonally adjusted and not seasonally adjusted metrics.
- Labor Market Insight: Offers insights into labor force participation rates, aiding in understanding workforce dynamics.
- Financial Health Assessment: Personal saving rates contribute to assessing the financial health of individuals and households.
- Industrial Sector Performance: Industrial production metrics provide insights into the performance of the industrial sector.

**Consumer Use:**

- Economic Researchers: Researchers can leverage the dataset to study and analyze trends in labor force participation, personal saving, employment, and industrial production.
- Policy Makers: Government officials and policy makers can use the data to formulate and assess economic policies based on labor market and financial indicators.
- Investors: Investors and financial analysts can utilize the dataset to assess economic conditions and make informed investment decisions.
- Economic Forecasting: The data supports economic forecasting by providing key indicators related to labor and financial performance.
- Educational Purposes: Students and educators can use the dataset for educational purposes, studying the relationships between different economic variables.
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
        -  **LABOR_FORCE_PARTICIPATION_RATE_SEASONALLY_ADJUSTED:**  This column contains data on the labor force participation rate, a critical metric reflecting the percentage of the working-age population that is actively engaged in the labor market. The data is seasonally adjusted to account for regular seasonal variations.
        -  **LABOR_FORCE_PARTICIPATION_RATE_NOT_SEASONALLY_ADJUSTED:**  This column contains data on the labor force participation rate, a critical metric reflecting the percentage of the working-age population that is actively engaged in the labor market. The data is without seasonally adjusted to account for regular seasonal variations.
        -  **PERSONAL_SAVING_RATE:**  This column offers insights into the personal saving rate, indicating the proportion of disposable income that individuals save rather than spend.
        -  **ALL_EMPLOYEES_TOTAL_NONFARM_SEASONALLY_ADJUSTED:**  This column presents data on total nonfarm employment, capturing the number of individuals employed across various industries. The data is seasonally adjusted to account for seasonal variations.
        -  **ALL_EMPLOYEES_TOTAL_NONFARM_NOT_SEASONALLY_ADJUSTED:**  This column presents data on total nonfarm employment, capturing the number of individuals employed across various industries. The data is not seasonally adjusted to account for seasonal variations.
        -  **INDUSTRIAL_PRODUCTION_SEASONALLY_ADJUSTED:**  This column includes data on industrial production, which gauges the output and performance of the industrial sector. The data is seasonally adjusted to mitigate the influence of seasonal patterns.
        -  **INDUSTRIAL_PRODUCTION_NOT_SEASONALLY_ADJUSTED:**  This column includes data on industrial production, which gauges the output and performance of the industrial sector. The data is not seasonally adjusted to mitigate the influence of seasonal patterns.
       """
    )

# SQL Queries section
    st.subheader('SQL Queries')

# Query 1
    st.markdown("""
    **Average Labor Force Participation Rate**
    ```sql
    SELECT 
        AVG(LABOR_FORCE_PARTICIPATION_RATE_SEASONALLY_ADJUSTED) AS Avg_Participation_Rate_Adjusted,
        AVG(LABOR_FORCE_PARTICIPATION_RATE_NOT_SEASONALLY_ADJUSTED) AS Avg_Participation_Rate_Not_Adjusted
    FROM FRED_FINANCIAL_LABOR_PERFORMANCE;""")

# Query 2
    st.markdown("""
    **Employment Metrics Comparison**
    ```sql
    SELECT 
        OBSERVATION_DATE,
        ALL_EMPLOYEES_TOTAL_NONFARM_SEASONALLY_ADJUSTED AS Employment_Adjusted,
        ALL_EMPLOYEES_TOTAL_NONFARM_NOT_SEASONALLY_ADJUSTED AS Employment_Not_Adjusted
    FROM FRED_FINANCIAL_LABOR_PERFORMANCE;""")

# Query 3
    st.markdown("""
    **Seasonally Adjusted Industrial Production**
    ```sql
    SELECT 
        OBSERVATION_DATE,
        INDUSTRIAL_PRODUCTION_SEASONALLY_ADJUSTED AS Industrial_Production_Adjusted
    FROM FRED_FINANCIAL_LABOR_PERFORMANCE
    ORDER BY OBSERVATION_DATE;""")

# Query 4
    st.markdown("""
    **Changes in Personal Saving Rate**
    ```sql
    SELECT
        OBSERVATION_DATE,
        PERSONAL_SAVING_RATE,
        (PERSONAL_SAVING_RATE - LAG(PERSONAL_SAVING_RATE) OVER (ORDER BY OBSERVATION_DATE)) / LAG(PERSONAL_SAVING_RATE) OVER (ORDER BY OBSERVATION_DATE) * 100 AS Saving_Rate_Change
    FROM FRED_FINANCIAL_LABOR_PERFORMANCE;""")

# Query 5
    st.markdown("""
    **Employment Growth Analysis**
    ```sql
    SELECT
        OBSERVATION_DATE,
        ALL_EMPLOYEES_TOTAL_NONFARM_SEASONALLY_ADJUSTED AS Employment_Adjusted,
        (ALL_EMPLOYEES_TOTAL_NONFARM_SEASONALLY_ADJUSTED - LAG(ALL_EMPLOYEES_TOTAL_NONFARM_SEASONALLY_ADJUSTED) OVER (ORDER BY OBSERVATION_DATE)) / LAG(ALL_EMPLOYEES_TOTAL_NONFARM_SEASONALLY_ADJUSTED) OVER (ORDER BY OBSERVATION_DATE) * 100 AS Employment_Growth_Adjusted
    FROM FRED_FINANCIAL_LABOR_PERFORMANCE;""")

# Query 6
    st.markdown("""
    **Seasonal Adjustment Impact**
    ```sql
    SELECT
        OBSERVATION_DATE,
        LABOR_FORCE_PARTICIPATION_RATE_SEASONALLY_ADJUSTED AS Participation_Rate_Adjusted,
        LABOR_FORCE_PARTICIPATION_RATE_NOT_SEASONALLY_ADJUSTED AS Participation_Rate_Not_Adjusted,
        (LABOR_FORCE_PARTICIPATION_RATE_SEASONALLY_ADJUSTED - LABOR_FORCE_PARTICIPATION_RATE_NOT_SEASONALLY_ADJUSTED) AS Adjustment_Impact
    FROM FRED_FINANCIAL_LABOR_PERFORMANCE;""")

    # Query 7
    st.markdown("""
    **Industrial Production Growth**
    ```sql
    SELECT
        OBSERVATION_DATE,
        INDUSTRIAL_PRODUCTION_SEASONALLY_ADJUSTED AS Industrial_Production_Adjusted,
        (INDUSTRIAL_PRODUCTION_SEASONALLY_ADJUSTED - LAG(INDUSTRIAL_PRODUCTION_SEASONALLY_ADJUSTED) OVER (ORDER BY OBSERVATION_DATE)) / LAG(INDUSTRIAL_PRODUCTION_SEASONALLY_ADJUSTED) OVER (ORDER BY OBSERVATION_DATE) * 100 AS Production_Growth_Adjusted,
        INDUSTRIAL_PRODUCTION_NOT_SEASONALLY_ADJUSTED AS Industrial_Production_Not_Adjusted,
        (INDUSTRIAL_PRODUCTION_NOT_SEASONALLY_ADJUSTED - LAG(INDUSTRIAL_PRODUCTION_NOT_SEASONALLY_ADJUSTED) OVER (ORDER BY OBSERVATION_DATE)) / LAG(INDUSTRIAL_PRODUCTION_NOT_SEASONALLY_ADJUSTED) OVER (ORDER BY OBSERVATION_DATE) * 100 AS Production_Growth_Not_Adjusted
    FROM FRED_FINANCIAL_LABOR_PERFORMANCE;""")

    

    st.subheader('Business Needs')


    # Display the text in a blue box with custom styling
    st.markdown("""
        -  **Economic Forecasting and Planning:**  Businesses can use labor force participation rate data to anticipate changes in the available workforce and plan hiring strategies accordingly.
        -  **Workforce Management:**  Labor force participation rate data aids in workforce planning, enabling businesses to align staffing levels with fluctuations in labor market activity. Employment data assists in managing talent acquisition, retention, and training initiatives.
        -  **Consumer Behavior Analysis:**  Personal saving rate data allows businesses to gauge consumer spending patterns and make informed decisions about product offerings and marketing campaigns.
        -  **Market Research and Strategy:**  Insights from labor and economic indicators guide businesses in identifying growth opportunities and potential challenges in the market. Businesses can align their strategies with anticipated economic trends to optimize product development and market positioning.
        -  **Financial Planning and Risk Management:**  Personal saving rate information informs financial planning strategies for both individuals and businesses. Industrial production data helps businesses assess potential disruptions in the supply chain and plan for contingencies.
        -  **Investment Decision-Making:**  Industrial production trends impact sectors like manufacturing, influencing investment decisions in equipment, machinery, and technologies. Economic indicators guide investment strategies by providing insights into economic stability and growth potential.
        -  **Regulatory Compliance:**  Labor force participation rate data can help businesses understand workforce dynamics and compliance requirements, particularly in industries subject to labor regulations.
        -  **Business Expansion and Contraction:**  Economic indicators guide business expansion decisions by highlighting regions experiencing growth and economic stability. Industrial production data can influence decisions regarding opening new facilities or closing underperforming ones.
        -  **Financial Services and Banking:**  Personal saving rate insights are essential for banks and financial institutions to tailor savings products and investment options to customer needs. Economic indicators assist in evaluating lending risk and setting interest rates for loans.
    """
    )


    st.subheader('Tables Included')
    st.markdown("""
    - FRED_LABOR_FORCE_PARTICIPATION_RATE_SEASONALLY_ADJUSTED 
    - FRED_LABOR_FORCE_PARTICIPATION_RATE_NOT_SEASONALLY_ADJUSTED 
    - FRED_PERSONAL_SAVING_RATE
    - FRED_ALL_EMPLOYEES_TOTAL_NONFARM_SEASONALLY_ADJUSTED
    - FRED_ALL_EMPLOYEES_TOTAL_NONFARM_NOT_SEASONALLY_ADJUSTED
    - FRED_INDUSTRIAL_PRODUCTION_SEASONALLY_ADJUSTED
    - FRED_INDUSTRIAL_PRODUCTION_NOT_SEASONALLY_ADJUSTED

    """)

    # Fields included section
    st.subheader('Fields Included')
    st.markdown("""
    - OBSERVATION_DATE,
    - LABOR_FORCE_PARTICIPATION_RATE_SEASONALLY_ADJUSTED,
    - LABOR_FORCE_PARTICIPATION_RATE_NOT_SEASONALLY_ADJUSTED,
    - PERSONAL_SAVING_RATE,
    - ALL_EMPLOYEES_TOTAL_NONFARM_SEASONALLY_ADJUSTED,
    - ALL_EMPLOYEES_TOTAL_NONFARM_NOT_SEASONALLY_ADJUSTED,
    - INDUSTRIAL_PRODUCTION_SEASONALLY_ADJUSTED,
    - INDUSTRIAL_PRODUCTION_NOT_SEASONALLY_ADJUSTED

    """)

    # Closing section
    st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")
