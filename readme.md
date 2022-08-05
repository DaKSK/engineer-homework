This project was created using Python 3.10.4
To store the data I used Oracle Instant Client and the Oracle Python package cx_Oracle
I created a free tier Oracle Cloud database and connected to it using the wallet
I used dotenv to store the credentials and load them into the environment

I knew of a public stocks API www.alphavantage.co for which I got a API key so I used that to get the AAPL stock data

I used the cx_Oracle package and SQL strings. Once I had the connection set up, it was relatively straight forward to add the data to the database
I interpreted the worst and best stock day as being the highest and the lowest stock close price

To create the plot I used the basic matplotlib.

Part 2 wasn't as familiar of a subject. Additonal challenges were presented by the fact my local machine is a windows based system.

The main problem seemed to be how to set up the app_server and db_server in a local environment, while still having the possibility to connect to them from Ansible through WSL. Additionally I was considering how to send my work for review. These considerartion led me towards Docker, which in threory seemed to be the best solution.

I went ahead and defined the Dockerfile for all the containers separetly and then wrote the Docker Compose file. I was able to run all the containers in parallel but the app_server and ansible containers were not able to connect to each other. This became my undoing. While I was aware that I'd need to map the ports and have SSH running on the app_server container, I was not able to get it to work. I kept getting the following error:
Connection refused
My last moment effort went on trying to recreate the setup on VirtualBox. The plan was to try using WSL with VirtualBox, so I loaded in the Ubuntu Server image and created the app_server and db_server machines. I then mapped the ports and tried to SSH from the WSL terminal to the VirtualBox machines. Initially the SSH connection was not working, kept timing out. Finally after a few hours of trying, I finally got the same error:
Connection refused
By that time it was Thursday midnight, I was out of ideas and tired.