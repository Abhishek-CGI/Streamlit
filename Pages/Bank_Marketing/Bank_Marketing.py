import streamlit as st

def show():
    # st.set_page_config(page_title="Bank Churn Customers ", page_icon="pages/image/logo.png")

    # Create two columns
    # col1, col2 = st.columns([1, 5])

    # Add the logo to the first column
    # col1.image("pages\image\Insights by CG Infinity 1.png", width=100)

    # Add the text to the second column
    st.write("# Bank Marketing")


    # Text to be displayed in the blue box
    info_text = """
    The "Bank Marketing Campaign Analysis Dataset" provides comprehensive data and insights derived from the analysis of a previous marketing campaign conducted by a financial institution. This dataset is designed to facilitate strategic decision-making for the institution's future marketing efforts. By examining the patterns, trends, and outcomes of the past campaign, marketers, analysts, and stakeholders can draw valuable conclusions to enhance the effectiveness of upcoming marketing strategies.
    """

    # Display the text in a blue box with custom styling
    st.markdown(
        f'<div style="background-color: #D3D3D3; padding: 20px; border-radius: 10px;">{info_text}</div>',
        unsafe_allow_html=True,
    )

    # Datasets section
    st.subheader('Factors Contributing to Churn')

    # Create an expandable box
    with st.expander("**Financial Performance**"):
        # Content inside the expandable box
        st.write("Changes in a customer's financial situation, such as reduced income, increased debt, or unemployment, can lead to decreased engagement with banking services.")
        
    # Create an expandable box
    with st.expander("**Service Dissatisfaction**"):
        # Content inside the expandable box
        st.write("Poor customer service experiences, unresolved issues, or dissatisfaction with the quality of services provided by the bank can drive customers to seek alternatives. ")
        
    # Create an expandable box
    with st.expander("**Competitive Offerings**"):
        # Content inside the expandable box
        st.write("Customers might be enticed by competitive offerings from other banks, such as better interest rates, lower fees, or innovative financial products.")
        
    # Create an expandable box
    with st.expander("**Life Events**"):
        # Content inside the expandable box
        st.write("Major life events like relocation, marriage, divorce, or retirement can prompt customers to reassess their banking relationships and potentially switch to institutions that better align with their changing needs.")
        
    # Create an expandable box
    with st.expander("**Lack of Relevance**"):
        # Content inside the expandable box
        st.write("If a bank fails to offer personalized solutions and relevant financial products to customers, they may feel neglected and seek banking services elsewhere.")
        
    # Create an expandable box
    with st.expander("**Technological Changes**"):
        # Content inside the expandable box
        st.write("Rapid advancements in digital technology and online banking can influence customer preferences, causing them to shift to banks that offer more convenient and user-friendly digital experiences.")
    
    

    # SQL Queries section
    st.subheader('SQL Queries')

    # Query 1
    st.markdown("""
    **View First few rows of the dataset:**
    ```sql
    SELECT *
    FROM BMarketingData
    LIMIT 10;
    ```""")

    # Query 2
    st.markdown("""
    **Analyse the distribution of education level by Age:**
    ```sql
    SELECT education,
    COUNT(*) AS age
    FROM BMarketingData
    GROUP BY education
    ORDER BY Age DESC;
    ```""")

    # Query 3
    st.markdown("""
    **Identify the average age of those who have subscribed to a deposit:**
    ```sql
    SELECT AVG(age) AS avg_age_subscribed
    FROM BMarketingData 
    WHERE y = 'yes';
    ```""")

    st.subheader('Business Needs')

    st.markdown("""
    The dataset encompasses a wide range of variables that shed light on the performance and impact of the bank's previous marketing campaign. It includes details about the campaign's target audience, communication channels used, campaign duration, and various engagement metrics. The dataset also incorporates customer demographic information, such as age, gender, education level, and marital status.""")

    st.markdown("""
    - **Campaign Performance Evaluation:** The dataset enables the assessment of the previous marketing campaign's 
    effectiveness in terms of customer engagement, response rates, and conversion metrics. This evaluation guides 
    the institution in understanding what worked well and what areas need improvement.

    - **Audience Segmentation Refinement:** By analyzing demographic information and customer characteristics, the 
    dataset helps refine audience segmentation strategies. Businesses can tailor their marketing efforts to resonate 
    with specific customer segments based on their preferences, behaviors, and demographic profiles.

	- **Channel Optimization:** Understanding the communication channels that yielded the highest engagement and conversion 
    rates allows the institution to allocate resources more effectively. It guides decisions on which channels to 
    prioritize and invest in for future campaigns.

	- **Campaign Duration Insights:** Analyzing the campaign's start and end dates in relation to engagement and 
    conversion rates can provide insights into the optimal duration for future marketing initiatives.

	- **Targeting New Customers:** By examining the number of new customers acquired as a result of the campaign, 
    the dataset helps the institution assess its ability to attract and convert prospects. This information informs 
    strategies for expanding the customer base.

	- **Customer Behavior Changes:** The dataset's outcome variables provide insights into how the campaign influenced 
    customer behavior post-engagement. This information can guide strategies for nurturing customer relationships 
    and driving long-term value.

	- **Continuous Improvement:** The dataset supports a culture of continuous improvement by providing a data-driven
    feedback loop for marketing strategies. Insights from previous campaigns guide iterative enhancements for future initiatives.
    """)

    st.subheader('Tables Included')
    st.markdown("""
    - BMARKETING_DATA
    """)

    # Fields included section
    st.subheader('Fields Included')
    st.markdown("""
    -   AGE 
    -	JOB 
    -	MARITAL_STATUS
    -	EDUCATION 
    -	DEFAULT 
    -	BALANCE 
    -	HOUSING
    -	LOAN
    -	CONTACT 
    -	DAY 
    -	MONTH
    -	DURATION,
    -	CAMPAIGN 
    -	PREVIOUS_DAYS 
    -	PREVIOUS
    -	PREVIOUS_OUTCOME
    -	DESPOSIT

    """)

    # Closing section
    st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")



