A full-stack retail intelligence system built with Python, SQL, and Power BI — delivering weekly-refreshed dashboards, customer segmentation, sales forecasting, and inventory insights from transactional retail data.

📋 Table of Contents

Overview
Features
Tech Stack
Project Structure
Getting Started
Data Sources
Analysis Modules
Power BI Dashboards
Dashboard Refresh Schedule
Results & Outputs
Contributing
License


🧭 Overview
This project is an end-to-end retail analytics pipeline that ingests raw sales, customer, and inventory data — processes it through SQL transformations and Python analysis — and surfaces insights via interactive Power BI dashboards that are refreshed every week.
Key business questions answered:

Which products and categories are driving or dragging revenue?
Who are our best customers, and which ones are at risk of churning?
How will sales trend over the next 30/60/90 days?
Where are inventory bottlenecks, overstocks, and dead stock?


✨ Features
ModuleDescription📊 EDADeep exploratory analysis on sales, customers, and inventory👥 Customer SegmentationRFM-based clustering to group customers by behavior📈 Sales ForecastingTime-series models (ARIMA / Prophet) for weekly & monthly predictions📦 Inventory AnalysisTurnover rates, overstock detection, reorder signals🖥️ Power BI DashboardsInteractive visuals refreshed automatically every week🗄️ SQL PipelinesStructured queries for data cleaning and transformation

🛠️ Tech Stack

Language: Python 3.9+
Database: SQL (PostgreSQL / MySQL)
BI Tool: Microsoft Power BI (weekly scheduled refresh)
Key Python Libraries:

pandas, numpy — data manipulation
matplotlib, seaborn, plotly — visualization
scikit-learn — segmentation & ML models
statsmodels, prophet — forecasting
sqlalchemy, psycopg2 — database connectivity
openpyxl — Excel/report export


🗂️ Project Structure
retail-analysis/
│
├── data/
│   ├── raw/                        # Raw source data (DO NOT edit)
│   ├── processed/                  # Cleaned & transformed datasets
│   └── external/                   # Holiday calendars, region maps, etc.
│
├── sql/
│   ├── schema.sql                  # Table definitions
│   ├── cleaning.sql                # Data cleaning queries
│   ├── sales_aggregation.sql       # Sales rollup queries
│   ├── customer_metrics.sql        # RFM and customer KPIs
│   └── inventory_metrics.sql       # Stock and turnover queries
│
├── notebooks/
│   ├── 01_eda_sales.ipynb          # Sales EDA
│   ├── 02_eda_customers.ipynb      # Customer EDA
│   ├── 03_eda_inventory.ipynb      # Inventory EDA
│   ├── 04_segmentation.ipynb       # RFM customer segmentation
│   └── 05_forecasting.ipynb        # Sales forecasting models
│
├── src/
│   ├── data/
│   │   ├── ingestion.py            # Data loading from DB / CSV
│   │   └── preprocessing.py        # Feature engineering & cleaning
│   ├── analysis/
│   │   ├── sales.py                # Sales trend analysis
│   │   ├── customers.py            # Customer analytics & RFM
│   │   └── inventory.py            # Inventory performance
│   ├── models/
│   │   ├── segmentation.py         # K-Means / RFM clustering
│   │   └── forecasting.py          # ARIMA / Prophet models
│   └── utils/
│       ├── db_connector.py         # SQL connection helper
│       └── plots.py                # Reusable chart functions
│
├── powerbi/
│   ├── retail_dashboard.pbix       # Main Power BI report file
│   └── refresh_schedule.md         # Dashboard refresh config notes
│
├── outputs/
│   ├── reports/                    # Auto-generated weekly reports
│   ├── figures/                    # Exported charts and plots
│   └── models/                     # Saved model files (.pkl)
│
├── tests/                          # Unit and integration tests
├── requirements.txt
├── .env.example
├── config.yaml
└── README.md

🚀 Getting Started
Prerequisites

Python 3.9+
PostgreSQL or MySQL database
Microsoft Power BI Desktop
pip

