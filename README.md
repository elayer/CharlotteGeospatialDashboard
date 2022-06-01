## City of Charlotte Geospatial Dashboard Project - Overview:

* Collected 3 areas of data tracked by the City of Charlotte found on the city's website (Serious Traffic Accidents, Police Incidents, 311 Call Requests.

* Cleaned and processed the data when ncessary, such as creating date columns or filtering out locations outside of Charlotte, North Carolina.

* Created a StreamLit application to consolidate all geospatial maps into one dashboard.

NOTE: The data used is too large to upload to GitHub (which I may not have permission to reupload). You may access the original datasets by following this link and searching for the data:
https://data.charlottenc.gov/

In addition, you will have to create a mapbox account as well as generate an access token in order to utilize making geospatial maps together with plotly. A link to mapbox's website is also provided below.


## Code and Resources Used:

**Python Version:** 3.8.5

**Packages:** numpy, pandas, matplotlib, seaborn, plotly, mapbox

## References:

* Documentation and guide on how to create geospatial maps using coordinates with plotly and mapbox:
https://plotly.com/python/scattermapbox/#mapbox-access-token-and-base-map-configuration

* Mapbox homepage where an account must be creatd as well as an access token:
https://www.mapbox.com/


## Data Collection:

The data used for this project comes from the City of Charlotte's open data portal I have linked above.


## Data Cleaning

After collecting the data, I made a few changes to the data where necessary, particularly with the date format in the Serious Traffic Accidents dataset.

In the Police Incidents dataset, there seemed to be some data entry errors with a few records where the year was 0200. I decided to keep only records coming after January 1st, 2000 which still held the large majority of the data. I also filtered out records not in the state of North Carolina.

In addition, there were records in the 311 Call Requests dataset that were not in Charlotte, NC. I removed these records from the dataset and created a new csv file.

* If you wish to follow the same dashboard construction, you can download the data from Charlotte's data portal and follow these cleaning steps.



## EDA
I conducted a little EDA to help with engaging the data in what to look for and found a few things.

Within the police incidente notebook, there were a few police divisions with more incidents reported than others. In addition, there were some addresses in the 311 Requests data that shined through with having a fair amount of records over other addresses. 

Below are pictures depicting these findings.


![alt text](https://github.com/elayer/CharlotteGeospatialDashboard/blob/main/st_commoncmpddivision.png "CMPD Divisions")
![alt text](https://github.com/elayer/CharlotteGeospatialDashboard/blob/main/st_commonlocs.png "Common 311 Locations")

With the 311 Requests data being so dense, I found that the large majority of records belonged to the Solid Waster Services department as well as the Non-Recyclable Items request type.

## StreamLit Dashboard Application
Once all cleaning tasks were completed, I moved into constructing a handy dashboard using Streamlit. Below are a few pictures showing the interface:

![alt text](https://github.com/elayer/CharlotteGeospatialDashboard/blob/main/st_top.png "StreamLit Top Page")
![alt text](https://github.com/elayer/CharlotteGeospatialDashboard/blob/main/st_trafficincidents.png "Serious Traffic Accidents")
![alt text](https://github.com/elayer/CharlotteGeospatialDashboard/blob/main/st_police.png "CMPD Incidents")
![alt text](https://github.com/elayer/CharlotteGeospatialDashboard/blob/main/st_311.png "311 Requests")

## Future Improvements
If it were possible, I could incorporate a way to ingest data into the application in real-time. This way, one wouldn't have to constantly import new data, and the dashboard would be readily available to analyze.

Some graphs could become very dense depending on the fields used. Therefore, I included default values to use once the app is launched. It would perhaps become more personalized for those who wish to narrow down records to their fields of preference.

There are also may be some potential memory issues pertaining to the 311 Requests data since there are so many records.
