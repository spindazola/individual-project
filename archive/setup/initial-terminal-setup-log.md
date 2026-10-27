Last login: Fri Oct  9 14:32:44 on console

adrian\@Adrians-Macbook \~ % dir

zsh: command not found: dir

adrian\@Adrians-Macbook \~ % cd 

adrian\@Adrians-Macbook \~ % cd devel

cd: no such file or directory: devel

adrian\@Adrians-Macbook \~ % cd

adrian\@Adrians-Macbook \~ % cd Developer 

adrian\@Adrians-Macbook Developer % dir

zsh: command not found: dir

adrian\@Adrians-Macbook Developer % cd university 

adrian\@Adrians-Macbook university % cd Year\ 3 

adrian\@Adrians-Macbook Year 3 % cd 

adrian\@Adrians-Macbook \~ % cd  

adrian\@Adrians-Macbook \~ % cd \~/Developer/university/"Year 3"



unzip \~/Downloads/individual-project-starter.zip



cd individual-project



git init



python3 -m venv .venv

source .venv/bin/activate



pip install -r requirements.txt



ls

Archive:  /Users/adrian/Downloads/individual-project-starter.zip

  inflating: individual-project/requirements.txt  

  inflating: individual-project/DECISIONS.md  

  inflating: individual-project/.gitignore  

  inflating: individual-project/PROJECT_CONTEXT.md  

  inflating: individual-project/README.md  

  inflating: individual-project/TASKS.md  

  inflating: individual-project/AGENTS.md  

  inflating: individual-project/meetings/2026-10-13-nery.md  

  inflating: individual-project/notebooks/00_conformal_reproduction.ipynb  

  inflating: individual-project/tests/test_calibration.py  

  inflating: individual-project/experiments/EXPERIMENT_LOG.md  

  inflating: individual-project/literature/SOURCE_MAP.md  

  inflating: individual-project/literature/references.bib  

  inflating: individual-project/data/README.md  

  inflating: individual-project/src/conformal/metrics.py  

  inflating: individual-project/src/conformal/\_\_init\_\_.py  

  inflating: individual-project/src/conformal/scores.py  

  inflating: individual-project/src/conformal/calibration.py  

  inflating: individual-project/reports/project_plan/README.md  

  inflating: individual-project/reports/report1/main.tex  

  inflating: individual-project/reports/report2/main.tex  

Initialized empty Git repository in /Users/adrian/Developer/university/Year 3/individual-project/.git/

Collecting numpy (from -r requirements.txt (line 1))

  Downloading numpy-2.5.4-cp313-cp313-macosx_14_0_arm64.whl.metadata (6.6 kB)

Collecting pandas (from -r requirements.txt (line 2))

  Downloading pandas-3.0.6-cp313-cp313-macosx_11_0_arm64.whl.metadata (79 kB)

Collecting matplotlib (from -r requirements.txt (line 3))

  Downloading matplotlib-3.11.2-cp313-cp313-macosx_11_0_arm64.whl.metadata (80 kB)

Collecting scikit-learn (from -r requirements.txt (line 4))

  Downloading scikit_learn-1.9.1-cp313-cp313-macosx_12_0_arm64.whl.metadata (9.3 kB)

Collecting jupyter (from -r requirements.txt (line 5))

  Downloading jupyter-1.1.1-py2.py3-none-any.whl.metadata (2.0 kB)

Collecting pytest (from -r requirements.txt (line 6))

  Downloading pytest-9.1.1-py3-none-any.whl.metadata (7.6 kB)

Collecting python-dateutil>=2.8.2 (from pandas->-r requirements.txt (line 2))

  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)

Collecting contourpy>=1.0.1 (from matplotlib->-r requirements.txt (line 3))

  Downloading contourpy-1.4.0-cp313-cp313-macosx_11_0_arm64.whl.metadata (3.8 kB)

Collecting cycler>=0.10 (from matplotlib->-r requirements.txt (line 3))

  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)

Collecting fonttools>=4.28.2 (from matplotlib->-r requirements.txt (line 3))

  Downloading fonttools-4.66.1-cp313-cp313-macosx_10_13_universal2.whl.metadata (130 kB)

Collecting kiwisolver>=1.3.1 (from matplotlib->-r requirements.txt (line 3))

  Downloading kiwisolver-1.5.1-cp313-cp313-macosx_11_0_arm64.whl.metadata (5.2 kB)

Collecting packaging>=20.0 (from matplotlib->-r requirements.txt (line 3))

  Downloading packaging-26.3-py3-none-any.whl.metadata (3.5 kB)

