import json

import scrapy

import brotli

from test1.items import Test1Item


class XuetangSpider(scrapy.Spider):
    name = 'xuetang'
    allowed_domains = ['xuetangx.com']
    base_url = 'https://www.xuetangx.com/api/v1/lms/get_product_list/?page='
    page_index = 1
    headers = {
        'accept': 'application/json,text/plain,*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en',
        'content-type': 'application/json',
        'cookie': 'provider=xuetang; django_language=zh',
        'django-language': 'en',
        'origin': 'https://www.xuetangx.com',
        'referer': 'https://www.xuetangx.com/search?query=&org=&classify=1&type=&status=&page=1',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63',
        'x-client': 'web',
        'xtbz': 'xt'
    }
    payload = {'query': "", 'chief_org': [], 'classify': ["1"], 'selling_type': [], 'status': [], 'appid': 10000}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.download_delay = 1

    def parse(self, response, **kwargs):
        item = Test1Item()
        #response.encoding = 'utf-8'

        content_encoding = response.headers.get('Content-Encoding', b'').decode('utf-8').lower()

        if 'br' in content_encoding:
            # 如果是 Brotli 编码，解压缩响应内容
            compressed_data = response.body
            decompressed_data = brotli.decompress(compressed_data)
            json_data = json.loads(decompressed_data.decode('utf-8'))

            # 在这里对解压缩后的 JSON 数据进行处理，例如提取信息或者其他操作
            # ...

        else:
            # 如果不是 Brotli 编码，你可能需要根据实际情况处理其他编码
            self.log(f"Unsupported Content-Encoding: {content_encoding}")

        # print(response.text)
        # print("ssa",)
        r_data = json.loads(response.text)
        # print(r_data)
        lesson_list = r_data['data']['product_list']
        # print(lesson_list)

        if not lesson_list:
            return

        for lesson in lesson_list:
            item['class_name'] = lesson['name']
            item['teacher'] = ''
            for single_teacher in lesson['teacher']:
                item['teacher'] += (single_teacher['name'] + ' ')
            item['school_name'] = lesson['org']['name']
            item['student_num'] = lesson['enroll_play_num']

            if item['class_name'] and item['teacher'] and item['school_name'] and item['student_num']:
                yield item

        url = self.base_url + str(self.page_index)
        self.page_index += 1
        yield scrapy.Request(
            url=url,
            method='POST',
            headers=self.headers,
            body=json.dumps(self.payload),
            callback=self.parse
        )

    def start_requests(self):
        url = self.base_url + str(self.page_index)
        self.page_index += 1

        yield scrapy.FormRequest(
            url=url,
            method='POST',
            headers=self.headers,
            body=json.dumps(self.payload),
            callback=self.parse
        )
