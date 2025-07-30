import streamlit as st
import streamlit.components.v1 as components

class FloatingChatbot:
    def __init__(self):
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

def render_floating_chatbot():
    """Render a floating chatbot that can be toggled on/off"""
    
    # Initialize session state
    if 'floating_chatbot' not in st.session_state:
        st.session_state.floating_chatbot = FloatingChatbot()
    
    if 'floating_chat_messages' not in st.session_state:
        st.session_state.floating_chat_messages = []
    
    if 'floating_chat_open' not in st.session_state:
        st.session_state.floating_chat_open = False
    
    # Add CSS for floating elements
    st.markdown("""
    <style>
    .floating-chat-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 1000;
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        font-size: 24px;
        cursor: pointer;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .floating-chat-button:hover {
        background-color: #2980b9;
        transform: scale(1.1);
    }
    .floating-chat-container {
        position: fixed;
        bottom: 100px;
        right: 20px;
        width: 350px;
        height: 500px;
        background-color: white;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        z-index: 999;
        display: flex;
        flex-direction: column;
        overflow: hidden;
        border: 1px solid #e0e0e0;
    }
    .floating-chat-header {
        background-color: #3498db;
        color: white;
        padding: 15px;
        text-align: center;
        font-weight: bold;
        border-radius: 15px 15px 0 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .floating-chat-close {
        background: none;
        border: none;
        color: white;
        font-size: 18px;
        cursor: pointer;
        padding: 0;
        width: 24px;
        height: 24px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .floating-chat-messages {
        flex: 1;
        overflow-y: auto;
        padding: 15px;
        background-color: #f8f9fa;
    }
    .floating-message {
        margin-bottom: 10px;
        padding: 10px;
        border-radius: 10px;
        max-width: 80%;
        word-wrap: break-word;
    }
    .floating-user-message {
        background-color: #3498db;
        color: white;
        margin-left: auto;
    }
    .floating-bot-message {
        background-color: white;
        color: #333;
        border: 1px solid #e0e0e0;
    }
    .floating-chat-input {
        padding: 15px;
        border-top: 1px solid #e0e0e0;
        background-color: white;
        display: flex;
        gap: 10px;
    }
    .floating-chat-input input {
        flex: 1;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 20px;
        outline: none;
    }
    .floating-chat-input input:focus {
        border-color: #3498db;
    }
    .floating-chat-input button {
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 20px;
        padding: 10px 15px;
        cursor: pointer;
    }
    .floating-chat-input button:hover {
        background-color: #2980b9;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Floating chat button
    if st.button("💬", key="floating_chat_toggle", help="Chat with me about Christopher's background"):
        st.session_state.floating_chat_open = not st.session_state.floating_chat_open
        st.rerun()
    
    # Floating chat container
    if st.session_state.floating_chat_open:
        # Create the chat interface using HTML
        chat_html = f"""
        <div class="floating-chat-container">
            <div class="floating-chat-header">
                <span>💬 Resume Assistant</span>
                <button class="floating-chat-close" onclick="closeChat()">×</button>
            </div>
            <div class="floating-chat-messages" id="floating-chat-messages">
        """
        
        # Add messages
        for message in st.session_state.floating_chat_messages:
            if message["role"] == "user":
                chat_html += f'<div class="floating-message floating-user-message">{message["content"]}</div>'
            else:
                chat_html += f'<div class="floating-message floating-bot-message">{message["content"]}</div>'
        
        chat_html += """
            </div>
            <div class="floating-chat-input">
                <input type="text" id="floating-chat-input" placeholder="Ask about Christopher's background..." onkeypress="handleKeyPress(event)">
                <button onclick="sendMessage()">Send</button>
            </div>
        </div>
        
        <script>
        function sendMessage() {{
            const input = document.getElementById('floating-chat-input');
            const message = input.value.trim();
            if (message) {{
                // Send message to Streamlit
                window.parent.postMessage({{
                    type: 'floating_chat_message',
                    message: message
                }}, '*');
                input.value = '';
            }}
        }}
        
        function handleKeyPress(event) {{
            if (event.key === 'Enter') {{
                sendMessage();
            }}
        }}
        
        function closeChat() {{
            window.parent.postMessage({{
                type: 'floating_chat_close'
            }}, '*');
        }}
        
        // Auto-scroll to bottom
        function scrollToBottom() {{
            const chatMessages = document.getElementById('floating-chat-messages');
            if (chatMessages) {{
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }}
        }}
        
        // Scroll when page loads
        window.addEventListener('load', scrollToBottom);
        
        // Listen for messages from Streamlit
        window.addEventListener('message', function(event) {{
            if (event.data.type === 'floating_chat_update') {{
                // Update chat messages
                const chatMessages = document.getElementById('floating-chat-messages');
                chatMessages.innerHTML = event.data.messages;
                scrollToBottom();
            }}
        }});
        </script>
        """
        
        # Render the chat interface
        components.html(chat_html, height=500, width=350)
        
        # Handle chat input (simplified for now)
        if st.button("Send Test Message", key="test_message"):
            st.session_state.floating_chat_messages.append({"role": "user", "content": "Hello! Tell me about Christopher's experience."})
            bot_response = st.session_state.floating_chatbot.get_response("Hello! Tell me about Christopher's experience.")
            st.session_state.floating_chat_messages.append({"role": "assistant", "content": bot_response})
            st.rerun() 