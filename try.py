import trio
import asks  # An asynchronous HTTP library compatible with trio

async def main():
    # Define the URL of the local API endpoint
    url = 'http://127.0.0.1:8000/add'

    #Define the user data you want to insert
    # user_data = {
    #     "email": "marktristanfabellar.pro@gmail.com",
    #     "password": ""
    # }

    items_data = {
            "money_spent": 43242,
            "category": "food",
            "user_id": "",
            "access_token": ""
        }   

    # Make a POST request to the API to create a new user
    async with trio.open_nursery() as nursery:
        response = await asks.post(url, json=items_data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the response data
            data = response.json()
            print("DONE")

            print(data)
           # print(data[1])
        else:
            # Handle the error if the request was not successful
            print('Error:', response.status_code)

# Run the trio event loop with main function
trio.run(main)

# pip install trio
# pip install asks
# pip install anyio==4.2.0