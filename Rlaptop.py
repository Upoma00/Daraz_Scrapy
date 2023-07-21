import scrapy


class RlaptopSpider(scrapy.Spider):
    name = "Rlaptop"
    start_urls = ["https://www.ryanscomputers.com/category/laptop-all-laptop?limit=100&osp=0"]

    def parse(self, response):
        for product in response.xpath('//div[@class="card-body text-center"]'):
            title = product.xpath('.//p[@class="card-text p-0 m-0 grid-view-text"]/a/text()').get()
            url = product.xpath('.//p[@class="card-text p-0 m-0 grid-view-text"]/a/@href').get()
            price = product.xpath('.//p[@class="pr-text cat-sp-text pb-1"]/text()').get()
            ram = product.xpath('.//li[contains(text(),"RAM")]/text()').get()
            storage = product.xpath('.//li[contains(text(),"Storage")]/text()').get()
            graphics = product.xpath('.//li[contains(text(),"Graphics Memory")]/text()').get()
            display_size = product.xpath('.//li[contains(text(),"Display Size")]/text()').get()
            generation = product.xpath('.//li[contains(text(),"Generation")]/text()').get()
            processor = product.xpath('.//li[contains(text(),"Processor")]/text()').get()
            discount = "not available"  # Set default value for discount

            yield {
                'title': title,
                'url': url,
                'price': price,
                'ram': ram,
                'storage': storage,
                'graphics': graphics,
                'display_size': display_size,
                'generation': generation,
                'processor': processor,
                'discount': discount
            }

        next_page = response.xpath('//a[@class=aria-label="Next »"]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            


