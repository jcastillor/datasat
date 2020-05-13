# Datasat
DataSat is a web accessible database app developed by José Castillo within the ALGGEN group at the UPC.  
The web application is based on the Django framework and the database engine used is PostgreSQL for its ideonity for large volumes of data.

Detailed information about the project can be found on [this](https://github.com/jcastillor/datasat/blob/master/DATASAT%20documentation.pdf  "Master's thesis of the project") document.

##Database updating and maintenance

In this section I'm going to explain the steps to follow in order to add new species to the database.
The *sat* machine contains everything needed in order to add new species to the datasat application in the form of executable bash scripts, for this reason, in short, all that is needed is to push the desired files to the *sat* machine and then execute the scripts needed for every step. The whole process has been divided into several steps in order to make it possible for the user to control and supervise the correct execution of each step. Bellow figure summarizes the whole process.



1. Batch file renaming (optional (but not really))
This first step is needed due to the way Genbank formats the files when you want to download batch files from a query. Normally Genbanks puts all the files selected in a *.rar* file with generic names relative to the query and not to the file itself.
