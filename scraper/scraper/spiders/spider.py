import re

import scrapy
from scrapy.utils.url import canonicalize_url, add_http_if_no_scheme
from scrapy.linkextractors import LinkExtractor


class BaseSpider(scrapy.Spider):
    name = 'base'

    def __init__(self, url, search_terms=None, *args, **kwargs):
        if url.startswith('.'):
            with open(url) as f:
                urls = [line.strip() for line in f]
        else:
            urls = [url]
        self.start_urls = [add_http_if_no_scheme(_url) for _url in urls]
        self.search_terms = search_terms
        self._extra_search_terms = None
        self._reset_link_extractors()
        self.images_link_extractor = LinkExtractor(
            tags=['img'], attrs=['src'], deny_extensions=[])
        self.state = {}
        super().__init__(*args, **kwargs)

    def parse(self, response):
        self.logger.info(f"Response received: {response.url}")

    def _looks_like_url(txt):
        """
            Return True if text looks like an URL (probably relative).
            >>> _looks_like_url("foo.bar")
            False
            >>> _looks_like_url("http://example.com")
            True
            >>> _looks_like_url("/page2")
            True
            >>> _looks_like_url("index.html")
            True
            >>> _looks_like_url("foo?page=1")
            True
            >>> _looks_like_url("x='what?'")
            False
            >>> _looks_like_url("visit this page?")
            False
            >>> _looks_like_url("?")
            False
        """
        if " " in txt or "\n" in txt:
            return False
        if "/" in txt:
            return True
        if re.search(r'\?\w+=.+', txt):
            return True
        if re.match(r"\w+\.html", txt):
            return True
        return False
