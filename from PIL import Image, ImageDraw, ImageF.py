import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
import win32print
import win32ui
import win32con
import os
import glob

#사진 찍은거 저장할때 처음부터 New파일에 저장함 ㅇㅋㅇㅋ

# 이미지 생성 함수
def create_image():
    #여기서는 이전에 만들어졌던 output.jpg를 삭제함(output폴더)
    def delete_images(directory, image_extensions):
        if not os.path.exists(directory):
            print(f"The directory '{directory}' does not exist. Skipping image deletion.")
            return

        for extension in image_extensions:
            pattern = os.path.join(directory, f'*.{extension}')
            image_files = glob.glob(pattern)

            if not image_files:
                print(f"No {extension} files found in '{directory}'. Skipping image deletion.")
                continue

            for image_file in image_files:
                os.remove(image_file)
                print(f"Deleted: {image_file}")

    if __name__ == "__main__":
        target_directory = "C:\\Users\\kms01\\OneDrive\\바탕 화면\\output"
        valid_image_extensions = ["jpg", "jpeg", "png", "gif"]

        delete_images(target_directory, valid_image_extensions)
    
    #여기서는 폴더 내의 사진 이름 바꾸기
    folder_path = "C:\\Users\\kms01\\OneDrive\\바탕 화면\\New"
    pattern = "image"  # 새로운 파일 이름 패턴
    count = 1

    # 폴더 내에 .jpg 파일이 있는지 확인
    if any(filename.endswith(".jpg") for filename in os.listdir(folder_path)):
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg"):
                new_filename = f"{pattern}{count}.jpg"
                file_path = os.path.join(folder_path, filename)
                new_file_path = os.path.join(folder_path, new_filename)
                os.rename(file_path, new_file_path)
                count += 1
    else:
        print("이미지 파일이 폴더 내에 없습니다. 넘어갑니다.")
        
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
    image1 = Image.open("C:\\Users\\kms01\\OneDrive\\바탕 화면\\New\\image1.jpg")
    image2 = Image.open("C:\\Users\\kms01\\OneDrive\\바탕 화면\\New\\image2.jpg")
    image3 = Image.open("C:\\Users\\kms01\\OneDrive\\바탕 화면\\New\\image3.jpg")
    image4 = Image.open("C:\\Users\\kms01\\OneDrive\\바탕 화면\\New\\image4.jpg")

    image1 = image1.resize((image_width_px, image_height_px), Image.ANTIALIAS)
    image2 = image2.resize((image_width_px, image_height_px), Image.ANTIALIAS)
    image3 = image3.resize((image_width_px, image_height_px), Image.ANTIALIAS)
    image4 = image4.resize((image_width_px, image_height_px), Image.ANTIALIAS)

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

    # 결과 이미지 저장(output폴더에 저장)
    output_folder = "C:\\Users\\kms01\\OneDrive\\바탕 화면\\output"
    output_filename = "output.jpg"
    output_path = os.path.join(output_folder, output_filename)
    new_image.save(output_path, dpi=(dpi, dpi))
    
    #처음 4장을 지움(New폴더)
    def delete_images(directory, image_extensions):
        if not os.path.exists(directory):
            print(f"The directory '{directory}' does not exist. Skipping image deletion.")
            return

        for extension in image_extensions:
            pattern = os.path.join(directory, f'*.{extension}')
            image_files = glob.glob(pattern)

            if not image_files:
                print(f"No {extension} files found in '{directory}'. Skipping image deletion.")
                continue

            for image_file in image_files:
                os.remove(image_file)
                print(f"Deleted: {image_file}")

    if __name__ == "__main__":
        target_directory = "C:\\Users\\kms01\\OneDrive\\바탕 화면\\New"
        valid_image_extensions = ["jpg", "jpeg", "png", "gif"]

        delete_images(target_directory, valid_image_extensions)
    
    #이제 찬우가 위에서 저장한 (output 파일에 있는)output.jpg를 googl drive로 옮기고 
    
    #찬우의 코드
    #찬우의 코드
    #찬우의 코드

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
