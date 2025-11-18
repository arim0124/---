from utils import create_button,root

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

create_button(50, 50, screen_width//2 - 25, 150, "창문 열기", lambda :print(1))
create_button(screen_width//2 + 25, 50, screen_width - 50, 150, "창문 닫기", lambda: print("상단 우"))

x1_right = screen_width*2//3
y1_right = 200
x2_right = screen_width - 50
y2_right = screen_height - 50
create_button(x1_right, y1_right, x2_right, y2_right, "에어컨 끄기", lambda: print("우측 길게"))

left_w = screen_width*2//3 - 60
left_h = y2_right - y1_right
btn_w = (left_w - 30)//2
btn_h = (left_h - 30)//2
l = [['냉방','난방'],['제습','송풍']]
for i in range(2):
    for j in range(2):
        x1 = 50 + j*(btn_w + 10)
        y1 = y1_right + i*(btn_h + 10)
        x2 = x1 + btn_w
        y2 = y1 + btn_h
        create_button(x1, y1, x2, y2, l[i][j], lambda i=i,j=j: print(f"좌측 {i*2+j+1}"))

root.mainloop()