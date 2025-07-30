import streamlit as st

def contact_page():
    st.markdown('<h2 class="section-header">Get In Touch</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Contact Information
        
        📧 **Email:** vchristopherton@gmail.com  
        📱 **Phone:** (669) 254-6967  
        🌐 **LinkedIn:** [linkedin.com/in/chriztopherton](https://linkedin.com/in/chriztopherton)  
        💻 **GitHub:** [github.com/chriztopherton](https://github.com/chriztopherton)  
        🏠 **Location:** US Citizen  
        """)
    
    with col2:
        st.markdown("""
        ### Let's Connect!
        
        I'm always interested in new opportunities and collaborations in:
        
        - Machine Learning & AI
        - Data Engineering
        - Cloud Architecture
        - LLM Applications
        - Data Science
        
        Feel free to reach out for:
        - Job opportunities
        - Project collaborations
        - Technical discussions
        - Mentorship
        """)
    
    # Contact form
    st.markdown("### Send a Message")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message")
        
        if st.form_submit_button("Send Message"):
            if name and email and message:
                st.success("Thank you for your message! I'll get back to you soon.")
            else:
                st.error("Please fill in all required fields.") 