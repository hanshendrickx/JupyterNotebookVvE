cls
cmd
cd anaconda3\scripts
activate
cd.. & cd envs
conda info
conda create --name JP901 python=3.10
Y
conda update -n base -c defaults conda
Y
Y
cd JP901
md root & cd root
conda activate JP901

conda install -c conda-forge jupyterlab
Y
conda install -c anaconda pandas
Y
conda install -c anaconda plotly
Y
conda install -c plotly plotly_express
Y
conda install -c anaconda csvkit
Y
conda install -c anaconda openpyxl
Y
conda install -c conda-forge xlsxwriter
Y
conda install -c anaconda xlwt
Y
conda install -c anaconda xlrd
Y
conda install -c conda-forge ipywidgets
Y
jupyter nbextension enable --py widgetsnbextension
Y
conda install -c plotly plotly
Y
conda install -c conda-forge pandoc
Y
conda install -c conda-forge tabulate
Y
conda install -c conda-forge python-kaleido
Y

conda list --explicit > spec-file.txt
conda list --export > requirements.txt
conda env export > environment.yml