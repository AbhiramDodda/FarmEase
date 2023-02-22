# FarmEase

### Ststus: Developing

### A project to bring farmers onto an integrated platform 

### Motive

Lack of necessary nutrients and care that has to be taken apart from what we were doing. But the nutrient levels in soil cannot be measured by us and there were no services to come home to test soil. This problem is just faced by those maintaining home gardens and large scale farmers. In many cases lack of proper care does not lead to fail of crop but reduction in yield. So the web app is created to make the soil test bookings easy.

### Technologies used:
1. DJango framework
2. Python 
3. HTML
4. CSS
5. <a href="https://openweathermap.org/api">OpenWeather API</a>

## Farmer side

1. index page asks for login or register.
2. If registering then details are to be filled and username of farmer is generated using firstname, mobile number and lastname rather than asking farmer to choose one.
3. If login the user is expected to give username generated and password.
4. Login or registering takes user(farmer) to home page where his/her username is displayed.
5. In the homepage of every farmer they are able to access SoilCare(soil test booking), Shop(fertilizers, seeds, tools etc) and FromFarm(seller registration) services.
6. Farmer is not registered as a seller by default and left to their decision. 
7. Weather is displayed on the homepage of farmers. Weather is obtaines through OpenWeather API.

### Soil Care

Under soil care when farmer goes to the SoilCare platform all the available soil test laboratories(registered from laboratories side) are displayed along with the IDs and location details the farmer is asked to enter labId and farmerId to book the test and once booked farmers are able to see all the tests they booked. 

#### Farmer Databses 
There are two tables to store Farmer data. One table stores the farmer credentials and the other stores the seller data if farmer registers as a seller.

### Laboratory side

1. Admin of a laboratory can register themselves to provide their services.
2. From the homepage they can access the list of their bookings and also a link to shop to get necessary chemicals and apparatus.

### FromFarm

In FromFarm any buyer can visit the page and can look for the products along with the farmer contact details. The direct contact with farmers is provided so as to eliminate mediation which is a major cause for price increment and production fluctuations.
