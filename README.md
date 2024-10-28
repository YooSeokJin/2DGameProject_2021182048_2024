# 2DGameProgramming - ZomBoogie
- 2021182048 게임공학과 유석진
- 2024.10.04 ~ 2024.12.~
- 언어: Python
- 엔진/라이브러리: Pygame
- IDE: VSCode
- 운영체제: Windows
- 버전 관리: Git / Source Tree

# ZomBoogie 
![Title](https://github.com/user-attachments/assets/fce170cd-ead1-45c2-a79a-91e9081a3bc0)
## [컨셉 소개]
- 참고 게임: Vampire Survivors
- 장르: 탑다운 슈팅 로그라이트
- 목표: 끝없이 몰려오는 좀비를 피하고, 쓰러뜨리며 최대한 오래 살아남는다.
- 성장 요소: 좀비를 처치해 자원을 얻고, 캐릭터를 점점 더 강하게 성장시킨다.
- 특징: 빠르고 간단한 조작으로 누구나 쉽게 즐길 수 있는 캐주얼한 게임플레이.

## [핵심 메카닉]
### 캐릭터 컨트롤
- wasd: 8방향 이동 지원.
- 좌클릭: 마우스 위치로 사격.
### 좀비
- 기본 타입: 플레이어에 다가가며 공격을 한다.
- 원거리 타입: 기본적으로 플레이어와 거리를 유지하며, 원거리 공격을 한다.
- 탱커 타입: 총알을 세 번 맞으면 죽는다.
### 아이템
- 경험치: 좀비를 처치하면 경험치 구슬 드랍.
- 백신: 좀비를 처치하면 낮은 확률로 백신 드랍.
### 게임 기능
- 감염 디버프:
    - Hp의 개념.
    - 플레이어는 피격 시 감염 디버프 추가.
    - 감염 디버프 중첩 횟수가 특정 횟수 이상이면 게임 오버.
- 백신: 백신을 통해 감염 디버프를 0으로 초기화.
- 일정 게임 레벨(20)을 버티면 게임 클리어
### 레벨업 시스템
- 능력치 선택: 레벨업 시 랜덤한 3개의 능력치 중 1개를 선택하여 강화.
1. 면역력 증가. (현재 적용중인 감염 디버프를 초기화 시킨다)
2. 이동 속도 증가.
3. 사격 속도 증가.
4. 탄환 관통 횟수 증가.
5. 멀티샷. (가로)
6. 멀티샷. (세로)
7. 사거리 증가.
8. 감염 디버프 최대 횟수 증가.
   
## [게임 흐름]
1. 사방에서 몰려오는 좀비로부터 생존한다.
2. 플레이어는 직접 사격하여 좀비를 물리친다.
3. 플레이어는 좀비와 충돌시 감염 디버프가 증가한다. (Hp 개념)
4. 감염 디버프가 특정 횟수 이상이 되면 게임 오버가 된다.
5. 남은 시간이 0이되면 게임을 승리한다.
    - 스테이지 레벨은 20레벨로 구성되었으며, 30초마다 레벨이 증가한다.
### 게임 화면
![메인 씬](https://github.com/user-attachments/assets/b731f682-0586-45d1-8182-2ace79fb81dd)
### 레벨업
![Zombogie레벨업](https://github.com/user-attachments/assets/d14f12c0-18a4-4833-a170-a6181321e693)

## [씬 구성]
### 로딩 씬
- 구성: bg, guage
- 전환 규칙: 게임을 시작하면 로딩 씬으로 전환.
- GameObject:
   1. bg
      - 역할: 로딩 화면.
      - 생김새: 한국공학대 아이콘.
   2. guage
      - 역할: 로딩 진행 상황을 시각적으로 표시.
      - 생김새: 직사각형 형태의 프로그레스 바.
### 메인 메뉴 씬
- 구성: bg, button
- 전환 규칙: 버튼에 알맞은 씬으로 전환.
- GameObject:
   1. bg
      - 역할: 타이틀 화면.
      - 생김새: 좀비들에게 둘러 쌓인 주인공 이미지.
   1. button
      - 역할: 게임 시작, 설정, 종료 기능을 수행, 입력에 따라 해당 씬으로 전환.
      - 생김새: 직사각형 디자인에 텍스트가 적힌 형태.
### 메인 게임 씬
- 구성: bg, zombie, player, item, ui, controller
- 전환 규칙: 플레이어의 승리 또는 패배에 따라 엔딩 씬으로 전환.
- GameObject:
   1. bg
      - 역할: 플레이어의 이동에 따라 랜덤하게 타일을 생성.
      - 생김새: 초록색 잔디밭.
   2. player
      - 역할: 사용자가 조작하는 캐릭터, 이동 공격 아이템 수집 수행.
      - 생김새: 캐주얼한 도트 그래픽의 인간형 캐릭터.
      - class:
         1. bullet
         2. status
   3. zombie
      - 역할: 사용자와 전투할 캐릭터, 행동 트리에 따라 움직이며 플레이어를 공격.
      - 생김새: 캐주얼한 도트 그래픽의 좀비형 캐릭터.
      - class:
         1. defaultZombie
         2. rangeZombie
         3. tankerZombie
   4. item
      - 역할: 플레이어가 수집하여 레벨을 높히거나, Hp를 회복.
      - 생김새:
          - 백신: 빨간색 통조림 모양에 가운데 하트가 그려진 이미지
          - 경험치 코인: 황금색 코인 이미지
      - class:
         1. Coin
         2. Vaccine
   5. ui
      - 역할: 게임 진행 정보를 화면에 표시.
      - 생김새: 적절한 이미지와 텍스트로 표시.
- Controller
   - Collision_Checker: 충돌 감지 및 처리 담당.
   - Enermy_Zen: 좀비 생성을 담당.
   - Behavior_Tree: 좀비의 행동을 담당.
### 레벨업 씬
- 구성: card, controller
- 전환 규칙: 특정 카드를 누르면 메인 게임 씬으로 전환.
- GameObject
   1. card
      - 역할: 플레이어가 선택하여 능력치를 업그레이드할 수 있는 카드.
      - 생김새: 능력치를 상징하는 아이콘과 설명이 적힌 직사각형 카드 형태.
- controller:
   1. LevelUpController: 플레이어의 카드 선택 및 능력치를 적용.
### 엔딩 씬
- 구성: button
- 전환 규칙: 버튼을 누르면 메인 메뉴 씬으로 전환.
- GameObject:
   1. 버튼
      - 역할: 버튼과 알맞은 씬으로 전환 또는 설정 적용.
      - 생김새: 직사각형 디자인에 텍스트가 적힌 형태.

## [개발 요소]
### 스테이지 레벨
- 스테이지: 20레벨
   - '30'초 간격으로 스테이지 레벨 상승.
   -  난이도를 조절하는 변수로 사용.
   -  약 20분
### 레벨업
- 경험치 요구량:
   - 레벨에 비례해 30씩 선형적으로 증가한다.
   - 예시)
      - 레벨1: 필요 경험치 30
      - 레벨2: 필요 경험치 60
### 능력
- 능력: 레벨 제한 없음
   1. 감염 디버프 제거: 현재 누적된 감염 디버프를 모두 제거한다.
   2. 이동 속도 증가: 초당 이동 거리 증가.
   3. 사격 속도 증가: 현재 사격 간격의 5% 만큼 감소.
   4. 탄환 관통 횟수 증가: 좀비를 관통하는 횟수가 1회 증가.
   5. 탄환 개수 증가: 사격시 부채꼴 모양으로 퍼지는 탄환 증가.
   7. 사거리 증가: 탄환의 사거리가 5픽셀 증가.
   8. 감염 디버프 최대 횟수 증가: 기존의 최대 감염 횟수에서 +1이 증가한다.
### 맵
- 크기: 제한 없음
   - 맵은 무한히 확장되며, 플레이어의 이동에 따라 새로운 타일이 생성된다.
   - 타일 제너레이터를 통해 랜덤한 맵이 동적으로 구성된다.
   - 타일 하나의 사이즈는 19x19 픽셀
### 아이템
- 경험치 코인: 100%
   - 좀비를 처치하면 100% 확률로 경험치 구슬을 드랍한다.
   - 이를 획득하면 경험치가 증가한다.
- 백신: 0.1%
   - 좀비를 처치하면 0.1% 확률로 드랍한다.
   - 감염 디버프를 초기화하는 아이템이다.
### 적
- 타입: 기본, 원거리, 탱커
- 스테이지 레벨에 비례해 최대 좀비 수가 30마리씩 선형적으로 증가한다.
- 예시)
   - 스테이지1: 좀비 30마리
   - 스테이지2: 좀비 60마리
- 게임이 진행됨에 따라 좀비수가 증가하며 난이도 상승한다.
- 행동 트리를 통해 좀비의 AI를 설정한다.

## [사용한/사용할 개발 기법]
### OOP
- 클래스와 객체를 활용해 코드의 재사용성과 유지보수성을 높히는 기법.
### Event Driven Programming
- 사용자의 입력이나 게임 내 이벤트에 반응해 로직을 실행하는 기법.
### State Machines
- 게임 상태나 오브젝트의 상태를 상태 기계로 관리하는 기법.

## [게임 프레임워크]
### gfw
- 각 씬을 스택 구조로 관리하여 게임의 흐름을 제어.
### world
- 각 씬별 필요한 오브젝트들을 업데이트, 드로우, 이벤트처리.
### image 
- 게임에서 사용하는 이미지를 딕셔너리에 캐시 및 관리.
### sheetSprite
- 오브젝트의 스프라이트 시트를 관리 및 애니메이션 재생.
### scoreSprite
- 기타 정보를 화면에 시각적으로 렌더링.
### guage
- 로딩 정보나 상태를 시각적으로 표시하는 게이지를 렌더링.
### infiniteScrollBackground
- 무한이 이어지는 배경을 구현
### behaviorTree
- 적 AI의 행동 패턴을 설계하고 관리.
### randomTileGenerator
- 랜덤한 타일을 생성하여 동적으로 변하는 맵을 구성.

## [일정]
### 10/28일 이전 준비
- 리소스 수집
- 기본 프레임 워크 구상
- 맵 및 UI 구상

### 1주차: 
1. randomTileGenerator 구현
2. 캐릭터 컨트롤러 구현
### 2주차: 
2. 좀비 및 아이템 구현
3. 충돌 처리 구현
### 3주차: 
1. 좀비 행동 트리 구현
2. 플레이어 능력치 구현
### 4주차: 
1. 플레이어 레벨업 구현
2. UI 구현
### 5주차: 
1. 로딩 씬 구현
2. 메인 메뉴 씬 구현
### 6주차: 
1. 사운드 구현
2. 게임 종료 로직 구현
3. 부족한 기능 구현
### 7주차:
1. 밸런스 조절 및 최종 점검
2. 릴리즈

## [성과]
### 10/28일 이전
- 게임 리소스 수집 완료
  - 출처: https://goldmetal.co.kr/
- 기본 프레임 워크 구상 완료
- 맵 및 UI 구상 완료

### 1주차
### 2주차
### 3주차
### 4주차
### 5주차
### 6주차
### 7주차

## [Youtube]
- 1차 발표: https://youtu.be/JN8lkWoDTZI
