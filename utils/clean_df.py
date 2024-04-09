import pandas as pd
import re

# Đọc DataFrame từ tệp CSV
# df = pd.read_csv('test0804.csv')

# # Hàm để đổi tên giá trị trong cột 'Label'
# def rename_label(value):
#     match = re.search(r'([A-Za-z0-9]+)', value)  # Trích xuất phần trước dấu '_' trong giá trị
#     if match:
#         return match.group()  # Trả về giá trị khớp
#     return value  # Nếu không khớp, trả về giá trị ban đầu

# # Đổi tên toàn bộ các bản ghi trong cột 'Label' thành matched_label tương ứng
# df['Label'] = df['Label'].apply(rename_label)

# # In ra DataFrame sau khi đã đổi tên

# # Lưu DataFrame mới vào tệp CSV
# df.to_csv('test1.csv', index=False)
df1 = pd.read_csv(
    'D:\TL_DH/nghiencuukhoahoc/predictorangesugar/data/data_brix_new.csv')
df2 = pd.read_csv('test1.csv')
df_new = pd.merge(df1, df2, on='Label')
df_new.to_csv('test_done1.csv', index=False)
