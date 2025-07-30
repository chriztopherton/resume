import streamlit as st

def education_page():
    st.markdown('<h2 class="section-header">Education</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### San Jose State University
        **Master of Science, Data Analytics**  
        *Graduated May 2024*
        """)
    
    with col2:
        st.markdown("""
        ### University of California, Davis
        **Bachelor of Science, Statistics**  
        *Graduated June 2020*
        """)
    
    st.markdown("### Publications")
    st.markdown("""
    **[arXiv: A Comparison of LLM Finetuning Methods & Evaluation Metrics with Travel Chatbot Use Case](https://arxiv.org/abs/2408.03562)**
    
    Implemented various fine-tuning techniques such as Supervised fine-tuning (SFT), Retrieval Augmented fine-tuning, and Reinforcement Learning with Human Feedback (RLHF).
    """) 