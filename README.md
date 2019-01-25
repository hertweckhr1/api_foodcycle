# api_foodcycle
Food-Cycle API Django Rest Framework

Supports Mobile App Idea inspired to connect supermarkets, restaurants, and farms with foodbanks and nonprofit organizations city-wide.

[Deployed Link](http://104.199.122.67:8000/api/user/donee-info/)

## Motivation 
40% of foodwaste worldwide is produced in the US

40% of foodwaste in US is at the levels of retailers and restaurants. 

## Setup 
- install docker

**To Run**
- docker-compose up 

**To Stop**
- docker-compose down

## Endpoints 
**Users**

Create User:

- ```/api/user/create/```

Get Token:

- ```/api/user/token/```

View User Info:

- ```/api/user/me/```

View all user info:

- ```/api/user/donee-info/```

**Donations**

View all Donations:

- ```/api/donation/donations```

To edit, delete, view donation detail:

- ```/api/donation/donations/{donation_number}```

## React-Native Front End Reference 
Uses a backend API using Django with Postgresql database. 
Link to to API:
- [Github](https://github.com/hertweckhr1/FoodCycle_Expo)
