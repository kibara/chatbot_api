# -*- coding: utf-8 -*-

import falcon
import json
import random
import dbaccess


class ItemsResource:
    def on_get(self, req, resp):
        items = {}
        contents = {}
        if ('key' in req.params) and (req.params['key'] not in ('\'', '_', '%', '#', '&')):
            value = req.params['key']
            res = dbaccess.postquery(value)
            i = random.randint(0, len(res) - 1)  # DBでHITした内容が複数あったら、
                                                 # 単純なランダムで1つ返す

            # contents
            contents['type'] = 'text'
            contents['value'] = res[i][3]  # DB応答のテキスト部分

            # items
            if res[i][4] == 'ng001':
                items['status'] = 'warning'
                items['description'] = 'Your request key has no data in DB'
            else:
                items['status'] = 'success'
                items['description'] = 'your request has been successfully processed'
            items['contents'] = [contents]
            resp.status = falcon.HTTP_200

        else:
            # contents
            contents['type'] = 'Error'
            contents['description'] = 'your request key is empty or invalid'
            contents['value'] = 'InputError'

            # items
            items['status'] = 'fail'
            items['contents'] = [contents]

            # response code
            resp.status = falcon.HTTP_400  # Bad Request

        print(req.headers)

        resp.content_type = 'text/plain; charset=utf-8'
        resp.body = json.dumps(items, ensure_ascii=False)

#    def on_post(self, req, resp):
#        params = req.stream.read().decode('utf-8')
#        items = {
#            u'title': u'WebAPIテスト',
#            u'tags': [
#                {
#                    u'name': u'テスト',
#                    u'バージョン': []
#                },
#                {
#                    u'name': u'request',
#                    params: []
#                }
#            ]
#        }
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/plain; charset=utf-8'
        resp.body = json.dumps(items, ensure_ascii=False)


api = falcon.API()
api.add_route('/test_api', ItemsResource())

if __name__ == "__main__":
    from wsgiref import simple_server

    httpd = simple_server.make_server("127.0.0.1", 8008, api)
    httpd.serve_forever()
