import os

def create_log_dir(dir_name):
    """Tạo thư mục an toàn, tránh lỗi FileExistsError."""
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
