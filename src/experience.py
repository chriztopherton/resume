import streamlit as st

def experience_page(experience_data):
    st.markdown('<h2 class="section-header">Professional Experience</h2>', unsafe_allow_html=True)
    
    for i, job in enumerate(experience_data):
        with st.container():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f'<p class="job-title">{job["title"]}</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="company-name">{job["company"]} | {job["location"]}</p>', unsafe_allow_html=True)
                st.markdown(f'*{job["duration"]}*')
                
                st.markdown("**Key Achievements:**")
                for achievement in job["achievements"]:
                    st.markdown(f"• {achievement}")
            
            with col2:
                st.markdown("**Technologies:**")
                tech_html = ''.join([f'<span class="skill-badge">{tech}</span>' for tech in job["technologies"]])
                st.markdown(f'<div style="display: flex; flex-wrap: wrap; gap: 4px;">{tech_html}</div>', unsafe_allow_html=True)
            
            if i < len(experience_data) - 1:
                st.divider() 