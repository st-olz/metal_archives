# What are the predominant genres and themes in metal music and where they are most popular
In this project we will web scrape, clean and analyse data about metal bands from all over the world. The goal is to 
answer the following questions:
- Which countries are the most metal bands from in total numbers and by population?
- What are the most popular sub-genres and lyrical themes?
- Are there differences in the questions above for bands that are independent or signed to a label?
- Are there differences in the questions above for bands from different world regions?

The data we use is web scraped from Encyclopaedia Metallum: The Metal Archives (https://www.metal-archives.com/) that is 
an online encyclopedia based upon musical artists who predominantly 
perform heavy metal music along with its various sub-genres. It attempts to provide comprehensive 
information on each band, such as a discography, logos, pictures, lyrics, line-ups, biography, trivia and user-submitted 
reviews. The site also provides a system for submitting bands to the archives. The website is free of advertisements and 
is run completely independently. 

The data about country population is sourced from https://www.cia.gov/the-world-factbook and stored as CSV file 
[worlds_popultion.csv](/worlds_popultion.csv).

To generate a geographic heat map with python library GeoPandas a shapefile was downloaded from 
https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-details/.

## Web scraping metal_archives.com into a SQLite database
1. To create the SQLite database run [create_metal_db.py](/create_metal_db.py), a python script using the **Sqlite3** library. 
It will also create the table "band_info" in which later the scraped data is committed. The table contains the following
columns:

- band_id: an integer as the auto-incremented primary key
- band_name: the bands name, that do not have to be unique 
- url: the unique URL to the band's site on metal_archives.com
- country_of_origin: the country the band was founded
- location: the city or region the band is located
- status: status of activity (activ, on hold, split up, changed name, unknown) 
- formed_in: year of founding
- genre: type of played metal style, can be more than one genre
- lyrical_themes: topic of lyrics, can be more than one theme
- current_label: the current music label the band is signed or unsigned/independent
- years_active: time ranges the band was activ, sometimes with additional information
- data_retrieved: the date the data set was retrieved from the given URL

2. To scrape the data run [web_scraping_metal_archives.py](/web_scraping_metal_archives.py). To get a list of bands and 
their websites URL it has to use 
the **Selenium** library. It allows to open the websites in a browser which is necessary to run JavaScript. Only in this way
we get access to some needed data and are able to automate to change sites by click. To use Selenium in this script you 
need the **Chrome browser** and the latest version of **Chromdriver** which controls the browser. To finally collect the data 
from the individual band websites the script uses the **Beautiful Soup** library. For further information take a look at the
comments in the python scripts. The data in the deposited database was retrieved between 15.12.2022 - 17.12.2022.

Additional to the highlighted libraries you also need: **String, Time, Request** and **Datetime** 

## Clean and analyse the web scraped data
The process of cleaning and analysing the data is described in Jupiter notebook [analyse_metal_archives.ipynb](/analyse_metal_archives.ipynb).

![Active metal bands per 100k inhabitants (World 2022)](https://user-images.githubusercontent.com/121058227/212565199-ec54b3ff-fdfc-4fc7-a336-858874f3d70e.PNG)
