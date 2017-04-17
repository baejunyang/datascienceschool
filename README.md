## 1. predict_sodam
목표: 교내 커뮤니티 사이트에 올라오는 새로운 게시글의 적절성 여부를 판단하는 알고리즘 개발
- 커뮤니티 유저들은 자신이 부적절하다고 판단한 게시글에 '냉동'을 클릭할 수 있고, '냉동'이 5개가 누적되면 게시글이 삭제된다.
- 기본 가정 : '냉동'을 받은 글은 부적절한 내용(욕설, 비속어, 비방 등)을 포함하는 글일 것이다
- '냉동'을 1개라도 받은 'frozen' 게시글 3000개, 냉동을 받지 않은 'unfrozen' 게시글 3000개를 학습 데이터로 사용.
- Logistic regression, multinomial naive beyes, support vector classification 등의 여러 모형을 사용해서 학습시킨다

## 2. wine_recommendation
목표 : 사용자가 선호하는 와인 1개를 입력 받아서 그와 가장 유사한 5개의 와인을 추천해준다.
- 와인 관련 웹페이지에서 와인에 관련된 정보(당도, 바디감, 향, 포도품종 등)를 크롤링
- 데이터를 분석 가능한 형태로 인코딩
- 유클리드 거리와 코사인 유사도를 바탕으로 입력받은 와인과 가장 유사한 와인을 탐색 및 추천
