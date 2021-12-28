import requests,json


headers = {
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}

def get_image():
    req = requests.get('https://api.lolicon.app/setu/v2?size=small')
    res_text = json.loads(req.text)
    for item in res_text.get('data'):
        origin = (item.get('urls').get('small'))
        print(origin)
        # https://proxy-jp1.pixivel.moe/img-original/img/
        # https://proxy-jp1.pixivel.moe/c/
        print((str(origin).split('/c/')[1]))
    return 'https://proxy-jp1.pixivel.moe/c/' + (str(origin).split('/c/')[1])


def get_image_normal():
    req = requests.get('https://api.ixiaowai.cn/api/api.php?return=json', headers=headers)
    req.encoding = 'utf-8-sig'
    res_text = json.loads(req.text)
    return (res_text.get('imgurl'))

def get_image_tag(tag):
    req = requests.get(f'https://api.lolicon.app/setu/v2?tag={tag}')
    res_text = json.loads(req.text)
    print(res_text)
    for item in res_text.get('data'):
        origin = (item.get('urls').get('original'))
        # https://proxy-jp1.pixivel.moe/img-original/img/
    return 'https://proxy-jp1.pixivel.moe/img-original/img/' + (str(origin).split('/img/')[1])

def get_image_tag_quickly():
    req = requests.get(f'https://api.lolicon.app/setu/v2?size=regular')
    res_text = json.loads(req.text)
    print(res_text)
    for item in res_text.get('data'):
        origin = (item.get('urls').get('regular'))
        # https://proxy-jp1.pixivel.moe/img-original/img/
    return 'https://proxy-jp1.pixivel.moe/img-master/img/' + (str(origin).split('/img/')[1])


print(get_image())