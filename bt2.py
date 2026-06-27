# Endpoint hiện tại trong source code là gì?
# endpoint hiện tại trong source code là /student

# Vì sao khi gọi GET /students lại bị lỗi 404 Not Found?
# vì hiện tại endpoint đang là /student nên khi ta /students sẽ không có dữ liệu và báo lỗi 404

# Vì sao tên endpoint /student chưa phù hợp với yêu cầu lấy danh sách sinh viên?
# Tại vì lấy danh sách sinh viên phải là số nhiều nên phải thêm s vào cuối: /students

# Vì sao dòng return students[0] chưa đúng với yêu cầu nghiệp vụ?
# Yêu cầu nghiệp vụ là cần phải trả về toàn bộ danh sách sinh viên nhưng dòng return students[0] lại chỉ trả về sinh viên có vị trí là 0 nên chỉ trả về đúng 1 sinh viên duy nhất

# API đúng theo yêu cầu khách hàng nên có đường dẫn là gì?
# nên có đường dẫn là /students

from fastapi import FastAPI

app = FastAPI()

students = [
{"id": 1, "name": "An"},
{"id": 2, "name": "Binh"},
{"id": 3, "name": "Cuong"},
]

@app.get("/students")
def get_student():
    return students