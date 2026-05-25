import json
import os
from data_loader import load_data
from hard_constraints import evaluate_hard_constraints
from soft_constraints import evaluate_soft_constraints

# THÊM ĐOẠN NÀY: Bộ dịch ép kiểu Numpy int64/float64 về chuẩn Python
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'item'):
            return obj.item()
        return super().default(obj)


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Trỏ tới file Excel do NSGA II vừa xuất ra
    excel_path = os.path.join(base_dir, "../exam-scheduling-engine-main NSGA II/outputs/Ket_Qua_Xep_Lich.xlsx")
    if not os.path.exists(excel_path):
        return
        
    # 2. Chạy đánh giá
    df_can_bo, df_ca_thi, df_lich_truc = load_data() 
    hard_results = evaluate_hard_constraints(df_can_bo, df_ca_thi, df_lich_truc)
    total_penalty, soft_results = evaluate_soft_constraints(df_can_bo, df_ca_thi, df_lich_truc)

    # 3. Gom dữ liệu cho Biểu đồ
    chart_data = []
    for rb, info in soft_results.items():
        if info['score'] > 0:
            chart_data.append({
                "name": rb.split('_')[1], 
                "penalty": round(info['score'], 2)
            })

    # 4. Định dạng dữ liệu tổng hợp
    output_data = {
        "total_score": round(total_penalty, 2),
        "charts": chart_data,
        "logs_hard": hard_results,
        "logs_soft": soft_results
    }

    # 5. Lưu JSON vào thư mục public của Web để Frontend dễ gọi
    json_path = os.path.join(base_dir, "../exam-scheduling-solver NSGA II/public/benchmark_result.json")

    # THÊM DÒNG NÀY: Yêu cầu hệ thống tự động tạo thư mục "public" nếu nó chưa tồn tại
    os.makedirs(os.path.dirname(json_path), exist_ok=True)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4, cls=CustomJSONEncoder)

if __name__ == "__main__":
    main()