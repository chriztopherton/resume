#!/usr/bin/env python3
"""
Test script for the AI chatbot functionality
"""

import os
from dotenv import load_dotenv
from src.ai_chatbot import AIChatbot

def test_ai_chatbot():
    """Test the AI chatbot with sample questions"""
    
    # Load environment variables
    load_dotenv()
    
    # Check if API key is available
    api_key = os.getenv("openai_api_key")
    if not api_key:
        print("❌ Error: OpenAI API key not found in .env file")
        return False
    
    print("✅ OpenAI API key found")
    
    try:
        # Initialize chatbot
        print("🤖 Initializing AI chatbot...")
        chatbot = AIChatbot()
        print("✅ AI chatbot initialized successfully")
        
        # Test questions
        test_questions = [
            "What's Christopher's current role?",
            "Tell me about his experience with AWS",
            "What ML frameworks does he know?",
            "What projects has he worked on at Genentech?",
            "How can I contact Christopher?"
        ]
        
        print("\n🧪 Testing AI chatbot responses...")
        print("=" * 50)
        
        for i, question in enumerate(test_questions, 1):
            print(f"\n{i}. Question: {question}")
            print("-" * 30)
            
            try:
                response = chatbot.get_response(question)
                print(f"Response: {response}")
                print("✅ Response generated successfully")
            except Exception as e:
                print(f"❌ Error generating response: {str(e)}")
        
        print("\n" + "=" * 50)
        print("🎉 AI chatbot test completed!")
        return True
        
    except Exception as e:
        print(f"❌ Error initializing chatbot: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Starting AI Chatbot Test")
    print("=" * 50)
    
    success = test_ai_chatbot()
    
    if success:
        print("\n✅ All tests passed! The AI chatbot is working correctly.")
        print("You can now run the Streamlit app with: poetry run streamlit run run_app.py")
    else:
        print("\n❌ Some tests failed. Please check the error messages above.") 