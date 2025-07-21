## 1. 개요
- 개인화된 영어 단어 학습 앱으로, “나만의 단어장”에서 사용자만의 맞춤형 단어장을 생성할 수 있습니다.
- 해마 학습법을 AI 기술과 접목해, 단기간에 더 많은 영어 단어를 외울 수 있는 시스템을 구축하고자 기획하게 되었습니다.

<br>

## 2. 주요 기능
### **⭐ 연상 예문 생성 (LLM)**

- “나만의 단어장”에서 생성하고 싶은 **영단어 입력** → 단어의 발음과 **연관된 연상 예문을 생성**
- 사용자가 선택한 관심사 정보(스포츠, 음식 등)를 DB에 저장 → **예문 생성 시 관심사를 반영**
- ex) 출처 : 경선식 영단어장 (수능)
    
    
    | **영어** | **뜻** | **연상 예문** |
    | --- | --- | --- |
    | hindrance | 방해, 방해물 | 힌드런스 → [힘들었스] : 여기까지 오는 데 {장애물}이 많아서 [힘들었어]. |

### **⭐ 이미지 생성 (DALL E)**

- “나만의 단어장”에서 연상 문장을 생성한 후, **생성된 문장을 프롬프팅**해서 이미지를 생성
- 시각적 이미지를 제공해 연상을 통한 단어 암기 효과를 증대

### **⭐ 발음 교정 (STT)**

- 단어 학습 중 “발음 교정”을 통해 음성 인식 기술(STT)을 통한 **발음 평가 기능 제공**
- **버튼을 통해 발음을 입력** → **STT가 해당 발음 평가를 진행**
- 정확도, 유창성, 완성도, 총점에 대한 **평균 점수와 운소별 세세한 점수를 제공** (100점 만점)
- 점수가 **80점 미만**일 경우, 별도의 **발음 교정 팁 제공**
  
<br>

## 3. 기술 스택
<img width="458" height="274" alt="image" src="https://github.com/user-attachments/assets/b30485a3-9fac-43ef-9d30-d1bd0b4b94df" />

<br><br>

## 4. 시스템 구조
### **시스템 아키텍처**
<img width="1946" height="926" alt="시스템 아키텍쳐" src="https://github.com/user-attachments/assets/a1b90bd1-90b2-4153-9d6b-c676f2db9fb2" />

### ERD
<img width="2010" height="949" alt="erd" src="https://github.com/user-attachments/assets/c0280fbe-73f0-4134-ac11-b301cc9cf63b" />

<br><br>

## 5. 개발 결과

### **⭐ 회원 가입 및 로그인 → 메인 화면**
회원 가입 과정에서 사용자의 관심사를 DB에 저장해, 연상 문장 생성 시 활용합니다.

메인 화면에서는 ⒈ 기본 제공 단어장 ⒉ 나만의 단어장 ⒊ 즐겨찾기 단어장에 접근할 수 있습니다.

<img width="328" height="327" alt="로그인 회원가입" src="https://github.com/user-attachments/assets/8c3289ee-fcf5-4464-b3f8-7985cb41efe6" />
<img width="160" height="329" alt="메인 화면" src="https://github.com/user-attachments/assets/58740226-5761-40a5-a4da-adf9fcf37700" />

### **⭐ 기본 제공 단어장 → 단어 학습** 
“기본 제공 단어장”은 앱에서 기본으로 단어장으로 DB에 저장된 단어들을 불러옵니다.

“학습 시작”을 통해 단어 암기를 시작할 수 있습니다.

<img width="340" height="327" alt="기본 제공 단어장 목록" src="https://github.com/user-attachments/assets/b18151a8-bc04-4ee9-af55-ecb229d81211" />
<img width="539" height="327" alt="단어 학습 과정" src="https://github.com/user-attachments/assets/513090d7-a957-4835-8fa9-9eb40e2b2181" />

### **⭐ 단어 학습 → 발음 교정** 
단어 학습 중 발음 평가를 진행할 수 있습니다. 

정확도, 유창성, 완성도, 총점에 대한 **평균 점수와 운소별 세세한 점수를 제공**합니다.

100점 만점 중 80점 미만일 경우, 별도의 발음 교정 팁을 제공합니다.

<img width="664" height="332" alt="발음 교정 과정" src="https://github.com/user-attachments/assets/f527ecb7-955e-4ee9-b831-2e971f509c46" />

### **⭐ 즐겨찾기 단어장**

단어 학습 중, 원하는 단어에 “별”을 누르면 “즐겨찾기 단어장”에서 확인할 수 있습니다.

<img width="339" height="324" alt="즐겨찾기 단어장" src="https://github.com/user-attachments/assets/68d320d2-1582-4150-83c6-60fd57a87cb9" />

### **⭐ 나만의 단어장**

⒈ **단어 직접 생성**

원하는 단어를 입력해 단어장을 생성할 수 있습니다. 카드를 넘겨 새 단어를 추가합니다.

⒉ **단어 랜덤 생성**

기본 제공 단어장에 있는 단어를 랜덤으로 10개 생성해, 사용자가 단어 확인 후 선택할 수 있습니다.

<img width="513" height="332" alt="나만의 단어장 생성" src="https://github.com/user-attachments/assets/ffc689f4-efbe-43d2-8fc7-2b5043531026" />

<br><br>

## 6. 개발 진행 일정
<img width="932" height="869" alt="image" src="https://github.com/user-attachments/assets/44e5be9f-97d4-4c2f-81cf-bd5dad5b3c24" />

