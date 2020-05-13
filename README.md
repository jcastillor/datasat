# Datasat
DataSat is a web accessible database app developed by José Castillo within the ALGGEN group at the UPC.  
The web application is based on the Django framework and the database engine used is PostgreSQL for its good performance for large volumes of data.

Detailed information about the project can be found on [this](https://github.com/jcastillor/datasat/blob/master/DATASAT%20documentation.pdf  "Master's thesis of the project") document.

## Database updating and maintenance
In this section I'm going to explain the steps to follow in order to add new species to the database.
The **sat** machine contains everything needed in order to add new species to the datasat application in the form of executable bash scripts, for this reason, in short, all that is needed is to push the desired files to the **sat** machine and then execute the scripts needed for every step. The whole process has been divided into several steps in order to make it possible for the user to control and supervise the correct execution of each step. Bellow figure summarizes the whole process.

![alt text][logo]

[logo]: https://github.com/jcastillor/datasat/blob/master/file_flow.jpg "File flow schematic"

As you can see on the figure, there are 3 steps: batch file renaming, batch satellite computation and batch formatting. The concept is simple, for each file, every step has to be done one by one (two *.awk* scripts for file formatting and the satfind program), and the process is done in batch for multiple files in a same directory thanks to their corresponding bash script. Executable bash scripts are located on the **sat** machine in the `bin/` directory. 
> Please make sure to read the bash script before executing it, they are very simple and they indicate where to put the files. 

### 1. Batch file renaming (optional (but not really))

This first step is needed due to the way Genbank formats the files when you want to download batch files from a query. Normally Genbank puts all the files selected in a *.rar* file with generic names relative to the query and not to the file itself.
To batch rename this files you simply have to put the files you want to rename in a directory and modify the **FILES** and **DIRECTORY** variables in the `rename` script. 
For example, if I have some files in `/home/sat/Genomes/Bacteria/` I have to modify the `rename` script so that the **FILES** and **LOCATION** variable look like this:

`FILES=/home/sat/Genomes/Bacteria/*`
`LOCATION=/home/sat/Genomes/Bacteria/`

After this, simply put `rename` in the **sat** machine command prompt and the renaming will be done automatically thanks to the *filename.awk* script.

> note that the SPATH variable has to remain unchanged during the process.

### 2. Batch satellite computing 

Satellite computing is done thanks to the **SATFIND** program. In order to batch compute a set of files you have to modify the `satfindall` script with the desired parameters for the satellite computation. As in the case of the previous script, if you have some files for the satellite computing in `/home/sat/Genomes/Bacteria3/`, you have to modify the **FILES** variable so it looks like this:
`FILES=/home/sat/Genomes/Bacteria3/*`
After that, you just have to type `satfindall` in the sat machine command prompt, the program will ask you to press `y` to create an *Output* directory inside the *SATFIND* program location, where the computed files will be stored.

> note that everything else besides the *FILES* variable and the *SATFIND* parammeters have to remain unchanged within the `satfindall` script.

### 3. Formatting the *SATFIND* output into *.csv* files

This step is crucial in order to have the files formatted in a way that makes the importing of the data into the **PostgreSQL** database.
