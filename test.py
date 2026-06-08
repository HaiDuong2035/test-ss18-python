student_list = [
    {
        'id': 'SV001',
        'name': 'Nguyen Van A',
        'math': 8.5,
        'physical': 7.0,
        'chemistry': 9.0,
        'average': 8.17,
        'rank': 'Giỏi'
    }
]

def find_student_by_id(input_id):
    for index, student in enumerate(student_list):
        if student['id'] == input_id:
            return index
    return -1

def validate_score(score):
    try:
        score = float(score)
        if 0 <= score <= 10:
            return True
        return False
    except:
        return False

def rank_classification(avg):
    if avg < 5:
        return 'Yếu'
    elif avg < 7:
        return 'Trung bình'
    elif avg < 8:
        return 'Khá'
    return 'Giỏi'

def display_student_list():
    print('--- DANH SÁCH SINH VIÊN ---')
    print('Mã SV | Họ và tên            | Điểm Toán | Điểm Lý | Điểm Hóa | Điểm TB | Xếp loại')
    print('-' * 100)
    for student in student_list:
        print(f'{student['id']:<5} | {student['name']:<20} | {student['math']:<9.1f} | {student['physical']:<7.1f} | {student['chemistry']:<8.1f} | {student['average']:<7.2f} | {student['rank']}')
    print('-' * 100)

def add_student():
    while True:
        new_id = input('Nhập mã sinh viên: ').strip().upper()
        if new_id == '':
            print('Mã sinh viên đang trống')
        elif find_student_by_id(new_id) != -1:
            print('Mã sinh viên đã tồn tại')
        else:
            break
    while True:
        new_name = input('Nhập họ và tên sinh viên: ').strip().title()
        if new_name == '':
            print('Tên sinh viên đang trống')
        else:
            break
    while True:
        new_math = input('Nhập điểm Toán: ').strip()
        if new_math == '':
            print('Điểm Toán đang trống')
        elif not validate_score(new_math):
            print('Điểm Toán phải là số thực từ 0 đến 10')
        else:
            new_math = float(new_math)
            break
    while True:
        new_physical = input('Nhập điểm Lý: ').strip()
        if new_physical == '':
            print('Điểm Lý đang trống')
        elif not validate_score(new_physical):
            print('Điểm Lý phải là số thực từ 0 đến 10')
        else:
            new_physical = float(new_physical)
            break
    while True:
        new_chemistry = input('Nhập điểm Hóa: ').strip()
        if new_chemistry == '':
            print('Điểm Hóa đang trống')
        elif not validate_score(new_chemistry):
            print('Điểm Hóa phải là số thực từ 0 đến 10')
        else:
            new_chemistry = float(new_chemistry)
            break
    new_avg = (new_math + new_physical + new_chemistry) / 3
    new_rank = rank_classification(new_avg)
    student_list.append({
        'id': new_id,
        'name': new_name,
        'math': new_math,
        'physical': new_physical,
        'chemistry': new_chemistry,
        'average': new_avg,
        'rank': new_rank
    })
    print(f'Đã thêm sinh viên {new_name}')

def update_student():
    while True:
        find_id = input('Nhập mã sinh viên: ').strip().upper()
        if find_id == '':
            print('Mã sinh viên đang trống')
        else:
            student_index = find_student_by_id(find_id)
            if student_index == -1:
                print('Mã sinh viên không tồn tại')
                return
            else:
                break
    while True:
        new_math = input('Nhập điểm Toán: ').strip()
        if new_math == '':
            print('Điểm Toán đang trống')
        elif not validate_score(new_math):
            print('Điểm Toán phải là số thực từ 0 đến 10')
        else:
            new_math = float(new_math)
            break
    while True:
        new_physical = input('Nhập điểm Lý: ').strip()
        if new_physical == '':
            print('Điểm Lý đang trống')
        elif not validate_score(new_physical):
            print('Điểm Lý phải là số thực từ 0 đến 10')
        else:
            new_physical = float(new_physical)
            break
    while True:
        new_chemistry = input('Nhập điểm Hóa: ').strip()
        if new_chemistry == '':
            print('Điểm Hóa đang trống')
        elif not validate_score(new_chemistry):
            print('Điểm Hóa phải là số thực từ 0 đến 10')
        else:
            new_chemistry = float(new_chemistry)
            break
    new_avg = (new_math + new_physical + new_chemistry) / 3
    student_list[student_index]['math'] = new_math
    student_list[student_index]['physical'] = new_physical
    student_list[student_index]['chemistry'] = new_chemistry
    student_list[student_index]['average'] = new_avg
    student_list[student_index]['rank'] = rank_classification(new_avg)
    print(f'Đã cập nhật sinh viên {student_list[student_index]['name']}')

