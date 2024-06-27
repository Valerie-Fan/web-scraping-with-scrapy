import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ReiItem
from scrapy.loader import ItemLoader

class ProductsSpider(CrawlSpider):
    name = "products"
    allowed_domains = ["rei.com"]
    start_urls = ["https://www.rei.com/c/camping-and-hiking/f/scd-deals"]
    
    rules = (
            Rule(LinkExtractor(allow=(r"page=",))),
            Rule(LinkExtractor(allow=(r"product",)), callback="parse_item"),
            )

    def parse_item(self, response):
        l = ItemLoader(item=ReiItem(), response=response)
        l.add_css("title", "h1#product-page-title")
        l.add_css("price", "span#buy-box-product-price-compare")
        l.add_css("item_no", "span#product-item-number")
        l.add_css("rating", "h1#product-page-title::text")

        return l.load_item()

       
