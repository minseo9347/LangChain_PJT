import meilisearch as ms
# meilisearch의 클라이언트의 객체
# client = meilisearch.Client('로컬호스트', '서버의키')
client = ms.Client('http://localhost:7700', 'aSampleMasterKey')

# 검색하기
def search_company(symbol):
    # 'nasdaq' 인덱스(목록, 이름)에서 심볼로 검색
    return client.index('nasdaq').search(symbol)


# 자료 서칭을 위한 클래스
class SearchhResult:
    # 객체 생성자, 크래스를 객체화 할 때 무조건 실행
    def __init__(self, item):
        self.item = item

    # 심볼값 가져오기
    @property # 프로퍼티로 선언하면, 함수처럼 사용가능 (파이썬 데코레이터)
    def symbol(self):
        return self.item['Symbol']

    # 회사명 가져오기
    @property
    def name(self):
        return self.item['Name']
    
    # print() 또는 str()문을 만났을 때 출력형태
    def __str__(self):
        # return f"{self.symbole} : {self.name()}"
        return f"{self.symbol} : {self.name}" # 프로펄티가 있으므로 self.symbole()로 호출하지 않아도 됨
        # 속성처럼 호출 가능

# 모듈 테스트
if __name__ == "__main__":
    # symbol = "AAPL"  # 검색할 심볼키워드
    symbol = "Apple"  # 검색할 심볼키워드
    company_info = search_company(symbol)
    hits = company_info['hits']
    # print(hits)
    # result = []
    # for hit in hits:
        # print(SearchhResult(hit))  # SearchhResult 클래스의 객체를 생성하고 출력
        # print("-" * 20)
        # result.append(SearchhResult(hit))
    
    # 리스트 컴프리헨션으로 변경
    result = [SearchhResult(hit) for hit in hits]
    # result의 최종결과
    print(result)
    print(result[0].name)
    print(result[0].symbol)

    # 메모리 값이 출력된다. 해당 메모리 값을 프린트로 찍으면 이런 형태로 출력
    # -------------------
    # APDN : Applied DNA Sciences Inc. Common Stock
    # -------------------
    # APLD : Applied Digital Corporation Common Stock
    # --------------------



    # company_symbol = company_info['hits'][0]['Symbol']  # 검색할 심볼키워드
    # company_name = company_info['hits'][0]['Name']  # 검색된 첫번째 결과
    # company_asd = company_info['hits'][0]['Market Cap']  # 검색된 첫번째 결과
    # print(f"{company_symbol} : {company_name}") # 검색된 회사 이름 출력
    # print(company_info)

    # print(company_name)
    # print(company_symbol) 
    # print(company_asd)  # 검색된 회사 이름 출력
