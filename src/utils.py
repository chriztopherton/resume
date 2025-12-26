import pandas as pd
import plotly.express as px
import streamlit as st


def create_timeline_chart(experience_data):
    """Create a timeline visualization of work experience"""
    timeline_data = []

    for job in experience_data:
        # Parse dates (simplified - you might want to add proper date parsing)
        start_date = job["duration"].split(" - ")[0]
        end_date = job["duration"].split(" - ")[1] if " - " in job["duration"] else "Present"

        timeline_data.append(
            {
                "Company": job["company"],
                "Title": job["title"],
                "Start": start_date,
                "End": end_date,
                "Duration": job["duration"],
            }
        )

    df = pd.DataFrame(timeline_data)

    # Create a simple timeline visualization
    fig = px.timeline(
        df,
        x_start="Start",
        x_end="End",
        y="Company",
        title="Professional Timeline",
        color="Company",
        hover_data=["Title", "Duration"],
    )

    fig.update_layout(height=400, showlegend=False, xaxis_title="Time", yaxis_title="Company")

    return fig


def create_skills_heatmap(skills_data):
    """Create a heatmap visualization of skills by category"""
    # Flatten skills data for heatmap
    heatmap_data = []

    for category, skills in skills_data.items():
        for skill in skills:
            heatmap_data.append({"Category": category, "Skill": skill, "Count": 1})

    df = pd.DataFrame(heatmap_data)

    # Create pivot table for heatmap
    pivot_df = df.pivot_table(index="Category", columns="Skill", values="Count", fill_value=0)

    fig = px.imshow(
        pivot_df, title="Skills Heatmap by Category", color_continuous_scale="Blues", aspect="auto"
    )

    fig.update_layout(height=500, xaxis_title="Skills", yaxis_title="Categories")

    return fig


def create_achievement_metrics(experience_data):
    """Extract and display key achievement metrics"""
    metrics = {
        "Total Experience": len(experience_data),
        "Companies Worked": len(set(job["company"] for job in experience_data)),
        "Technologies Used": len(
            set(tech for job in experience_data for tech in job["technologies"])
        ),
        "Key Achievements": sum(len(job["achievements"]) for job in experience_data),
    }

    return metrics


def format_duration(duration_str):
    """Format duration string for better display"""
    if "Present" in duration_str:
        return duration_str.replace("Present", "Current")
    return duration_str


def get_skill_proficiency_level(skill, experience_data):
    """Determine skill proficiency based on usage in experience"""
    usage_count = 0
    recent_usage = False

    for job in experience_data:
        if skill in job["technologies"]:
            usage_count += 1
            # Check if it's recent experience (last 2 years)
            if (
                "2023" in job["duration"]
                or "2024" in job["duration"]
                or "Present" in job["duration"]
            ):
                recent_usage = True

    if usage_count >= 2 and recent_usage:
        return "Expert"
    elif usage_count >= 2:
        return "Advanced"
    elif usage_count >= 1:
        return "Intermediate"
    else:
        return "Beginner"


def create_skill_proficiency_chart(skills_data, experience_data):
    """Create a chart showing skill proficiency levels"""
    proficiency_data = []

    for category, skills in skills_data.items():
        for skill in skills:
            proficiency = get_skill_proficiency_level(skill, experience_data)
            proficiency_data.append(
                {"Category": category, "Skill": skill, "Proficiency": proficiency}
            )

    df = pd.DataFrame(proficiency_data)

    # Count proficiency levels
    proficiency_counts = df["Proficiency"].value_counts()

    fig = px.pie(
        values=proficiency_counts.values,
        names=proficiency_counts.index,
        title="Skill Proficiency Distribution",
        color_discrete_sequence=px.colors.qualitative.Set3,
    )

    fig.update_layout(height=400)

    return fig


def create_project_impact_chart(projects_data):
    """Create a chart showing project impact metrics"""
    # Extract impact keywords and create metrics
    impact_keywords = {"reduced": 0, "improved": 0, "deployed": 0, "automated": 0, "enhanced": 0}

    for project in projects_data:
        impact_lower = project["impact"].lower()
        for keyword in impact_keywords:
            if keyword in impact_lower:
                impact_keywords[keyword] += 1

    # Create bar chart
    fig = px.bar(
        x=list(impact_keywords.keys()),
        y=list(impact_keywords.values()),
        title="Project Impact Types",
        labels={"x": "Impact Type", "y": "Count"},
    )

    fig.update_layout(height=400, showlegend=False)

    return fig


def add_download_resume_button():
    """Add a download button for the PDF resume"""
    st.markdown("---")
    st.markdown("### Download Resume")

    # You can add a PDF file here later
    st.info(
        "PDF version coming soon! For now, you can view the full resume in the Experience section."
    )

    # Placeholder for future PDF download functionality
    # with open("main.pdf", "rb") as pdf_file:
    #     PDFbyte = pdf_file.read()
    #     st.download_button(
    #         label="Download PDF Resume",
    #         data=PDFbyte,
    #         file_name="Christopher_Ton_Resume.pdf",
    #         mime="application/pdf"
    #     )


def create_contact_form_validation():
    """Validate contact form inputs"""

    def validate_email(email):
        import re

        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    return validate_email
