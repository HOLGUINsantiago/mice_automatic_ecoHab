# Automtic analysis for Eco-hab data extracted with [pyEcoHab](https://github.com/Neuroinflab/pyEcoHAB)

- Written by Santiago Holguin 
- [holguinsanty@gmail.com](mailto:holguinsanty@gmail.com)

## 1. Clone pyEcoHab repositorys and install libraries:  
First make sur to have [Git](https://git-scm.com/downloads) installed on your pc 

1. Clone our repository (on the path of your choice)

    `git clone https://github.com/HOLGUINsantiago/mice_automatic_ecoHab`

2. Go into our project :
   
    `cd mice_automatic_ecoHab`

 3. Clone pyEcoHab repository inside :
   
    `git clone https://github.com/Neuroinflab/pyEcoHAB`

## Create conda environment :
Make sur to have [conda](https://www.anaconda.com/docs/getting-started/miniconda/install#windows-powershell) installed

1. Create a new environment (used in the futur for ipynb) :
   
    `conda create -n ecohab_env python=3`

2. Activate the created envnironment : 
   
    `conda activate ecohab_env`

3. Install pyEcoHab dependencies : 
   
    ```{bash}
    cd pyEcoHAB
    pip install -r requirements.txt
    ```

4. Use the librarie as an editable package : 

    `pip install -e .`

## Start your analysis : 
The [Jupyter notebook](exploration.ipynb) on this project extracts all possible parameters that can be obtained with the RFID on the Eco-hab, and put the important dataframes on different directorys (for example [Habituation results](Results)). 

Then this results can be analysed with our [R script](ResultsAnalysis.Rmd).

## Data availability
Rawdata are available on demand by contacting Dr. M. Rivalan at [Neuropsi team](https://neuropsi.cnrs.fr/departements/cnn/equipe-sylvie-granon/)

### Good EcoHab processing !!!!!