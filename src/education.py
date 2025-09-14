import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def education_page():
    st.markdown('<h2 class="section-header">🎓 Education & Academic Achievements</h2>', unsafe_allow_html=True)
    
    
    # Enhanced degree information
    st.markdown("### 🎯 Degree Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Master's Degree Card
        st.markdown("""
        <div class="project-card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.5rem;">
                <div style="flex: 1;">
                    <h3 style="color: #2c3e50; margin-bottom: 0.5rem; font-size: 1.5rem;">🎓 Master of Science, Data Analytics</h3>
                    <p style="color: #3498db; font-weight: bold; margin-bottom: 0.5rem;">San Jose State University</p>
                    <p style="color: #7f8c8d; margin-bottom: 1rem;">Graduated May 2024</p>
                </div>
                <div style="text-align: right; margin-left: 1rem;">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">MS</div>
                    <small style="color: #7f8c8d;">Degree</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Master's details
        st.markdown("**📚 Key Coursework:**")
        st.markdown("• Advanced Machine Learning")
        st.markdown("• Big Data Analytics")
        st.markdown("• Statistical Computing")
        st.markdown("• Data Mining & Visualization")
        st.markdown("• Database Systems")
        
        st.markdown("**🏆 Notable Achievements:**")
        st.markdown("• Published research paper on LLM fine-tuning")
        st.markdown("• Completed capstone project on travel chatbot")
        st.markdown("• Dean's List recognition")
        st.markdown("• Graduate research assistant")
    
    with col2:
        # Bachelor's Degree Card
        st.markdown("""
        <div class="project-card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.5rem;">
                <div style="flex: 1;">
                    <h3 style="color: #2c3e50; margin-bottom: 0.5rem; font-size: 1.5rem;">🎓 Bachelor of Science, Statistics</h3>
                    <p style="color: #3498db; font-weight: bold; margin-bottom: 0.5rem;">University of California, Davis</p>
                    <p style="color: #7f8c8d; margin-bottom: 1rem;">Graduated June 2020 </p>
                </div>
                <div style="text-align: right; margin-left: 1rem;">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">BS</div>
                    <small style="color: #7f8c8d;">Degree</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Bachelor's details
        st.markdown("**📚 Key Coursework:**")
        st.markdown("• Mathematical Statistics")
        st.markdown("• Applied Regression Analysis")
        st.markdown("• Probability Theory")
        st.markdown("• Statistical Computing")
        st.markdown("• Experimental Design")
        
        st.markdown("**🏆 Notable Achievements:**")
        st.markdown("• Dean's List multiple quarters")
        st.markdown("• Statistics Department honors")
        st.markdown("• Undergraduate research experience")
        st.markdown("• Academic excellence awards")
    
    
    # Publications and Research
    st.markdown("### 📖 Publications & Research")
    
    # Publication card
    st.markdown("""
    <div class="project-card">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.5rem;">
            <div style="flex: 1;">
                <h3 style="color: #2c3e50; margin-bottom: 0.5rem; font-size: 1.5rem;">📄 A Comparison of LLM Finetuning Methods & Evaluation Metrics with Travel Chatbot Use Case</h3>
                <p style="color: #3498db; font-weight: bold; margin-bottom: 0.5rem;">arXiv: 2408.03562</p>
                <p style="color: #7f8c8d; margin-bottom: 1rem;">Published August 2024</p>
            </div>
            <div style="text-align: right; margin-left: 1rem;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">📊</div>
                <small style="color: #7f8c8d;">Research</small>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Research details
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🔬 Research Focus:**")
        st.markdown("• Large Language Model fine-tuning techniques")
        st.markdown("• Supervised fine-tuning (SFT)")
        st.markdown("• Retrieval Augmented fine-tuning")
        st.markdown("• Reinforcement Learning with Human Feedback (RLHF)")
        st.markdown("• Evaluation metrics for chatbot performance")
    
    with col2:
        st.markdown("**💡 Key Contributions:**")
        st.markdown("• Comprehensive comparison of fine-tuning methods")
        st.markdown("• Novel evaluation framework for travel chatbots")
        st.markdown("• Practical implementation guidelines")
        st.markdown("• Performance benchmarking results")
        st.markdown("• Open-source code repository")
    
    # Link to paper
    st.markdown("**🔗 Access the Research:**")
    st.markdown("[📄 View on arXiv](https://arxiv.org/abs/2408.03562)")
    
    # Certifications and additional education
    st.markdown("### 🏆 Certifications & Additional Education")
    
    certifications = [
        {
            "name": "AWS Certified Solutions Architect",
            "issuer": "Amazon Web Services",
            "year": "2023",
            "status": "Active"
        },
        {
            "name": "Google Cloud Professional Data Engineer",
            "issuer": "Google Cloud",
            "year": "2023",
            "status": "Active"
        },
        {
            "name": "Microsoft Azure Data Engineer Associate",
            "issuer": "Microsoft",
            "year": "2022",
            "status": "Active"
        },
        {
            "name": "Databricks Certified Associate Developer",
            "issuer": "Databricks",
            "year": "2023",
            "status": "Active"
        }
    ]
    
    # for cert in certifications:
    #     status_color = '#27ae60' if cert['status'] == 'Active' else '#f39c12'
    #     st.markdown(f"""
    #     <div style="background: rgba(255, 255, 255, 0.1); padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border-left: 4px solid {status_color};">
    #         <h4 style="margin: 0 0 0.5rem 0; color: #2c3e50;">{cert['name']}</h4>
    #         <p style="margin: 0; color: #7f8c8d;">{cert['issuer']} • {cert['year']} • <span style="color: {status_color};">{cert['status']}</span></p>
    #     </div>
    #     """, unsafe_allow_html=True)
    