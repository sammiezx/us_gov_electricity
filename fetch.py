import requests

start_date = '2001-01'
end_date = '2023-01'
offset = 0
length = 5000

api_url = f"https://api.eia.gov/v2/electricity/retail-sales/data/?frequency=monthly&data[0]=customers&data[1]=price&data[2]=revenue&data[3]=sales&start={start_date}&end={end_date}&sort[0][column]=period&sort[0][direction]=desc&offset={offset}&length={length}"

response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse and work with the response data (assuming it's in JSON format)
    data = response.json()
    
    # Example: Print the data
    print(data)
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code} - {response.text}")