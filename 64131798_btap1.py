import string

def tan_suat_ky_tu(text):
    tan_suat = {}
    for ky_tu in string.ascii_uppercase:
        tan_suat[ky_tu] = text.count(ky_tu)
    return sorted(tan_suat.items(), key=lambda x: x[1], reverse=True)

def giai_ma_don_bang(text_ma, khoa_giai):
    text_giai_ma = ""
    for ky_tu in text_ma:
        if ky_tu in string.ascii_uppercase:
            vi_tri = ord(ky_tu) - ord('A')
            text_giai_ma += khoa_giai[vi_tri]
        else:
            text_giai_ma += ky_tu
    return text_giai_ma

# Ví dụ mã hóa:
text_ma = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"
tan_suat = tan_suat_ky_tu(text_ma)

print("Tần suất ký tự:", tan_suat)

# Dựa trên phân tích tần suất ký tự, nhập khóa giải (ví dụ: giải mã thủ công)
khoa_giai = "ETAOINSHRDLCUMWFGYPBVKJXQZ"  # Khóa tạm thời, sắp xếp theo tần suất tiếng Anh
text_giai_ma = giai_ma_don_bang(text_ma, khoa_giai)

print("Kết quả giải mã:", text_giai_ma)
