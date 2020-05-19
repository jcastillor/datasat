# Datasat
DataSat is a web accessible database app developed by José Castillo within the ALGGEN group at the UPC.  
The web application is based on the Django framework and the database engine used is PostgreSQL for its good performance for large volumes of data.

Detailed information about the project can be found on [this](https://github.com/jcastillor/datasat/blob/master/DATASAT%20documentation.pdf  "Master's thesis of the project") document.

## Database updating and maintenance
In this section I'm going to explain the steps to follow in order to add new species to the database.
The **sat** machine contains everything needed in order to add new species to the datasat application in the form of executable bash scripts, for this reason, in short, all that is needed is to push the desired files to the **sat** machine and then execute the scripts needed for every step. The whole process has been divided into several steps in order to make it possible for the user to control and supervise the correct execution of each step. Bellow figure summarizes the whole process.

![alt text][logo]

[logo]: https://github.com/jcastillor/datasat/blob/master/file_flow.jpg "File flow schematic"

As you can see on the figure, there are 3 steps: batch file renaming, batch satellite computation and batch formatting. The concept is simple, for each file, every step has to be done one by one (two *.awk* scripts for file formatting and the satfind program), and the process is done in batch for multiple files in a same directory thanks to their corresponding bash script. Executable bash scripts are located on the **sat** machine in the `~/bin` directory. 
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

Satellite computing is done thanks to the **SATFIND** program (located in `~/tools/satfindp`). In order to batch compute a set of files you have to modify the `satfindall` script with the desired parameters for the satellite computation. As in the case of the previous script, if you have some files for the satellite computing in `/home/sat/Genomes/Bacteria3/`, you have to modify the **FILES** variable so it looks like this:
`FILES=/home/sat/Genomes/Bacteria3/*`
After that, you just have to type `satfindall` in the sat machine command prompt, the program will ask you to press `y` to create an *Output* directory inside the *SATFIND* program location, where the computed files will be stored.

> note that everything else besides the *FILES* variable and the *SATFIND* parammeters have to remain unchanged within the `satfindall` script.

### 3. Formatting the *SATFIND* output into *.csv* files

This step is crucial in order to have the files formatted in a way that makes the importing of the data into the **PostgreSQL** database easy. The formatting is done with the help of `formatdb2` script located in the `~/bin` directory. `formatdb2` uses a *.awk* script called `dbformat.awk` in order to work.
The idea of this step is to format the output files of the `satfindall` script that are located, as stated in the previous step, within the `Output` folder that the scripts creates to store the output of the **SATFIND** program. If you look closely inside the `Output` folder, there are several directories that store the files of different species. Let's work with an example. Say you have already computed the satellites with **SATFIND** and they are located in `/home/sat/tools/satfindp/Output/Arqueas`, you'll need to modify `formatdb2` `FILES` and `SPATH` variables so they look like this: `FILES=/home/sat/tools/satfindp/Output/Arqueas/*` `SPATH=/home/sat/tools/satfindp/Output/Arqueas`. Then, you just have to put the `dbformat.awk` script (located in `~/tools/formatting`) inside the same folder and just run the program by typing `formatdb2` in the machine command prompt. The formatted *.csv* files will be located in a directory called `FormatOutput` inside the same directory you modified the variables with. 

## Importing the *.csv* files into the PostgreSQL database

For this step, you just have to modify the `FILES` and `SPATH` variables with the directory where the *.csv* files are located so they look like this: `FILES=/home/sat/tools/satfindp/Output/Bacteria/FormatOutput/*` `SPATH=/home/sat/tools/satfindp/Output/Bacteria/FormatOutput/`. The simply type `importall` in the machine command prompt in order to import the files into the table of the database that outputs the data to the **datasat** web application. 

## Update Django project for new content

Once the files have been introduced in the database with the help of the `importall` script, the migrations on the `datasatv2` **Django** project need to be updated. First you need to activate the virtual environment with the repositories needed in order for the project to work. To do this, simply type within the `home` directory in the `sat` machine command prompt. 
`source environments/datasatv2_env/bin/activate`, you'll now that the environment is activated if `(datasatv2_env)` appears before the command prompt. 

> to deactivate the virtual environment simply type `deactivate` in the command prompt of the `sat` machine. 

Once we've activated the virtual environment all we need to do is navigate to the directory of the django project `/home/sat/projects/datasatv2` and type:
`python3 manage.py makemigrations` and
`python3 manage.py migrate`

Once all this is done, please contact the systems administrators to restart the apache server in order to update the information in the web application.
