#!/usr/bin/env python
#
#  Copyright 2010 Daniel Gasienica <daniel@gasienica.ch>
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

class ZoomItService(object):
    """A client for the Zoom.it API.

    See http://zoom.it/pages/api for complete documentation of the API.
    """
    def __init__(self, endpoint="http://api.zoom.it/v1"):
        self.endpoint = endpoint

    def get_content_by_id(self, id):
        pass

    def get_content_by_url(self, url):
        pass

class ContentInfo(object):
    def __init__(self, id, url, ready, failed, progress, share_url,
                 embed_html, title, attribution_text, attribution_url, dzi=None)
        self.id = id
        self.url = url
        self.ready = ready
        self.failed = failed
        self.progress = progress
        self.share_url = share_url
        self.embed_html = embed_html
        self.title = title
        self.attribution_text = attribution_text
        self.attribution_url = attribution_url
        self.dzi = dzi


class DZIInfo(object):
    def __init__(self, url, width, height,
                 tile_size, tile_overlap, tile_format):
        self.url = url
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.tile_overlap = tile_overlap
        self.tile_format = tile_format
