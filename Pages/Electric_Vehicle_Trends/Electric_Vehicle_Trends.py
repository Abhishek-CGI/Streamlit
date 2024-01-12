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
    The "Electric Vehicle Population" is a comprehensive and dynamic dataset that provides invaluable insights into the evolution of electric vehicle (EV) adoption across various geographic regions. This dataset meticulously tracks the historical growth of EV ownership, offering a granular breakdown by county, allowing businesses, government agencies, researchers, and policymakers to gain a deep understanding of the shifting landscape of sustainable transportation.
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
    **Retrieve all records from the view for vehicles with "Clean Alternative Fuel Vehicle (CAFV) Eligibility"**:
    ```sql
    SELECT *
    FROM VW_Vehicle_Population
    WHERE "Clean Alternative Fuel Vehicle (CAFV) Eligibility" IS NOT NULL;
    """)

# Query 2
    st.markdown("""
    **Count the total number of electric vehicles (EVs) and non-electric vehicles by state:**
    ```sql
    SELECT State,
       SUM(CASE WHEN "Electric Vehicle (EV) Total" IS NOT NULL THEN 1 ELSE 0 END) AS Total_EVs,
       SUM(CASE WHEN "Non-Electric Vehicle Total" IS NOT NULL THEN 1 ELSE 0 END) AS Total_Non_EVs
       FROM VW_Vehicle_Population
       GROUP BY State;
    """)

# Query 3
    st.markdown("""
    **3.	Find the average electric range of vehicles by "Model Year":**
    ```sql
    SELECT "Model Year",
       AVG("Electric Range") AS Avg_Electric_Range
    FROM VW_Vehicle_Population
    WHERE "Electric Range" IS NOT NULL
    GROUP BY "Model Year";

    """)

# Query 4
    st.markdown("""
    **4.	Get the top 5 counties with the highest percentage of electric vehicles (EVs) among "Total Vehicles":**
    ```sql
    SELECT County,
       "Percent Electric Vehicles"
    FROM VW_Vehicle_Population
    ORDER BY "Percent Electric Vehicles" DESC
    LIMIT 5;

    """)


    st.subheader('Business Needs')


    # Display the text in a blue box with custom styling
    st.markdown("""

    - **Government and Regulatory Compliance:** Many regions and governments have set targets and regulations related to electric vehicle (EV) adoption to reduce emissions. Businesses need to monitor EV population size by county to ensure compliance with these regulations.

    - **Policy Assessment:** Government incentives, tax breaks, and subsidies for EVs can significantly impact the adoption rate. Businesses and policymakers need data on historical population sizes to assess the effectiveness of such policies and make necessary adjustments.

    - **Market Analysis:** Businesses in the automotive industry, energy sector, and related industries rely on data about EV adoption trends to plan product offerings, marketing strategies, and infrastructure development. Tracking population history by county helps identify emerging markets and customer preferences.

    - **Charging Infrastructure Planning:** EV charging infrastructure needs to be strategically placed based on population density. Historical data by county helps businesses and governments plan the expansion of charging networks efficiently.

    - **Environmental Impact Assessment:** Companies with sustainability goals or those required to report on their carbon footprint use EV population data to estimate the environmental impact of EV adoption in different areas.

    - **Utility and Energy Planning:** Electric utilities monitor EV adoption to anticipate changes in electricity demand and plan for grid capacity and infrastructure upgrades.

    - **Competitive Analysis:** Businesses in the automotive industry use EV population data to benchmark their market share and competitive position in different regions.

    - **Marketing and Sales Strategies:** Companies in the EV industry use historical data to identify regions with high growth potential and tailor marketing and sales strategies to target those areas effectively.

    - **Insurance and Risk Assessment:** Insurance companies assess the risk associated with insuring EVs in different regions. Historical data informs risk models and pricing strategies.

    """)


    st.subheader('Tables Included')
    st.markdown("""
    - Vehicle_Population
    - vehicle_details
    """)

    # Fields included section
    st.subheader('Fields Included')
    st.markdown("""
    - VIN
    - County
    -	City
    -	State
    -	"Postal Code"
    -	"Model Year"
    -	Make
    -	Model
    -	"Electric Vehicle Type"
    -	"Clean Alternative Fuel Vehicle (CAFV) Eligibility"
    -	"Electric Range"
    -	"Base MSRP"
    -	"Legislative District"
    -	"DOL Vehicle ID"
    -	"Vehicle Location"
    -	"Electric Utility"
    -	"2020 Census Tract" VARCHAR(255)
    -	Vehicle Primary Use
    -	Battery Electric Vehicles (BEVs)
    -	Plug-In Hybrid Electric Vehicles (PHEVs)
    -	Electric Vehicle (EV) Total
    -	Non-Electric Vehicle Total
    -	Total Vehicles
    -	Percent Electric Vehicles


    """)

    # Closing section
    st.markdown("For further analysis and queries, please use the provided SQL queries with your Snowflake environment.")
