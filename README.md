# Global Coronavirus Disease 2019 (COVID-19) Monitoring Dashboard

At the beginning of 2019, some people in Wuhan, China, suffered from unusual pneumonia, a respiratory syndrome, which eventually and quickly led to a local outbreak. Initially, the cause was unknown; however, it did not take the health experts a long time to determine that an unusual and new coronavirus caused that pneumonia, and they name it severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) or coronavirus disease 2019 (COVID-19). Right after identifying SARS-CoV-2, the virus started to spread in almost all the Chinese provinces and then to the whole world (Dong, Du, & Gardner, 2020). One of the vital characteristics of covid-19 is that its ability to spread quickly among communities. The virus can be transmitted from one person and caught by another one even before showing any symptoms of covid-19 by the first contagious individual (CDC, 2021). As a result, the virus would negatively impact individuals, societies, cities, countries, and the entire globe, and that impact can take many different forms. For example, according to World Health Organization (2021), the death tolls of the pandemic of covid-19 had exceeded 3 million humans in the entire world in the year of 2020 and more than four million and a half as of this day, Sep 08, 2021. Due to the high mortality rate of covid 19, the whole world has been hurt from the outbreak in terms of health and economy. Hospitalization associated with Covid-19 has spiked many times since the coronavirus pandemic has emerged, pushing health systems to their limit. Many economies have been slowed down ever since. Consequently, the novel Coronavirus has left the earth in a crisis.  

Therefore, it is crucial for us to closely monitoring the instantly covid-19 cases, deaths, hospitalizations, and the virus prevalence locally and worldwide. By doing so, we can collect data and retrieve information about the disease and detailed information about whom it affects. We also can build up more insights into the nature of the disease, which can help control the spread of the virus. This project aims to transfer the all-raw data of Covid-19 being collected from all around the world since the start of the pandemic into visualized pictures and charts. The data that will be used contains many types of information, such as demographic information, symptoms, treatments, and health outcomes. Visualizing Covid-19 data is helpful for scientists and ordinary individuals. It can assist medical experts in learning who can be severely sick and what kind of health care they should receive based on the visual of historical data of recovered patients. It also can be helpful for ordinary people in a way that it eases the understanding of the impact of the outbreak and which areas have been witnessed more cases and deaths or recoveries associated with Covid-19.  

Algorithms/Project Solution
-	The dataset I will be using for the project is going to be “COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University” from Github.  
-	The reason of choosing this dataset is because after doing some research I have found this dataset to be one of the most comprehensive datasets, and it’s updated daily between 03:30 and 04:00 UTC.
-	The data are time series and there are in wide format. The data are spitted in three datasets:
o	time_series_covid19_confirmed_global.csv
	Contains data of the confirmed cases globally
o	time_series_covid19_deaths_global.csv
	Contains data of the confirmed deaths worldwide
o	time_series_covid19_recovered_global.csv
	Contains data of the recovered cases
-	Each dataset consists of the following variables:
o	`FIPS`: FIPS stands for Federal Information Processing Standards, which are “are standards and guidelines for federal computer systems that are developed by National Institute of Standards and Technology (NIST) in accordance with the Federal Information Security Management Act (FISMA) and approved by the Secretary of Commerce” (NIST, 2019). It is only for the US.
o	`Admin2`: It is the County name, and it’s only for the US.
o	`Province_State`: Province, state, or dependency name.
o	`Country_Region`: Country region or sovereignty name.
o	` Last Update`: MM/DD/YYYY HH:mm:ss (24-hour format, in UTC).
o	`Lat and Long`: Dot locations on the dashboard.
o	` Confirmed`: The number of confirmed cases for each record and where it was reported. 
o	` Deaths`: The number of confirmed cases for each record and where it was reported. 
o	`Recovered`: Recovered cases are estimates based on local media reports, and state and local reporting when available. 
o	`Active`: Active cases = total cases - total recovered - total deaths.
o	`Incident_Rate`: It is calculated as follows incidence Rate = cases per 100,000 persons.
o	`Case_Fatality_Ratio (%) `: Case-Fatality Ratio (%) = Number recorded deaths / Number cases.
-	I will also be using another dataset for the population for each country to perform some functions that require calculations involving population of countries. The dataset is “Population by Country – 2020” From Kaggle. The dataset contains 11 columns, but only two columns are needed, which are:
o	`country`: List of all countries in the world
o	`population`: the population of each country
o	` Density (P/Km²)`: the density of the population
-	The Tableau Workbook will contain several pages or worksheets plus a dashboard. All the worksheets will be designed and added to the dashboard to create the active Covid-19 Dashboard. The list of worksheets as follows:
o	`confirmed_cases`: A worksheet displaying the number of confirmed cases.
o	`recovered_cases`: A worksheet that displays the number of individuals who have recovered from covid-19.
o	`total_deaths`: A worksheet to present the number of death cases.
o	`recovery_rate`: A worksheet for showing the percentage of recovery from the total confirmed cases. 
o	`mortality_rate`: A worksheet to display the number of deaths in a particular population.
o	` globe_map`: An interactive map for the entire world with all countries’ borders. 
o	`daily_cases`: A worksheet containing a histogram of the daily cases on a specific period of time.
o	`top_10_countries`:  A worksheet to display the top ten countries with the highest confirmed cases in a chart. 
o	`dashboard`: A dashboard containing all the sheets created. 

-	The Tableau Workbook will contain a number of functions or measures to purse some calculations. The would be as follows:
o	`get_mortality_rate`: calculate the death rates by dividing the total deaths over the total of confirmed cases. 
o	`get_recovery_rate`: calculate the recovery rate by dividing the total of recovery cases over the total of confirmed cases. 
o	`get_top_10_countries`: retrieve a list of the top ten countries with the highest confirmed cases in a chart.


Implementation
 To implement this project, the following technologies and tools would be used: 
-	Python: as the main programming language to wrangle data
o	PyCharm:  An integrated development environment (IDE) specifically utilized in computer programing with Python. The tool will be used to write the Python scripts that download the data from the Internet. 
o	Jupyter Notebook: “The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.” (Jupyter, n.d.)
o	The libraries that are needed to accomplish the tasks requiring using of Python are:
	Pandas: Is an open-source data analysis tool that is built in top of Python used to analyze and manipulate data.  
	NumPy:  Is a Python library offering comprehensive mathematical functions, random number generators, linear algebra routines, Fourier transforms, and more. 
	Python Request: Request library allows users to send HTTP/1.1 requests extremely easily. It will be used to download the datasets needed for this project from their sources (GitHub and Kaggle). 
	GitHub: Is a development platform and vision control system that uses Git. 
	Kaggle: Is an online community for people who are interested in data scientists and machine learning. It contains thousands of datasets from almost all the specializations (Wiki, n.d.).
-	Tableau: Is an American company specialized on business intelligence. It has a data visualization tool named Tableau. Tableau is unlike other data-related applications, such as MS Excel or Apple Numbers, Tableau is powerful since it can produce complex and interactive dashboards. 
