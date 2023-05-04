# Trimming_Img
이미지에 불필요한 공백을 제거할 수 있도록 파이썬으로 제작한 프로그램이다. 
이미지 속 물체의 윤곽선을 인식한 후, 정사각형으로 이미지를 재단한다. 
이미지를 정사각형으로 재단할 수 없는 경우, 기존의 이미지를 반환한다.

<figure class="half">
  <img src="https://user-images.githubusercontent.com/60128466/236175809-19db1f4f-d886-4d97-824d-4ceb0f05e964.png">
  <img src="https://user-images.githubusercontent.com/60128466/236177304-8272ccec-b424-4900-8047-a4496c550d24.png">
figure>

<재단이 불가한 경우>
1. 정사각형으로 자르게 되면 원본 이미지의 사이즈를 초과하는 경우
2. 이미지에 노이즈가 지나치게 많아 물체의 윤곽선이 뚜렷하지 않은 경우
3. 검출된 물체의 크기가 150pix미만인 경우


## 개발일자
2022.11.03
