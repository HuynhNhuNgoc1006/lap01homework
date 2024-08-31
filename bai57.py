import random

class SinhVien:
    def __init__(self, ma_sv, ho_ten, diem_tb):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.diem_tb = diem_tb
        self.xep_loai = self.cap_nhat_xep_loai()

    def cap_nhat_xep_loai(self):
        if self.diem_tb < 3.5:
            return "Kém"
        elif 3.5 <= self.diem_tb < 5.0:
            return "Yếu"
        elif 5.0 <= self.diem_tb < 7.0:
            return "Trung bình"
        elif 7.0 <= self.diem_tb < 8.0:
            return "Khá"
        elif 8.0 <= self.diem_tb < 9.0:
            return "Giỏi"
        elif 9.0 <= self.diem_tb <= 10:
            return "Xuất sắc"

class QuanLySinhVien:
    def __init__(self):
        self.danh_sach_sv = []

    def khoi_tao_sv(self, danh_sach_sv):
        self.danh_sach_sv = danh_sach_sv

    def khoi_tao_ngau_nhien_sv(self, so_luong_sv):
        for _ in range(so_luong_sv):
            ma_sv = random.randint(10000, 99999)
            ho_ten = "Sinh Vien {}".format(ma_sv)
            diem_tb = round(random.uniform(0, 10), 1)
            sv = SinhVien(ma_sv, ho_ten, diem_tb)
            self.danh_sach_sv.append(sv)

    def xuat_thong_tin_sv(self):
        for sv in self.danh_sach_sv:
            print("Mã SV: {}, Họ tên: {}, Điểm TB: {}, Xếp loại học lực: {}".format(sv.ma_sv, sv.ho_ten, sv.diem_tb, sv.xep_loai))

    def tim_sv_theo_ma_sv(self, ma_sv):
        for sv in self.danh_sach_sv:
            if sv.ma_sv == ma_sv:
                return sv
        return None

    def tim_sv_theo_diem_tb(self, diem_tb):
        sv_diem_cao_nhat = None
        for sv in self.danh_sach_sv:
            if sv.diem_tb == diem_tb:
                sv_diem_cao_nhat = sv
        return sv_diem_cao_nhat

    def tra_ve_sv_diem_cao_nhat(self):
        self.danh_sach_sv.sort(key=lambda x: x.diem_tb, reverse=True)
        return self.danh_sach_sv[:10]

    def tra_ve_sv_diem_thap_nhat(self):
        self.danh_sach_sv.sort(key=lambda x: x.diem_tb)
        return self.danh_sach_sv[:10]


ql_sv = QuanLySinhVien()


danh_sach_sv = [SinhVien(10001, "Nguyen Van A", 8.5), SinhVien(10002, "Tran Thi B", 6.5), SinhVien(10003, "Le Van C", 4.5)]
ql_sv.khoi_tao_sv(danh_sach_sv)


ql_sv.khoi_tao_ngau_nhien_sv(5)

ql_sv.xuat_thong_tin_sv()


sv = ql_sv.tim_sv_theo_ma_sv(10002)
if sv:
    print("Sinh viên có mã SV 10002: {}, Xếp loại học lực: {}".format(sv.ho_ten, sv.xep_loai))
else:
    print("Không tìm thấy sinh viên có mã SV 10002")


sv_cao_nhat = ql_sv.tra_ve_sv_diem_cao_nhat()
print("Sinh viên có điểm TB cao nhất:")
