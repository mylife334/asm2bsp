import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file Excel
file_path = 'sale_table.xlsx'
data = pd.read_excel(file_path)

# Thiết lập phong cách chung cho biểu đồ
plt.style.use('ggplot')  # Sử dụng phong cách 'ggplot'

# Biểu đồ phân phối (Histogram) cho cột 'TotalAmount'
plt.figure(figsize=(12, 6))
plt.hist(data['TotalAmount'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Total Amount', fontsize=16)
plt.xlabel('Total Amount', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Biểu đồ hộp (Box Plot) để xem phân phối của 'TotalAmount' theo 'SalesChannel'
plt.figure(figsize=(12, 6))
data.boxplot(column='TotalAmount', by='SalesChannel', grid=False, patch_artist=True,
             boxprops=dict(facecolor='lightblue', color='black'),
             medianprops=dict(color='red'))
plt.title('Distribution of Total Amount by Sales Channel', fontsize=16)
plt.suptitle('')  # Loại bỏ tiêu đề mặc định của Matplotlib
plt.xlabel('Sales Channel', fontsize=12)
plt.ylabel('Total Amount', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Biểu đồ cột (Bar Plot) cho tổng số lượng sản phẩm bán ra theo từng phương thức thanh toán
plt.figure(figsize=(12, 6))
payment_method_summary = data.groupby('PaymentMethod')['Quantity'].sum()
payment_method_summary.plot(kind='bar', color='salmon', edgecolor='black')
plt.title('Total Quantity Sold by Payment Method', fontsize=16)
plt.xlabel('Payment Method', fontsize=12)
plt.ylabel('Total Quantity', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Biểu đồ tản mạn (Scatter Plot) để thấy mối quan hệ giữa Tổng Số Tiền và Số Lượng
plt.figure(figsize=(12, 6))
plt.scatter(data['Quantity'], data['TotalAmount'], c='green', edgecolor='black', alpha=0.6)
plt.title('Relationship between Quantity and Total Amount', fontsize=16)
plt.xlabel('Quantity', fontsize=12)
plt.ylabel('Total Amount', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
