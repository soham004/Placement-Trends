# Placement-Trends

## Overview
This project is a Streamlit application that provides insights into placement trends using a dataset of student placements. The application allows users to explore various factors influencing recruitment through interactive charts and graphs.

## Features
- **Overview**: Displays key metrics such as total students, placed students, and placement rate. Includes a pie chart showing the distribution of placement status.
- **Academic Analysis**: Analyzes academic performance with histograms for CGPA distribution and a line chart for academic performance trends (SSC Marks, HSC Marks, CGPA).
- **Skills Analysis**: Examines the impact of skills and activities on placement with histograms for projects, internships, soft skills rating, and aptitude test scores.
- **Placement Statistics**: Provides detailed placement statistics with pie charts for placement distribution by projects and line charts for placement rate trends. Also includes a histogram for workshops/certifications distribution.

## Dataset
The dataset used in this project is `Placement.csv`, which contains the following columns:
- `StudentID`: Unique identifier for each student
- `CGPA`: Cumulative Grade Point Average
- `Internships`: Number of internships completed
- `Projects`: Number of projects completed
- `Workshops/Certifications`: Number of workshops or certifications completed
- `AptitudeTestScore`: Score in the aptitude test
- `SoftSkillsRating`: Rating of soft skills
- `ExtracurricularActivities`: Participation in extracurricular activities (Yes/No)
- `PlacementTraining`: Participation in placement training (Yes/No)
- `SSC_Marks`: Marks obtained in SSC (Secondary School Certificate)
- `HSC_Marks`: Marks obtained in HSC (Higher Secondary Certificate)
- `PlacementStatus`: Placement status (Placed/NotPlaced)

## Installation
To run the application, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Placement-Trends.git
    cd Placement-Trends
    ```

2. Install the required packages:
    ```bash
    pip install streamlit pandas plotly
    ```

3. Run the application:
    ```bash
    streamlit run main.py
    ```

## Usage
- Navigate to different sections using the sidebar.
- Explore various charts and graphs to gain insights into placement trends.
- Filter and analyze data based on different attributes.

## Notes
- The analysis is based on the provided placement dataset.
- CGPA appears to be a significant factor in placement.
- Students with more projects and internships tend to have higher placement rates.

## License
This project is licensed under the MIT License.

## Acknowledgements
- The dataset used in this project is fictional and created for demonstration purposes.
- Special thanks to the Streamlit and Plotly communities for their excellent tools and documentation.