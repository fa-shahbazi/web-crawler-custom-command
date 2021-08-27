import requests
from bs4 import BeautifulSoup


def crawl_product(url, page_number_limit):

    data = []
    page_number = 1
    crawl = True
    while crawl:
        response = requests.get(url.format(page_number=page_number))
        crawl = response.ok

        soup = BeautifulSoup(response.text, features='html.parser')

        names = soup.select(
            '#inspire > div > div:nth-child(2) > div.lg\:tw-bg-gray-100 > div > div > main > div.tw-grid.tw-grid-cols-1.tw-mt-4.tw-gap-y-3.sm\:tw-grid-cols-2.sm\:tw-gap-3.lg\:tw-gap-4.lg\:tw-grid-cols-3.xl\:tw-grid-cols-4 > a > section > div > h4 > span'
        )

        prices = soup.select(
            '#inspire > div > div:nth-child(2) > div.lg\:tw-bg-gray-100 > div > div > main > div.tw-grid.tw-grid-cols-1.tw-mt-4.tw-gap-y-3.sm\:tw-grid-cols-2.sm\:tw-gap-3.lg\:tw-gap-4.lg\:tw-grid-cols-3.xl\:tw-grid-cols-4 > a > section > div > div > div.tw-flex.tw-flex-row.tw-justify-end.tw-items-end.tw-mt-2.lg\:tw-mt-4.lg\:tw-pt-4.tw-space-x-reverse.tw-space-x-2.lg\:tw-min-h-\[5\.0625rem\] > div.tw-flex.tw-flex-col.tw-items-center.tw-justify-center > span.tw-flex.tw-items-center.tw-text-sm.lg\:tw-text-xl.lg\:tw-order-2.tw-font-bold > span'
        )
        if prices:
            pass
        else:
            prices = soup.select(
                '#inspire > div > div:nth-child(2) > div.lg\:tw-bg-gray-100 > div > div > main > div.tw-grid.tw-grid-cols-1.tw-mt-4.tw-gap-y-3.sm\:tw-grid-cols-2.sm\:tw-gap-3.lg\:tw-gap-4.lg\:tw-grid-cols-3.xl\:tw-grid-cols-4 > a > section > div > div > div.tw-flex.tw-flex-row.tw-justify-end.tw-items-end.tw-mt-2.lg\:tw-mt-4.lg\:tw-pt-4.tw-space-x-reverse.tw-space-x-2.lg\:tw-min-h-\[5\.0625rem\] > div > div'

            )

        discount_prices = soup.select(
            '#inspire > div > div:nth-child(2) > div.lg\:tw-bg-gray-100 > div > div > main > div.tw-grid.tw-grid-cols-1.tw-mt-4.tw-gap-y-3.sm\:tw-grid-cols-2.sm\:tw-gap-3.lg\:tw-gap-4.lg\:tw-grid-cols-3.xl\:tw-grid-cols-4 > a > section > div > div > div.tw-flex.tw-flex-row.tw-justify-end.tw-items-end.tw-mt-2.lg\:tw-mt-4.lg\:tw-pt-4.tw-space-x-reverse.tw-space-x-2.lg\:tw-min-h-\[5\.0625rem\] > div.tw-flex.tw-flex-col.tw-items-center.tw-justify-between > span.tw-flex.tw-items-center.tw-text-sm.lg\:tw-text-xl.lg\:tw-order-2.tw-font-bold > span'
        )

        all_prices = [*prices, *discount_prices]

        for name, price in zip(names, all_prices):
            data.append({
                'name': name.text.strip(),
                'price': price.text.strip()

            })

        page_number += 1
        if page_number > page_number_limit:
            crawl = False

    print(data)

mobile_phone = crawl_product("https://www.mobit.ir/search/digital-devices/mobile/mobilephone?sort=-view&page={page_number}",7)
cable = crawl_product ("https://www.mobit.ir/search/digital-devices/mobile/mobile-accessories/cable-converter?sort=-view&page={page_number}",7)
cover = crawl_product("https://www.mobit.ir/search/digital-devices/mobile/mobile-accessories/phone-case-and-cover?sort=-view&page={page_number}",7)
headphones = crawl_product("https://www.mobit.ir/search/digital-devices/mobile/mobile-accessories/headphones-headset-handsfree?sort=-view&page={page_number}",7)
screen_protector = crawl_product("https://www.mobit.ir/search/digital-devices/mobile/mobile-accessories/screen-protector?sort=-view&page={page_number}",7)
computer_eqipment = crawl_product("https://www.mobit.ir/search/digital-devices/computer-equipments&page={page_number}" ,7)
audiovisiual = crawl_product("https://www.mobit.ir/search/digital-devices/audiovisual-equipment/audio-video-accessories?sort=-view&page={page_number}",7)
powerbank = crawl_product("https://www.mobit.ir/search/digital-devices/mobile/mobile-accessories/powerbank?sort=-view&page={page_number}" ,7)
smartwatch = crawl_product("https://www.mobit.ir/search/digital-devices/smart-watch-wristband/smart-watch?sort=-view&page={page_number}" ,7)
game_console = crawl_product("https://www.mobit.ir/search/digital-devices/game-console&page={page_number}" ,7)
xiaomi_accessories = crawl_product("https://www.mobit.ir/search/digital-devices/xiaomi-accessories?sort=-view&page={page_number}" ,7)