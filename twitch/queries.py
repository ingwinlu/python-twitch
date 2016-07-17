# -*- encoding: utf-8 -*-
import six

from six.moves.urllib.error import URLError
from six.moves.urllib.parse import urlencode, urljoin
from six.moves.urllib.parse import quote_plus  # NOQA
from six.moves.urllib.request import Request, urlopen

from twitch import CLIENT_ID, MAX_RETRIES
from twitch.exceptions import ResourceUnavailableException
from twitch.keys import USER_AGENT, USER_AGENT_STRING
from twitch.logging import log

try:
    import json
except:
    import simplejson as json  # @UnresolvedImport

_kraken_baseurl = 'https://api.twitch.tv/kraken/'
_hidden_baseurl = 'http://api.twitch.tv/api/'
_usher_baseurl = 'http://usher.twitch.tv/'

_v2_headers = {'ACCEPT': 'application/vnd.twitchtv.v2+json'}
_v3_headers = {'ACCEPT': 'application/vnd.twitchtv.v3+json'}


class Query(object):
    def __init__(self, url):
        self._url = url

        self._headers = {USER_AGENT: USER_AGENT_STRING}
        self._params = dict()
        self._urlkws = dict()

    @property
    def url(self):
        formatted_url = self._url.format(**self._urlkws)  # throws KeyError
        encoded_params = urlencode(self.params)
        full_url = '?'.join([formatted_url, encoded_params])
        return full_url

    @property
    def headers(self):
        return self._headers

    def update_headers(self, additional_headers):
        self._headers.update(additional_headers)

    @property
    def params(self):
        return self._params

    @property
    def urlkws(self):
        return self._urlkws

    def add_path(self, path):
        self._url = urljoin(self._url, path)
        return self

    def add_param(self, key, value, default=None):
        assert_new(self._params, key)
        if value != default:
            self._params[key] = value
        return self

    def add_urlkw(self, kw, replacement):
        assert_new(self._urlkws, kw)
        self._urlkws[kw] = replacement
        return self

    def __str__(self):
        return 'Query to {url}, params {params}, headers {headers}'.format(
                url=self.url, params=self.params, headers=self.headers)

    def execute(self):
        '''Executes the Query, wraps resolve in try catch'''
        try:
            return self._resolve()
        except URLError:
            raise ResourceUnavailableException(str(self))

    def _resolve(self):
        '''Resolves the Query and tries to return data'''
        log.debug('Querying ' + self.url)
        request = Request(self.url, headers=self.headers)
        answer = ""

        for _ in range(MAX_RETRIES):
            try:
                response = urlopen(request)
                if six.PY2:
                    answer = response.read()
                else:
                    answer = response.read().decode('utf-8')
                response.close()
                break
            except Exception as err:
                if not isinstance(err, URLError):
                    log.debug("Error %s during HTTP Request, abort", repr(err))
                    raise  # propagate non-URLError
            log.debug("Error %s during HTTP Request, retrying", repr(err))
        else:
            raise
        return answer


class JsonQuery(Query):
    def _resolve(self):
        raw_json = super(JsonQuery, self)._resolve()
        jsonDict = json.loads(raw_json)
        log.debug(json.dumps(jsonDict, indent=4))
        return jsonDict


class ApiQuery(JsonQuery):
    def __init__(self, path):
        super(ApiQuery, self).__init__(_kraken_baseurl)
        self.add_path(path)
        self.update_headers({'Client-Id': CLIENT_ID})


class HiddenApiQuery(JsonQuery):
    def __init__(self, path):
        super(HiddenApiQuery, self).__init__(_hidden_baseurl)
        self.add_path(path)


class UsherQuery(Query):
    def __init__(self, path):
        super(UsherQuery, self).__init__(_usher_baseurl)
        self.add_path(path)


class V3Query(ApiQuery):
    def __init__(self, path):
        super(V3Query, self).__init__(path)
        self.update_headers(_v3_headers)


class V2Query(ApiQuery):
    def __init__(self, path):
        super(V2Query, self).__init__(path)
        self.update_headers(_v2_headers)


def assert_new(d, k):
    if k in d:
        v = d.get(k)
        raise ValueError("Key '{}' already set to '{}'".format(
                         k, v))


def query(f):
    def wrapper(*args, **kwargs):
        qry = f(*args, **kwargs)
        if not isinstance(qry, Query):
            raise ValueError('{} did not return a Query, was: {}'.format(
                             f.__name__, repr(qry)))
        log.debug('QUERY: url: %s, params: %s, '
                  'headers: %r, target_func: %r',
                  qry.url, qry.params, qry.headers, f.__name__)
        return qry.execute()
    return wrapper
