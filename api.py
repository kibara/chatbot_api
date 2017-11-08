# -*- coding: utf-8 -*-

import falcon
import json


class ItemsResource:
    def on_get(self, req, resp):
        value = req.params['key']
        items = {
            'title': 'WebAPIテスト',
            'tags': [
                {
                    'name': 'テスト',
                    'バージョン': []
                },
                {
                    'name': 'request', value: []
                }
            ]
        }
        print(req.headers)
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/plain; charset=utf-8'
        resp.body = json.dumps(items, ensure_ascii=False)

    def on_post(self, req, resp):
        params = req.stream.read().decode('utf-8')
        items = {
            u'title': u'WebAPIテスト',
            u'tags': [
                {
                    u'name': u'テスト',
                    u'バージョン': []
                },
                {
                    u'name': u'request', params: []
                }
            ]
        }
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/plain; charset=utf-8'
        resp.body = json.dumps(items, ensure_ascii=False)


api = falcon.API()
api.add_route('/test_api', ItemsResource())

if __name__ == "__main__":
    from wsgiref import simple_server

    httpd = simple_server.make_server("127.0.0.1", 8008, api)
    httpd.serve_forever()

