import subprocess
from bs4 import BeautifulSoup
from weasyprint import HTML

# 로컬 HTML 파일 경로 설정
html_file_path = '/path/to/your/local/file.html'  # 로컬 파일 경로로 변경

# 저장할 A4 PDF 파일 경로 설정
output_pdf_path = '/path/to/your/output.pdf'  # 저장할 PDF 파일 경로로 변경

# HTML 파일을 파싱하여 BeautifulSoup 객체 생성
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()
    soup = BeautifulSoup(html_content, 'html.parser')

# 클래스가 "container"인 요소와 그 하위 요소 추출
container_elements = soup.find_all(class_='container')

# A4 크기 페이지에 인쇄
pdf_pages = []
for container in container_elements:
    container_html = str(container)
    pdf_pages.append(HTML(string=container_html).render())

# A4 PDF 파일로 저장
pdf_pages[0].write_pdf(output_pdf_path)

print('A4 PDF 파일 생성 완료!')

# 인쇄할 A4 PDF 파일 경로 설정
pdf_file_path = '/path/to/your/output.pdf'  # 인쇄할 PDF 파일 경로로 변경

# Windows에서 Adobe Acrobat Reader를 사용하여 인쇄하는 예제
printer_name = 'Your_Printer_Name'  # 프린터 이름으로 변경
acrobat_path = r'C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe'  # Adobe Acrobat Reader 경로로 변경

# 인쇄 명령어 실행
print_command = [acrobat_path, '/t', pdf_file_path, printer_name]
subprocess.run(print_command)

print(f'{pdf_file_path} 파일을 인쇄합니다.')
