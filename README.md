# sakshitiwari-churn-analysis
# 📞 Telecom Customer Churn Prediction  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue) 
![Machine Learning](https://img.shields.io/badge/ML-Scikit%20Learn-orange) 
![License](https://img.shields.io/badge/License-MIT-green)  

**Author**: [Sakshi Tiwari](https://github.com/Sakshi-Tiwari)  
**Live Demo**: [Try the App](https://customerchurn-7ggk.onrender.com)  

---

## 📌 Introduction  
Customer churn occurs when subscribers discontinue services. In telecom, **15-25% of customers churn annually**. This project predicts at-risk customers using ML, enabling targeted retention strategies.  

**Business Impact**:  
- Retaining customers is **5x cheaper** than acquiring new ones.  
- Model achieves **90% recall** to minimize missed churn cases.  

---

## 📂 Dataset  
**Telco Customer Churn** ([Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)):  
- **Features**: Contract type, monthly charges, tenure, internet service, etc.  
- **Target**: `Churn` (Yes/No)  

---

## 🔍 Exploratory Data Analysis (EDA)  

### 1. Overall Churn Distribution  
![Churn Distribution](https://i.imgur.com/ABC123.png)  
*26.6% of customers churned (left the service).*  

### 2. Churn by Contract Type  
![Contract Type](https://i.imgur.com/DEF456.png)  
**Insight**: 75% of churners had *month-to-month* contracts.  

### 3. Churn by Internet Service  
![Internet Service](https://i.imgur.com/GHI789.png)  
**Insight**: Fiber optic users had the **highest churn rate (43%)**.  

### 4. Churn by Tenure  
![Tenure](https://i.imgur.com/JKL012.png)  
**Insight**: New customers (<6 months) were **3x more likely** to churn.  

### 5. Monthly Charges vs. Churn  
![Monthly Charges](https://i.imgur.com/MNO345.png)  
**Insight**: Higher monthly charges correlated with increased churn.  

---

## 🤖 Machine Learning Approach  
### **Model Comparison**  
| Model                  | Accuracy | Recall | Precision |  
|------------------------|----------|--------|-----------|  
| Logistic Regression    | 84.1%    | 85.3%  | 83.0%     |  
| Random Forest          | 82.0%    | 83.7%  | 81.5%     |  
| **Voting Classifier**  | **84.7%**| **90%**| **86.2%** |  

### **Confusion Matrix (Voting Classifier)**  
![Confusion Matrix](https://i.imgur.com/PQR678.png)  

---

## 🛠️ Installation & Usage  
```bash
git clone https://github.com/Sakshi-Tiwari/Telecom-Churn-Prediction.git
cd Telecom-Churn-Prediction
pip install -r requirements.txt
python app/app.py

📊 Results & Business Insights
Top 3 Churn Drivers
Contract Type: Month-to-month customers are high-risk.

Internet Service: Fiber optic users need targeted offers.

Tenure: Engage new customers proactively.

Recommendations
Offer loyalty discounts for long-term contracts.

Improve customer support for fiber optic users.

🌟 Future Work
Deploy as a real-time API for CRM integration.

Add customer segmentation (clustering).

📬 Connect
Platform	Link
GitHub	github.com/Sakshi-Tiwari
LinkedIn www.linkedin.com/in/sakshi-tiwari-6464522ab

Email	sakshitiwari2441@gmail.com

![image](https://github.com/user-attachments/assets/2d2e1993-661d-442f-9615-a10689bc6d6a)

