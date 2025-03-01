from PIL import Image

def add_white_space(image_path, output_path, padding=300):
    # 이미지 열기
    img = Image.open(image_path)
    
    # 원본 이미지 크기
    width, height = img.size
    
    # 새 이미지 크기 설정 (양옆에 padding 추가)
    new_width = width + 2 * padding
    new_height = height
    
    # 흰색 배경의 새 이미지 생성
    new_img = Image.new("RGB", (new_width, new_height), (255, 255, 255))
    
    # 원본 이미지를 중앙에 배치
    new_img.paste(img, (padding, 0))
    
    # 결과 저장
    new_img.save(output_path, "JPEG")
    print(f"이미지가 저장되었습니다: {output_path}")

# 사용 예시
add_white_space("input.jpg", "output.jpg")
