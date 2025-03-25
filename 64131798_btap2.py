from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def ma_hoa_file(file_vao, file_ra, khoa):
    cipher = AES.new(khoa, AES.MODE_CBC)  # Chế độ mã hóa CBC
    with open(file_vao, 'rb') as f:
        du_lieu = f.read()
    ma_hoa_du_lieu = cipher.encrypt(pad(du_lieu, AES.block_size))
    
    with open(file_ra, 'wb') as f:
        # Lưu IV (vector khởi tạo) và dữ liệu đã mã hóa vào file đầu ra
        f.write(cipher.iv)
        f.write(ma_hoa_du_lieu)

def giai_ma_file(file_vao, file_ra, khoa):
    with open(file_vao, 'rb') as f:
        iv = f.read(16)  # Đọc IV từ đầu file
        ma_hoa_du_lieu = f.read()
    cipher = AES.new(khoa, AES.MODE_CBC, iv)
    du_lieu = unpad(cipher.decrypt(ma_hoa_du_lieu), AES.block_size)

    with open(file_ra, 'wb') as f:
        f.write(du_lieu)

# Ví dụ:
khoa = b'ThisIsA16ByteKey'  # Khóa phải có độ dài là 16, 24 hoặc 32 byte
file_goc = 'input.txt'
file_ma_hoa = 'encrypted.bin'
file_giai_ma = 'decrypted.txt'

# Mã hóa file
ma_hoa_file(file_goc, file_ma_hoa, khoa)

# Giải mã file
giai_ma_file(file_ma_hoa, file_giai_ma, khoa)
