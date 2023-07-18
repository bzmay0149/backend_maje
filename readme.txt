##create virtual environment
python3 -m venv .venv linux
py -3 -m venv .venv windows



##Activate virtual environment
. .venv/bin/activate linux
.venv\Scripts\activate windows


##nstall libraries
pip install -r requirements.txt
