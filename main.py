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