Collecting pillow>=9 (from matplotlib->-r requirements.txt (line 3))

  Downloading pillow-12.3.0-cp313-cp313-macosx_11_0_arm64.whl.metadata (9.1 kB)

Collecting pyparsing>=3 (from matplotlib->-r requirements.txt (line 3))

  Downloading pyparsing-3.3.3-py3-none-any.whl.metadata (5.9 kB)

Collecting scipy>=1.10.0 (from scikit-learn->-r requirements.txt (line 4))

  Downloading scipy-1.18.1-cp313-cp313-macosx_14_0_arm64.whl.metadata (62 kB)

Collecting joblib>=1.4.0 (from scikit-learn->-r requirements.txt (line 4))

  Downloading joblib-1.6.0-py3-none-any.whl.metadata (6.5 kB)

Collecting narwhals>=2.0.1 (from scikit-learn->-r requirements.txt (line 4))

  Downloading narwhals-2.27.1-py3-none-any.whl.metadata (15 kB)

Collecting threadpoolctl>=3.5.0 (from scikit-learn->-r requirements.txt (line 4))

  Downloading threadpoolctl-3.7.0-py3-none-any.whl.metadata (24 kB)

Collecting notebook (from jupyter->-r requirements.txt (line 5))

  Downloading notebook-7.6.3-py3-none-any.whl.metadata (10 kB)

Collecting jupyter-console (from jupyter->-r requirements.txt (line 5))

  Downloading jupyter_console-6.6.3-py3-none-any.whl.metadata (5.8 kB)

Collecting nbconvert (from jupyter->-r requirements.txt (line 5))

  Downloading nbconvert-7.17.2-py3-none-any.whl.metadata (8.4 kB)

Collecting ipykernel (from jupyter->-r requirements.txt (line 5))

  Downloading ipykernel-7.4.0-py3-none-any.whl.metadata (3.4 kB)

Collecting ipywidgets (from jupyter->-r requirements.txt (line 5))

  Downloading ipywidgets-8.1.9-py3-none-any.whl.metadata (2.4 kB)

Collecting jupyterlab (from jupyter->-r requirements.txt (line 5))

  Downloading jupyterlab-4.6.4-py3-none-any.whl.metadata (16 kB)

Collecting iniconfig>=1.0.1 (from pytest->-r requirements.txt (line 6))

  Downloading iniconfig-2.3.1-py3-none-any.whl.metadata (2.8 kB)

Collecting pluggy<2,>=1.5 (from pytest->-r requirements.txt (line 6))

  Downloading pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)

Collecting pygments>=2.7.2 (from pytest->-r requirements.txt (line 6))

  Downloading pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)

Collecting cloudpickle>=3.0 (from joblib>=1.4.0->scikit-learn->-r requirements.txt (line 4))

  Downloading cloudpickle-3.1.2-py3-none-any.whl.metadata (7.1 kB)

Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas->-r requirements.txt (line 2))

  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)

