# Web scrape, clean and analyse data about metal bands
General information about the project

## Web scraping metal_archives.com into a SQLite database
1. To create the SQLite database you have to run create_metal_db.py, a python script using the sqlite3 library. 
It will also create the table "band_info" in which later we commit the scraped data. It contains the following columns:

- band_id: an integer as the auto-incremented primary key
- band_name: the bands name, that do not have to be unique 
- url: the unique url to the band's site on metal_archives.com
- country_of_origin: the country the band was founded
- location: the city or region the band is located
- status: status of activity (activ, on hold, split up, changed name, unknown) 
- formed_in: year of founding
- genre: type of played metal style, can be more than one genre
- lyrical_themes: topic of lyrics, can be more than one theme
- current_label: the current music label the band is signed or unsigned/independent
- years_active: time ranges the band was activ, sometimes with additional information
- data_retrieved: the date the data set was retrieved from the given url

2. To scrape the data run web_scraping_metal_archives.py. To get a list of bands and their website url we have to use 
the Selenium library. It allows to open the websites in a browser which is necessary to run JavaScript. Only in this way
we get access to some needed data and are able to automate to load sites by click. To use Selenium in this script you 
need the Chrome browser and the fitting version of Chromdriver which controls the browser. To finally collect the data 
from the individual band websites it uses the Beautiful Soup library. For further information take a look at the
comments in the python scripts.

## Clean the web scraped data
The process of exploring an cleaning the data is described in the Jupiter notebook xxxx.