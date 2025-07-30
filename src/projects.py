import streamlit as st

def projects_page(projects_data):
    st.markdown('<h2 class="section-header">Featured Projects</h2>', unsafe_allow_html=True)
    
    for project in projects_data:
        with st.container():
            st.markdown(f"### {project['title']}")
            st.markdown(f"**Description:** {project['description']}")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown("**Technologies Used:**")
                tech_html = ''.join([f'<span class="skill-badge">{tech}</span>' for tech in project["technologies"]])
                st.markdown(f'<div style="display: flex; flex-wrap: wrap; gap: 4px;">{tech_html}</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown("**Impact:**")
                st.markdown(f"*{project['impact']}*")
            
            st.divider() 