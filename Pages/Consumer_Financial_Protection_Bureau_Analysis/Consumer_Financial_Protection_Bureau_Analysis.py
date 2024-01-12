import streamlit as st

def show():
    # Create two columns
    # col1, col2 = st.columns([1, 5])

# Add the logo to the first column
    # col1.image("pages\image\Insights by CG Infinity 1.png", width=100)

# Add the text to the second column
    st.write("# Consumer Financial Protection Bureau Analysis")


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
The Consumer Complaint Database is a collection of complaints about consumer financial products and services that we sent to companies for response. Complaints are published after the company responds, confirming a commercial relationship with the consumer, or after 15 days, whichever comes first. Complaints referred to by other regulators, such as complaints about depository institutions with less than $10 billion in assets, are not published in the Consumer Complaint Database. 
"""


# Display the text in a blue box with custom styling
    st.markdown(
    f'<div style="background-color: #D3D3D3; padding: 20px; border-radius: 10px;">{info_text}</div>',
    unsafe_allow_html=True,
    )

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
    - 	**Customer Feedback Analysis:** The database can help businesses analyze and track customer complaints to understand recurring issues, identify trends, and gauge customer satisfaction levels.

    -	**Product/Service Improvement:** By analyzing the complaints, businesses can identify areas of improvement for their products or services, leading to better offerings that align with customer needs and preferences. The database can aid in monitoring the quality of products or services, ensuring that they meet the required standards and reducing the likelihood of complaints.

    -	**Risk Management:** Identifying and addressing complaints promptly can help mitigate potential risks, such as legal disputes, reputation damage, or regulatory non-compliance.

    -	**Competitive Analysis:** Comparing complaint data with competitors can provide insights into relative strengths and weaknesses, allowing businesses to position themselves better in the market.

    -	**Compliance and Regulatory Reporting:**     Some industries and jurisdictions have specific regulations for handling consumer complaints. A centralized database can facilitate compliance and reporting requirements.

    -	**Employee Training and Development:** Analyzing complaints can highlight areas where employees may need additional training, leading to improved customer service and support.

    -	**Identifying Fraud and Abuse:** A database can help detect patterns of fraudulent activities or misuse, allowing businesses to take appropriate actions against offenders.

    -	**Predictive Analytics:** Applying data analytics to the complaint data can enable businesses to predict potential issues and take proactive measures to prevent complaints in the future.

    -	**Customer Insights and Segmentation:** Analyzing complaint data can provide valuable insights into customer preferences, pain points, and segmentation, enabling targeted marketing strategies.

    """)


    st.subheader('Tables Included')
    st.markdown("""
    - CFPB_DATA
    """)

    # Fields included section
    st.subheader('Fields Included')
    st.markdown("""
    -	DATE_RECEIVED
    -	PRODUCT 
    -	SUB_PRODUCT 
    -	ISSUE VARCHAR
    -	SUB_ISSUE 
    -	CONSUMER_COMPLAINT_NAME 
    -	COMPANY_PUBLIC_RESPONSE 
    -	COMPANY 
    -	STATE 
    -	ZIP_CODE 
    -	TAGS 
    -	COMSUMER_CONSENT_PROVIDED 
    -	SUBMITTED_VIA 
    -	DATE_SENT_TO_COMPANY 
    -	COMPANY_RESPONSE_TO_CONSUMER
    -	TIMELY_RESPONSE 
    -	CONSUMER_DISPUTE
    -	COMPLAINT_ID 
    """)

    # Closing section
    st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")
