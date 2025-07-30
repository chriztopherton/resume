import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()

class AIChatbot:
    def __init__(self):
        # Initialize OpenAI client
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            api_key=os.getenv("openai_api_key")
        )
        
        # Resume context
        self.resume_context = """
        You are an AI assistant helping people learn about Christopher Ton, a ML/Data Engineer. Here's his background:

        **Personal Info:**
        - Name: Christopher Ton
        - Title: ML/Data Engineer
        - Email: christopher.ton@sjsu.edu

        **Work Experience:**
        1. Genentech - Data Engineer (Apr 2024 - Present)
           - Built and deployed a full stack LLM-powered chat assistant using Streamlit
           - Designed scalable ETL pipelines for Azure AI Search
           - Developed serverless APIs using AWS Lambda, S3, Bedrock, and OpenSearch
           - Engineered data models in Snowflake using Talend, PySpark, and SQL

        2. Genentech - Data Scientist Intern (Jun 2022 - Apr 2024)
           - Reduced resolution times by 20% with predictive anomaly detection models
           - Automated clinical reporting validation processes using R

        3. Deloitte - Data Engineer (Feb 2022 - May 2022)
           - Worked on data engineering projects

        4. Shell Recharge - Data Curator (Nov 2021 - Mar 2022)
           - Data curation and management

        **Technical Skills:**
        - Languages: Python, R, SQL
        - Data Engineering: PySpark, Pandas, NumPy, scikit-learn, SageMaker, LangChain
        - Cloud Platforms: AWS (S3, Lambda, Redshift), GCP BigQuery, Azure AI Indexes
        - DevOps: Docker, Git, CI/CD pipelines

        **Key Projects:**
        1. LLM-Powered Chat Assistant - Full-stack application using Streamlit with end-to-end architecture
        2. RAG Applications with Serverless APIs - Multiple Retrieval-Augmented Generation applications using AWS services
        3. Predictive Anomaly Detection Models - Reduced resolution times by 20%
        4. Clinical Reporting Validation Automation - Automated processes using R

        **Education:**
        - Relevant coursework and certifications in data science and engineering

        **Contact:**
        - Email: christopher.ton@sjsu.edu
        - LinkedIn and other contact information available in the Contact section

        Your role is to provide helpful, accurate information about Christopher's background, experience, skills, and projects. Be conversational, professional, and always refer to the information provided above. If asked about something not covered in this context, politely redirect to the relevant sections of the resume or suggest contacting Christopher directly.
        """
        
        # Initialize conversation memory
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # Create prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", self.resume_context),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])
        
        # Create LLM chain
        self.chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt,
            memory=self.memory,
            verbose=False
        )
    
    def get_response(self, user_input):
        """Generate AI-powered response using LangChain and OpenAI"""
        try:
            # Get response from the chain
            response = self.chain.run(input=user_input)
            return response.strip()
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
            return "I apologize, but I'm having trouble generating a response right now. Please try again or check your internet connection."
    
    def clear_memory(self):
        """Clear conversation memory"""
        self.memory.clear()

