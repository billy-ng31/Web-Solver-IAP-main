import os

# ==========================================
# CẤU HÌNH ĐƯỜNG DẪN VÀ TÊN FILE DỮ LIỆU
# ==========================================
# 1. Lấy vị trí gốc của chính file config.py này (thư mục benchmark)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Trỏ đường dẫn ngược ra ngoài và đi vào thư mục của Web Solver NSGA II
PATH_CAN_BO = os.path.join(BASE_DIR, "../exam-scheduling-engine-main NSGA II/data/can_bo.xlsx")
PATH_CA_THI = os.path.join(BASE_DIR, "../exam-scheduling-engine-main NSGA II/data/ca_thi.xlsx")
PATH_LICH_TRUC = os.path.join(BASE_DIR, "../exam-scheduling-engine-main NSGA II/outputs/Ket_Qua_Xep_Lich.xlsx")

# ==========================================
# CẤU HÌNH TRỌNG SỐ ĐIỂM PHẠT (PENALTIES)
# ==========================================
# Trọng số càng cao thể hiện tiêu chí càng quan trọng. 
# Lịch trình tốt là lịch trình có tổng điểm phạt càng thấp.

WEIGHT_FAIRNESS = 8                 # Phạt nếu số ca trực chênh lệch so với mức trung bình
WEIGHT_DISTANCE = 0.1              # Phạt dựa trên tổng khoảng cách di chuyển
WEIGHT_SAME_DAY_DIFF_FACILITY = 6   # Phạt nếu gác >2 ca/ngày mà phải di chuyển 2 cơ sở khác nhau
WEIGHT_MIN_SHIFT = 5                # Phạt nếu có cán bộ không được gác ca nào (số ca = 0)
WEIGHT_CONSECUTIVE_SHIFTS = 4       # Phạt nếu 2 ca xếp quá gần nhau (thời gian nghỉ ngắn)
WEIGHT_AGE_PRIORITY = 3             # Phạt nếu xếp nhiều ca cho người lớn tuổi (>45 tuổi)
WEIGHT_PARTNER_DIVERSITY = 2        # Phạt nếu 2 người gác chung với nhau quá nhiều lần
WEIGHT_WEEKEND = 1                  # Phạt nếu phải gác vào ngày nghỉ (Thứ 7, Chủ Nhật)
WEIGHT_GENDER_BALANCE = 0           # Phạt nếu số lượng nữ gác quá nhiều

# ==========================================
# CÁC HẰNG SỐ LOGIC KHÁC (Tùy chọn)
# ==========================================
AGE_THRESHOLD = 45                  # Ngưỡng tuổi để tính ưu tiên
MIN_REST_HOURS = 3                  # Thời gian nghỉ tối thiểu giữa 2 ca (đơn vị: giờ)
MAX_PARTNER_REPETITION = 3          # Số lần tối đa 2 người được gác chung trước khi bị phạt