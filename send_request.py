import requests

def send_request(url, payload):
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://316562-f4.myshopify.com',
        'priority': 'u=1, i',
        'referer': 'https://316562-f4.myshopify.com/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
    }
    
    # If payload is a dictionary, convert it to a URL-encoded string
    if isinstance(payload, dict):
        payload = '&'.join(f'{key}={value}' for key, value in payload.items())
    
    # Ensure payload is encoded in UTF-8
    payload = payload.encode('utf-8')
    
    try:
        response = requests.post(url, headers=headers, data=payload)
        response.encoding = 'utf-8'  # Explicitly set the encoding
        print(response.text)
        return response
    except requests.RequestException as e:
        print(f"An error occurred: {e}")