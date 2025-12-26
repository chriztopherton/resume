import plotly.graph_objects as go
import streamlit as st


def skills_page(skills_data):
    st.markdown('<h2 class="section-header">Technical Skills</h2>', unsafe_allow_html=True)

    # Create tabs for different skill categories
    tabs = st.tabs(list(skills_data.keys()))

    for tab, (category, skills) in zip(tabs, skills_data.items()):
        with tab:
            skills_html = "".join([f'<span class="skill-badge">{skill}</span>' for skill in skills])
            st.markdown(
                f'<div style="display: flex; flex-wrap: wrap; gap: 4px;">{skills_html}</div>',
                unsafe_allow_html=True,
            )

    # Skills visualization
    st.markdown("### Skills Overview")

    # Create a radar chart for skill categories
    categories = list(skills_data.keys())
    skill_counts = [len(skills) for skills in skills_data.values()]

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=skill_counts,
            theta=categories,
            fill="toself",
            name="Skills Distribution",
            line_color="#3498db",
        )
    )

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, max(skill_counts) + 2])),
        showlegend=False,
        title="Skills Distribution by Category",
    )

    st.plotly_chart(fig, use_container_width=True)
