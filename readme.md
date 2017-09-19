# Texts Statistical Analysis

Analyzes texts for compliance with the Zipf's second law and Heaps' law.

Prerequisites
-------------

Having Python 3 installed, clone the project and install its dependencies:

```bash
git clone git@github.com:ZitRos/edu-texts-analyzer.git
cd edu-texts-analyzer
pip3 install -r requirements.txt
```

Texts for analysis are taken from `texts` directory.
Every file in this directory and its subdirectories will be treated as a text file.
There are already some articles, but you may place your own.

Zipf's Law
----------

Having Python 3 installed, install dependencies and run the program: 

```bash
py index.py
```

It will generate `Zipf.xlsx` file with word ranks/frequencies data.

![Zipf's Law](https://user-images.githubusercontent.com/4989256/30581003-a1c5072e-9cec-11e7-90da-6376ddd9198d.png)

Heaps' Law
-----------

Output will go to `Heaps.xlsx` file.

![Heaps Law](https://user-images.githubusercontent.com/4989256/30581002-a1a844f4-9cec-11e7-8470-6a13a006d92e.png)