'''오늘 미세먼지 농도 불러오는 애
류혜윤 담당 '''
import requests as rq

def get_dust() : 

    MY_KEY = 'c65a493de678400bd8136f3cae8817528a1faecd0a4238f9f46a0ba85c1b1370'

    url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey={MY_KEY}&returnType=json&dataTerm=Daily&stationName=%EC%95%84%EC%A3%BC%EB%8F%99'
    save_file_path = 'data/observatory_file.txt'

    response = rq.get(url)
    data = response.json()

    return data['response']['body']['items'][0]['khaiValue']

if __name__ == '__main__' :
    #시험용 코드
    print(get_dust())