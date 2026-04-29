import streamlit as st
import pandas as pd
import plotly.express as px
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stTextInput input {
        border-radius: 10px;
        padding: 10px;
    }
    .css-1d391kg {
        padding: 20px;
    }
    </style>
""", unsafe_allow_html=True)
df = pd.read_csv("jobs.csv")
df['skills'] = df['skills'].str.lower().str.split(',')
all_skills = sum(df['skills'], [])
skill_freq = pd.Series(all_skills).value_counts()
st.markdown("<h1 style='text-align: center;'>🚀 AI Job Market Dashboard</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.metric("📊 Total Jobs", len(df))
col2.metric("💰 Avg Salary", int(df['salary'].mean()))
col3.metric("🔥 Top Skill", skill_freq.idxmax())
st.subheader("📊 Top Skills")
st.bar_chart(skill_freq.head(5))
role = st.selectbox("Select Job Role", df['job_title'].unique())
user_input = st.text_input("Enter your skills")

if user_input:
    user = [s.strip() for s in user_input.lower().split(",")]

# Load data
df = pd.read_csv("jobs.csv")

# Clean skills
df['skills'] = df['skills'].str.lower().str.split(',')

# Flatten skills
all_skills = sum(df['skills'], [])

# Frequency
skill_freq = pd.Series(all_skills).value_counts()

# UI
st.title("AI-Powered Job Market Analyzer")

st.subheader("📊 Top Skills in Market")


fig = px.bar(
    x=skill_freq.head(5).index,
    y=skill_freq.head(5).values,
    title="Top Skills Demand",
    color=skill_freq.head(5).values
)

st.plotly_chart(fig)

st.subheader("💰 Average Salary")
st.write(f"₹ {int(df['salary'].mean()):,}")
# 🔥 Role-based analysis
role = st.selectbox("🎯 Select Job Role", df['job_title'].unique())

filtered_df = df[df['job_title'] == role]

skills_role = sum(filtered_df['skills'], [])
skill_freq_role = pd.Series(skills_role).value_counts()

st.subheader(f"📊 Skills for {role}")
st.bar_chart(skill_freq_role.head(5), use_container_width=True)

st.subheader("🧠 Check Your Skill Match")

user_input = st.text_input("Enter your skills (comma separated)")

if user_input:

    user = [s.strip() for s in user_input.lower().split(",")]

    top_skills = skill_freq.head(5).index.tolist()

    match = [s for s in user if s in top_skills]
    missing = [s for s in top_skills if s not in user]

    score = (len(match)/len(top_skills))*100

    st.success(f"✅ Match Score: {score:.2f}%")
    st.progress(int(score))

    if missing:
        st.warning("⚠️ Recommended Skills: " + ", ".join(missing))
    else:
        st.success("🔥 You are job-ready!")

# 👇 ये if के बाहर होना चाहिए (ELSE नहीं)
if not user_input:
    st.info("👉 Enter skills to check your match")