"""
.. module:: core
   :platform: Unix, Windows
   :synopsis: Contains the API's "core" classes for constructing queries.

.. moduleauthor:: Michael Barr <micbarr+developer@gmail.com>

"""
# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
#import urllib
#import urllib2
import re
#   Requests
from requests import get as requests_get
from requests import post as requests_post
from requests.compat import urlencode

# API Imports
from .settings import STEAM_API_KEY, DEFAULT_LANGUAGE
from .util.decorators import public
from .util.exceptions import APIKeyInvalidError


# =============================================================================
# >> GLOBALS
# =============================================================================
API_KEY_RE = re.compile('[A-Z0-9]{32}')


# =============================================================================
# >> CLASSES
# =============================================================================
@public
class SteamWebAPI(object):
    def __init__(self, key=STEAM_API_KEY, language=DEFAULT_LANGUAGE):
        """.. method:: __init__(key=STEAM_API_KEY, language=DEFAULT_LANGUAGE)

        API base class which contains the default settings for all queries.

        :param key: The alphanumeric Steam Web API Key assigned by Steam.
        :type key: str.
        :param language: The default language to used return data.
        :type language: str.
        :param data_format: The default data format to return data in.
        :type data_format: str.
        :returns:  SteamWebAPI
        :raises: SteamWebAPIKeyError, SteamWebAPIDataFormatError

        """
        # Check the key to make sure it is the valid format
        if key and not API_KEY_RE.match(key):
            raise APIKeyInvalidError

        # Set the instance attributes
        self.key = key
        self.language = language

    def api_query(self, *args, **kwargs):
        """.. method:: api_query(interface, method, method_version=1, httpmethod='GET', parameters={})

        Returns an APIQuery instance of the method that was passed in, or an
        executed APIQuery that returns urllib2.urlopen() if a default format is
        specified.

        :param interface: The alphanumeric Steam Web API Key assigned by Steam.
        :type interface: str.
        :param method: The default language to used return data.
        :type method: str.
        :param method_version: The default data format to return data in.
        :type method_version: str.
        :param httpmethod: The HTTP method (GET or POST)
        :type httpmethod: str.
        :param parameters: The parameters for the API query.
        :type parameters: dict.
        :returns:  APIQuery
        :raises: ?

        """
        # Return the APIQuery instance
        return APIQuery(*args, **kwargs)


@public
class APIQuery(object):
    """.. class:: APIQuery

    Utility class for returning data in either raw JSON, XML, or VDF format
    as queried from urllib2.urlopen(API_URL) via any interface method.

    Example Usage:
        >>> iSteamUser = ISteamUser()
        >>> # Using the APIQuery methods
        >>> return_xml = iSteamUser.GetFriendList(steamid).as_xml()
        >>> return_json = iSteamUser.GetFriendList(steamid).as_json()
        >>> return_vdf = iSteamUser.GetFriendList(steamid).as_vdf()

        >>> # Using the APIQuery properties
        >>> return_xml = iSteamUser.GetFriendList(steamid).xml
        >>> return_json = iSteamUser.GetFriendList(steamid).json
        >>> return_vdf = iSteamUser.GetFriendList(steamid).vdf

    """
    def __init__(self, interface, method, method_version=1, httpmethod='GET',
                 parameters={}):
        """.. method:: __init__(interface, method, method_version=1, httpmethod='GET', parameters={})

        :param interface: The alphanumeric Steam Web API Key assigned by Steam.
        :type interface: str.
        :param method: The default language to used return data.
        :type method: str.
        :param method_version: The default data format to return data in.
        :type method_version: str.
        :param httpmethod: The HTTP method (GET or POST)
        :type httpmethod: str.
        :param parameters: The parameters for the API query.
        :type parameters: dict.
        :returns:  APIQuery
        :raises: URLError,

        """
        self._interface = interface
        self._method = method
        self._version = 'v{0:04d}'.format(method_version)
        self._parameters = parameters
        self._httpmethod = str(httpmethod).upper()

        # Set self._url
        self._encode_url()

    def _encode_url(self):
        """.. method:: _encode_url()

        Formats the URL for the call via the Steam Web API.

        :returns:  url
        """
        self._url = 'http://api.steampowered.com/{0}/{1}/{2}/?{3}'.format(
            self._interface,
            self._method,
            self._version,
            # urllib.urlencode(self._parameters)
            urlencode(self._parameters),
        )

    @property
    def interface(self):
        """.. attribute:: interface

        (str) The interface that is being called.

        Returns private variable interface."""
        return self._interface

    @property
    def method(self):
        """.. attribute:: method

        (str) The method that is being called.

        Returns private variable method.

        """
        return self._method

    @property
    def version(self):
        """.. attribute:: version

        (str) The version of the method (method_version).

        Returns private variable version.

        """
        return self._version

    @property
    def httpmethod(self):
        """.. attribute:: httpmethod

        (str) GET or POST.

        Returns private variable httpmethod.

        """
        return self._httpmethod

    @property
    def url(self):
        """.. attribute:: url

        (str) - The URL formatted for the query.

        Returns private variable url.

        """
        return self._url

    @property
    def parameters(self):
        """.. attribute:: parameters

        (str) - Returns private variable parameters (read-only).

        (dict) The parameters for the query.

        """
        return self._parameters

    @property
    def xml(self):
        """.. attribute:: xml

        Returns """
        return self.as_xml()

    @property
    def json(self):
        """.. attribute:: json"""
        return self.as_json()

    @property
    def vdf(self):
        """.. attribute:: vdf"""
        return self.as_vdf()

    def as_xml(self):
        """.. method:: as_xml()"""
        # We need to encode the URL again to prevent appending the format
        # multiple times.
        self._encode_url()
        self._url += '&format=xml'
        return self._execute_query()

    def as_json(self):
        """.. method:: as_json()"""
        # We need to encode the URL again to prevent appending the format
        # multiple times.
        self._encode_url()
        self._url += '&format=json'
        return self._execute_query()

    def as_vdf(self):
        """.. method:: as_vdf()"""
        # We need to encode the URL again to prevent appending the format
        # multiple times.
        self._encode_url()
        self._url += '&format=vdf'
        return self._execute_query()

    def _execute_query(self):
        # GET
        if self.httpmethod == 'GET':
            # return urllib2.urlopen(self._url)
            return requests_get(self._url)

        # POST
        # data = urllib.urlencode(self.parameters)
        data = urlencode(self.parameters)
        # req = urllib2.Request(self._url, data)
        # return urllib2.urlopen(req)
        return requests_post(self._url, data)