def render_ai_chatbot():
    """Render the AI-powered chatbot in the sidebar"""
    
    # Initialize session state for AI chatbot
    if 'ai_chatbot' not in st.session_state:
        st.session_state.ai_chatbot = AIChatbot()
    
    if 'ai_chat_messages' not in st.session_state:
        st.session_state.ai_chat_messages = []
    
    # Create sidebar for chatbot
    with st.sidebar:
        st.markdown("## 🤖 AI Resume Assistant")
        st.markdown("Powered by OpenAI GPT-3.5")
        st.markdown("Ask me anything about Christopher's background!")
        
        # Display chat messages
        chat_container = st.container()
        
        with chat_container:
            for message in st.session_state.ai_chat_messages:
                if message["role"] == "user":
                    with st.chat_message("user"):
                        st.write(message["content"])
                else:
                    with st.chat_message("assistant"):
                        st.write(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Ask about Christopher's experience, skills, or projects..."):
            # Add user message to history
            st.session_state.ai_chat_messages.append({"role": "user", "content": prompt})
            
            # Show typing indicator
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    # Get AI response
                    bot_response = st.session_state.ai_chatbot.get_response(prompt)
                    st.session_state.ai_chat_messages.append({"role": "assistant", "content": bot_response})
            
            # Rerun to display new messages
            st.rerun()
        
        # Clear chat button
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Clear Chat", type="secondary"):
                st.session_state.ai_chat_messages = []
                st.session_state.ai_chatbot.clear_memory()
                st.rerun()
        
        with col2:
            if st.button("Reset AI", type="secondary"):
                st.session_state.ai_chatbot = AIChatbot()
                st.session_state.ai_chat_messages = []
                st.rerun()
        
        # Add some helpful suggestions
        st.markdown("---")
        st.markdown("**💡 Try asking:**")
        st.markdown("- What's Christopher's experience with AWS?")
        st.markdown("- Tell me about his projects at Genentech")
        st.markdown("- What ML frameworks does he know?")
        st.markdown("- How can I contact him?")
        st.markdown("- What's his background in data engineering?")
        
        # Show current model info
        st.markdown("---")
        st.markdown("**🔧 Model:** GPT-3.5-turbo")
        st.markdown("**🎯 Context:** Resume-focused responses")

def render_floating_ai_chatbot():
    """Render a floating AI chatbot that can be toggled on/off"""
    
    # Initialize session state
    if 'floating_ai_chatbot' not in st.session_state:
        st.session_state.floating_ai_chatbot = AIChatbot()
    
    if 'floating_ai_chat_messages' not in st.session_state:
        st.session_state.floating_ai_chat_messages = []
    
    if 'floating_ai_chat_open' not in st.session_state:
        st.session_state.floating_ai_chat_open = False
    
    # Add CSS for floating elements
    st.markdown("""
    <style>
    .floating-chat-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background-color: #1f77b4;
        color: white;
        border: none;
        cursor: pointer;
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        transition: all 0.3s ease;
    }
    
    .floating-chat-button:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 16px rgba(0,0,0,0.2);
    }
    
    .floating-chat-window {
        position: fixed;
        bottom: 90px;
        right: 20px;
        width: 350px;
        height: 500px;
        background-color: white;
        border-radius: 12px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.15);
        z-index: 1000;
        display: flex;
        flex-direction: column;
        border: 1px solid #e0e0e0;
    }
    
    .chat-header {
        background-color: #1f77b4;
        color: white;
        padding: 15px;
        border-radius: 12px 12px 0 0;
        font-weight: bold;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .chat-messages {
        flex: 1;
        padding: 15px;
        overflow-y: auto;
        max-height: 350px;
    }
    
    .chat-input-container {
        padding: 15px;
        border-top: 1px solid #e0e0e0;
    }
    
    .chat-input {
        width: 100%;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 20px;
        outline: none;
    }
    
    .message {
        margin-bottom: 10px;
        padding: 8px 12px;
        border-radius: 15px;
        max-width: 80%;
        word-wrap: break-word;
    }
    
    .user-message {
        background-color: #007bff;
        color: white;
        margin-left: auto;
    }
    
    .bot-message {
        background-color: #f1f1f1;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Floating chat button
    if not st.session_state.floating_ai_chat_open:
        st.markdown("""
        <button class="floating-chat-button" onclick="document.querySelector('.floating-chat-window').style.display='flex'">
            🤖
        </button>
        """, unsafe_allow_html=True)
    
    # Floating chat window
    if st.session_state.floating_ai_chat_open:
        st.markdown("""
        <div class="floating-chat-window">
            <div class="chat-header">
                <span>AI Resume Assistant</span>
                <button onclick="document.querySelector('.floating-chat-window').style.display='none'" style="background:none;border:none;color:white;cursor:pointer;">✕</button>
            </div>
            <div class="chat-messages" id="chat-messages">
                <!-- Messages will be populated here -->
            </div>
            <div class="chat-input-container">
                <input type="text" class="chat-input" placeholder="Ask about Christopher's background..." id="chat-input">
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # JavaScript for handling chat interactions
    st.markdown("""
    <script>
    // Add JavaScript for handling chat interactions
    document.addEventListener('DOMContentLoaded', function() {
        const chatInput = document.getElementById('chat-input');
        const chatMessages = document.getElementById('chat-messages');
        
        if (chatInput) {
            chatInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    const message = this.value;
                    if (message.trim()) {
                        // Add user message
                        const userDiv = document.createElement('div');
                        userDiv.className = 'message user-message';
                        userDiv.textContent = message;
                        chatMessages.appendChild(userDiv);
                        
                        // Clear input
                        this.value = '';
                        
                        // Scroll to bottom
                        chatMessages.scrollTop = chatMessages.scrollHeight;
                        
                        // Here you would typically send the message to your backend
                        // For now, we'll just show a placeholder response
                        setTimeout(() => {
                            const botDiv = document.createElement('div');
                            botDiv.className = 'message bot-message';
                            botDiv.textContent = 'I\'m processing your request...';
                            chatMessages.appendChild(botDiv);
                            chatMessages.scrollTop = chatMessages.scrollHeight;
                        }, 1000);
                    }
                }
            });
        }
    });
    </script>
    """, unsafe_allow_html=True) 