# docker-finalexam
ccit2_finalexam

Q1. python으로 random 숫자를 n개 생성하는 함수를 만드세요. (20점)
함수: gen_random(n), sorted_random(n)
gen_random(n) : 정렬되지 않는 n개의 난수 숫자 리스트를.
sorted_random(n) : 정렬된 n개의 난수 리스트.
1) INPUT n = n개의 숫자를 의미
2) OUTPUT :  list : [r] 에,
r = random 정수 숫자, 0 < r <= n
-. gen_random()의 경우, 정렬되지 않은 그 상태로 출력,
-. sorted_random() 의 경우 작은 숫자부터 정렬되어 결과가 나오도록 출력
3) 함수를 실행하는 메인함수 작성필요
4) 정렬 알고리즘의 시간복잡도 설명하시오. (README.md 파일에 추가할 것)(시간복잡도가 좋은 것에 따라 평가점수 달라짐)

A1.
- gen_random(n), sorted_random(n) 함수 작성 완료
- sorted_random(n)에서 정렬 알고리즘 quick sort 사용
- quick sort의 시간복잡도는 평균 nlogn, 최악은 n^2 > 빠른편

Q2. Docker 기반의 워드 프레스를 구축하시오. (20점)
1) 웹서버: nginx, DB: MySQL 를 사용할 것.
2) Theme : 기본 테마가 아닌 다른 새로운 테마가 추가되어 있어야 함.
3) Plugin : 기본 플러그인이 아닌 새로운 플러그인이 추가되어 있어야 함.
4) docker-compose 로 실행시, Theme와 Plugin이 추가된 상태가 되어 있어야 할 것.
=> 다시말해, container를 띄우면 새로운 테마와 플러그인이 보여야 함
=> id/pass  == admin/password 로 셋팅해 둘 것.

A2.
- 구축완료
- XXX Theme 및 XXX Plugin 새로운 테마와 플러그인이 폴더로 옮겨짐 > 저작권 문제가 있을 수 있으므로 해당 폴더 삭제
- docker-compose 실행시 알아서 셋팅됨
- id/pass == admin/password 셋팅됨
- 워드프레스 사이트 URL > http://[webserver]

Q3. 워드프레스 테이블 wp_users 에 대한 CRUD api를 생성할 것.(60점)
1) python api 로 생성한 사용자 데이터로 인해, wordpress가 웹페이지에서 로그인이 되어야 함.
2) swagger 문서를 위한 코드도 추가할 것. (이걸로 api 를 테스트해 볼 예정)
3) docker-compose 실행시, swagger 문서를 볼 수 있는 URL 제공해야 함.(README.md 파일에 추가할 것)

A3.
- CRUD api 작성완료
- swagger 작성완료
- swagger 문서 볼 수있는 URL > http://[webserver-flask도커IP]:5000 에 포함
   
Q4. 워드프레스에 Table: wp_random 을 추가할 것. (20점)
comlumn: id(int, autoincrement), random(int)
1) CRUD API 작성할 것. (swagger 필요)
2) Q1번에서 작성한 random list를 이 테이블에 추가하도록 연결할 것(python 프로그램 작성)
gen_random(n)을 두번 실행하여 나온 결과를 api를 사용하여, table에 저장할 수 있도록 할 것.
3) docker-compose 실행시, swagger 문서를 볼 수 있는 URL 제공해야 함.(README.md 파일에 추가할 것)

A4.
- 해당 실습전 mysql docker에 wp_random 추가 > create table wp_random(id INT PRIMARY KEY AUTO_INCREMENT, random INT(10)); 사용
- swagger 문서 볼 수있는 URL > http://[webserver-flask도커IP]:5000 에 포함 

Q5. 다음 query를 수행하는 테이블 데이터가 저장된 wp_random에서 random 컬럼에 index생성/미생성 간의 성능비교를 할 것. (80점)
query : select id, random from wp_random where random = cast(n/2 as int);
1) n = 100  인경우, 출력 결과, 수행시간 기록  (Index 생성/미생성)
2) n = 1,000  인경우, 출력 결과, 수행시간 기록 (Index 생성/미생성)
3) n = 10,000 인경우, 출력 결과, 수행시간 기록 (Index 생성/미생성)
4) n = 100,000 인경우, 출력 결과, 수행시간 기록 (Index 생성/미생성)
5) README.md 파일에 기록할 것 ==> 어느쪽이 빠른지 평가해 볼 것. (edited) 

A5.
- 3만개 데이터 기준
- select id, random from wp_random where random = cast(n/2 as unsigned int); 로 조회
- alter table wp_random add index idx (random); 로 Index 생성
1) n = 100  인경우, 출력 결과, 수행시간 기록  (Index 생성/미생성)
- 12852 | 50
- Index 생성 시 0.00초, 미생성시 0.01초
2) n = 1,000  인경우, 출력 결과, 수행시간 기록 (Index 생성/미생성)
- 5235 | 500
- Index 생성 시 0.00초, 미생성시 0.01초
3) n = 10,000 인경우, 출력 결과, 수행시간 기록 (Index 생성/미생성)
- None
- Index 생성 시 0.00초, 미생성시 0.01초
4) n = 100,000 인경우, 출력 결과, 수행시간 기록 (Index 생성/미생성)
- None
- Index 생성 시 0.00초, 미생성시 0.02초
- 결론 : Index 생성하는 것이 검색 속도가 빠르며, 데이터 량이 늘수록 차이가 커짐
