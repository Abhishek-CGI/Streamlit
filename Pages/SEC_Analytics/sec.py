import streamlit as st

def show():
    # Create two columns
    # col1, col2 = st.columns([1, 5])

# Add the logo to the first column
    # col1.image("pages\image\Insights by CG Infinity 1.png", width=100)

# Add the text to the second column
    st.write("# Sec Analytics")


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
    The U.S. Securities and Exchange Commission (SEC) is an independent federal government regulatory agency responsible for protecting investors, maintaining fair and orderly functioning of the securities markets, and facilitating capital formation. It was created by Congress in 1934 as the first federal regulator of the securities markets. The SEC promotes full public disclosure, protects investors against fraudulent and manipulative practices in the market, and monitors corporate takeover actions in the United States. It also approves registration statements for bookrunners among underwriting firms.
    """


# Display the text in a blue box with custom styling
    st.markdown(
    f'<div style="background-color: #D3D3D3; padding: 20px; border-radius: 10px;">{info_text}</div>',
    unsafe_allow_html=True,
    )

    st.markdown("""
    **Factors Contributing to SEC:**

    -	The Securities and Exchange Commission (SEC) is a U.S. government oversight agency responsible for regulating the securities markets and protecting investors.

    -   The SEC was established by the passage of the U.S. Securities Act of 1933 and the Securities and Exchange Act of 1934, largely in response to the stock market crash of 1929 that led to the Great Depression.

    -   The SEC can itself bring civil actions against lawbreakers, and also works with the Justice Department on criminal cases.
    """)
# SQL Queries section
    st.subheader('SQL Queries')

# Query 1
    st.markdown("""
    **Retrieve basic information about companies:**
    ```sql
    SELECT ADSH, CIK, NAME, SIC, COUNTRYBA, STPRBA, CITYBA
    FROM SUB;   
    """)

# Query 2
    st.markdown("""
    **Find companies based on specific criteria (e.g., in a certain state):**
    ```sql
    SELECT *
    FROM SCT_ARAJPOOT_DB.MARKETPLACE.SUB
    WHERE STPRBA = 'CA';
    """)

# Query 3
    st.markdown("""
    **Aggregate numeric data by tag and version:**
    ```sql
    SELECT TAG, VERSION, SUM(VALUE) AS TOTAL_VALUE
    FROM SCT_ARAJPOOT_DB.MARKETPLACE.NUM
    GROUP BY TAG, VERSION;
    """)

# Query 4
    st.markdown("""
    **Count the number of unique dimension hashes:**
    ```sql
    SELECT COUNT(DISTINCT DIMHASH) AS NUM_DIMENSIONS
    FROM DIM;
    """)


    st.subheader('Business Needs')


    # Display the text in a blue box with custom styling
    st.markdown("""

    The Securities and Exchange Commission (SEC) is the U.S. government agency in charge of the nation's securities industry. It monitors transactions, as well as the activities of financial professionals. Its mission is to promote fairness, integrity and transparency; prevent fraud and other deceptive acts; and ensure orderly and efficient markets.

    **Regulatory Compliance**:  

    -	Ensure compliance with SEC regulations by monitoring and analyzing financial reports and disclosures.Stay updated on changes in SEC guidelines and adjust business practices accordingly.

    **Risk Management**:  

    - 	Identify and assess potential risks associated with investment decisions and market activities.Analyze historical SEC data to understand patterns and trends that may indicate emerging risks.

    **Fraud Detection**: 

    -	Use analytics to detect irregularities or potential fraud within financial statements and transactions.
    -	Monitor for unusual trading patterns or activities that may be indicative of market manipulation.

    **Competitive Analysis**:  

    - 	Benchmark against competitors by comparing financial performance and strategic initiatives disclosed in SEC filings.
    -	Identify market trends and competitor strategies to stay ahead in the industry.

    """)


    st.subheader('Tables Included')
    st.markdown("""
    - 	DIM
    -  	NUM
    -	SUB

    """)

    # Fields included section
    st.subheader('Fields Included')
    st.markdown("""
    -	ADSH
    -	CIK  
    -	NAME 
    -	SIC  
    -	COUNTRYBA  
    -	STPRBA  
    -	CITYBA 
    -	ZIPBA  
    -	BAS1 
    -	BAS2 
    -	BAPH  
    -	COUNTRYMA  
    -	STPRMA  
    -	CITYMA  
    -	ZIPMA  
    -	MAS1 
    -	MAS2 
    -	COUNTRYINC  
    -	STPRINC  
    -	EIN  
    -	FORMER 
    -	CHANGED  
    -	AFS  
    -	WKSI  
    -	FYE  
    -	FORM  
    -	PERIOD  
    -	FY  
    -	FP  
    -	FILED  
    -	ACCEPTED 
    -	PREVRPT  
    -	DETAIL  
    -	INSTANCE 
    -	NCIKS  
    -	ACIKS 
    -	PUBFLOATUSD 
    -	FLOATDATE 
    -	FLOATAXIS 
    -	FLOATMEMS

    """)

    # Closing section
    st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")
