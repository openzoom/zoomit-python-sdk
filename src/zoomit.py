#!/usr/bin/env python
#
#  Copyright 2010 Daniel Gasienica <daniel@gasienica.ch>
#  Copyright 2010 Boris Bluntschli <boris@bluntschli.ch>
#  Copyright 2010 Facebook
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# Find a JSON parser (from Facebook Python SDK)
try:
    import json
    _parse_json = lambda s: json.loads(s)
except ImportError:
    try:
        import simplejson
        _parse_json = lambda s: simplejson.loads(s)
    except ImportError:
        # For Google AppEngine
        from django.utils import simplejson
        _parse_json = lambda s: simplejson.loads(s)

import urllib

class ZoomItService(object):
    """A client for the Zoom.it API.

    See http://zoom.it/pages/api for complete documentation of the API.
    """
    def __init__(self, endpoint="http://api.zoom.it/v1"):
        self.endpoint = endpoint

    def get_content_by_id(self, id):
        try:
            response = urllib.urlopen('%s/content/%s' % (self.endpoint, id))
            if response.code != 200:
                message = response.read()
                raise ZoomitServiceException(response.code, message)
            return _parse_json(response.read())
        except Exception, e:
            raise e
        finally:
            if response:
                response.close()

    def get_content_by_url(self, url):
        try:
            request_url = '%s/content/?%s' % (self.endpoint, urllib.urlencode({'url': url}))
            response = urllib.urlopen(request_url)
            if response.code >= 400:
                message = response.read()
                raise ZoomitServiceException(response.code, message)
            return _parse_json(response.read())
                
        except Exception, e:
            raise e
        finally:
            if response:
                response.close()
        # content_info = _parse_json(content_info_response.read())

class ZoomitServiceException(Exception):
    def __init__(self, status_code, message):
        Exception.__init__(self, message)
        self.status_code = status_code
            

# ------------------------------------------------------------------------------

import unittest

class ZoomItServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = ZoomItService()

    def test_missing_id(self):
        def aux_test_missing_id():
            # Try to retrieve content for image with a funny smiley making
            # the OMG face as its id. This should obviously fail, as 
            # zoom.it uses non-smileys as identifiers.
            self.service.get_content_by_id(u'8=o')            
        
        self.assertRaises(ZoomitServiceException, aux_test_missing_id)

    def test_existing_id(self):
        # This test is pedo bear approved
        test_id = '8'
        
        content = self.service.get_content_by_id(test_id)
        self.assertEquals(content['failed'], False)
        self.assertEquals(content['ready'], True)
        self.assertEquals(content['id'], test_id)

    def test_existing_url(self):
        url = 'http://answers.yahoo.com/question/index?qid=20080331170418AAhm4TU'
        content = self.service.get_content_by_url(url)
        required_keys = [u'id', u'embedHtml', u'url', u'shareUrl', u'dzi', u'failed', u'ready', u'progress']
        for key in required_keys:
            self.assertTrue(key in content, "Required key '%s' missing" % key)

if __name__ == '__main__':
    unittest.main()            