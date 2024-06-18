# Module 10 Challenge 

## Jupyter Notebook Database Connection
- Use the SQLAlchemy create_engine() function to connect to your SQLite database
- Use the SQLAlchemy automap_base() function to reflect your tables into classes
- Save references to the classes named station and measurement
- Link Python to the database by creating a SQLAlchemy session
- Close your session at the end of your notebook

## Precipitation Analysis 
- Create a query that finds the most recent date in the dataset (8/23/2017)
- Create a query that collects only the date and precipitation for the last year of data without passing the date as a variable
- Save the query results to a Pandas DataFrame to create date and precipitation columns

![Alt text](/SurfsUp/output/DATE1.png)


## Sort the DataFrame by date
- Plot the results by using the DataFrame plot method with date as the x and precipitation as the y variables
- Use Pandas to print the summary statistics for the precipitation data

![Alt text](/SurfsUp/output/DF1.png)
![Alt text](/SurfsUp/output/prcp.png)

## Station Analysis
- Design a query that correctly finds the number of stations in the dataset\
- ![Alt text](/SurfsUp/output/Station1.png)
- Design a query that correctly lists the stations and observation counts in descending order and finds the most active station (USC00519281)
- ![Alt text](/SurfsUp/output/STATION2.png)
- Design a query that correctly finds the min, max, and average temperatures for the most active station (USC00519281)
- ![Alt text](/SurfsUp/output/STATION3.png)
- Design a query to get the previous 12 months of temperature observation (TOBS) data that filters by the station that has the greatest number of observations
- Save the query results to a Pandas DataFrame 
- ![Alt text](/SurfsUp/output/DF2.png)
- Correctly plot a histogram with bins=12 for the last year of data using tobs as the column to count. 
![Alt text](/SurfsUp/output/tobs.png)


## API SQLite Connection & Landing Page
- Correctly generate the engine to the correct sqlite file 
- Use automap_base() and reflect the database schema 
- Correctly save references to the tables in the sqlite file (measurement and station)
- Correctly create and binds the session between the python app and database 
- Display the available routes on the landing page
![Alt text](/SurfsUp/output/app1.png)
## API Static Routes
### A precipitation route that:
- Returns json with the date as the key and the value as the precipitation
- Only returns the jsonified precipitation data for the last year in the database
![Alt text](/SurfsUp/output/app2.png)
### A stations route that:
- Returns jsonified data of all of the stations in the database
![Alt text](/SurfsUp/output/app3.png)
### A tobs route that:
- Returns jsonified data for the most active station (USC00519281)
- Only returns the jsonified data for the last year of data 
![Alt text](/SurfsUp/output/app4.png)
## API Dynamic Route
- This 2-part question was consolidated into a single app with x2 decorators--
![Alt text](/SurfsUp/output/app5.png)

### A start route that:PT1
- Accepts the start date as a parameter from the URL 
- Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset 

### A start/end route that:PT2
- Accepts the start and end dates as parameters from the URL 
- Returns the min, max, and average temperatures calculated from the given start date to the given end date 

## Coding Conventions and Formatting 
- Place imports at the top of the file, just after any module comments and docstrings, and before module globals and constants.
- Name functions and variables with lowercase characters, with words separated by underscores.
- Follow DRY (Don't Repeat Yourself) principles, creating maintainable and reusable code.
- Use concise logic and creative engineering where possible.

## Deployment and Submission 
- Submit a link to a GitHub repository that’s cloned to your local machine and contains your files.
- Use the command line to add your files to the repository.
- Include appropriate commit messages in your files.

## Comments
- Be well commented with concise, relevant notes that other developers can understand.

##RESOURCES
- Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xmlLinks to an external site.
- With help from tutoring EDX(Kourt) and Mr GPT