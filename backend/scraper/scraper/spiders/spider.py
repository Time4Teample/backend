import scrapy
from scraper.items import ScraperItem

class BaseSpider(scrapy.Spider):
    name = "base"
    allowed_domains = ['sugang.seongnam.go.kr']

    def __init__(self, url=None, search_terms=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start_requests(self):
        start_pagination = 1
        end_pagination = 15
        for page in range(start_pagination, end_pagination+1):
            page_url = f'https://sugang.seongnam.go.kr/ilms/learning/learningList.do?searchUseYn=Y&searchCondition=1&searchKeyword=&pageIndex={page}'
            yield scrapy.Request(page_url, self.parse)

    def parse(self, response):
        for detail in response.xpath('//a[contains(@href, "javascript:;") and contains(@onclick, "false")]').getall():
            title = response.xpath('//span[contains(@class, "tit")]')
            organization = response.xpath('//span[contains(@class, "org")]')
            status = response.xpath('//span[contains(@class, "s_btn")]')
            meta = { 'title': title, 'organization': organization, 'status': status }
            url = f"https://sugang.seongnam.go.kr/ilms/learning/learningDetail.do?learning_id={detail[52:54+15]}"
            yield scrapy.Request(url, callback=self.parse_detail, meta=meta)

    def parse_detail(self, response):
        self.logger.info(f"Response detail received: {response.url}")

        for detail in response.xpath('//div[contains(@class, "form_group")]//p/text()').getall():
            meta = response.meta
            yield ScraperItem(
                title=meta['title'],
                organization=meta['organization'],
                status=meta['status'],
                url=response.url,
                content=detail)