# Data for experience
experience_data = [
    {
        "company": "Genentech",
        "title": "Data Engineer",
        "location": "San Diego County, CA",
        "duration": "Apr 2024 - Present",
        "achievements": [
            "Researched and spearheaded migration of prototype chat applications to a production-grade AWS platform, leveraging serverless APIs to invoke model capabilities using s3, Bedrock - OpenSearch, Agents, and metadata filtering, serving 50+ regulatory users interacting with global health authorities",
            "Refactored a data ingestion pipeline to transform and embed complex SOP documents, using Langchain and Azure AI indexes to host and store contexts",
            "Implemented LLM evaluation processes to assess model performance, identified baselines to drive optimization decisions and better RAG configurations"
        ],
        "technologies": ["AWS", "S3", "Bedrock", "OpenSearch", "LangChain", "Azure AI", "LLM", "RAG", "Serverless APIs"]
    },
    {
        "company": "Genentech",
        "title": "Data Scientist Intern",
        "location": "San Diego County, CA",
        "duration": "Jun 2022 - Apr 2024",
        "achievements": [
            "Developed complex time series regression models for manufacturing predictive maintenance, accelerating time to insight for outlier detection and root cause analysis",
            "Generated insights and recommendations for timely delivery of quality control through investigative queries and visuals",
            "Deployed an internal R software package for efficient and accurate querying of clinical reporting tables by innovating a sliding window search algorithm"
        ],
        "technologies": ["R", "Time Series Analysis", "Predictive Modeling", "Manufacturing Analytics", "Clinical Data"]
    },
    {
        "company": "Deloitte",
        "title": "Informatica TDM Engineer via Brooksource",
        "location": "Remote",
        "duration": "Feb 2022 - May 2022",
        "achievements": [
            "Leveraged Informatica to build source connectors, transform and prepare fields for data anonymization transformation procedures",
            "Designed evaluation and testing scripts in python to estimate risk of identification for PII attributes"
        ],
        "technologies": ["Informatica TDM", "Python", "Data Anonymization", "PII", "Risk Assessment"]
    },
    {
        "company": "Volta Charging",
        "title": "Data Curator",
        "location": "San Francisco Bay Area County, CA",
        "duration": "Nov 2021 - Mar 2022",
        "achievements": [
            "Developed python scripts to web scrape, transform and curate raw datasets to drive network planning analytics",
            "Designed tests to ensure a reliable process to continuously refresh data on a weekly cadence"
        ],
        "technologies": ["Python", "Web Scraping", "ETL", "Data Curation", "Network Analytics"]
    },
    {
        "company": "Volta Charging",
        "title": "Marketing Data Analyst Intern",
        "location": "San Francisco Bay Area County, CA",
        "duration": "Jul 2021 - Sep 2021",
        "achievements": [
            "Developed and maintained executive client-facing dashboards that automates information query to status report on EV performance, sustainability ad-hoc analysis requests, business insights across 10+ months",
            "Performed product, time series, geographical and longitudinal analyses to uncover correlations among consumer behavior and trends, leveraging Sigma Computing, Looker, SQL, Excel, Python, Snowflake, ESRI to retrieve, manipulate, analyze ads campaign KPI's and usage rates",
            "Collaborated cross-functionally with site sales, marketing, & engineering to support data storytelling",
            "Led training sessions for internal stakeholders on the efficient querying process via dashboard interface & methodologies, promoting efficiency by 50% and 100% respectively",
            "Identified and recommended latencies within data governance infrastructure, took proactive measures to ensure data lineages across BI tool platform was consistent, independent, and durable"
        ],
        "technologies": ["Sigma Computing", "Looker", "SQL", "Excel", "Python", "Snowflake", "ESRI", "Data Governance", "BI Tools"]
    },
    {
        "company": "Tesla",
        "title": "Data Annotation Specialist",
        "location": "San Francisco Bay Area County, CA",
        "duration": "Oct 2020 - Jun 2021",
        "achievements": [
            "Collaborated with project managers, engineers, and leads to ensure the quality of internal labeling software tool",
            "Improved Autopilot deep learning software by providing labeled data using image recognition and classification",
            "Performed quality assurance, reported bugs and communicated consistent feedback regarding feature latencies",
            "Maintained expected workflow performance quotas by using Excel to track progress, allowing time for essential data curation and backlog management"
        ],
        "technologies": ["Data Annotation", "Image Recognition", "Deep Learning", "Quality Assurance", "Excel"]
    },
    {
        "company": "Guardant Health",
        "title": "Biostatistician/Data Analyst Intern",
        "location": "San Francisco Bay Area County, CA",
        "duration": "Jun 2020 - Sep 2020",
        "achievements": [
            "Built and published an internal tool to profile patient journey undergoing treatment",
            "Modeled Kaplan-Meier survival curve to visualize time-to-event trend",
            "Prototyped interactive cohort/patient-level filtering Shiny features to segment and generate insightful views, based on database queries",
            "Developed and implemented an R Shiny dashboard to facilitate visualizations & embedded SQL insights from patient & prescription level data, manipulated & aggregated numerous real-world clinical genomic data sources",
            "Conducted survival analysis using Cox, Kaplan-Meier estimator, and log-rank tests for differences between comparable drugs and 100,000+ patient undergoing treatment durations lasting 125+ months",
            "Achieved data product queries requested by FDA and biopharma stakeholders, engaged in weekly data reviews and discussions regarding RWE and statistical analysis plans by presenting recommendations and findings",
            "Presented scaling prototype development updates to VP - product was adopted for internal use & medical affairs operations",
            "Contributed to paper: Abstract PS18-28: Genomic heterogeneity and associated clinical outcomes of breast cancers treated with CDK4/6 inhibitors: Insights from real-world clinical genomic data"
        ],
        "technologies": ["R", "R Shiny", "SQL", "Kaplan-Meier", "Cox Regression", "Survival Analysis", "Clinical Genomics", "FDA", "Biopharma"]
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