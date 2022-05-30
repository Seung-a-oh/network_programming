import requests

API_URL = 'https://dapi.kakao.com/v2/translation/translate'
REST_API_KEY = '본인의 REST_API_KEY'

def translate_get(text): # GET 요청
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'src_lang': 'kr', 'target_lang': 'en', 'query': text}
    rsp = requests.get(API_URL, headers=headers, params=data)
    return rsp.json()

def translate_post(text): # POST 요청
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'src_lang': 'kr', 'target_lang': 'fr', 'query': text}
    rsp = requests.post(API_URL, headers=headers, data=data)
    return rsp.json()

if __name__ == "__main__":
    while True:
        text = input('Enter the sentence to translate: ')
        if text != 'q':
            translated_text = translate_get(text)
            print(translated_text)
            print('[GET]', translated_text['translated_text'][0][0])
            translated_text = translate_post(text)
            print(translated_text)
            print('[POST]', translated_text['translated_text'][0][0], '\n')
        else:
            break