from get_name import random_name, random_surname, random_name_and_surname, random_language
from get_city import get_random_city
import random, csv
from time import sleep
from send_request import send_request
from phone import generate_random_phone

while True:
    id,commune_name,commune_name_ascii,daira_name,daira_name_ascii,wilaya_code,wilaya_name,wilaya_name_ascii = get_random_city()
    name, surename = random_name_and_surname(random_language())
    province = f'{wilaya_code}.+{wilaya_name_ascii.upper()}'
    payload = f"firstname={name}&phone={generate_random_phone()}&chippingprovince={province}&chippingcity={commune_name_ascii.upper()}&quantity=1&discount=&delivery_fees=350.00&variant_id=0"
    url = 'https://leadform.braquets.dev/orders/add/316562-f4.myshopify.com/9564246671662'

    response = send_request(url, payload)   
    # save response in csv
    with open('response.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([id,commune_name,commune_name_ascii,daira_name,daira_name_ascii,wilaya_code,wilaya_name,wilaya_name_ascii,name,surename,payload,response.text])

    # sleep random time between 0 seconds and 10 seconds
    sleep(random.randint(0, 10))