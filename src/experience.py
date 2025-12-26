from datetime import datetime

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


def experience_page(experience_data):
    st.markdown('<h2 class="section-header">Professional Experience</h2>', unsafe_allow_html=True)

    # Experience overview with metrics
    st.markdown("### Experience Overview")

    # Interactive experience timeline
    st.markdown("### Career Timeline")

    # Create Gantt chart data
    gantt_data = []
    colors = ["#3498db", "#e74c3c", "#2ecc71", "#f39c12", "#9b59b6", "#1abc9c", "#34495e"]

    for i, job in enumerate(reversed(experience_data)):
        # Parse duration to get start and end dates
        duration = job["duration"]
        if " - " in duration:
            start_str, end_str = duration.split(" - ")
            # Convert to datetime objects and then to strings for Plotly
            try:
                start_date = datetime.strptime(start_str.strip(), "%b %Y")
                if end_str.strip() == "Present":
                    end_date = datetime.now()
                else:
                    end_date = datetime.strptime(end_str.strip(), "%b %Y")

                # Convert to string format for Plotly
                start_str_formatted = start_date.strftime("%Y-%m-%d")
                end_str_formatted = end_date.strftime("%Y-%m-%d")
            except Exception:
                # Fallback if parsing fails
                start_str_formatted = "2020-01-01"
                end_str_formatted = "2024-12-31"
        else:
            start_str_formatted = "2020-01-01"
            end_str_formatted = "2024-12-31"

        gantt_data.append(
            {
                "Company": job["company"],
                "Title": job["title"],
                "Start": start_str_formatted,
                "End": end_str_formatted,
                "Duration": job["duration"],
                "Location": job["location"],
                "Color": colors[i % len(colors)],
            }
        )

    gantt_df = pd.DataFrame(gantt_data)

    # Create longitudinal timeline
    fig_gantt = go.Figure()

    # Add the main timeline bar
    fig_gantt.add_trace(
        go.Scatter(
            x=[gantt_df["Start"].min(), gantt_df["End"].max()],
            y=[0, 0],
            mode="lines",
            line=dict(color="#34495e", width=8),
            name="Timeline",
            showlegend=False,
            hoverinfo="skip",
        )
    )

    # Add experience segments and annotations
    for i, row in gantt_df.iterrows():
        start_date = datetime.strptime(row["Start"], "%Y-%m-%d")
        end_date = datetime.strptime(row["End"], "%Y-%m-%d")

        # Add experience segment
        fig_gantt.add_trace(
            go.Scatter(
                x=[row["Start"], row["End"]],
                y=[0, 0],
                mode="lines",
                line=dict(color=row["Color"], width=12),
                name=row["Company"],
                showlegend=False,
                hovertemplate=f'<b>{row["Title"]}</b><br>'
                + f'Company: {row["Company"]}<br>'
                + f'Duration: {row["Duration"]}<br>'
                + f'Location: {row["Location"]}<br>'
                + f'Start: {start_date.strftime("%b %Y")}<br>'
                + f'End: {end_date.strftime("%b %Y")}<extra></extra>',
            )
        )

        # Add start and end markers
        fig_gantt.add_trace(
            go.Scatter(
                x=[row["Start"], row["End"]],
                y=[0, 0],
                mode="markers",
                marker=dict(color=row["Color"], size=15, line=dict(color="white", width=2)),
                name=f'{row["Company"]} markers',
                showlegend=False,
                hovertemplate=f'<b>{row["Title"]}</b><br>'
                + f'Company: {row["Company"]}<br>'
                + f'Duration: {row["Duration"]}<br>'
                + f'Location: {row["Location"]}<br>'
                + f'Start: {start_date.strftime("%b %Y")}<br>'
                + f'End: {end_date.strftime("%b %Y")}<extra></extra>',
            )
        )

        # Add alternating labels above and below timeline
        mid_date = start_date + (end_date - start_date) / 2
        y_position = 0.3 if i % 2 == 0 else -0.3  # Alternate above and below

        fig_gantt.add_annotation(
            x=mid_date,
            y=y_position,
            text=f"<b>{row['Title']}</b><br>{row['Company']}<br>{row['Duration']}",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor=row["Color"],
            ax=0,
            ay=-20 if i % 2 == 0 else 20,
            font=dict(size=10, color=row["Color"]),
            bgcolor="rgba(255,255,255,0.9)",
            bordercolor=row["Color"],
            borderwidth=1,
            xanchor="center",
            yanchor="middle",
        )

    # Add year markers on timeline
    start_year = datetime.strptime(gantt_df["Start"].min(), "%Y-%m-%d").year
    end_year = datetime.strptime(gantt_df["End"].max(), "%Y-%m-%d").year

    for year in range(start_year, end_year + 1):
        year_date = f"{year}-01-01"
        fig_gantt.add_annotation(
            x=year_date,
            y=-0.1,
            text=str(year),
            showarrow=False,
            font=dict(size=12, color="#7f8c8d"),
            xanchor="center",
            yanchor="top",
        )

    fig_gantt.update_layout(
        title="Professional Career Timeline",
        xaxis_title="Timeline",
        yaxis_title="",
        height=500,
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(
            tickformat="%b %Y", tickangle=45, showgrid=True, gridcolor="rgba(128,128,128,0.2)"
        ),
        yaxis=dict(range=[-0.8, 0.8], showticklabels=False, showgrid=False),
        margin=dict(l=50, r=50, t=80, b=80),
    )

    st.plotly_chart(fig_gantt, use_container_width=True)

    # Industry experience breakdown
    st.markdown("### Industry Experience")

    industry_data = {
        "Industry": ["Healthcare/Biotech", "Automotive Tech", "Technology", "Consulting"],
        "Years": [3.6, 0.7, 0.6, 0.3],
        "Percentage": [69, 13, 12, 6],
    }

    industry_df = pd.DataFrame(industry_data)

    # Create pie chart for industry distribution
    fig_industry = px.pie(
        industry_df,
        values="Years",
        names="Industry",
        title="Years of Experience by Industry",
        color_discrete_sequence=px.colors.qualitative.Set3,
    )

    fig_industry.update_traces(textposition="inside", textinfo="percent+label")

    st.plotly_chart(fig_industry, use_container_width=True)

    # Enhanced job cards with animations
    st.markdown("### Detailed Experience")

    for i, job in enumerate(experience_data):
        with st.container():
            # Create job card with enhanced styling
            st.markdown(
                f"""
            <div class="job-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                    <div>
                        <h3 class="job-title">{job["title"]}</h3>
                        <p class="company-name">{job["company"]} | {job["location"]}</p>
                        <p style="color: #7f8c8d; font-style: italic;">{job["duration"]}</p>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">{chr(65 + i)}</div>
                        <small style="color: #7f8c8d;">Experience Level</small>
                    </div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

            # Job details in columns
            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown("**Key Achievements:**")
                for j, achievement in enumerate(job["achievements"]):
                    st.markdown(f"• **{achievement}**")

                # Add impact metrics if available
                if "impact_metrics" in job:
                    st.markdown("**Impact Metrics:**")
                    for metric in job["impact_metrics"]:
                        st.markdown(f"• {metric}")

            with col2:
                st.markdown("**Technologies:**")
                tech_html = "".join(
                    [f'<span class="skill-badge">{tech}</span>' for tech in job["technologies"]]
                )
                st.markdown(
                    f'<div style="display: flex; flex-wrap: wrap; gap: 4px;">{tech_html}</div>',
                    unsafe_allow_html=True,
                )

                # Add project count if available
                if "projects_count" in job:
                    st.markdown(f"**Projects:** {job['projects_count']}")

                # Add team size if available
                if "team_size" in job:
                    st.markdown(f"**Team Size:** {job['team_size']}")

            # Add expandable details section
            with st.expander(f"More Details about {job['title']} at {job['company']}"):
                st.markdown("**Architecture & Design:**")
                st.markdown("• Designed and implemented scalable data architectures")
                st.markdown("• Led technical decision-making for ML/AI initiatives")
                st.markdown("• Established best practices for data engineering")

                st.markdown("**Leadership & Collaboration:**")
                st.markdown("• Mentored junior engineers and data scientists")
                st.markdown("• Collaborated with cross-functional teams")
                st.markdown("• Presented technical solutions to stakeholders")

                st.markdown("**Business Impact:**")
                st.markdown("• Drove data-driven decision making")
                st.markdown("• Improved operational efficiency")
                st.markdown("• Enhanced customer experience through AI")

            if i < len(experience_data) - 1:
                st.markdown(
                    "<hr style='margin: 2rem 0; border: none; border-top: 2px solid #ecf0f1;'>",
                    unsafe_allow_html=True,
                )
