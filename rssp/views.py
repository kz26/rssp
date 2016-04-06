from pyramid.view import view_config
from pyramid.response import FileIter, Response

from contextlib import closing
import requests

from . import __version__


ALLOWED_CONTENT_TYPES = (
	'application/atom+xml',
	'application/rdf+xml',
	'application/rss+xml',
	'text/xml'
)

USER_AGENT = "rssp/%s" % __version__

@view_config(route_name='index', renderer='templates/index.pt')
def index(request):
	return {'version': USER_AGENT}

@view_config(route_name='feed')
def get_feed(request):
	url = request.matchdict['url']
	headers = {'User-Agent': USER_AGENT, 'Accept': ', '.join(ALLOWED_CONTENT_TYPES)}
	try:
		with closing(requests.get(url, headers=headers, stream=True)) as r:
			ct = r.headers.get('content-type', '').split(';')[0].lower()
			if ct in ALLOWED_CONTENT_TYPES:
				res = Response()
				res.content_type = ct
				if r.headers.get('cache-control'):
					res.cache_control = r.headers.get('cache-control')
				for x in r.iter_content(1024 * 1024):
					if x:
						res.body_file.write(x)
				return res
			else:
				return Response(status_code=400)
	except requests.exceptions.RequestException as e:
		return Response(str(e), status_code=400)
