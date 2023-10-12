import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
import win32print
import win32ui
import win32con

# 이미지 생성 함수
def create_image():
    # 원하는 인치 단위 크기 설정
    width_inch = 4
    height_inch = 6
    dpi = 300  # DPI (인치 당 도트 수)

    # 이미지 비율 설정 (가로 2, 세로 3)
    image_width_inch = 1.8
    image_height_inch = 2.5

    # 픽셀로 크기 계산
    width_px = int(width_inch * dpi)
    height_px = int(height_inch * dpi)

    image_width_px = int(image_width_inch * dpi)
    image_height_px = int(image_height_inch * dpi)

    # 새 이미지를 생성합니다.
    new_image = Image.new('RGB', (width_px, height_px))

    # 이미지를 로드하고 크기 조정
    image1 = Image.open("222.jpg")
    image2 = Image.open("333.jpg")
    image3 = Image.open("444.jpg")
    image4 = Image.open("555.jpg")

    image1 = image1.resize((image_width_px, image_height_px), Image.ANTIALIAS)
    image2 = image2.resize((image_width_px, image_height_px), Image.ANTIALIAS)
    image3 = image3.resize((image_width_px, image_height_px), Image.ANTIALIAS)
    image4 = image4.resize((image_width_px, image_height_px), Image.ANTIALIAS)

    # 원하는 가로, 세로 개수 설정
    columns = 2
    rows = 2

    # 이미지를 삽입
    new_image.paste(image1, (int(dpi * 0.1), int(dpi * 0.1)))
    new_image.paste(image2, (image_width_px + int(dpi * 0.3), int(dpi * 0.1)))
    new_image.paste(image3, (int(dpi * 0.1), image_height_px + int(dpi * 0.3)))
    new_image.paste(image4, (image_width_px + int(dpi * 0.3), image_height_px + int(dpi * 0.3)))

    # 여백 및 텍스트 추가
    padding = int(dpi * 0.1)  # 0.1 인치 여백
    draw = ImageDraw.Draw(new_image)
    font_size = int(dpi * 0.3)  # 원하는 폰트 크기 설정
    font = ImageFont.load_default()  # 기본 폰트 사용
    font = ImageFont.truetype("arial.ttf", font_size)  # 폰트 크기 설정

    text = "Yeungnam 4cut"
    text_color = (255, 255, 255)  # 텍스트 색상 설정
    text_position = ((padding + image_width_px) * 0.5, height_px - padding - int(dpi * 0.5))  # 텍스트 위치 설정
    draw.text(text_position, text, fill=text_color, font=font)

    # 결과 이미지 저장
    new_image.save("output.jpg", dpi=(dpi, dpi))

# 이미지 인쇄 함수
def print_image():
    printer_name = "Your_Printer_Name"
    hprinter = win32print.OpenPrinter(printer_name)
    printer_info = win32print.GetPrinter(hprinter, 2)
    printer_info["pDatatype"] = "RAW"
    printer_info["pDefault"] = "RAW"
    printer_info["Attributes"] = win32print.PRINTER_ATTRIBUTE_NORMAL
    win32print.SetPrinter(hprinter, 2, printer_info, 0)

    image = Image.open("output.jpg")

    printer_dc = win32ui.CreateDC()
    printer_dc.CreatePrinterDC(printer_name)
    printer_dc.StartDoc('Document')
    printer_dc.StartPage()
    printer_dc.StretchBlt((0, 0, image.width, image.height), image, (0, 0, image.width, image.height), win32con.SRCCOPY)
    printer_dc.EndPage()
    printer_dc.EndDoc()
    printer_dc.DeleteDC()
    label.config(text="이미지 인쇄 완료")

# GUI 생성
root = tk.Tk()
root.title("이미지 생성 및 인쇄")

# 폰트 설정
custom_font = ("Helvetica", 30)

create_button = tk.Button(root, text="이미지 생성", command=create_image, font=custom_font, width=20, height=5)
print_button = tk.Button(root, text="이미지 인쇄", command=print_image, font=custom_font, width=20, height=5)
label = tk.Label(root, text="")

create_button.pack()
print_button.pack()
label.pack()

root.mainloop()
