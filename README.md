# ECharts MySQL Demo

This project demonstrates a simple web application using ECharts for visualization, MySQL for data storage, FastAPI as the backend, and HTML for the frontend.

## Prerequisites
- Python 3.8+
- MySQL Server
- Node.js (optional, for local development server)
- Modern web browser

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pjlau/echarts-mysql-demo
   cd echarts-mysql-demo
   
2. Install required libraries:
   ```bash
   cd backend
   pip install -r requirements.txt
   
3. Run the backend app:
   ```bash
   uvicorn main:app --reload
   
4. Use a local development server:
   ```bash
   cd ..
   cd frontend
   python -m http.server 8080
   
5. Access at `http://localhost:8080`.

