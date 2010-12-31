Zoom.it Python SDK
==================

This client library is designed to support the 
[Zoom.it API](http://zoom.it/pages/api).

Basic usage:

    service = zoomit.ZoomItService()
    content = service.get_content_by_url('http://openzoom.org')
    id = content['id']
    dzi = content['dzi']
    print(id, dzi)

Reporting Issues
----------------

Please [file bugs or issues][issues] you encounter.

[issues]: https://github.com/openzoom/zoomit-python-sdk/issues
