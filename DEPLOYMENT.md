# Deployment Guide

This guide covers how to deploy Christopher Ton's Resume Website to various platforms.

## 🚀 Quick Start

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run src/app.py
```

## ☁️ Cloud Deployment Options

### 1. Streamlit Cloud (Recommended)

**Pros**: Free, easy setup, automatic deployments
**Cons**: Limited customization

#### Steps:
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select your repository
5. Set the path to `src/app.py`
6. Deploy!

#### Configuration:
- **Main file path**: `src/app.py`
- **Python version**: 3.8+
- **Requirements file**: `requirements.txt`

### 2. Heroku

**Pros**: Good free tier, easy deployment
**Cons**: Limited resources on free tier

#### Steps:
1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: streamlit run src/app.py --server.port=$PORT --server.address=0.0.0.0
   ```
3. Create `setup.sh`:
   ```bash
   mkdir -p ~/.streamlit/
   echo "\
   [server]\n\
   headless = true\n\
   port = $PORT\n\
   enableCORS = false\n\
   " > ~/.streamlit/config.toml
   ```
4. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### 3. AWS (EC2 + Docker)

**Pros**: Full control, scalable
**Cons**: More complex setup, costs

#### Dockerfile:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Docker Compose:
```yaml
version: '3.8'
services:
  resume-app:
    build: .
    ports:
      - "8501:8501"
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

### 4. Google Cloud Platform (Cloud Run)

**Pros**: Serverless, pay-per-use
**Cons**: Cold starts

#### Steps:
1. Create Dockerfile (same as above)
2. Build and deploy:
   ```bash
   gcloud builds submit --tag gcr.io/PROJECT_ID/resume-app
   gcloud run deploy resume-app --image gcr.io/PROJECT_ID/resume-app --platform managed
   ```

### 5. Azure (App Service)

**Pros**: Good integration with Azure services
**Cons**: More expensive than alternatives

#### Steps:
1. Create Azure App Service
2. Configure Python runtime
3. Deploy using Azure CLI or GitHub Actions

## 🔧 Configuration

### Environment Variables
```bash
# Optional: Set these for production
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

### Custom Domain
1. Purchase domain
2. Configure DNS records
3. Set up SSL certificate
4. Update Streamlit configuration

## 📊 Performance Optimization

### For Production:
1. **Enable caching**:
   ```python
   @st.cache_data
   def load_data():
       # Your data loading logic
   ```

2. **Optimize images**:
   - Use WebP format
   - Compress images
   - Use appropriate sizes

3. **Minimize dependencies**:
   - Remove unused packages
   - Use specific versions

4. **Enable compression**:
   - Configure web server (nginx/Apache)
   - Enable gzip compression

## 🔒 Security Considerations

### Production Checklist:
- [ ] Enable HTTPS
- [ ] Set secure headers
- [ ] Configure CORS properly
- [ ] Use environment variables for secrets
- [ ] Regular security updates
- [ ] Monitor for vulnerabilities

### Security Headers:
```python
# Add to your app.py
st.set_page_config(
    page_title="Christopher Ton - ML/Data Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add security headers
st.markdown("""
<meta http-equiv="Content-Security-Policy" content="default-src 'self' 'unsafe-inline' 'unsafe-eval' data: blob:;">
""", unsafe_allow_html=True)
```

## 📈 Monitoring & Analytics

### Recommended Tools:
- **Google Analytics**: Track visitors
- **Sentry**: Error monitoring
- **Uptime Robot**: Uptime monitoring
- **Google Search Console**: SEO monitoring

### Basic Analytics Setup:
```python
# Add to your app.py
import streamlit as st

# Track page views
if 'page_views' not in st.session_state:
    st.session_state.page_views = 0
st.session_state.page_views += 1

# Display analytics (optional)
if st.sidebar.checkbox("Show Analytics"):
    st.sidebar.metric("Page Views", st.session_state.page_views)
```

## 🚀 CI/CD Pipeline

### GitHub Actions Example:
```yaml
name: Deploy Resume Website

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        python -m pytest tests/
    
    - name: Deploy to Streamlit Cloud
      run: |
        # Your deployment commands
```

## 📞 Support

If you encounter issues during deployment:

1. Check the [Streamlit documentation](https://docs.streamlit.io)
2. Review platform-specific guides
3. Check logs for error messages
4. Ensure all dependencies are installed

## 🎯 Next Steps

After successful deployment:

1. **Test thoroughly** on the deployed platform
2. **Set up monitoring** and analytics
3. **Configure custom domain** (optional)
4. **Set up SSL certificate** (if not automatic)
5. **Create backup strategy**
6. **Document deployment process**

---

*Happy deploying! 🚀* 