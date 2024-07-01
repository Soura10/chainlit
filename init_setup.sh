echo [$(date)]: "START"
echo [$(date)]: "Creating a conda Environment with python 3.10"
conda create -p ./chainlit_env python=3.10 -y
echo [$(date)]: "Created conda Env"
source activate ./chainlit_env
echo [$(date)]: "Activated Conda Environment"
echo [$(date)]: "Installing requirements"
pip install -r requirements.txt
echo [$(date)]: "Installed all requirements"
echo [$(date)]: "END"
