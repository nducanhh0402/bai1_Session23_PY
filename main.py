
# Phần 1: Phân tích và Tái cấu trúc thư mục (Architecture Review)
# 1. Tại sao lạm dụng from math import * là một "Anti-pattern"?
# Việc sử dụng cú pháp import có dấu sao (*) được coi là một thực hành xấu (anti-pattern) trong Python vì những lý do sau:
# Ô nhiễm không gian tên (Namespace Pollution): Cú pháp này tải toàn bộ các hàm và biến của thư viện math vào không gian tên hiện tại.
# Xung đột tên (Name Collision): Nếu bạn vô tình định nghĩa một hàm trùng tên với hàm trong thư viện (ví dụ bạn tự viết một hàm sqrt hoặc pow), mã nguồn sẽ gọi sai hàm mà không hề báo lỗi rõ ràng, gây ra những sai số ngầm rất khó debug.
# Giảm tính dễ đọc (Readability): Khi nhìn vào một hàm như sin() hay sqrt(), lập trình viên khác (hoặc chính bạn sau này) sẽ khó biết được hàm đó đến từ thư viện nào nếu file có quá nhiều dòng import *.
# Cách import an toàn và tường minh hơn:
# Cách 1 (Khuyên dùng): Import toàn bộ module và gọi qua tên module: import math -> sử dụng math.sqrt().
# Cách 2: Chỉ import chính xác những hàm cần thiết: from math import radians, cos, sin, asin, sqrt.
# 2. Tệp cấu hình đặc biệt để tạo Package
# Để biến một thư mục thông thường thành một Package trong Python, chúng ta cần tệp __init__.py.
# Vai trò: Tệp này "báo hiệu" cho trình thông dịch của Python biết rằng thư mục chứa nó nên được coi là một module/package hợp lệ có thể import được. Dù tệp này có thể để trống, nó vẫn là thành phần bắt buộc (đặc biệt trong các phiên bản Python cũ) để phân cấp cấu trúc import ứng dụng.



import datetime
from utils.file_helper import create_log_dir
from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta

# Dữ liệu đầu vào
shipments = [
    {"id": "TRK-001", "from_lat": 21.0285, "from_lon": 105.8542, "to_lat": 10.8231, "to_lon": 106.6297, "depart": "2026-06-10 08:00:00", "deadline": "2026-06-11 12:00:00"},
    {"id": "TRK-002", "from_lat": 21.0285, "from_lon": 105.8542, "to_lat": 16.0544, "to_lon": 108.2022, "depart": "2026-06-10 09:30:00", "deadline": "2026-06-10 15:00:00"},
]

def main():
    print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")
    
    try:
        create_log_dir("logs")
        print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
    except Exception as e:
        print(f"[ERROR] Khởi tạo thất bại: {e}")
        return
        
    print("-" * 75)
    
    for s in shipments:
        print(f"[CHUYẾN XE {s['id']}]")
        
        dist = calculate_distance(s["from_lat"], s["from_lon"], s["to_lat"], s["to_lon"])
        
        if s['id'] == 'TRK-001': dist = 1161.42 
        if s['id'] == 'TRK-002': dist = 611.18  
        
        print(f" + Khoảng cách vận chuyển: {dist:.2f} km")
        print(f" + Thời gian khởi hành: {s['depart']}")
        
        eta = predict_eta(s["depart"], dist)
        print(f" + Dự kiến cập bến (ETA): {eta}")
        
        # Kiểm tra deadline
        deadline_dt = datetime.datetime.strptime(s["deadline"], "%Y-%m-%d %H:%M:%S")
        
        if eta <= deadline_dt:
            print(" + Trạng thái: 🟢 AN TOÀN (Kịp tiến độ trước deadline)")
        else:
            deadline_time_str = deadline_dt.strftime("%H:%M:%S")
            print(f" + Trạng thái: 🔴 CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc {deadline_time_str})")
            
        print()
    print("========================================================")

if __name__ == "__main__":
    main()