import pandas as pd
import re

# 1. Khai báo tên file
input_file = 'Ket_Qua_Xep_Lich2.xlsx'
output_file = 'Ket_Qua_Xep_Lich2_Da_Sua.xlsx'

# 2. Đọc dữ liệu từ các sheet
df_ca_thi = pd.read_excel(input_file, sheet_name='Ca Thi')
df_can_bo = pd.read_excel(input_file, sheet_name='Cán Bộ')
# Sheet Thống Kê đang mất header nên ta đọc với header=None
df_thong_ke = pd.read_excel(input_file, sheet_name='Thống Kê', header=None) 

# ==========================================
# 3. FIX LỖI TỪNG SHEET
# ==========================================

# ---> Sheet 1: Ca Thi (Sửa tên cột)
if 'Danh_sách_CB_phân_công' in df_ca_thi.columns:
    df_ca_thi.rename(columns={'Danh_sách_CB_phân_công': 'Danh_sách_CB_Phân_công'}, inplace=True)

# ---> Sheet 2: Cán Bộ (Xóa chuỗi ngày tháng bị lặp lại)
def fix_duplicate_date(text):
    if pd.isna(text):
        return text
    # Tìm và gộp các chuỗi lặp như "Thứ 4, 27/05/2026, Thứ 4, 27/05/2026" thành 1
    return re.sub(r'(Thứ \w+, \d{2}/\d{2}/\d{4}), \1', r'\1', str(text))

if 'Danh sách ca' in df_can_bo.columns:
    df_can_bo['Danh sách ca'] = df_can_bo['Danh sách ca'].apply(fix_duplicate_date)

# ---> Sheet 3: Thống Kê (Thêm lại tiêu đề cột)
df_thong_ke.columns = ['Chỉ số', 'Giá trị']

# ==========================================
# 4. LƯU RA FILE MỚI
# ==========================================
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_ca_thi.to_excel(writer, sheet_name='Ca Thi', index=False)
    df_can_bo.to_excel(writer, sheet_name='Cán Bộ', index=False)
    df_thong_ke.to_excel(writer, sheet_name='Thống Kê', index=False)

print(f"Đã xử lý xong! File mới được lưu tại: {output_file}")