import streamlit as st
import json
from datetime import datetime

class ResumeChatbot:
    def __init__(self):
        self.conversation_history = []
        self.resume_data = {
            "name": "Christopher Ton",
            "title": "ML/Data Engineer",
            "experience": [
                {
                    "company": "Genentech",
                    "title": "Data Engineer",
                    "duration": "Apr 2024 - Present",
                    "key_achievements": [
                        "Built and deployed a full stack LLM-powered chat assistant using Streamlit",
                        "Designed scalable ETL pipelines for Azure AI Search",
                        "Developed serverless APIs using AWS Lambda, S3, Bedrock, and OpenSearch",
                        "Engineered data models in Snowflake using Talend, PySpark, and SQL"
                    ]
                },
                {
                    "company": "Genentech",
                    "title": "Data Scientist Intern",
                    "duration": "Jun 2022 - Apr 2024",
                    "key_achievements": [
                        "Reduced resolution times by 20% with predictive anomaly detection models",
                        "Automated clinical reporting validation processes using R"
                    ]
                }
            ],
            "skills": {
                "Languages": ["Python", "R", "SQL"],
                "Data Engineering": ["PySpark", "Pandas", "NumPy", "scikit-learn", "SageMaker", "LangChain"],
                "Cloud Platforms": ["AWS (S3, Lambda, Redshift)", "GCP BigQuery", "Azure AI Indexes"],
                "DevOps": ["Docker", "Git", "CI/CD pipelines"]
            },
            "projects": [
                {
                    "title": "LLM-Powered Chat Assistant",
                    "description": "Full-stack application using Streamlit with end-to-end architecture"
                },
                {
                    "title": "RAG Applications with Serverless APIs",
                    "description": "Multiple Retrieval-Augmented Generation applications using AWS services"
                }
            ]
        }
    
    def get_response(self, user_input):
        """Generate a response based on user input and resume data"""
        user_input_lower = user_input.lower()
        
        # Initialize response
        response = "I'm here to help you learn more about Christopher Ton's background and experience. "
        
        # Check for specific questions
        if any(word in user_input_lower for word in ["experience", "work", "job", "career"]):
            response += "Christopher has worked at Genentech as a Data Engineer (Apr 2024 - Present) and Data Scientist Intern (Jun 2022 - Apr 2024), at Deloitte as a Data Engineer (Feb 2022 - May 2022), and at Shell Recharge as a Data Curator (Nov 2021 - Mar 2022). "
        
        elif any(word in user_input_lower for word in ["skills", "technologies", "tools", "languages"]):
            response += "Christopher's key skills include Python, R, SQL, PySpark, AWS services, Docker, and various ML frameworks. He's experienced with cloud platforms like AWS, GCP, and Azure. "
        
        elif any(word in user_input_lower for word in ["projects", "portfolio"]):
            response += "Key projects include an LLM-powered chat assistant built with Streamlit, RAG applications using AWS services, predictive anomaly detection models, and clinical reporting validation automation. "
        
        elif any(word in user_input_lower for word in ["education", "degree", "school"]):
            response += "Christopher's educational background includes relevant coursework and certifications in data science and engineering. "
        
        elif any(word in user_input_lower for word in ["contact", "email", "linkedin", "reach"]):
            response += "You can find Christopher's contact information in the Contact section of this resume. "
        
        elif any(word in user_input_lower for word in ["hello", "hi", "hey"]):
            response = "Hello! I'm here to help you learn more about Christopher Ton's professional background. Feel free to ask about his experience, skills, projects, or anything else! "
        
        elif any(word in user_input_lower for word in ["help", "what can you do"]):
            response = "I can help you learn about Christopher's work experience, technical skills, projects, education, and contact information. Just ask me anything about his background! "
        
        else:
            response += "I can help you learn about Christopher's experience, skills, projects, and background. What would you like to know more about? "
        
        return response

def render_chatbot():
    """Render the chatbot in the sidebar"""
    
    # Initialize session state for chatbot
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = ResumeChatbot()
    
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []
    
    # Create sidebar for chatbot
    with st.sidebar:
        st.markdown("## 💬 Resume Assistant")
        st.markdown("Ask me anything about Christopher's background!")
        
        # Display chat messages
        chat_container = st.container()
        
        with chat_container:
            for message in st.session_state.chat_messages:
                if message["role"] == "user":
                    with st.chat_message("user"):
                        st.write(message["content"])
                else:
                    with st.chat_message("assistant"):
                        st.write(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Ask about Christopher's experience, skills, or projects..."):
            # Add user message to history
            st.session_state.chat_messages.append({"role": "user", "content": prompt})
            
            # Get bot response
            bot_response = st.session_state.chatbot.get_response(prompt)
            st.session_state.chat_messages.append({"role": "assistant", "content": bot_response})
            
            # Rerun to display new messages
            st.rerun()
        
        # Clear chat button
        if st.button("Clear Chat", type="secondary"):
            st.session_state.chat_messages = []
            st.rerun()
        
        # Add some helpful suggestions
        st.markdown("---")
        st.markdown("**💡 Try asking:**")
        st.markdown("- What's Christopher's work experience?")
        st.markdown("- What skills does he have?")
        st.markdown("- Tell me about his projects")
        st.markdown("- How can I contact him?") 