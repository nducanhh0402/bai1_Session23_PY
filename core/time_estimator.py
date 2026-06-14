import datetime

def predict_eta(departure_str, distance_km, speed=60):
    """Tính toán thời gian ETA dựa trên khoảng cách và vận tốc."""
    dep_time = datetime.datetime.strptime(departure_str, "%Y-%m-%d %H:%M:%S")
    hours_needed = distance_km / speed
    
    # timedelta tự động quy đổi số thập phân của giờ ra phút/giây chính xác
    eta = dep_time + datetime.timedelta(hours=hours_needed)
    
    # Loại bỏ phần microseconds để log ra console cho gọn (nếu có)
    return eta.replace(microsecond=0)