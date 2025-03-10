import streamlit as st
from streamlit_option_menu import option_menu
from db import Database, LogDatabase
from .analysis import analyze_logs  #
from .data import explore_data  
from .protocol import analyze_flows  

def user_page():
    """User Dashboard page."""

    # Title
    st.title(f"User Dashboard - Welcome, {st.session_state.username}!")

    # Sidebar navigation with streamlit-option-menu
    with st.sidebar:
        # Navigation menu with icons
        selected_tab = option_menu(
            menu_title=None,  # Added menu_title parameter
            options=["Home", "Analysis", "Datasets", "Protocol", "Machine Learning"],  # Fixed typo in "Protocol"
            icons=["house", "bar-chart", "search", "robot", "cpu"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "5px", "background-color": "#f0f2f6"},
                "icon": {"color": "orange", "font-size": "18px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "color": "black"},
                "nav-link-selected": {"background-color": "#4CAF50", "color": "white"},
            }
        )

        # Quick links section
        st.markdown("---")
        st.markdown("### Quick Links")
        if st.button("📄 Documentation"):
            st.write("Redirecting to documentation...")
        if st.button("🛠️ Settings"):
            st.write("Redirecting to settings...")
        if st.button("📤 Logout"):
            st.write("Logging out...")
            # Add logout logic here

    # Content based on selection
    if selected_tab == "Home":
        st.write("Welcome to the Security M2 SISE dashboard!")
        st.markdown("""
            **Overview:**
            - View your security logs
            - Analyze data trends
            - Explore datasets
            - Apply machine learning models
        """)

    elif selected_tab == "Analysis":
        analyze_logs()
        
    elif selected_tab == "Datasets":
        explore_data()
    elif selected_tab == "Protocol":  # Fixed typo in "Protocol"
        st.write("Protocol content coming soon!")  # Fixed typo in "Protocol"
        analyze_flows()

    elif selected_tab == "Machine Learning":
        st.write("Machine Learning content coming soon!")
        st.markdown("""
            **Planned Features:**
            - Model training
            - Prediction analysis
            - Model evaluation
        """)

    # Example of database usage (uncomment if needed)
    # db = LogDatabase()
    # logs = db.get_all_logs()
    # st.table(logs)
