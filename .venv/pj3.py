import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Kiểm tra sự tồn tại của tệp Excel
file_path = 'sale_table.xlsx'
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Tệp '{file_path}' không tồn tại. Vui lòng kiểm tra đường dẫn tệp.")

# Đọc dữ liệu từ file Excel
data = pd.read_excel(file_path)

# Xử lý các giá trị thiếu (nếu có)
data = data.dropna()

# Tiền xử lý dữ liệu
# Chuyển đổi các biến phân loại thành các biến số
label_encoder_sales_channel = LabelEncoder()
label_encoder_payment_method = LabelEncoder()

data['SalesChannel_encoded'] = label_encoder_sales_channel.fit_transform(data['SalesChannel'])
data['PaymentMethod_encoded'] = label_encoder_payment_method.fit_transform(data['PaymentMethod'])

# Chọn các đặc trưng và biến mục tiêu
features = ['Quantity', 'SalesChannel_encoded', 'PaymentMethod_encoded']
target = 'TotalAmount'

X = data[features]
y = data[target]

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Khởi tạo mô hình hồi quy tuyến tính
model = LinearRegression()

# Huấn luyện mô hình
model.fit(X_train, y_train)

# Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá mô hình
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

# Hiển thị các hệ số hồi quy
coefficients = pd.DataFrame(model.coef_, features, columns=['Coefficient'])
print(coefficients)

# Vẽ biểu đồ so sánh giữa giá trị thực và giá trị dự đoán
plt.figure(figsize=(12, 6))
plt.scatter(y_test, y_pred, color='blue', edgecolor='black', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2)
plt.title('Actual vs Predicted Total Amount', fontsize=16)
plt.xlabel('Actual Total Amount', fontsize=12)
plt.ylabel('Predicted Total Amount', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

