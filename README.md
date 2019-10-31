# ETL news sites

A three phases project where processes like Extracting, Transforming and Loading are carried out.
And all working together using a pipeline.

* Extract

Data is taken usig techniques of web scraping from news websites such as [El universal][1] , [El pais][2] and [Panorama][3] where the titles, bodies and urls of news are saved in a .csv file.
(Libraries like pyyaml, resquests, regex and urllib3 are needed)

* Transform 

Data is taken from a .csv file created by the extracting process, the missing information is filled, the bodies is cleaned and more information tokenizing the body and title of the news is added. A new .csv file is created to be used by the load process
(Libraries like pandas, nltk and nltk.corpus are need)

* Load 

The cleaned .csv file with more information is loaded in relational database, creating or making bigger a .db file.
(sqlalchemy is needed)

## How to use

Every process could work by itself just running on prompt main.py and the name of the .csv file or the name of the news site (a patter like "eluniversal" for extracting, "eluniversal_01_11_19.csv" for transforming and "clean_eluniversal_01_11_19.csv" for loading). But to use the whole process just run the pipeline.py file.


[1]: https://www.eluniversal.com.mx/
[2]: https://elpais.com
[3]: https://www.panorama.com.ve
