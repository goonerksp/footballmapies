#pip install requests-html
#pip install gmplot
#pip install bs4

#install these modules by using the pip command in the terminal
import requests

from bs4 import BeautifulSoup

import gmplot

latlist = [] #a list to hold latitudes
longlist = [] #a list to hold longitudes


count = input("Enter the country in top 5 leagues you want the succesful clubs' location for ")

if count.lower() == "england" or count.lower() == 'e':
    for i in range(4):
        if i == 0:
            print("1. Manchester United FC")
            url = 'https://www.findlatitudeandlongitude.com/l/old+trafford'

            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            lat = soup.find_all('span', class_ = 'value green')[0].get_text() #finds the latitude coordinate in the site, and gets the text


            lon = soup.find(id = 'lon_address').get_text()
            
            # lon gets longitude value, I used id here because both latitude and longitude have the same span name and and class name.

            lon1 = lon.replace('Longitude:','') #I got Longitude: (value), annoying I know, but as the fields are same for both 
            # latitude and longitude I HAD to use id and it came with this Longitude.

            latlist.append(float(lat)) #appends the latitude's float value, as get_text() gets string.

            longlist.append(float(lon1)) #same as the latitude one.

        elif i == 1:

            #Same routine, different URL.

            print("2. Liverpool FC")

            url = 'https://www.findlatitudeandlongitude.com/l/anfield'

            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            lat = soup.find_all('span', class_ = 'value green')[0].get_text()


            lon = soup.find(id = 'lon_address').get_text()

            lon1 = lon.replace('Longitude:','')

            latlist.append(float(lat))

            longlist.append(float(lon1))


        elif i == 2:
            print("3. Arsenal FC")

            url = 'https://www.findlatitudeandlongitude.com/l/emirates+stadium'

            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            lat = soup.find_all('span', class_ = 'value green')[0].get_text()

            lon = soup.find(id = 'lon_address').get_text()

            lon1 = lon.replace('Longitude:','')

            latlist.append(float(lat))

            longlist.append(float(lon1))

        elif i == 3:
            print("4. Chelsea FC")

            url = 'https://www.findlatitudeandlongitude.com/l/stamford+bridge'

            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            lat = soup.find_all('span', class_ = 'value green')[0].get_text()

            lon = soup.find(id = 'lon_address').get_text()

            lon1 = lon.replace('Longitude:','')

            latlist.append(float(lat))

            longlist.append(float(lon1))

            print("The coordinates of the most successful English Clubs' stadiums are given by: ")

            print("Latitudes : ")
            print(latlist)

            print("Longitudes : ")
            print(longlist)

    gmap = gmplot.GoogleMapPlotter(51.509865, -0.118092, 5) #Gives the base location, basically the location of the capital, here, london

elif count.lower() == "spain" or count.lower() == 's' or count.lower() == 'espana':
    #Same routine as in 'england'
    for i in range(4):
        if i == 0:
            
            print("1. Futbol Club Barcelona")
            url = 'https://www.findlatitudeandlongitude.com/l/camp+nou'

            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            lat = soup.find_all('span', class_ = 'value green')[0].get_text()


            lon = soup.find(id = 'lon_address').get_text()

            lon1 = lon.replace('Longitude:','')

            latlist.append(float(lat))

            longlist.append(float(lon1))

        elif i == 1:
            print("2. Real Madrid Club Futbol")

            url = 'https://www.findlatitudeandlongitude.com/l/santiago+bernabeu'

            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            lat = soup.find_all('span', class_ = 'value green')[0].get_text()

            lon = soup.find(id = 'lon_address').get_text()

            lon1 = lon.replace('Longitude:','')

            latlist.append(float(lat))

            longlist.append(float(lon1))



        elif i == 2:
            print("3. Athletic Club de Bilbao")

            url = "https://www.findlatitudeandlongitude.com/?lat=43.264183&lon=-2.949421"

            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            lat = soup.find_all('span', class_ = 'value green')[0].get_text()

            lon = soup.find(id = 'lon_address').get_text()

            lon1 = lon.replace('Longitude:','')

            latlist.append(float(lat))

            longlist.append(float(lon1))

        elif i == 3:
            print("4. Atletico de Madrid")

            url = "https://www.findlatitudeandlongitude.com/?lat=40.43628&lon=-3.599548"

            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            lat = soup.find_all('span', class_ = 'value green')[0].get_text()



            lon = soup.find(id = 'lon_address').get_text()

            lon1 = lon.replace('Longitude:','')

            latlist.append(float(lat))

            longlist.append(float(lon1))

            print("The coordinates of the most successful Spanish Clubs' stadiums are given by: ")

            print("Latitudes : ")
            print(latlist)

            print("Longitudes : ")
            print(longlist)

    gmap = gmplot.GoogleMapPlotter(40.4168, -3.7038, 5) #Base location set to Madrid

