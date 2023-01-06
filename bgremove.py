from pathlib import Path
import os
from PIL import Image
# import backgroundremover

# png 파일을 jpg파일로 변환
for f in Path("C:/projects/backgroundremover111/rsPoop/").glob("*.png"):
    inputpath = str(f)
    outputpath = str(f.parent / (f.stem + "-as.jpg")) #같은 위치에, (원래파일명)-as.png
    img = Image.open(inputpath).convert('RGB')
    img.save(outputpath)

#jpg 파일들만 전부 배경 제거
for file in Path("C:/projects/backgroundremover111/rsPoop/POOP/").glob("*.jpg"):
    input_path = str(file)  #C:/projects/backgroundremover111/rsPoop/pop1/(file번째 이미지).png
    os.system('backgroundremover -i "'+ input_path +'" -m "u2netp" '
                                 '-o "C:/projects/backgroundremover111/rsPoop/pngRspop/'+ file.stem +'-output.jpg"')  #(원래파일명)-output.png

###########################
#가상환경 cmd에서 설치하고 나서 스크립트 실행
#pip3 install torch torchvision torchaudio
#pip install ffmpeg
#pip install --upgrade pip
#pip install backgroundremover
###########################
