import trio
import asks  # An asynchronous HTTP library compatible with trio

async def main():
    # Define the URL of the local API endpoint
    url = 'http://127.0.0.1:8000/add'

    #Define the user data you want to insert
    # user_data = {
    #     "email": "marktristanfabellar.pro@gmail.com",
    #     "password": "123456789"
    # }

    items_data = {
            "money_spent": 43242,
            "category": "aa",
            "user_id": "d12f8f27-88e3-4fc4-bc15-09891ee53861",
            "access_token": "eyJhbGciOiJIUzI1NiIsImtpZCI6ImFjcWVjaWZGMHc1OEd0WmUiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzA3ODk5ODgzLCJpYXQiOjE3MDc4OTYyODMsImlzcyI6Imh0dHBzOi8vZ3h5bHRsdnFzZnh5Y3N4bWpwd2Yuc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6ImQxMmY4ZjI3LTg4ZTMtNGZjNC1iYzE1LTA5ODkxZWU1Mzg2MSIsImVtYWlsIjoibWFya3RyaXN0YW5mYWJlbGxhci5wcm9AZ21haWwuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJlbWFpbCIsInByb3ZpZGVycyI6WyJlbWFpbCJdfSwidXNlcl9tZXRhZGF0YSI6e30sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoicGFzc3dvcmQiLCJ0aW1lc3RhbXAiOjE3MDc4OTU5OTh9XSwic2Vzc2lvbl9pZCI6ImY3NjQzZDU5LTJhZWQtNDMzMy1hOWI1LWNlZmI0Yzc3YmI5MiJ9.XGae-4j88sSSqi35Xoo8DjUSrdLu-mwilUuekuCJgeI",
            "refresh_token": "KCskfhnplPi3B26sFR7rSQ"
        }   

    # Make a POST request to the API to create a new user
    async with trio.open_nursery() as nursery:
        response = await asks.post(url, json=items_data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the response data
            data = response.json()
            print(data)

        else:
            # Handle the error if the request was not successful
            print('Error:', response.status_code)

# Run the trio event loop with main function
trio.run(main)

# pip install trio
# pip install asks
# pip install anyio==4.2.0