def delete_student():
    while True:
        find_id = input('Nhập mã sinh viên: ').strip().upper()
        if find_id == '':
            print('Mã sinh viên đang trống')
        else:
            student_index = find_student_by_id(find_id)
            if student_index == -1:
                print('Mã sinh viên không tồn tại')
                return
            else:
                break
    while True:
        confirm = input('Bạn có chắc muốn xóa? (y/n): ').strip().lower()
        if confirm == 'y':
            break
        elif confirm == 'n':
            print(f'Hủy xóa sinh viên {student_list[student_index]['name']}')
            return
        else:
            print("Vui lòng nhập 'y' hoặc 'n'")
    print(f'Đã xóa sinh viên {student_list[student_index]['name']}')
    student_list.pop(student_index)

def find_student():
    check = False
    while True:
        keyword  = input('Nhập thông tin cần tìm kiếm (tên / mã SV): ').strip()
        if keyword == '':
            print('Thông tin đang trống')
        else:
            break
    print('--- KẾT QUẢ TÌM KIẾM ---')
    for student in student_list:
        if student['id'] == keyword.upper() or keyword.title() in student['name']:
            print(f'{student['id']} - {student['name']}')
            check = True
    if not check:
        print('Không có sinh viên với thông tin trùng khớp')

def rank_statistics():
    count_good = 0
    count_rather = 0
    count_medium = 0
    count_week = 0
    for student in student_list:
        rank = rank_classification(student['average'])
        if rank == 'Giỏi':
            count_good += 1
        elif rank == 'Khá':
            count_rather += 1
        elif rank == 'Trung bình':
            count_medium += 1
        else:
            count_week += 1
    print(f'''--- THỐNG KÊ XẾP HẠNG ---
Giỏi: {count_good} sinh viên
Khá: {count_rather} sinh viên
Trung bình: {count_medium} sinh viên
Yếu: {count_week} sinh viên''')

def main():
    while True:
        choice = input('''\n--- CHƯƠNG TRÌNH QUẢN LÝ DANH SÁCH SINH VIÊN ---
1. Hiển thị danh sách sinh viên
2. Tiếp nhận sinh viên
3. Cập nhật kết quả học tập
4. Xoá sinh viên 
5. Tìm kiếm sinh viên
6. Thống kê điểm TB
7. Thoát
> Nhập lựa chọn: ''').strip()
        print()
        match choice:
            case '1':
                if student_list:
                    display_student_list()
                else:
                    print('Danh sách chưa có sinh viên')
            case '2':
                add_student()
            case '3':
                if student_list:
                    update_student()
                else:
                    print('Danh sách chưa có sinh viên')
            case '4':
                if student_list:
                    delete_student()
                else:
                    print('Danh sách chưa có sinh viên')
            case '5':
                if student_list:
                    find_student()
                else:
                    print('Danh sách chưa có sinh viên')
            case '6':
                if student_list:
                    rank_statistics()
                else:
                    print('Danh sách chưa có sinh viên')
            case '7':
                print('Kết thúc chương trình')
                break
            case _:
                print('Lựa chọn không phù hợp')

main()