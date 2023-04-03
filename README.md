# src_heavensAngelbot
ICT Probono 2023 출품작 "Heaven's Angelbot" 프로젝트 입니다.

Heaven's Angelbot 프로젝트는 web RCS 즉 웹 로봇관제 시스템의 일종으로, 복수의 서로 다른 로봇들을 웹에서 중앙제어하는 시스템 입니다.

현장에서 발생하는 대부분의 작업요청은 비즈니스로직에 따라 자동적으로 대응하며, 관리자 또는 사용자는 어떤 로봇이 어디서 무엇을 하고 있는지 직관적인 GUI로 인식하고 필요할 경우 작업을 지시할 수 있습니다.

이러한 webRCS의 특성을 ict프로보노의 주제에 걸맞게 적용시킨것이 요양원 돌봄로봇 웹 관제시스템 "Heaven's Angelbot" 입니다.

아래는 전체 시스템의 대략적인 구조입니다.

![228803583-78f41ad0-e67a-42df-959a-7b09cfb471c2](https://user-images.githubusercontent.com/124308667/229501099-ea190721-d507-4964-8dac-8000366e0d80.png)


우리는 다음의 개발 규칙을 가지고 있습니다. ################################
fork
  1. 모든 팀원은 이 repository 를 fork 한 뒤, clone 하여 작업하십시오.
  
branch
  1. main : 공개적인 발표용 정식 버전을 관리할 branch 입니다. 관리자와 상담없이 건드리지 마십시오.
  2. develop : 개발의 기준 브렌치로, 이 branch는 작동하는 마지막 공통 branch로 존재합니다.
  3. feature/{이슈번호}-{이슈제목 혹은 설명} : 항상 이 양식으로 branch를 생성하여 작업하십시오. 자신의 local에서 정상동작이 확인되면, upstream의 develop branch에 pull request 하십시오.

commit
  1. git commit -m "{이슈번호}-{작업내용}" 으로 작성합니다. 이슈번호가 없을 경우 0 으로 작성합니다.




우리는 다음의 개발 환경을 가지고 있습니다. ################################
os
  1. linux ubuntu 20.04

Language
  1. python3.9



