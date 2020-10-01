# matplotlib_csv
Advanced Python - Matplotlib - using CSV files

In the Sitka_valley program, after importing CSV, the csv files are opened as
read data. Next, the csv files are opened like DictReader, instead of a regular reader, in order to read each row by the fieldnames. In order to read the headers only, when printing out the name of the cities as titles, there is a header_row variable assigned. 

After empty lists are created for both sitka and death valley, a for loop is created for each city, and a try/ expect command is implemented to check for any missing data. In order to get the information on a plot, I created a subplot to have the graphs on the same page. After formating the data, the plot is displayed.

--this project is to teach students how to use CSV files in python
--this project also teaches students how to visualize the data using matplotlib

