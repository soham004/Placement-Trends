import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Placement Trends Analysis", layout="wide")
# st.markdown(
#     """
#     <style>
#         section[data-testid="stSidebar"] {
#             width: 200px !important; # Set the width to your desired value
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('dataset/Placement.csv')
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
        placed_students = len(df[df['PlacementStatus'] == 'Placed'])
        placement_rate = (placed_students/total_students) * 100
        
        st.metric("Total Students", total_students)
        st.metric("Placed Students", placed_students)
        st.metric("Placement Rate", f"{placement_rate:.2f}%")
    
    with col2:
        fig = px.pie(df, names='PlacementStatus', title='Placement Status Distribution')
        st.plotly_chart(fig)

elif page == "Academic Analysis":
    st.title("📚 Academic Performance Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # CGPA Distribution
        fig1 = px.histogram(df, x='CGPA', color='PlacementStatus',
                          title='CGPA Distribution by Placement Status',
                          barmode='group')
        st.plotly_chart(fig1)
    
    with col2:
        # Academic Performance Trend
        academic_metrics = ['SSC_Marks', 'HSC_Marks', 'CGPA']
        avg_scores = df.groupby('PlacementStatus')[academic_metrics].mean().reset_index()
        
        # Create a long-format dataframe for plotting
        avg_scores_melted = pd.melt(avg_scores, 
                                  id_vars=['PlacementStatus'],
                                  value_vars=academic_metrics,
                                  var_name='Academic Metrics',
                                  value_name='Average Score')
        
        fig2 = px.line(avg_scores_melted, 
                      x='Academic Metrics', 
                      y='Average Score',
                      color='PlacementStatus',
                      title='Academic Performance Trend',
                      markers=True)
        st.plotly_chart(fig2)

elif page == "Skills Analysis":
    st.title("🔧 Skills & Activities Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Projects Distribution
        fig1 = px.histogram(df, x='Projects', color='PlacementStatus', 
                          title='Projects Distribution',
                          barmode='group')
        st.plotly_chart(fig1)
    
    with col2:
        # Internships Distribution
        fig2 = px.histogram(df, x='Internships', color='PlacementStatus',
                          title='Internships Distribution',
                          barmode='group')
        st.plotly_chart(fig2)
    
    # Skills Distribution
    col3, col4 = st.columns(2)
    
    with col3:
        fig3 = px.histogram(df, x='SoftSkillsRating', color='PlacementStatus',
                          title='Soft Skills Rating Distribution',
                          barmode='group')
        st.plotly_chart(fig3)
    
    with col4:
        fig4 = px.histogram(df, x='AptitudeTestScore', color='PlacementStatus',
                          title='Aptitude Test Score Distribution',
                          barmode='group')
        st.plotly_chart(fig4)

else:  # Placement Statistics
    st.title("📊 Placement Statistics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Placement by Projects
        projects_placement = df.groupby('Projects')['PlacementStatus'].value_counts().unstack()
        fig1 = px.pie(names=projects_placement.index, 
                     values=projects_placement['Placed'],
                     title='Placement Distribution by Projects')
        st.plotly_chart(fig1)
    
    with col2:
        # Placement Rate Trend
        placement_trend = df.groupby(['Projects', 'PlacementStatus']).size().unstack()
        placement_rate = (placement_trend['Placed'] / (placement_trend['Placed'] + placement_trend['NotPlaced'])) * 100
        fig2 = px.line(x=placement_rate.index, y=placement_rate.values,
                      title='Placement Rate Trend',
                      labels={'x': 'Number of Projects', 'y': 'Placement Rate (%)'})
        st.plotly_chart(fig2)

    # Workshops/Certifications Distribution
    fig3 = px.histogram(df, x='Workshops/Certifications', color='PlacementStatus',
                      title='Workshops/Certifications Distribution',
                      barmode='group')
    st.plotly_chart(fig3)

# Footer
st.markdown("---")
st.markdown("### 📝 Notes")
st.markdown("""
- The analysis is based on the provided placement dataset
- CGPA appears to be a significant factor in placement
- Students with more projects and internships tend to have higher placement rates
""")