Installation

Clone the repository

bash   git clone https://github.com/taskinmulani-deep/retail-analysis.git
   cd retail-analysis

Create a virtual environment

bash   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows

Install dependencies

bash   pip install -r requirements.txt

Configure environment variables

bash   cp .env.example .env
Edit .env and fill in:
   DB_HOST=your_database_host
   DB_PORT=5432
   DB_NAME=retail_db
   DB_USER=your_username
   DB_PASSWORD=your_password

Set up the database schema

bash   psql -U your_username -d retail_db -f sql/schema.sql
   psql -U your_username -d retail_db -f sql/cleaning.sql

Run the pipeline

bash   python src/main.py --config config.yaml

🗄️ Data Sources
DatasetDescriptionFormatsales_transactionsPOS transaction records with invoice detailsSQL Table / CSVcustomersCustomer master data — demographics, region, join dateSQL Table / CSVproductsProduct catalog — SKU, category, priceSQL Table / CSVinventoryDaily stock level snapshots per store/warehouseSQL Table / CSVstoresStore/branch metadata — location, size, regionSQL Table / CSV

Note: Place raw CSV files in data/raw/ before running the pipeline. Sensitive data should never be committed to the repository.


📊 Analysis Modules
🔍 Exploratory Data Analysis (EDA)

Distribution of sales by category, region, and time period
Missing value profiling and outlier detection
Correlation heatmaps between sales, pricing, and quantity
Customer purchase frequency distributions

👥 Customer Segmentation

RFM Scoring — Recency, Frequency, Monetary value per customer
K-Means Clustering — Group customers into behavioral tiers
Segment labels: Champions · Loyal · Potential · At-Risk · Lost
Cohort retention analysis across monthly acquisition groups

📈 Sales Forecasting

ARIMA / SARIMA — For stationary and seasonal time series
Facebook Prophet — Holiday-aware seasonal decomposition
Forecast horizon: 30 / 60 / 90 days
Outputs: predicted sales, confidence intervals, trend components

📦 Inventory Analysis

Stock turnover ratio by SKU and category
Overstock and dead stock flagging
Low-stock / reorder point alerts
Days of inventory outstanding (DIO) metric


🖥️ Power BI Dashboards
The powerbi/retail_dashboard.pbix file contains 4 interactive report pages:
PageKPIs Covered📊 Sales OverviewRevenue, units sold, avg. order value, growth %👥 Customer InsightsSegment distribution, retention, LTV, churn risk📦 Inventory HealthStock levels, turnover, overstock alerts📈 Forecast View30/60/90-day projections with confidence bands
Opening the Dashboard

Install Power BI Desktop
Open powerbi/retail_dashboard.pbix
Update the data source connection to your database in Transform Data → Data Source Settings


🔄 Dashboard Refresh Schedule
Power BI dashboards are refreshed every week with the latest data.
RefreshScheduleScope🟢 Weekly Auto-RefreshEvery Monday, 6:00 AMAll dashboard pages📤 Data Pipeline RunEvery Sunday, 11:00 PMSQL + Python ETL📁 Report ExportEvery Monday, 7:00 AMPDF summary → outputs/reports/

To configure scheduled refresh in Power BI Service, publish the .pbix to your workspace and set up the gateway connection under Dataset Settings → Scheduled Refresh.


📤 Results & Outputs
OutputLocationDescriptionWeekly Sales Reportoutputs/reports/Auto-generated PDF summaryEDA Chartsoutputs/figures/PNG/SVG visualizationsSegment Labelsoutputs/segments.csvCustomer RFM tier assignmentsForecast Dataoutputs/forecast.csvPredicted sales with CI bandsTrained Modelsoutputs/models/Serialized .pkl model files

🧪 Running Tests
bashpytest tests/ -v

🤝 Contributing

Fork the repository
Create a feature branch

bash   git checkout -b feature/your-feature-name

Commit your changes

bash   git commit -m "Add: description of your feature"

Push and open a Pull Request

bash   git push origin feature/your-feature-name

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
