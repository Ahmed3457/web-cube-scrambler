
# Web Cube scrambler

I made this since [**Cube desk**](https://cubedesk.io) doesn't have Last Layer scrambles and F2L scrambles.

# Running locally

if you are using windows, you can use the pre-built binaries but if you are on mac os or Linux you have to run it from the source code.

you need the following:

1. Python 3.8

2. Pip 3

3. --NodeJS (Required for the scrambling library)-- **Just skip this, i added the nodejs-bin pypi package it fixes it**

4. Git (optional)

  

The **First step** is to clone this repo

```Bash
git clone https://github.com/Ahmed3457/web-cube-scrambler
```

alternatively, you can just download the source code from the GitHub web interface.

  

The **Second step** is to install the libraries.

```bash
cd web-cube-scrambler
python -m pip install -r requirements.txt
```

the **Third step** is just to run the file

```bash
python main.py
```

You also can run it on any **port** your not just limited to 5000

```bash
#The following command starts the scrambler at the port 8080
python main.py 8080
```  

if you encounter any Errors, please open an **Issue**

  

# To-Do

TO-DO

- [ ] Improve the GUI

- [x] Add a timer

- [ ] Add 2 Look OLL scrambles

- [ ] Add 2 Look PLL scrambles

  

# License

To ensure This project is **Free for everyone** this project is published under the **GNU GPL-3.0** License or later.
