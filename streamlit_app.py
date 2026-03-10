import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="Rita Yang | Portfolio", page_icon="📊", layout="wide")

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOAD DATA ---
def load_data():
    skills_data = {
        "Technical Skill": ["Python", "SQL", "R", "Tableau", "Power BI", "Machine Learning", "STATA"],
        "Proficiency (%)": [95, 90, 85, 80, 85, 80, 75],
        "Category": ["Language", "Database", "Language", "BI Tool", "BI Tool", "ML", "Stats"]
    }
    return pd.DataFrame(skills_data)

df_skills = load_data()

# --- SIDEBAR NAVIGATION (Requirement: Widget 1) ---
st.sidebar.image("https://via.placeholder.com/150", caption="Rita (Shuya) Yang") # You can replace with a real URL
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a Section:", ["Professional Summary", "Experience & Education", "Interactive Skills Lab"])

# --- HEADER ---
st.title("Rita (Shuya) Yang")
st.write("📍 Toronto, ON | 📧 shuya.yang@rotman.utoronto.ca | 🔗 [LinkedIn](https://linkedin.com)")
st.write("---")

# --- PAGE 1: SUMMARY ---
if page == "Professional Summary":
    st.subheader("Candidate: Master of Management Analytics (MMA)")
    st.write("""
    Results-driven Data Scientist with a strong background in Economics and Management Analytics. 
    Experienced in warehouse optimization, causal inference, and building end-to-end ML pipelines.
    """)
    
    # Requirement: Widget 2 (Checkbox)
    if st.checkbox("View Academic Honors"):
        st.success("🏆 1st Place: NaviGATE Case Competition")
        st.success("🏆 3rd Place: McGill Retail Innovation Challenge")
        st.success("🎓 Dean's List (2021-2024)")

# --- PAGE 2: EXPERIENCE & EDUCATION ---
elif page == "Experience & Education":
    st.header("Education")
    # Requirement: Table
    edu_data = {
        "Degree": ["Master of Management Analytics", "Honours BA (Economics)"],
        "Institution": ["University of Toronto, Rotman", "University of Toronto, St. George"],
        "Year": ["2025-2026", "2021-2025"]
    }
    st.table(pd.DataFrame(edu_data))

    st.header("Work History")
    # Requirement: Widget 3 (Selectbox)
    job_view = st.selectbox("Filter Experience:", ["Staples Canada (Co-op)", "Green Square Research", "Personal Projects"])
    
    if job_view == "Staples Canada (Co-op)":
        st.subheader("Data Scientist Co-op")
        st.write("- Developed warehouse slotting optimization to reduce picker travel time.")
        st.write("- Managed analytical datasets using SQL in BigQuery/GCP.")
    elif job_view == "Green Square Research":
        st.subheader("Data Science Intern")
        st.write("- Automated data ingestion and model execution workflows.")
        st.write("- Built ML models to forecast stock price movements.")
    else:
        st.subheader("Vaping Tax Policy Research")
        st.write("- Used Difference-in-Difference (DiD) methodology on 100k+ records.")

# --- PAGE 3: SKILLS LAB ---
elif page == "Interactive Skills Lab":
    st.header("Technical Proficiency")
    
    # Requirement: Chart
    # Widget 4 (Slider to filter skills by proficiency)
    min_skill = st.slider("Filter skills above proficiency level:", 0, 100, 80)
    filtered_df = df_skills[df_skills["Proficiency (%)"] >= min_skill]
    
    fig = px.bar(
        filtered_df, 
        x="Technical Skill", 
        y="Proficiency (%)", 
        color="Category",
        text_auto=True,
        title="My Top Technical Skills"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("This chart updates dynamically based on the slider above!")
