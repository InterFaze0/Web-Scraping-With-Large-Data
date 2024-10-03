# CSS SELECTORS

next_page = response.css("a[title='Nächste Seite']::attr(href)").get()
all_cars  = response.css("a[class='inline-block font-bold md:font-normal overflow-ellipsis overflow-hidden !no-underline']")
car_link  = response.css("a[class='inline-block font-bold md:font-normal overflow-ellipsis overflow-hidden !no-underline']::attr(href)").get()


car_name     = response.css("span[class='whitespace-pre']::text").get()
inner_text   = response.css("p[class='mb-0']").get() 
phone_number = response.css("a[class = 'company-profile-telephone underline hover:text-gray-dark focus-visible:text-gray-dark']::text").get()
mail_adress  = response.css("a[class = 'company-profile-email underline hover:text-gray-dark focus-visible:text-gray-dark']::text").get()
site         = response.css("a[class = 'company-profile-website underline hover:text-gray-dark focus-visible:text-gray-dark']::text").get().strip()
inhaber      = response.css("span[class='block break-words hyphens-auto']::text").get()
