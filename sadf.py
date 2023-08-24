import os
import glob
import win32print
import win32ui
from PIL import Image


def delete_images(directory, image_extensions):
    for extension in image_extensions:
        pattern = os.path.join(directory, f'*.{extension}')
        image_files = glob.glob(pattern)
        
        for image_file in image_files:
            os.remove(image_file)
            print(f"Deleted: {image_file}")

if __name__ == "__main__":
    target_directory = "C:\\Users\\AI_Super_01\\Desktop\\New"
    valid_image_extensions = ["jpg", "jpeg", "png", "gif"]

    delete_images(target_directory, valid_image_extensions)

image_paths = [
    "image1.jpg",
    "image2.jpg",
    "image3.jpg",
    "image4.jpg"
]

# 이미지들을 세로로 배열할 때의 폭과 높이 설정
new_width = 800  # 새로 조합된 이미지의 폭
new_height = sum(Image.open(img_path).height for img_path in image_paths)  # 이미지들 높이의 합

# 새로운 이미지 생성
combined_image = Image.new("RGB", (new_width, new_height))

# 이미지를 세로로 배열하여 병합
y_offset = 0
for img_path in image_paths:#image_paths자리에 제대로 된 경로 지정하기
    img = Image.open(img_path)
    combined_image.paste(img, (0, y_offset))
    y_offset += img.height

# 새로 조합된 이미지 저장
combined_image.save("combined_image.jpg")


#저장된 이미지  c:\New 로 저장하기




# 프린터 설정
printer_name = win32print.GetDefaultPrinter()
hprinter = win32print.OpenPrinter(printer_name)
printer_info = win32print.GetPrinter(hprinter, 2)
printer_info['pDevMode'].PaperSize = win32print.DMPAPER_A4

# 인쇄할 사진 파일 경로
image_path = "combined_image.jpg"#<-C:\\~~~

# 이미지 열기
image = Image.open(image_path)

# 프린터 DC 생성
hdc = win32ui.CreateDC()
hdc.CreatePrinterDC(printer_name)

# 사진 출력
hdc.StartDoc(image_path)
hdc.StartPage()
hdc.BitBlt((100, 100), (400, 400), image, (0, 0), win32print.SRCCOPY)
hdc.EndPage()
hdc.EndDoc()

# 자원 해제
hdc.DeleteDC()