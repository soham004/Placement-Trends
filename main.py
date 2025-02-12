import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Placement Trends Analysis", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('dataset/Placement_Data_Full_Class.csv')
    return df

df = load_data()

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Academic Analysis", "Skills Analysis", "Placement Statistics"])

if page == "Overview":
    st.title("🎓 Placement Trends Analysis")
    st.markdown("### Dataset Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        total_students = len(df)
        placed_students = len(df[df['status'] == 'Placed'])
        placement_rate = (placed_students/total_students) * 100
        
        st.metric("Total Students", total_students)
        st.metric("Placed Students", placed_students)
        st.metric("Placement Rate", f"{placement_rate:.2f}%")
    
    with col2:
        fig = px.pie(df, names='status', title='Placement Status Distribution')
        st.plotly_chart(fig)

elif page == "Academic Analysis":
    st.title("📚 Academic Performance Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # SSC Percentage Distribution
        fig1 = px.histogram(df, x='ssc_p', color='status',
                          title='SSC Percentage Distribution by Placement Status',
                          barmode='group')
        st.plotly_chart(fig1)
    
    with col2:
        # HSC Percentage Distribution
        fig2 = px.histogram(df, x='hsc_p', color='status',
                          title='HSC Percentage Distribution by Placement Status',
                          barmode='group')
        st.plotly_chart(fig2)
    
    # Degree Percentage Distribution
    fig3 = px.histogram(df, x='degree_p', color='status',
                      title='Degree Percentage Distribution by Placement Status',
                      barmode='group')
    st.plotly_chart(fig3)

elif page == "Skills Analysis":
    st.title("🔧 Skills & Activities Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Work Experience Distribution
        fig1 = px.histogram(df, x='workex', color='status', 
                          title='Work Experience Distribution by Placement Status',
                          barmode='group')
        st.plotly_chart(fig1)
    
    with col2:
        # E-test Percentage Distribution
        fig2 = px.histogram(df, x='etest_p', color='status',
                          title='E-test Percentage Distribution by Placement Status',
                          barmode='group')
        st.plotly_chart(fig2)
    
    # MBA Percentage Distribution
    fig3 = px.histogram(df, x='mba_p', color='status',
                      title='MBA Percentage Distribution by Placement Status',
                      barmode='group')
    st.plotly_chart(fig3)

else:  # Placement Statistics
    st.title("📊 Placement Statistics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Placement by Degree Specialization
        degree_placement = df.groupby('degree_t')['status'].value_counts().unstack()
        fig1 = px.pie(names=degree_placement.index, 
                     values=degree_placement['Placed'],
                     title='Placement Distribution by Degree Specialization')
        st.plotly_chart(fig1)
    
    with col2:
        # Placement Rate by Degree Specialization
        placement_trend = df.groupby(['degree_t', 'status']).size().unstack()
        placement_rate = (placement_trend['Placed'] / (placement_trend['Placed'] + placement_trend['Not Placed'])) * 100
        fig2 = px.line(x=placement_rate.index, y=placement_rate.values,
                      title='Placement Rate by Degree Specialization',
                      labels={'x': 'Degree Specialization', 'y': 'Placement Rate (%)'})
        st.plotly_chart(fig2)

    # Salary Distribution
    fig3 = px.histogram(df[df['salary'].notnull()], x='salary', color='status',
                      title='Salary Distribution by Placement Status',
                      barmode='group')
    st.plotly_chart(fig3)

# Footer
st.markdown("---")
st.markdown("### 📝 Notes")
st.markdown("""
- The analysis is based on the provided placement dataset
- Percentage in SSC, HSC, and Degree appears to be significant factors in placement
- Degree specialization in Sci&Tech and Comm&Mgmt are much demanded by corporate
- Students with work experience tend to have higher placement rates
""")