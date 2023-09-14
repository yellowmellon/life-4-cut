import cv2
import os
from PIL import Image, ImageDraw, ImageFont

# 저장 경로 설정
output_dir = os.path.expanduser("~/Desktop")  # 바탕화면 경로

# 카메라 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
else:
    print("카메라를 열었습니다. 사진을 찍는 중...")

# 사진 8장 찍기
for i in range(1, 9):
    ret, frame = cap.read()
    if not ret:
        print("사진을 찍을 수 없습니다.")
        break

    # 이미지 저장
    output_path = os.path.join(output_dir, f"image{i}.jpg")
    cv2.imwrite(output_path, frame)
    print(f"{output_path}에 사진을 저장했습니다.")

    # 잠시 대기 (1초)
    cv2.waitKey(1000)

# 카메라 종료
cap.release()
cv2.destroyAllWindows()

print("사진 촬영이 완료되었습니다.")

# 이미지 파일 경로
image_files = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", 
               "image5.jpg", "image6.jpg", "image7.jpg", "image8.jpg"]

# 이미지 크기 (픽셀)
image_width, image_height = int(4 * 37.8), int(2.25 * 37.8)  # 가로 4cm, 세로 2.25cm를 픽셀로 변환

# 여백 크기 (픽셀)
margin_pixels = int(0.25 * 37.8)  # 0.5cm를 픽셀로 변환 (1cm = 37.8픽셀)

# 출력 이미지 크기 계산
output_width = 2 * image_width + 3 * margin_pixels
output_height = 5 * image_height + 3 * margin_pixels

# 출력 이미지 생성
output_image = Image.new('RGB', (output_width, output_height), (0, 0, 0))  # 검은 배경 생성

# 텍스트 추가
font_size = 20  # 폰트 크기 설정
font = ImageFont.truetype("C:\Users\AI_Super_01\anaconda3\pkgs\anaconda-navigator-2.4.2-py311haa95532_0\Lib\site-packages\anaconda_navigator\static\fonts\Ubuntu-B.ttf", font_size)  # 폰트 선택 (원하는 폰트 파일 경로를 지정하세요)

margin_text = "Margin Text"  # 추가할 텍스트 내용

# Create a Draw object to draw the text
draw = ImageDraw.Draw(output_image)

# Calculate the size of the text using the Draw object and font
text_width, text_height = draw.textsize(margin_text, font=font)

# Calculate the position for the text
text_x = (output_width - text_width) // 2
text_y = output_height - text_height - margin_pixels

# Draw the text
draw.text((text_x, text_y), margin_text, fill=(255, 255, 255), font=font)

# 이미지를 가로 2개, 세로 4개로 배열하면서 여백을 띄움
for i, image_file in enumerate(image_files):
    image = Image.open(image_file)
    image = image.resize((image_width, image_height))

    row = i // 2
    col = i % 2

    # 이미지 위치 계산 (여백을 고려하여 계산)
    x = int(col * (image_width + margin_pixels))
    y = int(row * (image_height + margin_pixels))
    
    output_image.paste(image, (x + margin_pixels, y + margin_pixels))  # 여백 추가

# 결과 이미지 저장
output_image.save("output_image_with_margin.jpg")
output_image.show()