Collecting appnope>=0.1.2 (from ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading appnope-1.0.0-py3-none-any.whl.metadata (982 bytes)

Collecting comm>=0.1.1 (from ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading comm-0.2.3-py3-none-any.whl.metadata (3.7 kB)

Collecting debugpy>=1.6.5 (from ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading debugpy-1.8.22-cp313-cp313-macosx_15_0_universal2.whl.metadata (1.4 kB)

Collecting ipython>=7.23.1 (from ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading ipython-9.17.1-py3-none-any.whl.metadata (4.6 kB)

Collecting jupyter-client>=8.9.0 (from ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading jupyter_client-8.10.0-py3-none-any.whl.metadata (8.5 kB)

Collecting jupyter-core!=6.0.\*,>=5.1 (from ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading jupyter_core-5.9.1-py3-none-any.whl.metadata (1.5 kB)

Collecting matplotlib-inline>=0.1 (from ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading matplotlib_inline-0.2.2-py3-none-any.whl.metadata (2.4 kB)

Collecting nest-asyncio2>=1.7.0 (from ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading nest_asyncio2-1.7.4-py3-none-any.whl.metadata (7.0 kB)

Collecting pyzmq>=25 (from ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading pyzmq-27.2.0-cp312-abi3-macosx_10_15_universal2.whl.metadata (3.8 kB)

Collecting tornado>=6.5.7 (from ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading tornado-6.5.10-cp39-abi3-macosx_10_9_universal2.whl.metadata (2.8 kB)

Collecting traitlets>=5.4.0 (from ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading traitlets-5.16.1-py3-none-any.whl.metadata (10 kB)

Collecting ipython-pygments-lexers>=1.0.0 (from ipython>=7.23.1->ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading ipython_pygments_lexers-1.1.1-py3-none-any.whl.metadata (1.1 kB)

Collecting jedi>=0.18.2 (from ipython>=7.23.1->ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading jedi-0.20.1-py2.py3-none-any.whl.metadata (23 kB)

Collecting pexpect>4.6 (from ipython>=7.23.1->ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading pexpect-4.9.0-py2.py3-none-any.whl.metadata (2.5 kB)

Collecting prompt_toolkit<3.1.0,>=3.0.41 (from ipython>=7.23.1->ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading prompt_toolkit-3.0.53-py3-none-any.whl.metadata (6.4 kB)

Collecting psutil>=7 (from ipython>=7.23.1->ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading psutil-7.2.2-cp36-abi3-macosx_11_0_arm64.whl.metadata (22 kB)

Collecting stack_data>=0.6.0 (from ipython>=7.23.1->ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading stack_data-0.6.3-py3-none-any.whl.metadata (18 kB)

Collecting wcwidth>=0.1.4 (from prompt_toolkit<3.1.0,>=3.0.41->ipython>=7.23.1->ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading wcwidth-0.9.2-cp310-abi3-macosx_11_0_arm64.whl.metadata (23 kB)

Collecting parso<0.9.0,>=0.8.7 (from jedi>=0.18.2->ipython>=7.23.1->ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading parso-0.8.7-py2.py3-none-any.whl.metadata (8.2 kB)

Collecting typing-extensions>=4.13.0 (from jupyter-client>=8.9.0->ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)

Collecting platformdirs>=2.5 (from jupyter-core!=6.0.\*,>=5.1->ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading platformdirs-4.13.0-py3-none-any.whl.metadata (5.5 kB)

Collecting ptyprocess>=0.5 (from pexpect>4.6->ipython>=7.23.1->ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading ptyprocess-0.7.0-py2.py3-none-any.whl.metadata (1.3 kB)

Collecting executing>=1.2.0 (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading executing-2.3.0-py3-none-any.whl.metadata (9.1 kB)

Collecting asttokens>=2.1.0 (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading asttokens-3.0.2-py3-none-any.whl.metadata (5.7 kB)

Collecting pure-eval (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel->jupyter->-r requirements.txt (line 5))

  Downloading pure_eval-0.2.4-py3-none-any.whl.metadata (6.4 kB)

Collecting widgetsnbextension\~=4.0.16 (from ipywidgets->jupyter->-r requirements.txt (line 5))

  Downloading widgetsnbextension-4.0.16-py3-none-any.whl.metadata (1.6 kB)

Collecting jupyterlab_widgets\~=3.0.17 (from ipywidgets->jupyter->-r requirements.txt (line 5))

  Downloading jupyterlab_widgets-3.0.17-py3-none-any.whl.metadata (20 kB)

Collecting async-lru>=1.0.0 (from jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading async_lru-2.4.0-py3-none-any.whl.metadata (10 kB)

Collecting httpx<1,>=0.25.0 (from jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)

Collecting jinja2>=3.0.3 (from jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)

Collecting jupyter-builder>=1.0.2 (from jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading jupyter_builder-1.2.3-py3-none-any.whl.metadata (7.8 kB)

Collecting jupyter-lsp>=2.0.0 (from jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading jupyter_lsp-2.3.1-py3-none-any.whl.metadata (1.8 kB)

Collecting jupyter-server<3,>=2.19.0 (from jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading jupyter_server-2.21.1-py3-none-any.whl.metadata (8.5 kB)

Collecting jupyterlab-server<3,>=2.28.0 (from jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading jupyterlab_server-2.28.1-py3-none-any.whl.metadata (5.8 kB)

Collecting notebook-shim>=0.2 (from jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading notebook_shim-0.2.4-py3-none-any.whl.metadata (4.0 kB)

Collecting anyio (from httpx<1,>=0.25.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading anyio-4.15.1-py3-none-any.whl.metadata (4.7 kB)

Collecting certifi (from httpx<1,>=0.25.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading certifi-2026.7.22-py3-none-any.whl.metadata (2.5 kB)

Collecting httpcore==1.\* (from httpx<1,>=0.25.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)

Collecting idna (from httpx<1,>=0.25.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading idna-3.20-py3-none-any.whl.metadata (7.2 kB)

Collecting h11>=0.16 (from httpcore==1.\*->httpx<1,>=0.25.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)

Collecting argon2-cffi>=21.1 (from jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading argon2_cffi-25.1.0-py3-none-any.whl.metadata (4.1 kB)

Collecting jupyter-events>=0.11.0 (from jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading jupyter_events-0.12.1-py3-none-any.whl.metadata (5.8 kB)

Collecting jupyter-server-terminals>=0.4.4 (from jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading jupyter_server_terminals-0.5.4-py3-none-any.whl.metadata (5.9 kB)

Collecting nbformat>=5.3.0 (from jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading nbformat-5.11.1-py3-none-any.whl.metadata (3.7 kB)

Collecting prometheus-client>=0.9 (from jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading prometheus_client-0.26.0-py3-none-any.whl.metadata (2.1 kB)

Collecting send2trash>=1.8.2 (from jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading send2trash-2.1.0-py3-none-any.whl.metadata (4.1 kB)

Collecting terminado>=0.8.3 (from jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading terminado-0.18.1-py3-none-any.whl.metadata (5.8 kB)

Collecting websocket-client>=1.7 (from jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading websocket_client-1.9.2-py3-none-any.whl.metadata (8.3 kB)

Collecting babel>=2.10 (from jupyterlab-server<3,>=2.28.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading babel-2.18.0-py3-none-any.whl.metadata (2.2 kB)

Collecting json5>=0.9.0 (from jupyterlab-server<3,>=2.28.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading json5-0.17.3-py3-none-any.whl.metadata (27 kB)

Collecting jsonschema>=4.18.0 (from jupyterlab-server<3,>=2.28.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)

Collecting requests>=2.31 (from jupyterlab-server<3,>=2.28.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)

Collecting argon2-cffi-bindings (from argon2-cffi>=21.1->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading argon2_cffi_bindings-26.1.0-cp310-abi3-macosx_11_0_arm64.whl.metadata (7.5 kB)

Collecting MarkupSafe>=2.0 (from jinja2>=3.0.3->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading markupsafe-3.0.4-cp313-cp313-macosx_11_0_arm64.whl.metadata (2.7 kB)

Collecting attrs>=22.2.0 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.28.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)

Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.28.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)

Collecting referencing>=0.28.4 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.28.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)

Collecting rpds-py>=0.25.0 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.28.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading rpds_py-2026.9.1-cp313-cp313-macosx_11_0_arm64.whl.metadata (4.1 kB)

Collecting python-json-logger>=2.0.4 (from jupyter-events>=0.11.0->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading python_json_logger-4.2.0-py3-none-any.whl.metadata (2.9 kB)

Collecting pyyaml>=5.3 (from jupyter-events>=0.11.0->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading pyyaml-6.0.3-cp313-cp313-macosx_11_0_arm64.whl.metadata (2.4 kB)

Collecting rfc3339-validator (from jupyter-events>=0.11.0->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading rfc3339_validator-0.1.4-py2.py3-none-any.whl.metadata (1.5 kB)

Collecting rfc3986-validator>=0.1.1 (from jupyter-events>=0.11.0->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading rfc3986_validator-0.1.1-py2.py3-none-any.whl.metadata (1.7 kB)

Collecting fqdn (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading fqdn-1.6.0-py3-none-any.whl.metadata (9.4 kB)

Collecting isoduration (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading isoduration-20.11.0-py3-none-any.whl.metadata (5.7 kB)

Collecting jsonpointer>1.13 (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading jsonpointer-3.2.1-py3-none-any.whl.metadata (2.6 kB)

Collecting rfc3987-syntax>=1.1.0 (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading rfc3987_syntax-1.1.0-py3-none-any.whl.metadata (7.7 kB)

Collecting uri-template (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading uri_template-1.3.0-py3-none-any.whl.metadata (8.8 kB)

Collecting webcolors>=24.6.0 (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading webcolors-25.10.0-py3-none-any.whl.metadata (2.2 kB)

Collecting beautifulsoup4 (from nbconvert->jupyter->-r requirements.txt (line 5))

  Downloading beautifulsoup4-4.15.0-py3-none-any.whl.metadata (3.8 kB)

Collecting bleach!=5.0.0 (from bleach[css]!=5.0.0->nbconvert->jupyter->-r requirements.txt (line 5))

  Downloading bleach-6.4.0-py3-none-any.whl.metadata (32 kB)

Collecting defusedxml (from nbconvert->jupyter->-r requirements.txt (line 5))

  Downloading defusedxml-0.7.1-py2.py3-none-any.whl.metadata (32 kB)

Collecting jupyterlab-pygments (from nbconvert->jupyter->-r requirements.txt (line 5))

  Downloading jupyterlab_pygments-0.3.0-py3-none-any.whl.metadata (4.4 kB)

Collecting mistune<4,>=2.0.3 (from nbconvert->jupyter->-r requirements.txt (line 5))

  Downloading mistune-3.3.4-py3-none-any.whl.metadata (1.9 kB)

Collecting nbclient>=0.5.0 (from nbconvert->jupyter->-r requirements.txt (line 5))

  Downloading nbclient-0.11.0-py3-none-any.whl.metadata (7.3 kB)

Collecting pandocfilters>=1.4.1 (from nbconvert->jupyter->-r requirements.txt (line 5))

  Downloading pandocfilters-1.5.1-py2.py3-none-any.whl.metadata (9.0 kB)

Collecting webencodings (from bleach!=5.0.0->bleach[css]!=5.0.0->nbconvert->jupyter->-r requirements.txt (line 5))

  Downloading webencodings-0.6.1-py3-none-any.whl.metadata (3.4 kB)

Collecting tinycss2>=1.1.0 (from bleach[css]!=5.0.0->nbconvert->jupyter->-r requirements.txt (line 5))

  Downloading tinycss2-1.5.1-py3-none-any.whl.metadata (3.0 kB)

Collecting fastjsonschema>=2.15 (from nbformat>=5.3.0->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading fastjsonschema-2.22.2-py3-none-any.whl.metadata (2.1 kB)

Collecting charset_normalizer<4,>=2 (from requests>=2.31->jupyterlab-server<3,>=2.28.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading charset_normalizer-3.5.2-cp313-cp313-macosx_10_13_universal2.whl.metadata (46 kB)

Collecting urllib3<3,>=1.26 (from requests>=2.31->jupyterlab-server<3,>=2.28.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)

Collecting lark>=1.2.2 (from rfc3987-syntax>=1.1.0->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading lark-1.3.1-py3-none-any.whl.metadata (1.8 kB)

Collecting cffi>=1.0.1 (from argon2-cffi-bindings->argon2-cffi>=21.1->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading cffi-2.1.1-cp313-cp313-macosx_11_0_arm64.whl.metadata (2.5 kB)

Collecting pycparser (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi>=21.1->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading pycparser-3.11-py3-none-any.whl.metadata (8.2 kB)

Collecting soupsieve>=1.6.1 (from beautifulsoup4->nbconvert->jupyter->-r requirements.txt (line 5))

  Downloading soupsieve-3.0.3-py3-none-any.whl.metadata (4.4 kB)

Collecting arrow>=0.15.0 (from isoduration->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading arrow-1.4.0-py3-none-any.whl.metadata (7.7 kB)

Collecting tzdata (from arrow>=0.15.0->isoduration->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.19.0->jupyterlab->jupyter->-r requirements.txt (line 5))

  Downloading tzdata-2026.5-py2.py3-none-any.whl.metadata (1.4 kB)

Downloading numpy-2.5.4-cp313-cp313-macosx_14_0_arm64.whl (5.4 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.4/5.4 MB 11.5 MB/s  0:00:00

Downloading pandas-3.0.6-cp313-cp313-macosx_11_0_arm64.whl (10.1 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.1/10.1 MB 5.4 MB/s  0:00:01

Downloading matplotlib-3.11.2-cp313-cp313-macosx_11_0_arm64.whl (9.3 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.3/9.3 MB 9.4 MB/s  0:00:00

Downloading scikit_learn-1.9.1-cp313-cp313-macosx_12_0_arm64.whl (8.3 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.3/8.3 MB 13.5 MB/s  0:00:00

Downloading jupyter-1.1.1-py2.py3-none-any.whl (2.7 kB)

Downloading pytest-9.1.1-py3-none-any.whl (386 kB)

Downloading pluggy-1.6.0-py3-none-any.whl (20 kB)

Downloading contourpy-1.4.0-cp313-cp313-macosx_11_0_arm64.whl (285 kB)

Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)

Downloading fonttools-4.66.1-cp313-cp313-macosx_10_13_universal2.whl (3.1 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 15.1 MB/s  0:00:00

Downloading iniconfig-2.3.1-py3-none-any.whl (7.6 kB)

Downloading joblib-1.6.0-py3-none-any.whl (306 kB)

Downloading cloudpickle-3.1.2-py3-none-any.whl (22 kB)

Downloading kiwisolver-1.5.1-cp313-cp313-macosx_11_0_arm64.whl (64 kB)

Downloading narwhals-2.27.1-py3-none-any.whl (483 kB)

Downloading packaging-26.3-py3-none-any.whl (129 kB)

Downloading pillow-12.3.0-cp313-cp313-macosx_11_0_arm64.whl (4.8 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.8/4.8 MB 14.2 MB/s  0:00:00

Downloading pygments-2.21.0-py3-none-any.whl (1.3 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 12.1 MB/s  0:00:00

Downloading pyparsing-3.3.3-py3-none-any.whl (126 kB)

Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)

Downloading scipy-1.18.1-cp313-cp313-macosx_14_0_arm64.whl (20.5 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 20.5/20.5 MB 12.9 MB/s  0:00:01

Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)

Downloading threadpoolctl-3.7.0-py3-none-any.whl (26 kB)

Downloading ipykernel-7.4.0-py3-none-any.whl (123 kB)

Downloading appnope-1.0.0-py3-none-any.whl (4.2 kB)

Downloading comm-0.2.3-py3-none-any.whl (7.3 kB)

Downloading debugpy-1.8.22-cp313-cp313-macosx_15_0_universal2.whl (2.5 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 MB 10.2 MB/s  0:00:00

Downloading ipython-9.17.1-py3-none-any.whl (639 kB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 639.0/639.0 kB 3.1 MB/s  0:00:00

Downloading prompt_toolkit-3.0.53-py3-none-any.whl (392 kB)

Downloading ipython_pygments_lexers-1.1.1-py3-none-any.whl (8.1 kB)

Downloading jedi-0.20.1-py2.py3-none-any.whl (4.9 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.9/4.9 MB 10.4 MB/s  0:00:00

Downloading parso-0.8.7-py2.py3-none-any.whl (107 kB)

Downloading jupyter_client-8.10.0-py3-none-any.whl (110 kB)

Downloading jupyter_core-5.9.1-py3-none-any.whl (29 kB)

Downloading matplotlib_inline-0.2.2-py3-none-any.whl (9.5 kB)

Downloading nest_asyncio2-1.7.4-py3-none-any.whl (8.5 kB)

Downloading pexpect-4.9.0-py2.py3-none-any.whl (63 kB)

Downloading platformdirs-4.13.0-py3-none-any.whl (32 kB)

Downloading psutil-7.2.2-cp36-abi3-macosx_11_0_arm64.whl (129 kB)

Downloading ptyprocess-0.7.0-py2.py3-none-any.whl (13 kB)

Downloading pyzmq-27.2.0-cp312-abi3-macosx_10_15_universal2.whl (1.4 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 6.0 MB/s  0:00:00

Downloading stack_data-0.6.3-py3-none-any.whl (24 kB)

Downloading asttokens-3.0.2-py3-none-any.whl (28 kB)

Downloading executing-2.3.0-py3-none-any.whl (29 kB)

Downloading tornado-6.5.10-cp39-abi3-macosx_10_9_universal2.whl (465 kB)

Downloading traitlets-5.16.1-py3-none-any.whl (86 kB)

Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)

Downloading wcwidth-0.9.2-cp310-abi3-macosx_11_0_arm64.whl (609 kB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 610.0/610.0 kB 12.9 MB/s  0:00:00

Downloading ipywidgets-8.1.9-py3-none-any.whl (140 kB)

Downloading jupyterlab_widgets-3.0.17-py3-none-any.whl (217 kB)

Downloading widgetsnbextension-4.0.16-py3-none-any.whl (2.2 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 14.4 MB/s  0:00:00

Downloading jupyter_console-6.6.3-py3-none-any.whl (24 kB)

Downloading jupyterlab-4.6.4-py3-none-any.whl (17.2 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 17.2/17.2 MB 8.1 MB/s  0:00:02

Downloading httpx-0.28.1-py3-none-any.whl (73 kB)

Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)

Downloading jupyter_server-2.21.1-py3-none-any.whl (394 kB)

Downloading jupyterlab_server-2.28.1-py3-none-any.whl (60 kB)

Downloading anyio-4.15.1-py3-none-any.whl (132 kB)

Downloading argon2_cffi-25.1.0-py3-none-any.whl (14 kB)

Downloading async_lru-2.4.0-py3-none-any.whl (10 kB)

Downloading babel-2.18.0-py3-none-any.whl (10.2 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.2/10.2 MB 14.3 MB/s  0:00:00

Downloading h11-0.16.0-py3-none-any.whl (37 kB)

Downloading idna-3.20-py3-none-any.whl (69 kB)

Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)

Downloading json5-0.17.3-py3-none-any.whl (34 kB)

Downloading jsonschema-4.26.0-py3-none-any.whl (90 kB)

Downloading attrs-26.1.0-py3-none-any.whl (67 kB)

Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)

Downloading jupyter_builder-1.2.3-py3-none-any.whl (947 kB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 947.5/947.5 kB 18.3 MB/s  0:00:00

Downloading jupyter_events-0.12.1-py3-none-any.whl (19 kB)

Downloading jsonpointer-3.2.1-py3-none-any.whl (8.3 kB)

Downloading jupyter_lsp-2.3.1-py3-none-any.whl (77 kB)

Downloading jupyter_server_terminals-0.5.4-py3-none-any.whl (13 kB)

Downloading markupsafe-3.0.4-cp313-cp313-macosx_11_0_arm64.whl (12 kB)

Downloading nbconvert-7.17.2-py3-none-any.whl (262 kB)

Downloading mistune-3.3.4-py3-none-any.whl (66 kB)

Downloading bleach-6.4.0-py3-none-any.whl (165 kB)

Downloading nbclient-0.11.0-py3-none-any.whl (25 kB)

Downloading nbformat-5.11.1-py3-none-any.whl (79 kB)

Downloading fastjsonschema-2.22.2-py3-none-any.whl (27 kB)

Downloading notebook_shim-0.2.4-py3-none-any.whl (13 kB)

Downloading pandocfilters-1.5.1-py2.py3-none-any.whl (8.7 kB)

Downloading prometheus_client-0.26.0-py3-none-any.whl (64 kB)

Downloading python_json_logger-4.2.0-py3-none-any.whl (14 kB)

Downloading pyyaml-6.0.3-cp313-cp313-macosx_11_0_arm64.whl (173 kB)

Downloading referencing-0.37.0-py3-none-any.whl (26 kB)

Downloading requests-2.34.2-py3-none-any.whl (73 kB)

Downloading charset_normalizer-3.5.2-cp313-cp313-macosx_10_13_universal2.whl (366 kB)

Downloading urllib3-2.8.0-py3-none-any.whl (135 kB)

Downloading certifi-2026.7.22-py3-none-any.whl (136 kB)

Downloading rfc3986_validator-0.1.1-py2.py3-none-any.whl (4.2 kB)

Downloading rfc3987_syntax-1.1.0-py3-none-any.whl (8.0 kB)

Downloading lark-1.3.1-py3-none-any.whl (113 kB)

Downloading rpds_py-2026.9.1-cp313-cp313-macosx_11_0_arm64.whl (340 kB)

Downloading send2trash-2.1.0-py3-none-any.whl (17 kB)

Downloading terminado-0.18.1-py3-none-any.whl (14 kB)

Downloading tinycss2-1.5.1-py3-none-any.whl (28 kB)

Downloading webcolors-25.10.0-py3-none-any.whl (14 kB)

Downloading webencodings-0.6.1-py3-none-any.whl (8.7 kB)

Downloading websocket_client-1.9.2-py3-none-any.whl (95 kB)

Downloading argon2_cffi_bindings-26.1.0-cp310-abi3-macosx_11_0_arm64.whl (25 kB)

Downloading cffi-2.1.1-cp313-cp313-macosx_11_0_arm64.whl (184 kB)

Downloading beautifulsoup4-4.15.0-py3-none-any.whl (109 kB)

Downloading soupsieve-3.0.3-py3-none-any.whl (41 kB)

Downloading defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)

Downloading fqdn-1.6.0-py3-none-any.whl (12 kB)

Downloading isoduration-20.11.0-py3-none-any.whl (11 kB)

Downloading arrow-1.4.0-py3-none-any.whl (68 kB)

Downloading jupyterlab_pygments-0.3.0-py3-none-any.whl (15 kB)

Downloading notebook-7.6.3-py3-none-any.whl (5.5 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 12.4 MB/s  0:00:00

Downloading pure_eval-0.2.4-py3-none-any.whl (11 kB)

Downloading pycparser-3.11-py3-none-any.whl (51 kB)

Downloading rfc3339_validator-0.1.4-py2.py3-none-any.whl (3.5 kB)

Downloading tzdata-2026.5-py2.py3-none-any.whl (347 kB)

Downloading uri_template-1.3.0-py3-none-any.whl (11 kB)

Installing collected packages: pure-eval, ptyprocess, widgetsnbextension, websocket-client, webencodings, webcolors, wcwidth, urllib3, uri-template, tzdata, typing-extensions, traitlets, tornado, threadpoolctl, soupsieve, six, send2trash, rpds-py, rfc3986-validator, pyzmq, pyyaml, python-json-logger, pyparsing, pygments, pycparser, psutil, prometheus-client, pluggy, platformdirs, pillow, pexpect, parso, pandocfilters, packaging, numpy, nest-asyncio2, narwhals, mistune, MarkupSafe, lark, kiwisolver, jupyterlab_widgets, jupyterlab-pygments, jsonpointer, json5, iniconfig, idna, h11, fqdn, fonttools, fastjsonschema, executing, defusedxml, debugpy, cycler, comm, cloudpickle, charset_normalizer, certifi, babel, attrs, async-lru, asttokens, appnope, tinycss2, terminado, stack_data, scipy, rfc3987-syntax, rfc3339-validator, requests, referencing, python-dateutil, pytest, prompt_toolkit, matplotlib-inline, jupyter-core, joblib, jinja2, jedi, ipython-pygments-lexers, httpcore, contourpy, cffi, bleach, beautifulsoup4, anyio, scikit-learn, pandas, matplotlib, jupyter-server-terminals, jupyter-client, jupyter-builder, jsonschema-specifications, ipython, httpx, arrow, argon2-cffi-bindings, jsonschema, isoduration, ipywidgets, ipykernel, argon2-cffi, nbformat, jupyter-console, nbclient, jupyter-events, nbconvert, jupyter-server, notebook-shim, jupyterlab-server, jupyter-lsp, jupyterlab, notebook, jupyter

Successfully installed MarkupSafe-3.0.4 anyio-4.15.1 appnope-1.0.0 argon2-cffi-25.1.0 argon2-cffi-bindings-26.1.0 arrow-1.4.0 asttokens-3.0.2 async-lru-2.4.0 attrs-26.1.0 babel-2.18.0 beautifulsoup4-4.15.0 bleach-6.4.0 certifi-2026.7.22 cffi-2.1.1 charset_normalizer-3.5.2 cloudpickle-3.1.2 comm-0.2.3 contourpy-1.4.0 cycler-0.12.1 debugpy-1.8.22 defusedxml-0.7.1 executing-2.3.0 fastjsonschema-2.22.2 fonttools-4.66.1 fqdn-1.6.0 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 idna-3.20 iniconfig-2.3.1 ipykernel-7.4.0 ipython-9.17.1 ipython-pygments-lexers-1.1.1 ipywidgets-8.1.9 isoduration-20.11.0 jedi-0.20.1 jinja2-3.1.6 joblib-1.6.0 json5-0.17.3 jsonpointer-3.2.1 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 jupyter-1.1.1 jupyter-builder-1.2.3 jupyter-client-8.10.0 jupyter-console-6.6.3 jupyter-core-5.9.1 jupyter-events-0.12.1 jupyter-lsp-2.3.1 jupyter-server-2.21.1 jupyter-server-terminals-0.5.4 jupyterlab-4.6.4 jupyterlab-pygments-0.3.0 jupyterlab-server-2.28.1 jupyterlab_widgets-3.0.17 kiwisolver-1.5.1 lark-1.3.1 matplotlib-3.11.2 matplotlib-inline-0.2.2 mistune-3.3.4 narwhals-2.27.1 nbclient-0.11.0 nbconvert-7.17.2 nbformat-5.11.1 nest-asyncio2-1.7.4 notebook-7.6.3 notebook-shim-0.2.4 numpy-2.5.4 packaging-26.3 pandas-3.0.6 pandocfilters-1.5.1 parso-0.8.7 pexpect-4.9.0 pillow-12.3.0 platformdirs-4.13.0 pluggy-1.6.0 prometheus-client-0.26.0 prompt_toolkit-3.0.53 psutil-7.2.2 ptyprocess-0.7.0 pure-eval-0.2.4 pycparser-3.11 pygments-2.21.0 pyparsing-3.3.3 pytest-9.1.1 python-dateutil-2.9.0.post0 python-json-logger-4.2.0 pyyaml-6.0.3 pyzmq-27.2.0 referencing-0.37.0 requests-2.34.2 rfc3339-validator-0.1.4 rfc3986-validator-0.1.1 rfc3987-syntax-1.1.0 rpds-py-2026.9.1 scikit-learn-1.9.1 scipy-1.18.1 send2trash-2.1.0 six-1.17.0 soupsieve-3.0.3 stack_data-0.6.3 terminado-0.18.1 threadpoolctl-3.7.0 tinycss2-1.5.1 tornado-6.5.10 traitlets-5.16.1 typing-extensions-4.16.0 tzdata-2026.5 uri-template-1.3.0 urllib3-2.8.0 wcwidth-0.9.2 webcolors-25.10.0 webencodings-0.6.1 websocket-client-1.9.2 widgetsnbextension-4.0.16

AGENTS.md		experiments		notebooks		reports			TASKS.md

data			literature		PROJECT_CONTEXT.md	requirements.txt	tests

DECISIONS.md		meetings		README.md		src

(.venv) adrian\@Adrians-Macbook individual-project % 
