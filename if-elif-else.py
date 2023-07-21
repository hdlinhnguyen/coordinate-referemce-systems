Chương trình Python thực hiện tính thuế thu nhập cá nhân và chuyên đổi lương Gross sang lương Net như sau:

luong_gross=float(input("Nhập vào mức lương của bạn: "))
giamtru=int(input("Nhập vào số người phụ thuộc của bạn: "))
bhxh=luong_gross*0.105
tinhthue=luong_gross-bhxh-11-giamtru*4.4
print("Thu nhập tính thuế là: ", tinhthue)
if 0<tinhthue<=5:
    tncn=tinhthue*0.05
    print("Thuế TNCN bậc 1, mức đóng:", tncn)
    print("Lương Net là: ",luong_gross-bhxh-tncn)
elif 5<tinhthue<=10:
    tncn=5*0.05+(tinhthue-5)*0.1
    print("Thuế TNCN bậc 2, mức đóng:", tncn)
    print("Lương Net là: ",luong_gross-bhxh-tncn)
elif 10<tinhthue<=18:
    tncn=5*0.05+5*0.1+(tinhthue-10)*0.15
    print("Thuế TNCN bậc 3, mức đóng:", tncn)
    print("Lương Net là: ",luong_gross-bhxh-tncn)
elif 18<tinhthue<=32:
    tncn=5*0.05+5*0.1+8*0.15+(tinhthue-18)*0.2
    print("Thuế TNCN bậc 4, mức đóng:", tncn)
    print("Lương Net là: ",luong_gross-bhxh-tncn)
elif 32<tinhthue<=52:
    tncn=5*0.05+5*0.1+8*0.15+14*0.2+(tinhthue-32)*0.25
    print("Thuế TNCN bậc 5, mức đóng:", tncn)
    print("Lương Net là: ",luong_gross-bhxh-tncn)
elif 52<tinhthue<=80:
    tncn=5*0.05+5*0.1+8*0.15+14*0.2+20*0.25+(tinhthue-52)*0.3
    print("Thuế TNCN bậc 6, mức đóng:", tncn)
    print("Lương Net là: ",luong_gross-bhxh-tncn)
elif tinhthue>80:
    tncn=5*0.05+5*0.1+8*0.15+14*0.2+20*0.25+28*0.3+(tinhthue-80)*0.35
    print("Thuế TNCN bậc 7, mức đóng:", tncn)
    print("Lương Net là: ",luong_gross-bhxh-tncn)
else:
    print("Bạn không phải đóng thuế")
    print("Lương Net là: ", luong_gross-bhxh)
 Kết quả:

Nhập vào mức lương của bạn: 30
Nhập vào số người phụ thuộc của bạn: 1
Thu nhập tính thuế là:  11.450000000000001
Thuế TNCN bậc 3, mức đóng: 0.9675000000000001
Lương Net là:  25.8825
Ở chương trình trên, ta có rất nhiều điều kiện if...elif...else đó là do công thức tính thuế thu nhập cá nhân áp dụng có dạng lũy tiến. Trong mỗi điều kiện thì thuế TNCN lại được tính bằng tổng của mức tối đa ở bậc trước với số dư lũy tiến ở bậc sau.
