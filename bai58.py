class NhanVien:
    def __init__(self, ma_nv, ho_ten, luong_co_ban):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_co_ban = luong_co_ban
        self.luong_hang_thang = 0

class NhanVienVanPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_co_ban, so_ngay_lam_viec):
        super().__init__(ma_nv, ho_ten, luong_co_ban)
        self.so_ngay_lam_viec = so_ngay_lam_viec
        self.luong_hang_thang = luong_co_ban + so_ngay_lam_viec * 150000

class NhanVienBanHang(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_co_ban, so_san_pham_ban):
        super().__init__(ma_nv, ho_ten, luong_co_ban)
        self.so_san_pham_ban = so_san_pham_ban
        self.luong_hang_thang = luong_co_ban + so_san_pham_ban * 18000

class CongTy:
    def __init__(self):
        self.danh_sach_nhan_vien = []

    def them_nhan_vien(self, nhan_vien):
        self.danh_sach_nhan_vien.append(nhan_vien)

    def xuat_danh_sach_nhan_vien(self):
        for nhan_vien in self.danh_sach_nhan_vien:
            print("Mã nhân viên:", nhan_vien.ma_nv)
            print("Họ và tên:", nhan_vien.ho_ten)
            print("Lương cơ bản:", nhan_vien.luong_co_ban)
            print("Lương hằng tháng:", nhan_vien.luong_hang_thang)
            print()

    def tim_nhan_vien_theo_ma(self, ma_nv):
        for nhan_vien in self.danh_sach_nhan_vien:
            if nhan_vien.ma_nv == ma_nv:
                return nhan_vien
        return None

    def tim_nhan_vien_cao_nhat(self):
        max_luong = max(nv.luong_hang_thang for nv in self.danh_sach_nhan_vien)
        for nhan_vien in self.danh_sach_nhan_vien:
            if nhan_vien.luong_hang_thang == max_luong:
                return nhan_vien

    def tim_nhan_vien_ban_hang_thap_nhat(self):
        nhan_vien_ban_hang = [nv for nv in self.danh_sach_nhan_vien if isinstance(nv, NhanVienBanHang)]
        min_luong_ban_hang = min(nv.luong_hang_thang for nv in nhan_vien_ban_hang)
        for nhan_vien in nhan_vien_ban_hang:
            if nhan_vien.luong_hang_thang == min_luong_ban_hang:
                return nhan_vien


cong_ty = CongTy()


nv1 = NhanVienVanPhong("NV001", "Nguyen Van A", 3000000, 20)
nv2 = NhanVienBanHang("NV002", "Tran Thi B", 2000000, 50)
nv3 = NhanVienVanPhong("NV003", "Hoang Minh C", 2500000, 25)


cong_ty.them_nhan_vien(nv1)
cong_ty.them_nhan_vien(nv2)
cong_ty.them_nhan_vien(nv3)


cong_ty.xuat_danh_sach_nhan_vien()


print("Tìm nhân viên theo mã NV002:")
nv_tim_thay = cong_ty.tim_nhan_vien_theo_ma("NV002")
if nv_tim_thay:
    print("Họ và tên:", nv_tim_thay.ho_ten)
else:
    print("Không tìm thấy")