import requests
import json


# 通过Pixiv_Id返回原图,多图返回第一张
def search_pixivl(id):
    _id = id
    headers = {
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    req = requests.get(f'https://api.pixivel.moe/pixiv?type=illust&id={_id}', headers=headers)
    _json = json.loads(req.text)
    print(_json)
    try:
        pages = _json.get('meta_pages')
        # 单图
        if pages is None:
            page = _json.get('illust').get('meta_single_page').get('original_image_url')
            return str(page).replace('https://i.pximg.net/', 'https://proxy-jp1.pixivel.moe/')
        # 多图
        else:
            holder = []
            for i in pages:
                holder.append(i.get('image_urls').get('original').replace('https://i.pximg.net/',
                                                                          'https://proxy-jp1.pixivel.moe/'))
            return holder
    except:
        return 'Error'
