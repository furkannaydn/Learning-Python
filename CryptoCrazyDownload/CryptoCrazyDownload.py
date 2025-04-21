import requests




def get_crypto_data():
   
 response=requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json", allow_redirects=True)
 if response.status_code == 200:
    return response.json()
 


crypto_response = get_crypto_data()
user_input = input("Enter the name of the cryptocurrency: ").lower()

for crypto in crypto_response:
    if crypto['currency'].lower() == user_input:
        print(crypto['price'])
        break
