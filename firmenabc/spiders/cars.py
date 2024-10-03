#from bs4 import BeautifulSoup
import scrapy


class CarsSpider(scrapy.Spider):
    name = "cars"
    allowed_domains = ["firmenabc.at"]
    start_urls = ["https://www.firmenabc.at/suche/ergebnisse?tx_indexedsearch_pi2%5Baction%5D=search&tx_indexedsearch_pi2%5Bsearch%5D%5Bsword%5D=Auto&tx_indexedsearch_pi2%5Bsearch%5D%5BwhatId%5D=&tx_indexedsearch_pi2%5Bsearch%5D%5BwhatIndustry%5D=&tx_indexedsearch_pi2%5Bsearch%5D%5Bwhere%5D=&tx_indexedsearch_pi2%5Bsearch%5D%5BwhereId%5D=0&tx_indexedsearch_pi2%5Bsearch%5D%5BwhereRegion%5D=0&cHash=283e517fd637e40c14e42b2fbf09e42c"]

    def parse(self, response):
        for i in response.css("h3[class = 'flex h5 mb-0 overflow-hidden'] a::attr(href)"):
            yield response.follow(i.get(),callback = self.parse_detail)

        
        next_page = response.css("a[title='Nächste Seite']::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page,callback = self.parse)
        
    
    def parse_detail(self,response):
        company_name = response.css("span[class='whitespace-pre']::text").get()
        inner_text   = response.css("p[class='mb-0']").get()[response.css("p[class='mb-0']").get().find("<br>") + 4:response.css("p[class='mb-0']").get().find("<br>") + 8] 
        phone_number = response.css("a[class = 'company-profile-telephone underline hover:text-gray-dark focus-visible:text-gray-dark']::text").get()
        mail_adress  = response.css("a[class = 'company-profile-email underline hover:text-gray-dark focus-visible:text-gray-dark']::text").get()
        try:
            site = response.css("a[class = 'company-profile-website underline hover:text-gray-dark focus-visible:text-gray-dark']::text").get().strip()
        except:
            site = None
        try:
            #soup = BeautifulSoup(response.css("div[class='max-w-[860px] grid grid-cols-7 gap-x-2.5 lg:gap-y-2.5 mb-16 pt-5 md:pt-0 [&_a]:underline']").get(),'lxml')
            #soup.body.findAll('Geschäftsführer')
            inhaber = response.css("span[class='-ml-4 break-words hyphens-auto underline group-hover:text-gray-dark group-focus-visible:text-gray-dark']::text").get()
        except:
            inhaber = response.css("span[class='block break-words hyphens-auto']::text").get()
        
        if site is not None:
            site = site.replace("www.","")
            site = site.replace("http://","")
            site = site.replace("https://","")


        if (site and inhaber) is not None:
            yield {
                "1. Owner's Name ('Geschäftsführer' or 'Inhaber')": inhaber,
                '2. Website': site,
                '3. E-Mail': mail_adress,
                '4. Telefon Number': phone_number,
                '5. Post Code': inner_text,
                '6. Business Name': company_name,
                '7. Link': response.request.url
            }
       







