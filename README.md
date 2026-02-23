# 🏦 Bank & ATM Geographic Management System

## 📖 Giới thiệu (Overview)
Đây là hệ thống Web ứng dụng bản đồ GIS (Geographic Information System) cho phép quản lý, phân bổ và trực quan hóa vị trí của các Ngân hàng, Chi nhánh và cây ATM. Dự án tập trung vào kiến trúc cơ sở dữ liệu sạch (DRY) và tối ưu hóa hiệu suất truy vấn không gian.

## ✨ Tính năng nổi bật (Key Features)
* **Bản đồ trực quan:** Hiển thị và phân cụm (clustering) chính xác tọa độ vị trí của hệ thống Bank/Branch/ATM.
* **Quản trị phân quyền (Admin Dashboard):** Giám sát trạng thái hoạt động của ATM (Active/Maintenance/Offline) theo thời gian thực.
* **Tối ưu Database:** Ứng dụng Database Indexing chiến lược trên các trường Vĩ độ/Kinh độ giúp load bản đồ siêu tốc.
* **Bảo mật luồng xác thực:** Quản lý Session chặt chẽ, bảo vệ form bằng CSRF Token và ngăn chặn triệt để lỗ hổng Open Redirect.

## 🛠 Công nghệ sử dụng (Tech Stack)
* **Backend:** Python, Django
* **Database:** SQLite (Môi trường dev) / PostgreSQL
* **Frontend:** HTML, CSS, JavaScript 

## 🚀 Hướng dẫn cài đặt (Installation)

**1. Clone dự án về máy**
```bash
git clone [https://github.com/thanhnguyen221/MapBank.git](https://github.com/thanhnguyen221/MapBank.git)
cd MapBank/bank_project