elif count.lower() == "italy" or count.lower() == 'i' or count.lower() == 'italia':
    for i in range(3):
        if i == 0:
            
            print("1. Juventus")
            url = 'https://www.findlatitudeandlongitude.com/l/Allianz+stadium'

            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            lat = soup.find_all('span', class_ = 'value green')[0].get_text()


            lon = soup.find(id = 'lon_address').get_text()

            lon1 = lon.replace('Longitude:','')

            latlist.append(float(lat))

            longlist.append(float(lon1))


        elif i == 1:
            print("2. AC Milan")

            url = 'https://www.findlatitudeandlongitude.com/l/san+siro'

            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            lat = soup.find_all('span', class_ = 'value green')[0].get_text()


            lon = soup.find(id = 'lon_address').get_text()

            lon1 = lon.replace('Longitude:','')

            latlist.append(float(lat))

            longlist.append(float(lon1))


        elif i == 2:
            print("3. Internazionale Milano")

            url = 'https://www.findlatitudeandlongitude.com/l/san+siro'

            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            lat = soup.find_all('span', class_ = 'value green')[0].get_text()


            lon = soup.find(id = 'lon_address').get_text()

            lon1 = lon.replace('Longitude:','')

            latlist.append(float(lat))

            longlist.append(float(lon1))

            print("The coordinates of the most successful Italian Clubs' stadiums are given by: ")

            print("Latitudes : ")
            print(latlist)

            print("Longitudes : ")
            print(longlist)


    gmap = gmplot.GoogleMapPlotter( 41.902782, 12.496366, 5) #Base location set to Rome

elif count.lower() == "germany" or count.lower() == 'g' or count.lower() == 'deutschland':
    for i in range(3):
        if i == 0:
            
            print("1. Bayern Munich")
            url = 'https://www.findlatitudeandlongitude.com/l/allianz+arena'

            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            lat = soup.find_all('span', class_ = 'value green')[0].get_text()


            lon = soup.find(id = 'lon_address').get_text()

            lon1 = lon.replace('Longitude:','')

            latlist.append(float(lat))

            longlist.append(float(lon1))

        elif i == 1:
            print("2. Borussia Dortmund")

            url = 'https://www.findlatitudeandlongitude.com/l/signal+iduna+park'

            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            lat = soup.find_all('span', class_ = 'value green')[0].get_text()


            lon = soup.find(id = 'lon_address').get_text()

            lon1 = lon.replace('Longitude:','')

            latlist.append(float(lat))

            longlist.append(float(lon1))


        elif i == 2:
            print("3. Schalke 04")

            url = "https://www.findlatitudeandlongitude.com/l/VELTINS-Arena,-1,-Rudi-Assauer-Platz,-Erle-Berger-Feld,-Erle,-Gelsenkirchen-Ost,-Gelsenkirchen,-North-Rhine-Westphalia,-45891,-Germany/7507645/"

            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            lat = soup.find_all('span', class_ = 'value green')[0].get_text()


            lon = soup.find(id = 'lon_address').get_text()

            lon1 = lon.replace('Longitude:','')

            latlist.append(float(lat))

            longlist.append(float(lon1))

            print("The coordinates of the most successful German Clubs' stadiums are given by: ")

            print("Latitudes : ")
            print(latlist)

            print("Longitudes : ")
            print(longlist)

    gmap = gmplot.GoogleMapPlotter( 52.5200, 13.4050, 5)

elif count.lower() == "france" or count.lower() == 'f':
    for i in range(2):
        if i == 0:
            
            print("1. Paris Saint-Germain")
            url = 'https://www.findlatitudeandlongitude.com/l/parc+des+princes'

            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            lat = soup.find_all('span', class_ = 'value green')[0].get_text()


            lon = soup.find(id = 'lon_address').get_text()

            lon1 = lon.replace('Longitude:','')

            latlist.append(float(lat))

            longlist.append(float(lon1))

        elif i == 1:
            print("2. Olympique de Marseille")

            url = 'https://www.findlatitudeandlongitude.com/?lat=43.2698156&lon=5.3959373'

            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            lat = soup.find_all('span', class_ = 'value green')[0].get_text()


            lon = soup.find(id = 'lon_address').get_text()

            lon1 = lon.replace('Longitude:','')

            latlist.append(float(lat))

            longlist.append(float(lon1))

            print("The coordinates of the most successful French Clubs' stadiums are given by: ")

            print("Latitudes : ")
            print(latlist)

            print("Longitudes : ")
            print(longlist)



    gmap = gmplot.GoogleMapPlotter( 48.8566, 2.3522, 5) #Base location set to Paris


gmap.scatter(latlist, longlist, '#FF0000', size = 40, marker = False) #Marker = False cause I don't want pins dropping on the scattered points

gmap.polygon(latlist, longlist, color = 'cornflowerblue') #Creating a polygon made from the different points on the map

mapname = input("Enter the .html file in which in which you'd like to save ")
gmap.draw( "C:\\Users\\srira\\desktop\\"+mapname) #Creating the html file, to store the map in

