# 2DGameProgramming-Term-Project - ZomBoogie
- 2024.10.04 ~ 2024.12.~
- 언어: Python
- 엔진/라이브러리: Pygame
- IDE: VsCode
- 운영체제: Windows
- 버전 관리: Git / Source Tree

# ZomBoogie
![Title](https://github.com/user-attachments/assets/fce170cd-ead1-45c2-a79a-91e9081a3bc0)
## 컨셉 소개
- 장르: 탑다운 슈팅 로그라이트
- 목표: 끝없이 몰려오는 좀비를 피하고, 쓰러뜨리며 최대한 오래 살아남는다.
- 성장 요소: 좀비를 처치해 자원을 얻고, 캐릭터를 점점 더 강하게 업그레이드한다.
- 조작: 빠르고 간단한 조작으로 누구나 쉽게 즐길 수 있는 캐주얼한 게임플레이.
- 참고 게임: Vampire Survivors


## 핵심 메카닉
### 1) 캐릭터 컨트롤
- wasd: 8방향 이동 지원
- Spacebar: 짧은 대시 가능, 쿨다운 시스템 도입
- 좌클릭: 마우스 위치로 사격
### 2) 좀비
- 탱커 타입을 제외한 좀비들은 1번의 총알을 맞으면 죽는다.
- 기본 타입: 플레이어에 다가가며 공격을 한다.
- 원거리 타입: 기본적으로 플레이어와 거리를 유지하며, 원거리 공격을 한다.
- 탱커 타입: 총알을 세 번 맞으면 죽는다. 대시 기술이 있다.
### 3) 좀비 AI
- 설정된 속도로 플레이어의 좌표에 다가간다.
- 플레이어가 범위 내에 있으면 공격한다.
### 4) 드랍 시스템
- 경험치: 좀비를 처치하면 경험치 구슬 드랍.
- 백신: 좀비를 처치하면 낮은 확률로 백신 드랍.
    - 감염 디버프가 존재할 때 백신을 획득하면 디버프가 초기화 된다.
### 5) 난이도
- 게임 레벨 증가: 플레이 타임 '60초'를 기반으로 게임 레벨 증가한다.
- 좀비 생성 빈도 증가: 게임 레벨에 비례해 좀비 생성 빈도가 빨라진다.
### 6) 게임 기능
- 감염 디버프:
    - 플레이어는 피격 시 감염 디버프 추가.
    - 감염 디버프 중첩이 3이 되면 게임 오버.
- 백신: 백신을 통해 감염 디버프 초기화
### 7) 레벨업 시스템
- 능력치 선택: 레벨업 시 랜덤한 3개의 능력치 중 1개를 선택하여 강화.
1. 면역력 증가 (현재 적용중인 감염 디버프를 초기화 시킨다)
2. 이동 속도 증가
3. 사격 속도 증가
4. 탄환 관통 횟수 증가
5. 탄환 개수 증가 (가로)
6. 탄환 개수 증가 (세로)
7. 사거리 증가
8. 감염 디버프 최대 횟수 증가

# 게임 흐름
1. 사방에서 몰려오는 좀비를 물리치거나 피해야 한다.
2. 플레이어는 직접 사격하여 좀비를 물리친다.
3. 플레이어는 좀비와 충돌시 감염 디버프가 증가한다.
4. 감염 디버프가 3이 되면 게임 오버
- 사진 설명 추가 (간단한 맵 및 UI)
- 게임 흐름도 추가

# 개발 내용
## 씬 구성
1. 로딩 씬
2. 메인메뉴 씬
3. 메인게임 씬
4. 레벨업 씬
5. 설정 씬
6. 게임종료 씬
   
### 1. 로딩 씬
- 전환 규칙: 게임을 시작하면 전환
- Object:
  1. 배경 이미지:
     - 게임의 타이틀 화면을 나타내는 이미지
- Controller:
  1. 로딩 매니저:
     - 게임에 필요한 리소스 로드 및 진행상황 관리
     - 로딩이 완료되면 메인 메뉴 씬으로 전환

### 2. 메인메뉴 씬
- 전환 규칙: 로딩이 완료되면 전환
- Object:
  1. 이미지:
     - 게임의 타이틀 화면을 나타내는 이미지
  2. 버튼:
     - 각 씬으로 전환을 담당하는 오브젝트
     - 게임 시작, 설정, 종료 버튼 등
- Controller:
  1. 씬관리 매니저:
     - 사용자 입력에 따라 해당 씬으로 전환
  3. UI 매니저:
     - 버튼들의 배치 및 상호작용을 관리
  5. 사운드 매니저:
     - 배경음악을 관리
       
### 3. 메인게임 씬
- 전환 규칙: 게임 시작 버튼을 누르면 전환
- Object:
  1. 플레이어 캐릭터:
     - 캐주얼한 인간 타입의 도트 오브젝트
     - 플레이어가 조작할 오브젝트
  4. 좀비:
     - 캐주얼한 느낌의 좀비 타입의 도트 오브젝트
     - 플레이어와 전투할 오브젝트
  6. 맵 타일:
     - 초록색 배경의 맵 타일
     - 6가지의 종류로 구성
     - 게임 맵을 구성한다.
  8. 아이템:
     - 주사기 모양의 백신
     - 동그란 형태의 경험치 구슬
- Controller:
  1. 플레이어 컨트롤러:
     - 플레이어의 이동 사격 대시를 처리한다.
     - 플레이어의 상태를 관리
  2. 좀비 스포너:
     - 게임 레벨에 따라 적을 생성
     - 좀비의 종류와 수를 관리
  3. 충돌 매니저:
     - 오브젝트 간 충돌을 감지하고 처리
     - 충돌 시 발생하는 이벤트(데미지, 아이템 획득 등)를 관리
  4. UI 매니저:
     - 게임 내 UI를 업데이트하고 렌더링
     - 경험치 바, 감염 디버프 표시, 능력치 레벨 표시
  5. 사운드 매니저:
     - 배경음악 및 사격 등 효과음을 관리
- 함수 단위 설명:
  
### 4. 레벨업 씬
- 전환 규칙: 플레이어가 레벨업을 하게 되면, 게임이 Pause되며, 씬이 전환된다.
- Object:
  1. 능력치 선택 카드:
     - 랜덤한 3개의 능력치 옵션 제공
     - 각 카드에는 아이콘, 이름, 설명 포함
- Controller:
  1. 레벨업 매니저:
     - 레벨업 프로세스를 관리하고 능력치 선택을 처리
  3. UI 매니저:
   요
### 1. OOP
- 클래스와 객체를 활용해 코드의 재사용성과 유지보수성을 높인다.
### 2. Dictionary Cache Hit
- 자주 사용하는 데이터를 딕셔너리에 캐싱하여 성능을 향상시킨다.
### 3. Management Scene with Stack
- 스택 구조를 이용해 씬 전환을 관리한다.
### 4. Behavior Tree
- 적 AI의 행동 패턴을 설계하고 관리한다.
### 5. TileGenerator
- 랜덤한 타일로 맵을 생성한다.

## 개발 요소 (정략적으로 제시) 수정 필요
### 레벨 수
- 스테이지:
- 능력:
### 맵 크기
- 제한 없음
### 아이템
- 경험치 구슬: 좀비당 1개
- 백신: 좀비 20마리당 1개
### 적의 수
- 스테이지 레벨에 비례해 10마리씩 선형적 증가
### 프레임 속도
- 60FPS
### 레벨업 시스템
- 각 스테이지의 최대 좀비 수의 경험치량

## 게임 프레임워크
### 화면 및 렌더링 기능
### 이벤트 처리
### 타이머 및 프레임 속도
### 사운드 및 음악 재생
### Scene 관리
### GameObject 관리

## 일정
### 10/28일 이전 준비
- 리소스 수집
- 기본 프레임 워크 구상
- 맵 및 UI 구상
### 1주차: 랜덤한 타일로 맵을 생성하는 기법 구현
### 2주차: 플레이어 이동 구현 및 총알 구현
### 3주차: 좀비 구현
### 4주차: 좀비 행동 트리 구현
### 5주차: 레벨업 및 플레이어 능력치 구현
### 6주차: 사운드 추가 및 게임 종료 로직 구현
### 7주차: 밸런스 조절 및 최종 점검
