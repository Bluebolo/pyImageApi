import requests
import json

def search_pixiv(id):
    _id = id
    headers = {
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    req = requests.get(f'https://api.pixivel.moe/pixiv?type=illust&id={_id}',headers=headers)
    _json = json.loads(req.text)
    try:
        pages = _json.get('illust').get('meta_pages')
        if  pages == []:
            page = _json.get('illust').get('meta_single_page').get('original_image_url')
            return str(page).replace('https://i.pximg.net/','https://proxy-jp1.pixivel.moe/')
        else:
            first = pages[0].get('image_urls').get('original')
            return str(first).replace('https://i.pximg.net/','https://proxy-jp1.pixivel.moe/')
    except:
        return 'Error'
