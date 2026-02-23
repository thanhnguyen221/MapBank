# 🏦 Bank & ATM Geographic Management System

## 📖 Overview
This is a Web-based Geographic Information System (GIS) application for managing, distributing, and visualizing the locations of Banks, Branches, and ATMs. The project focuses on a clean database architecture (DRY) and optimizing spatial query performance.

## ✨ Key Features
* **Interactive Map:** Accurately displays and clusters the location coordinates of the Bank/Branch/ATM network.
* **Admin Dashboard & Authorization:** Monitors the operational status of ATMs (Active/Maintenance/Offline) in real-time.
* **Database Optimization:** Applies strategic Database Indexing on Latitude/Longitude fields for lightning-fast map loading.
* **Authentication Security:** Strict session management, form protection using CSRF Tokens, and thorough prevention of Open Redirect vulnerabilities.

## 🛠 Tech Stack
* **Backend:** Python, Django
* **Database:** SQLite (Dev environment) / PostgreSQL
* **Frontend:** HTML, CSS, JavaScript 

## 🚀 Installation

**1. Clone the repository**
```bash
git clone [https://github.com/thanhnguyen221/MapBank.git](https://github.com/thanhnguyen221/MapBank.git)
cd MapBank/bank_project