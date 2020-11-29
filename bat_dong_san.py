import scrapy
class bat_dong_san(scrapy.Spider):
    name = 'bat_dong_san'
    start_urls = ['https://trangvangvietnam.com/categories/486649/bat-dong-san.html']

    def parse(self,response):
        number_page = response.xpath('//*[@id="paging"]/a[last()-1]/text()').get()

        for i in range(1,int(number_page)+1):
            yield scrapy.Request(
                url=self.start_urls[0] + "?page=" + str(i),
                callback=self.parse_page
            )
    def parse_page(self,response):
        urls = response.xpath('.//h2[@class="company_name"]//a/@href').extract()
        for url in urls:
            yield scrapy.Request(
                url=url,
                callback = self.parse_detail
            )

    def parse_detail(self,response):
        name = response.xpath('//div[@class="tencongty"]/h1/text()').get()
        email = response.xpath('//div[@class="text_email"]/p/a/text()').get()
        website = response.xpath('//div[@class="text_website"]/p/a/text()').get()
        address = response.xpath('//div[@class="diachi_chitiet_li2dc"]/p/text()').get()
        phone = response.xpath('//div[@class="diachi_chitiet_li2"]/span/text()').get()
        thitruong = response.xpath('//div[@class="thitruong_loaidn_text"]/p/text()').get()
        loaihinh = response.xpath('//*[@id="listing_basic_info"]/div[5]/div[2]/div[2]/p/text()').get()

        yield {
            "name": name,
            "email": email,
            "website": website,
            "address": address,
            "phone": phone,
            "thitruong": thitruong,
            "loaihinh": loaihinh
        }