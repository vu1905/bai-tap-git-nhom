def tinh_thue_thu_nhap(thu_nhap):
    thu_nhap_chiu_thue = thu_nhap - 4000000  # Giảm trừ gia cảnh

    # Sinh viên sẽ cập nhật công thức tính thuế ở đây
    return max(0, thu_nhap_chiu_thue * 0.05)  # Ví dụ: Thuế suất 10%

print("Thuế phải nộp của bạn là:", tinh_thue_thu_nhap(10000000))
