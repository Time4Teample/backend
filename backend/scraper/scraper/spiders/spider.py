import scrapy


class BaseSpider(scrapy.Spider):
    name = "base"
    allowed_domains = ['sugang.seongnam.go.kr']

    def __init__(self, url=None, search_terms=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start_requests(self):
        page_index = 1
        list_url = f'https://sugang.seongnam.go.kr/ilms/learning/learningList.do?searchUseYn=Y&searchCondition=1&searchKeyword=&pageIndex={page_index}'


        yield scrapy.Request(list_url, self.parse)

    def parse(self, response):
        self.logger.info(f"Response received: {response.url}")
        for detail in response.xpath('//a[contains(@href, "javascript:;") and contains(@onclick, "false")]').getall():
            yield {
                'link': detail
            }
