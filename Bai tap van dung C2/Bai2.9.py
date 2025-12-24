import sys
import json
from json import JSONDecodeError


def tinh_tong_nhan_vien(data):
    # Safely sum employee counts, ignoring malformed entries
    don_vi_list = data.get('don_vi', []) if isinstance(data, dict) else []
    total = 0
    for dv in don_vi_list:
        try:
            total += int(dv.get('so_nhan_vien', 0))
        except Exception:
            # ignore entries with non-integer values
            continue
    return total


def in_thong_tin_cong_ty(data):
    print(f'Tên công ty: {data.get("ten_cong_ty", "<không xác định>")}')
    print(f'Địa chỉ: {data.get("dia_chi", "<không xác định>")}')


def in_thong_ke_don_vi(i, don_vi, tong_nhan_vien):
    ten_don_vi = don_vi.get('ten_don_vi', '<không có tên>')
    try:
        so_nhan_vien_don_vi = int(don_vi.get('so_nhan_vien', 0))
    except Exception:
        so_nhan_vien_don_vi = 0

    if tong_nhan_vien:
        ty_le = (so_nhan_vien_don_vi / tong_nhan_vien) * 100
    else:
        ty_le = 0.0

    print(f'{i}./ Tên đơn vị: {ten_don_vi}.')
    print(f'   - Số nhân viên: {so_nhan_vien_don_vi}')
    print(f'   - Tỷ lệ: {ty_le:.2f}%.\n')


def thong_ke_nhan_vien(data):
    # Tính tổng số nhân viên
    tong_nhan_vien = tinh_tong_nhan_vien(data)

    # In thông tin công ty
    in_thong_tin_cong_ty(data)
    print(f'Tổng số nhân viên: {tong_nhan_vien}')

    # In thống kê nhân viên theo đơn vị
    print('\n-----Thống kê nhân viên theo đơn vị ------')
    for i, don_vi in enumerate(data.get('don_vi', []), 1):
        in_thong_ke_don_vi(i, don_vi, tong_nhan_vien)


def _usage():
    print('Usage: python Bai2.9.py [du_lieu.json]')


def main(argv=None):
    argv = argv or sys.argv
    filename = argv[1] if len(argv) > 1 else 'du_lieu.json'
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            du_lieu = json.load(file)
    except FileNotFoundError:
        print(f'File không tìm thấy: {filename}', file=sys.stderr)
        _usage()
        return 1
    except JSONDecodeError as e:
        print(f'Lỗi phân tích JSON ({filename}): {e}', file=sys.stderr)
        return 2

    if not isinstance(du_lieu, dict):
        print('Dữ liệu không đúng định dạng (cần là object JSON).', file=sys.stderr)
        return 3

    thong_ke_nhan_vien(du_lieu)
    return 0


if __name__ == '__main__':
    sys.exit(main())
