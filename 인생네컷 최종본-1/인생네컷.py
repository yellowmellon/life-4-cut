import webbrowser
import os
import glob
import shutil

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
    target_directory = "c:\\Users\\AI_Super_01\\Desktop\\New"
    valid_image_extensions = ["jpg", "jpeg", "png", "gif"]

    delete_images(target_directory, valid_image_extensions)

file_path = "hello.html"   
if os.path.exists(file_path):
    os.remove(file_path)
    print(f'{file_path} 파일이 삭제되었습니다.')
else:
    print(f'{file_path} 파일이 존재하지 않습니다. 삭제 작업을 스킵합니다.')
    

def move_image(src_directory, dst_directory, filename):
    src_path = os.path.join(src_directory, filename)
    dst_path = os.path.join(dst_directory, filename)

    if os.path.exists(src_path):
        shutil.move(src_path, dst_path)
        print(f"Moved: {src_path} to {dst_path}")
    else:
        print(f"File not found: {src_path}. Skipping move operation.")

if __name__ == "__main__":
    src_directory = "c:\\Users\\AI_Super_01\\Downloads"
    dst_directory = "c:\\Users\\AI_Super_01\\Desktop\\New"

    filenames = ["photo1.jpg", "photo2.jpg", "photo3.jpg", "photo4.jpg"]

    for filename in filenames:
        move_image(src_directory, dst_directory, filename)




folder_path = "c:\\Users\\AI_Super_01\\Desktop\\New"
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
            margin: 0;
            display: flex;
            justify-content: center;
            background-image: url("./background.png");
        }

        .container {
            width: 390px;
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
        color: black;
        font-size: 48px;
        font-weight: 900;
        font-family: "sans-serif";
        background-color: rgba(255, 255, 255, 0.7); /* 흰 반투명 마진 추가 */
        padding: 5px; /* 원하는 크기로 조정하세요 */
        border-radius: 10px; /* 모서리 둥글게 만들기 */
        margin: 10px 0; /* 위아래 마진 추가 */
        }

        .f-date {
            color: rgb(123, 116, 128);
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

        .showText {
            opacity: 0;
        }

        .hideText {
            opacity: 1;
            transition: opacity 0.5s linear;
        }

        /* 이미지 변경을 위한 클래스 추가 */
        .selected-image {
            border: 2px solid red;
        }

    </style>
    <script>
        // 이미지 변경을 위한 함수
        function changeImage(number) {
            const container = document.querySelector(".container");
            const imagePaths = [
                "./New/image1.jpg",
                "./New/image2.jpg",
                "./New/image3.jpg",
                "./New/image4.jpg"
            ];

            // 무작위 이미지 선택 (16개 이미지 중 하나)
            const randomImagePath = [
            "./Pic/1.png",
            "./Pic/2.png",
            "./Pic/3.png",
            "./Pic/4.png",
            "./Pic/5.png",
            "./Pic/6.png",
            "./Pic/7.png",
            "./Pic/8.png",
            "./Pic/9.png",
            "./Pic/10.png",
            "./Pic/11.png",
            "./Pic/12.png"
            ][Math.floor(Math.random() * 12)];

            // 선택한 이미지를 배경으로 설정
            container.style.backgroundImage = `url('${randomImagePath}')`;

            // 선택한 이미지에 선택 효과 추가
            document.querySelectorAll(".photo-frame").forEach((frame, index) => {
                if (index + 1 === number) {
                    frame.classList.add("selected-image");
                } else {
                    frame.classList.remove("selected-image");
                }
            });
        }

        // 클릭 이벤트 처리 함수 (이미지 변경 및 경고창)
        function handleClick(number) {
            alertText(number);
            changeImage(number);
        }

        // 텍스트가 보여지는 기능, 감춰지는 기능 함수는 유지
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
            alert(`${number}번째 랜덤 사진!!`);
        }
        // 클릭 이벤트 처리 함수 (이미지 변경 및 경고창)
        function handleClick(number) {
            alertText(number);
            changeImage(number);
            // 0.3초 후에 선택 효과를 제거하는 함수 호출
            setTimeout(() => {
                removeSelectedImage();
            }, 300);
        }

        // 선택 효과를 제거하는 함수
        function removeSelectedImage() {
            document.querySelectorAll(".photo-frame").forEach((frame) => {
                frame.classList.remove("selected-image");
            });
        }
    </script>
</head>
<body>
    <div class="container">
        <div class="photos">
            <div id="image1" class="photo-frame"
                onmouseover="hideText(1)"
                onmouseout="showText(1)"
                onclick="handleClick(1)"
            >
            </div>
            <div id="image2" class="photo-frame"
                onmouseover="hideText(2)"
                onmouseout="showText(2)"
                onclick="handleClick(2)"
            >
            </div>
            <div id="image3" class="photo-frame"
                onmouseover="hideText(3)"
                onmouseout="showText(3)"
                onclick="handleClick(3)"
            >
            </div>
            <div id="image4" class="photo-frame"
                onmouseover="hideText(4)"
                onmouseout="showText(4)"
                onclick="handleClick(4)"
            > 
            </div>
        </div>
        <div class="footer">
            <p class="f-title">타이틀</p>
            <p class="f-date">날짜적기</p>
        </div>
    </div>
</body>
</html>
"""
 
filepath = "hello.html"
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(message)
    f.close()
 
webbrowser.open_new_tab(filepath)
