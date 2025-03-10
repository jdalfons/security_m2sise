import streamlit as st
from streamlit_option_menu import option_menu
from db import Database, LogDatabase
from .analysis import analyze_logs  #
from .data import explore_data  
from .protocol import analyze_flows  

def user_page():
    """User Dashboard page."""

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
        st.title("Analyse des logs de sécurité")
        analyze_logs()
        
    elif selected_tab == "Datasets":
        st.title("Exploration des données")
        explore_data()
    elif selected_tab == "Protocol":  # Fixed typo in "Protocol"
        st.title("Statistiques des flux réseau par protocole")
        analyze_flows()

    elif selected_tab == "Machine Learning":
        st.write("Machine Learning content coming soon!")
        st.markdown("""
            **Planned Features:**
            - Model training
            - Prediction analysis
            - Model evaluation
        """)
    
   # Quick links section after filters and content
    st.markdown("---")
    st.markdown("### Quick Links")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📄 Documentation"):
            st.write("Redirecting to documentation...")
            # Redirection vers la page de documentation
            st.session_state.current_page = "Documentation"
            st.experimental_rerun()
    with col2:
        if st.button("🛠️ Settings"):
            st.write("Redirecting to settings...")
    with col3:
        if st.button("📤 Logout"):
            st.write("Logging out...")
            # Add logout logic here
