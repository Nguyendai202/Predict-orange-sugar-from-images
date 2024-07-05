import pandas as pd
import json

# Đọc nội dung từ file JSON
with open('data/response_1712566288353.json') as file:
    json_data = file.read()

# Chuyển đổi từ JSON thành Python dictionary
data = json.loads(json_data)

# Lấy dữ liệu từ dictionary và tạo DataFrame
df = pd.DataFrame({
    'Label': list(data['predictions'].keys()),
    'Values': [value[0][0] for value in data['predictions'].values()],
    'Times': data['times']
})

# In ra DataFrame
# print(df)
df.to_csv("test0804.csv", index=False)
