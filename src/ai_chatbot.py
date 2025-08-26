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
        - Email: vchristopherton@gmail.com

        **Work Experience:**
        1. Biostatistician/Data Analyst Intern @ Guardant Health (June 2020 - September 2020)
        Built and published an internal too to profile patient journey undergoing treatment
        Modeled Kaplan-Meier survival curve to visualize time-to-event trend
        Prototyped interactive cohort/patient-level filtering Shiny features to segment and generate insightful views, based on database queries
        Developed and implemented an R Shiny dashboard to facilitate visualizations & embedded SQL insights from patient & prescription level data, manipulated & aggregated numerous real-world clinical genomic data sources
        Conducted survival analysis using Cox, Kaplan-Meier estimator, and log-rank tests for differences between comparable drugs and 100,000+ patient undergoing treatment durations lasting 125+ months 
        Achieved data product queries requested by FDA and biopharma stakeholders, engaged in weekly data reviews and discussions regarding RWE and statistical analysis plans by presenting recommendations and findings
        Presented scaling prototype development updates to VP - product was adopted for internal use & medical affairs operations
        Contributed to paper: Abstract PS18-28: Genomic heterogeneity and associated clinical outcomes of breast cancers treated with CDK4/6 inhibitors: Insights from real-world clinical genomic data

        2. Data Annotation Specialist @ Tesla: (October 2020 - June 2021)
        Collaborates with project managers, engineers, and leads to ensure the quality of internal labeling software tool 
        Improves Autopilot deep learning software by providing labeled data using image recognition and classification
        Performs quality assurance, reports bugs and communicates consistent feedback regarding feature latencies
        Maintains expected workflow performance quotas by using Excel to track progress, allowing time for essential data curation and backlog management

        3. Marketing Data Analyst Intern @ Volta Charging: (July 2021 - September 2021) 
        Developed and maintained executive client-facing dashboards that automates information query to status report on EV performance, sustainability ad-hoc analysis requests, business insights across 10+ months
        Performed product, time series, geographical and longitudinal analyses to uncover correlations among consumer behavior and trends with, leveraging Sigma Computing, Looker, SQL, Excel, Python, Snowflake, ESRI to retrieve, manipulate, analyze ads campaign KPI’s and usage rates
        Collaborated cross-functionally with site sales, marketing, & engineering to support data storytelling 
        Lead training sessions for internal stakeholders on the efficient querying process via dashboard interface & methodologies, promoting efficiency by 50% and 100% respectively
        Identified and recommended latencies within data governance infrastructure, took proactive measures to ensure data lineages across BI tool platform was consistent, independent, and durable

        4. Data Curator @ Volta Charging: (November 2021 - March 2022)
        Developed python scripts to web scrape, transform and curate raw datasets to drive network planning analytics
        Designed tests to ensure a reliable process to continuously refresh data on a weekly cadence

        Informatica TDM Engineer @ Deloitte via Brooksource (February 2022 - May 2022)
        Leverage Informatica to build source connectors, transform and prepare fields for data anonymization transformation procedures
        Designed evaluation and testing scripts in python to estimate risk of identification for PII attributes

        5. Data Scientist Intern @ Genentech (June 2022 - April 2024)
        Developed complex time series regression models for manufacturing predictive maintenance, accelerating time to insight for outlier detection and root cause analysis
        Generating insights and recommendations for timely delivery of quality control through investigative queries and visuals. Delivered YTD 
        Deployed an internal R software package for efficient and accurate querying of clinical reporting tables by innovating a sliding window search algorithm

        6. Data Engineer @ Genentech (April 2024 - Present) 
        Researched and spearheaded migration of prototype chat applications to a production-grade AWS platform, leveraging serverless APIs to invoke model capabilities using s3, Bedrock - OpenSearch, Agents, and metadata filtering, serving 50+ regulatory users interacting with global health authorities.
        Refactored a data ingestion pipeline to transform and embed complex SOP documents, using Langchain and Azure AI indexes to host and store contexts
        Implemented LLM evaluation processes to assess model performance, identified baselines to drive optimization decisions and better RAG configurations


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
        - Email: vchristopherton@gmail.com
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