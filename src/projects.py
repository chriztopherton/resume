import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def projects_page(projects_data):
    st.markdown('<h2 class="section-header">🚀 Featured Projects</h2>', unsafe_allow_html=True)
    
    # Project portfolio overview
    st.markdown("### 📊 Portfolio Overview")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">12+</div>
            <div class="metric-description">Projects Completed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">8</div>
            <div class="metric-description">Technologies Mastered</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">95%</div>
            <div class="metric-description">Success Rate</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">3</div>
            <div class="metric-description">Industries Served</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Project categories visualization
    st.markdown("### 🎯 Project Categories")
    
    # Create project categories data
    categories_data = {
        'Category': ['Machine Learning', 'Data Engineering', 'AI/LLM', 'Web Applications', 'Data Visualization'],
        'Count': [4, 3, 2, 2, 1],
        'Complexity': [9, 8, 9, 7, 6]
    }
    
    categories_df = pd.DataFrame(categories_data)
    
    # Create bubble chart
    fig_categories = px.scatter(
        categories_df,
        x='Count',
        y='Complexity',
        size='Count',
        color='Category',
        hover_name='Category',
        title="Project Categories by Complexity and Count",
        size_max=30
    )
    
    fig_categories.update_layout(height=400)
    st.plotly_chart(fig_categories, use_container_width=True)
    
    # Enhanced project cards with interactive elements
    st.markdown("### 💼 Project Showcase")
    
    for i, project in enumerate(projects_data):
        with st.container():
            # Create enhanced project card
            st.markdown(f"""
            <div class="project-card">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.5rem;">
                    <div style="flex: 1;">
                        <h3 style="color: #2c3e50; margin-bottom: 0.5rem; font-size: 1.5rem;">🎯 {project['title']}</h3>
                        <p style="color: #7f8c8d; font-size: 1.1rem; margin-bottom: 1rem;">{project['description']}</p>
                    </div>
                    <div style="text-align: right; margin-left: 1rem;">
                        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">#{i+1}</div>
                        <small style="color: #7f8c8d;">Project</small>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Project details in columns
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown("**🛠️ Technologies Used:**")
                tech_html = ''.join([f'<span class="skill-badge">{tech}</span>' for tech in project["technologies"]])
                st.markdown(f'<div style="display: flex; flex-wrap: wrap; gap: 4px; margin-bottom: 1rem;">{tech_html}</div>', unsafe_allow_html=True)
                
                st.markdown("**📈 Impact & Results:**")
                st.markdown(f"*{project['impact']}*")
                
                # Add project metrics if available
                if "metrics" in project:
                    st.markdown("**📊 Key Metrics:**")
                    for metric in project["metrics"]:
                        st.markdown(f"• {metric}")
            
            with col2:
                # Project complexity indicator
                complexity = project.get('complexity', 7)
                st.markdown("**🎯 Complexity Level:**")
                st.markdown(f"""
                <div style="background: linear-gradient(90deg, #e74c3c {complexity*10}%, #ecf0f1 {complexity*10}%); 
                            height: 20px; border-radius: 10px; margin: 0.5rem 0;"></div>
                <small>{complexity}/10</small>
                """, unsafe_allow_html=True)
                
                # Project duration
                if "duration" in project:
                    st.markdown(f"**⏱️ Duration:** {project['duration']}")
                
                # Team size
                if "team_size" in project:
                    st.markdown(f"**👥 Team Size:** {project['team_size']}")
                
                # Project status
                status = project.get('status', 'Completed')
                status_color = '#27ae60' if status == 'Completed' else '#f39c12'
                st.markdown(f"""
                <div style="background: {status_color}; color: white; padding: 0.3rem 0.8rem; 
                            border-radius: 15px; text-align: center; font-size: 0.9rem;">
                    {status}
                </div>
                """, unsafe_allow_html=True)
            
            # Expandable project details
            with st.expander(f"🔍 Detailed Project Information - {project['title']}"):
                st.markdown("**🏗️ Architecture & Design:**")
                st.markdown("• Designed scalable and maintainable system architecture")
                st.markdown("• Implemented best practices for code quality and performance")
                st.markdown("• Ensured security and compliance requirements")
                
                st.markdown("**🔄 Development Process:**")
                st.markdown("• Agile development methodology with regular sprints")
                st.markdown("• Continuous integration and deployment (CI/CD)")
                st.markdown("• Comprehensive testing and quality assurance")
                
                st.markdown("**📚 Technical Challenges & Solutions:**")
                st.markdown("• Overcame scalability challenges through optimization")
                st.markdown("• Implemented robust error handling and monitoring")
                st.markdown("• Ensured data privacy and security compliance")
                
                # Add demo link if available
                if "demo_link" in project:
                    st.markdown(f"**🔗 Demo:** [View Project Demo]({project['demo_link']})")
                
                # Add GitHub link if available
                if "github_link" in project:
                    st.markdown(f"**💻 Code:** [View on GitHub]({project['github_link']})")
            
            if i < len(projects_data) - 1:
                st.markdown("<hr style='margin: 2rem 0; border: none; border-top: 2px solid #ecf0f1;'>", unsafe_allow_html=True)
    
    # Technology stack visualization
    st.markdown("### 🛠️ Technology Stack Analysis")
    
    # Create technology usage data
    tech_usage = {}
    for project in projects_data:
        for tech in project['technologies']:
            tech_usage[tech] = tech_usage.get(tech, 0) + 1
    
    tech_df = pd.DataFrame(list(tech_usage.items()), columns=['Technology', 'Usage Count'])
    tech_df = tech_df.sort_values('Usage Count', ascending=True)
    
    # Create horizontal bar chart
    fig_tech = px.bar(
        tech_df,
        x='Usage Count',
        y='Technology',
        orientation='h',
        title="Technology Usage Across Projects",
        color='Usage Count',
        color_continuous_scale='Blues'
    )
    
    fig_tech.update_layout(height=400)
    st.plotly_chart(fig_tech, use_container_width=True)
    
    # Project timeline
    st.markdown("### 📅 Project Timeline")
    
    # Create project timeline data
    timeline_data = []
    for i, project in enumerate(projects_data):
        timeline_data.append({
            'Project': project['title'],
            'Month': f'Month {i+1}',
            'Category': project.get('category', 'ML/AI'),
            'Complexity': project.get('complexity', 7)
        })
    
    timeline_df = pd.DataFrame(timeline_data)
    
    # Create timeline visualization
    fig_timeline = go.Figure()
    
    fig_timeline.add_trace(go.Scatter(
        x=timeline_df['Month'],
        y=timeline_df['Complexity'],
        mode='lines+markers',
        line=dict(color='#3498db', width=3),
        marker=dict(size=12, color='#e74c3c'),
        text=timeline_df['Project'],
        hovertemplate='<b>%{text}</b><br>Complexity: %{y}/10<extra></extra>'
    ))
    
    fig_timeline.update_layout(
        title="Project Complexity Timeline",
        xaxis_title="Timeline",
        yaxis_title="Complexity Level",
        height=300,
        showlegend=False
    )
    
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Call to action for project collaboration
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(231, 76, 60, 0.1)); border-radius: 15px;">
        <h3>🤝 Interested in Collaboration?</h3>
        <p style="font-size: 1.1rem; margin: 1rem 0;">I'm always excited to work on new and challenging projects.</p>
        <p style="color: #7f8c8d;">Available for freelance work and open-source contributions</p>
    </div>
    """, unsafe_allow_html=True) 