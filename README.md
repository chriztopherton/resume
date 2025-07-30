# Christopher Ton - Professional Resume Website

A modern, interactive resume website built with Streamlit showcasing my experience as a Machine Learning and Data Engineer.

## 🚀 Features

- **Interactive Navigation**: Clean, professional navigation between different sections
- **Dynamic Visualizations**: Charts and graphs showcasing skills, experience, and achievements
- **Responsive Design**: Modern UI with custom CSS styling
- **Contact Form**: Built-in contact form for potential employers
- **AI Chatbot**: Intelligent chatbot powered by OpenAI GPT-3.5 for interactive resume exploration
- **Professional Layout**: Organized sections for experience, skills, projects, and education

## 📋 Sections

1. **Home**: Overview with key metrics and introduction
2. **Experience**: Detailed work history with achievements and technologies
3. **Skills**: Technical skills organized by category with visualizations
4. **Projects**: Featured projects with impact and technologies used
5. **Education**: Academic background and publications
6. **Contact**: Contact information and message form

## 🛠️ Technologies Used

- **Streamlit**: Web application framework
- **Plotly**: Interactive data visualizations
- **Pandas**: Data manipulation and analysis
- **Custom CSS**: Professional styling and layout

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd resume
   ```

2. **Install dependencies**:
   ```bash
   # Using pip
   pip install -r requirements.txt
   
   # Or using poetry
   poetry install
   ```

3. **Set up AI Chatbot (Optional)**:
   ```bash
   # Create a .env file with your OpenAI API key
   echo "openai_api_key=your_openai_api_key_here" > .env
   
   # Get your API key from: https://platform.openai.com/api-keys
   # Replace 'your_openai_api_key_here' with your actual API key
   ```

4. **Run the application**:
   ```bash
   streamlit run src/app.py
   ```

## 🎯 Usage

1. Start the application using the command above
2. Open your browser and navigate to `http://localhost:8501`
3. Explore different sections using the navigation menu
4. Use the contact form to send messages
5. **AI Chatbot**: Click the 🤖 button in the bottom-right corner to chat with an AI assistant about Christopher's background

### AI Chatbot Features
- **Intelligent Responses**: Powered by OpenAI GPT-3.5
- **Resume Context**: Trained on Christopher's complete professional background
- **Interactive Q&A**: Ask about experience, skills, projects, and more
- **Conversation Memory**: Remembers previous questions for context

## 📊 Key Highlights

### Professional Experience
- **Genentech**: Data Engineer (Current) - LLM applications, RAG systems, cloud architecture
- **Genentech**: Data Scientist Intern - Predictive modeling, anomaly detection
- **Deloitte**: Data Engineer - Data masking, compliance, risk assessment
- **Shell Recharge**: Data Curator - ETL automation, data quality improvement

### Technical Skills
- **Languages**: Python, R, SQL
- **Data Engineering**: PySpark, Pandas, NumPy, scikit-learn, SageMaker, LangChain
- **LLM & ML**: AWS SageMaker, AWS Bedrock, Dataiku DSS, PyTorch
- **Cloud Platforms**: AWS, GCP BigQuery, Azure AI Indexes
- **DevOps**: Docker, Git, CI/CD pipelines

### Key Achievements
- 20% reduction in resolution times through predictive modeling
- 30% improvement in data quality through automated workflows
- Built and deployed production-ready LLM chat assistant
- Integrated 7+ global data sources in Snowflake

## 🎨 Customization

### Adding New Content
1. **Experience**: Update the `experience_data` list in `src/app.py`
2. **Skills**: Modify the `skills_data` dictionary
3. **Projects**: Add new projects to the `projects_data` list
4. **Styling**: Customize CSS in the `st.markdown` section

### Styling
The application uses custom CSS for professional styling. You can modify:
- Color scheme in the CSS variables
- Font sizes and weights
- Layout and spacing
- Component styling

## 🔧 Troubleshooting

### AI Chatbot Issues
If the AI chatbot is not responding:

1. **Check API Key**: Ensure you have a valid OpenAI API key in your `.env` file
2. **Install Dependencies**: Make sure all requirements are installed:
   ```bash
   pip install -r requirements.txt
   ```
3. **Test the Chatbot**: Run the test script to verify setup:
   ```bash
   python test_ai_chatbot.py
   ```
4. **Check Console**: Look for error messages in the Streamlit console output

### Common Issues
- **"OpenAI API key not found"**: Create a `.env` file with your API key
- **"Module not found"**: Install missing dependencies with `pip install -r requirements.txt`
- **"Rate limit exceeded"**: Wait a moment and try again, or check your OpenAI usage

## 📱 Deployment

### Cloud Deployment
The application can be deployed to:
- **Streamlit Cloud**: Connect your GitHub repository
- **Heroku**: Use the provided `requirements.txt`
- **AWS/GCP**: Deploy as a containerized application

## 📄 PDF Resume

The application references a PDF version of the resume. To enable PDF download:
1. Place your `main.pdf` file in the root directory
2. Uncomment the PDF download code in `src/utils.py`
3. The download button will appear in the contact section

## 🤝 Contributing

This project uses [Commitizen](https://commitizen-tools.github.io/commitizen/) to enforce consistent commit messages following the [Conventional Commits](https://www.conventionalcommits.org/) specification.

### Making Commits

**Option 1: Use the helper script (Recommended)**
```bash
# Stage your changes
git add .

# Use the commit helper script
./scripts/commit.sh
```

**Option 2: Use Commitizen directly**
```bash
# Stage your changes
git add .

# Use Commitizen
cz commit
```

**Option 3: Manual conventional commit (if you know the format)**
```bash
git commit -m "type(scope): description"
```

### Commit Message Format

All commits must follow this format:
```
type(scope): description
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `build`: Build system changes
- `ci`: CI/CD changes
- `chore`: Maintenance tasks
- `revert`: Reverting previous commits

**Examples:**
- `feat: add AI chatbot functionality`
- `fix(auth): resolve login issue`
- `docs: update README with deployment instructions`
- `style: format code with black`
- `refactor: improve code structure`

### Pre-commit Hook

A pre-commit hook is installed that will automatically reject commits that don't follow the conventional commits format. This ensures consistency across all commits.

---

Feel free to fork this repository and customize it for your own use. The code is well-documented and modular for easy modification.

## 📞 Contact

- **Email**: christopher.ton@sjsu.edu
- **LinkedIn**: [linkedin.com/in/chriztopherton](https://linkedin.com/in/chriztopherton)
- **GitHub**: [github.com/chriztopherton](https://github.com/chriztopherton)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ❤️ using Streamlit* 