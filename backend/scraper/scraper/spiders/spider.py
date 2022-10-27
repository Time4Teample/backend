import scrapy


class BaseSpider(scrapy.Spider):
    name = "base"
    allowed_domains = ['sugang.seongnam.go.kr']

    def __init__(self, url=None, search_terms=None, *args, **kwargs):
        # if url.startswith('.'):
        #     with open(url) as f:
        #         urls = [line.strip() for line in f]
        # else:
        #     urls = [url]
        # self.start_urls = [add_http_if_no_scheme(_url) for _url in urls]
        # self.search_terms = search_terms
        # self._extra_search_terms = None
        # self._reset_link_extractors()
        # self.images_link_extractor = LinkExtractor(
        #     tags=['img'], attrs=['src'], deny_extensions=[])
        # self.state = {}
        super().__init__(*args, **kwargs)

    def start_requests(self):
        page_index = 1
        list_url = f'https://sugang.seongnam.go.kr/ilms/learning/learningList.do'


        yield scrapy.Request(list_url, self.parse)

    def parse(self, response):
        self.logger.info(f"Response received: {response.url}")
        with open("result.html", 'w') as f:
            f.write(response.text)
            f.close()


        for detail in response.xpath('//a[contains(@href, "javascript:;")]').getall():
            yield {
                'link': detail
            }

    def __init__(self, *args, **kwargs):
        # self.start_url = "https://learning.seongnam.go.kr/index.do?"
        self.start_url = "https://sugang.seongnam.go.kr/ilms/learning/learningList.do?"
        super().__init__(*args, **kwargs)

    def start_requests(self):
        url = self.start_url
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        self.logger.info(f"Response received: {response.text}")
        content = response.css("tr").getall()
        self.logger.info(f"{content}")

    def create_query_strings(
        self,
        search_condition: int,
        office_area_gu: str,
        office_area_dong: str,
        page_index: int = 0,
        search_uses_yn: str = 'Y'
    ):
        return f"?searchUsesYn={search_uses_yn}&searchCondition={search_condition}&pageIndex={page_index}&office_area_gu={office_area_gu}&office_area_dong={office_area_dong}"