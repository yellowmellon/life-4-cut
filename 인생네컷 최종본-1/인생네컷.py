import webbrowser
import os
import glob
import shutil

def delete_images(directory, image_extensions):
    for extension in image_extensions:
        pattern = os.path.join(directory, f'*.{extension}')
        image_files = glob.glob(pattern)
        
        for image_file in image_files:
            os.remove(image_file)
            print(f"Deleted: {image_file}")

if __name__ == "__main__":
    target_directory = "c:\\Users\\kms01\\OneDrive\\바탕 화면\\New"
    valid_image_extensions = ["jpg", "jpeg", "png", "gif"]

    delete_images(target_directory, valid_image_extensions)
    
    
    
    
    
filename = "photo1.jpg"
src = "c:\\Users\\kms01\\Downloads"
dst = "c:\\Users\\kms01\\OneDrive\\바탕 화면\\New"

shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
filename = "photo2.jpg"
src = "c:\\Users\\kms01\\Downloads"
dst = "c:\\Users\\kms01\\OneDrive\\바탕 화면\\New"

shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
filename = "photo3.jpg"
src = "c:\\Users\\kms01\\Downloads"
dst = "c:\\Users\\kms01\\OneDrive\\바탕 화면\\New"

shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
filename = "photo4.jpg"
src = "c:\\Users\\kms01\\Downloads"
dst = "c:\\Users\\kms01\\OneDrive\\바탕 화면\\New"

shutil.move(os.path.join(src, filename), os.path.join(dst, filename))





folder_path = "c:\\Users\\kms01\\OneDrive\\바탕 화면\\New"
pattern = "image"  # 새로운 파일 이름 패턴
count = 1

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):  # .jpg 파일만 대상으로
        new_filename = f"{pattern}{count}.jpg"
        file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(file_path, new_file_path)
        count += 1



message = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>

        /* body태그 자체에 css 요소 부여 */
        body {
            font-family: "LeeSeoyun";
            margin: 0;
            display: flex;
            justify-content: center;
            background-image: url("./background.png");
        }

        .container {
            width: 390px;
            background-color: #ff9d73;
            height: 100%;
        }

        .photos {
            margin-top: 30px;
        }

        .photo-frame {
            background-color: white;
            margin: 15px 20px;
            height: 200px;

            background-size: cover;
            position: relative;

            cursor: pointer;
        }

        .footer {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .f-title {
            color: white;
            font-size: 25px;
            font-weight: 900;
        }

        .f-date {
            color: white;
            font-size: 15px;
            font-weight: 500;
        }

        #image1 {
            background-image: url("./New/image1.jpg");
        }

        #image2 {
            background-image: url("./New/image2.jpg");
        }

        #image3 {
            background-image: url("./New/image3.jpg");
        }

        #image4 {
            background-image: url("./New/image4.jpg");
        }

        .photo_description {
            color: white;
            background-color: black;

            width: fit-content;
            padding: 0 20px;
            margin-bottom: 10px;

            border-radius: 10px;
            position: absolute;
            bottom: 0;

            transform: translate(-50%);
            left: 50%;

            opacity: 0;
        }

        .video {
            width: 100%;
            height: 100%;
        }

        .showText {
            opacity: 0;
        }

        .hideText {
            opacity: 1;
            transition: opacity 0.5s linear;
        }
    </style>
    <script>
        // 텍스트가 보여지는 기능
        // 1. 몇 번째 사진에 마우스가 올라갔는지 확인(if문)
        // 2. 해당 사진을 찾아 hideText class를 지워주고, showText는 삽입해줌
        function showText(number) {
        if (number === 1) {
            document.querySelector("#desc1").classList.remove("hideText");
            document.querySelector("#desc1").classList.add("showText");
        } else if (number === 2) {
            document.querySelector("#desc2").classList.remove("hideText");
            document.querySelector("#desc2").classList.add("showText");
        } else {
            document.querySelector("#desc3").classList.remove("hideText");
            document.querySelector("#desc3").classList.add("showText");
        }
        }

        // 텍스트가 감춰지는 기능
        // 1. 몇 번째 사진에서 마우스가 벗어났는지 확인(if문)
        // 2. 해당 사진을 찾아 shotText class를 지워주고, hideText는 삽입해줌
        function hideText(number) {
        if (number === 1) {
            document.querySelector("#desc1").classList.remove("showText");
            document.querySelector("#desc1").classList.add("hideText");
        } else if (number === 2) {
            document.querySelector("#desc2").classList.remove("showText");
            document.querySelector("#desc2").classList.add("hideText");
        } else {
            document.querySelector("#desc3").classList.remove("showText");
            document.querySelector("#desc3").classList.add("hideText");
        }
        }

        // 클릭 기능
        // 1. 선택된 사진의 숫자를 가진 텍스트를 alert 형태로 출력해줌
        function alertText(number) {
            alert(`${number}번째 추억이에요! `);
        }
    </script>
</head>
<body>
    <div class="container">
        <div class="photos">
            <div id="image1" class="photo-frame"
                onmouseover="hideText(1)"
                onmouseout="showText(1)"
                onclick="alertText(1)"
            >
            </div>
            <div id="image2" class="photo-frame"
                onmouseover="hideText(2)"
                onmouseout="showText(2)"
                onclick="alertText(2)"
            >
            </div>
            <div id="image3" class="photo-frame"
                onmouseover="hideText(3)"
                onmouseout="showText(3)"
                onclick="alertText(3)"
            >
            </div>
            <div id="image4" class="photo-frame"
                onmouseover="hideText(4)"
                onmouseout="showText(4)"
                onclick="alertText(4)"
            > 
            </div>
        </div>
        <div class="footer">
            <p class="f-title">타이틀</p>
            <p class="f-date">날짜적기</p>
        </div>
    </div>
</body>
</html>"""
 
filepath = "hello.html"
with open(filepath, 'w') as f:
    f.write(message)
    f.close()
 
webbrowser.open_new_tab(filepath)