import streamlit as st
from streamlit import markdown

def show():
    # st.set_page_config(
    # page_title="InSights",
    # page_icon="pages/image/img111.png"
    # )

    # Create two columns
    # col1, col2 = st.columns([1, 5])

    # Add the logo to the first column
    # col1.image("Pages/image/Insights by CG Infinity 1.png", width=100)

    # Add the text to the second column
    st.write("# Welcome to InSights by CG!")

    # st.sidebar.success("Select a documentations above.")

    st.markdown(
        """
    Welcome to InSights, the pinnacle of global decision-making data by CG Infinity. 
    Our cutting-edge data technology solutions compress data discovery to insights, saving time, effort, and budget. 
    Empower individuals and enterprises to explore, visualize, model, and present data for informed decisions and better business outcomes. 
    Revolutionize your world with InSights!
    """
    )

    st.subheader("Snowflake Marketplace")

    st.image("Pages/image/snowflake_marketplace.png", width=700)

    st.markdown("""  
        Snowflake Marketplace: Central hub for data and applications in the Snowflake Data Cloud, enabling
        organizations to easily acquire and share resources for data-driven initiatives.Here's a breakdown of its key features.

        **Benefits for users:**

        -  **Accelerated Analytics:** Save time on data pipelines and integrations within Snowflake, speeding up the path to insights.

        -  **Enhanced Data Exploration:** Access a diverse marketplace of external datasets to enrich analyses and discover new opportunities.

        -  **Easy Data Management:** Utilize readily available data governance and security services, simplifying data management tasks.

        -  **Efficient App Development:** Quickly build data-driven applications with pre-built Snowflake Native Apps, streamlining 
           development processes.
    """)

    # st.subheader("SnowChat")

    # st.markdown(
    #     """snowChat is an intuitive and user-friendly application that allows users to interact with their 
    #     Snowflake data using natural language queries. Type in your questions or requests, and SnowChat will 
    #     generate the appropriate SQL query and return the data you need. No more complex SQL queries or digging 
    #     through tables - SnowChat makes it easy to access your data! By bringing data one step closer, SnowChat 
    #     empowers users to make data-driven decisions faster and more efficiently, reducing the barriers between 
    #     users and the insights they seek.
    #     """
    # )

    st.subheader("Data Products")

    # Text to be displayed in the blue box
    # data_head1 = """ Banking Analytics Bundle """
    # data_info1 = """ Empowering financial decisions with comprehensive banking data for strategic insights and optimal outcomes. """
    # # Display the text in a blue box with custom styling
    # st.markdown(
    #     f'<div style="background-color: #D9EAF8; padding: 20px; border-radius: 10px;"><div>{data_head1}</div>{data_info1}</div>',
    #     unsafe_allow_html=True,
    # )
    # Create an expandable box
    with st.expander("**Banking Analytics Bundle** "):
        # Content inside the expandable box
        st.write("Empowering financial decisions with comprehensive banking data for strategic insights and optimal outcomes.")

    # Create an expandable box
    with st.expander("**Federal Financial Institutions Package** "):
        # Content inside the expandable box
        st.write("FFIEC provides U.S. banking data, reports, & insights for regulatory analysis and industry understanding.")

    # Create an expandable box
    with st.expander("**Bank Marketing** "):
        # Content inside the expandable box
        st.write("Find datasets an Promoting services, engaging customers,driving growth & insights on customer churn trends.")

    # Create an expandable box
    with st.expander("**Demographics Data Bundle** "):
        # Content inside the expandable box
        st.write("Statistical info about a population's characteristics like age, gender, income, ethnicity, and more.")

    # Create an expandable box
    with st.expander("**National Credit Union Administration (NCUA)** "):
        # Content inside the expandable box
        st.write("The NCUA keeps your credit union deposits safe and helps credit unions thrive.")

    # Create an expandable box
    with st.expander("**Layoff Data** "):
        # Content inside the expandable box
        st.write("Advance warning of mass job losses in the US, helping workers, governments, and individuals stay informed.")

    # Create an expandable box
    with st.expander("**Indicators of Health Insurance Coverage at the Time of Interview** "):
        # Content inside the expandable box
        st.write("Informational matter which is published as an individual document at Government expense.")

    # Create an expandable box
    with st.expander("**SEC Analytics** "):
        # Content inside the expandable box
        st.write("Documents by publicly traded companies to U.S. Securities and Exchange Commission that provide information.")

    # Create an expandable box
    with st.expander("**Consumer Financial Protection Bureau Analysis** "):
        # Content inside the expandable box
        st.write("Consumer data on Consumer insights, risk mitigation, competitive edge, compliance, and predictive analytics.")

    # Create an expandable box
    with st.expander("**Federal Exchange Rates** "):
        # Content inside the expandable box
        st.write("Dataset provides currency conversation rates, vital for global trade, finance, and investment decisions.")

    # Create an expandable box
    with st.expander("**Lottery Mega Millions Winning Numbers** "):
        # Content inside the expandable box
        st.write("Dataset contains information about the winning numbers and details from the Mega Millions lottery draws.")

    # Create an expandable box
    with st.expander("**Electric Vehicle Trends(EV)** "):
        # Content inside the expandable box
        st.write("Tracking the rise of Electric Vehicles on the Road")

    # Create an expandable box
    with st.expander("**Global Landslide Catalog Export** "):
        # Content inside the expandable box
        st.write("Goal of identifying nature-triggered events around the world, regardless of size, impacts or location.")

    # # Define your heading and paragraph text
    # heading = "**Your Heading Here**"
    # paragraph = "This is a paragraph inside the box. You can replace this text with your own content."

    # # Create the box with Markdown and styling
    # box = markdown(
    #     f"""
    #     <div style="padding: 1rem; border: 1px solid #ddd; border-radius: 5px;">
    #         {heading}
    #         <br />
    #         {paragraph}
    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )

    # # Display the box in Streamlit
    # st.write(box)

    st.subheader("About")

    st.markdown(""" People First + Driven to Transform """)

    # Create an expandable box
    with st.expander("**Our Mission** "):
        # Content inside the expandable box
        st.write("Our people-first approach drives innovation and transforms tomorrow. We aim to grow employees to deliver world class customer-value and customer experience.")


    # Create an expandable box
    with st.expander("**Our Values** "):
        # Content inside the expandable box
        st.subheader("Integrity")
        st.write("The only way to build trust is through transparency and integrity. So our team will do what's right even when it isn't easy.")

        st.subheader("Value")
        st.write("Our commitment is to deliver world-class services that exceeds expectations within a culture of excellence and transparency.")

        st.subheader("Excellence")
        st.write("It's about people, not just technology. We aspire to surpass our clients' goals through excellence in service and outcomes.")


    # Create an expandable box
    with st.expander("**Our Vision** "):
        # Content inside the expandable box
        st.write("We strive to be the top technology consulting brand and lead the market in implementing cutting-edge technologies with premium expertise, communication, and value.")

    # Create an expandable box
    with st.expander("**Our Leaders** "):
        # Content inside the expandable box
        st.write("It’s not just about technology, it’s about your business. At CG Infinity, we collaborate with you one-on-one to deliver only the best solutions for your company. Contact us today, and let’s start the conversation.")
