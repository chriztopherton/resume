# Data for experience
experience_data = [
    {
        "company": "Genentech",
        "title": "Data Engineer",
        "location": "San Diego County, CA",
        "duration": "Apr 2024 - Present",
        "achievements": [
            "Built and deployed a full stack LLM-powered chat assistant using Streamlit, owning end-to-end architecture including data ingestion, ETL, prompt engineering, model evaluation, inferencing, and deployment using Docker and Kubernetes",
            "Designed and implemented scalable ETL pipelines to process and embed Confluence-based documentation into Azure AI Search, enabling semantic search through RAG and LangChain workflows",
            "Developed serverless APIs using AWS Lambda, S3, Bedrock, and OpenSearch to support multiple Retrieval-Augmented Generation (RAG) applications, reducing latency and improving maintainability",
            "Engineered performant data models in Snowflake using Talend, PySpark, and SQL across 7+ global sources; leveraged dbt to enforce testing and materializations via GitLab CI/CD pipelines"
        ],
        "technologies": ["Streamlit", "Docker", "Kubernetes", "Azure AI Search", "RAG", "LangChain", "AWS Lambda", "S3", "Bedrock", "OpenSearch", "Snowflake", "Talend", "PySpark", "dbt", "GitLab CI/CD"]
    },
    {
        "company": "Genentech",
        "title": "Data Scientist Intern",
        "location": "San Diego County, CA",
        "duration": "Jun 2022 - Apr 2024",
        "achievements": [
            "Reduced resolution times by 20% and drove improvements in operational efficiency by developing and monitoring predictive anomaly detection models using XGBoostRegressor, in partnership with C3.AI",
            "Automated clinical reporting validation processes by building and deploying a sliding-window search module in R, reducing manual effort, streamlining cross-checks, and enhancing data accuracy and reliability"
        ],
        "technologies": ["XGBoost", "C3.AI", "R", "Predictive Modeling", "Anomaly Detection"]
    },
    {
        "company": "Deloitte",
        "title": "Data Engineer via Brooksource",
        "location": "Remote",
        "duration": "Feb 2022 - May 2022",
        "achievements": [
            "Deployed data pipelines using Informatica TDM to automate sensitive data masking, ensuring compliance with data protection regulations and minimizing security risks",
            "Developed Python-based solutions to model data distributions and population parameters, enabling risk assessment for data re-identification through quasi-identifier and pseudo-anonymization analysis"
        ],
        "technologies": ["Informatica TDM", "Python", "Data Masking", "Compliance", "Risk Assessment"]
    },
    {
        "company": "Shell Recharge (formerly Volta Charging)",
        "title": "Data Curator",
        "location": "San Francisco Bay Area County, CA",
        "duration": "Nov 2021 - Mar 2022",
        "achievements": [
            "Automated and optimized data ingestion workflows by developing Python scripts to extract, transform, and curate datasets from over three vendor sources, achieving a 30% improvement in data quality and observability"
        ],
        "technologies": ["Python", "ETL", "Data Quality", "Automation"]
    }
]

# Skills data
skills_data = {
    "Languages": ["Python", "R", "SQL"],
    "Data Engineering & Processing": ["PySpark", "Pandas", "NumPy", "scikit-learn", "SageMaker", "LangChain"],
    "LLM & ML Frameworks": ["AWS SageMaker", "AWS Bedrock", "Dataiku DSS", "PyTorch"],
    "Cloud Platforms": ["AWS (S3, Lambda, Redshift)", "GCP BigQuery", "Azure AI Indexes"],
    "DevOps & Containerization": ["Docker", "Git", "CI/CD pipelines"],
    "Development Tools": ["VSCode", "Jupyter Notebooks"],
    "Project Management & Documentation": ["Jira", "Confluence"]
}

# Projects data
projects_data = [
    {
        "title": "LLM-Powered Chat Assistant",
        "description": "Full-stack application using Streamlit with end-to-end architecture including data ingestion, ETL, prompt engineering, model evaluation, and deployment",
        "technologies": ["Streamlit", "Docker", "Kubernetes", "RAG", "LangChain"],
        "impact": "Deployed production-ready chat assistant for enterprise use"
    },
    {
        "title": "RAG Applications with Serverless APIs",
        "description": "Developed multiple Retrieval-Augmented Generation applications using AWS Lambda, S3, Bedrock, and OpenSearch",
        "technologies": ["AWS Lambda", "S3", "Bedrock", "OpenSearch", "RAG"],
        "impact": "Reduced latency and improved maintainability of AI applications"
    },
    {
        "title": "Predictive Anomaly Detection Models",
        "description": "Developed and monitored predictive models using XGBoostRegressor for anomaly detection in partnership with C3.AI",
        "technologies": ["XGBoost", "C3.AI", "Predictive Modeling"],
        "impact": "Reduced resolution times by 20% and improved operational efficiency"
    },
    {
        "title": "Clinical Reporting Validation Automation",
        "description": "Built and deployed sliding-window search module in R for clinical reporting validation",
        "technologies": ["R", "Automation", "Clinical Data"],
        "impact": "Reduced manual effort and enhanced data accuracy and reliability"
    }
] 