import json
import csv

# 輸入和輸出檔案路徑
input_json_file = 'i18n-report.json'
output_csv_file = 'i18n-report.csv'

# 讀取 JSON 檔案
with open(input_json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 提取 missingKeys 部分
missing_keys = data.get('missingKeys', [])

# 準備 CSV 資料
csv_data = []
for item in missing_keys:
    key = item['path']  # 例如 "home.greeting"
    module = key.split('.')[0]  # 從 key 中提取第一部分，例如 "home"
    
    # 每個項目對應 CSV 的一行
    row = {
        'Key': key,
        'Chinese (zh)': '',  # 留空，後續手動填入
        'English (en)': '',  # 留空，後續手動填入
        'Module': module,
        'Description': ''  # 留空，後續手動填入
    }
    csv_data.append(row)

# 定義 CSV 欄位
fieldnames = ['Key', 'Chinese (zh)', 'English (en)', 'Module', 'Description']

# 寫入 CSV 檔案
with open(output_csv_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # 寫入表頭
    writer.writerows(csv_data)  # 寫入資料

print(f"CSV file '{output_csv_file}' has been generated successfully!")