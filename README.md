# Source for https://www.boinor.space

This repository contains the source for https://www.boinor.space/.

_Based on the wonderful job by Jake Vanderplas https://github.com/jakevdp/jakevdp.github.io-source (MIT License)_
_Also based on the wonderful job by Juan Luis Cano and poliastro development team. (MIT License)_

[![boinor website CI](https://github.com/boinor/boinor.github.io/actions/workflows/main.yml/badge.svg)](https://github.com/boinor/boinor.github.io/actions/workflows/main.yml)

## Building the website

Clone the repository & make sure submodules are included

```
$ git clone https://github.com/boinor/boinor.github.io-source.git
$ git submodule update --init --recursive
```

_(Activate the python virtual environment before proceeding)_

Install pip-tools `pip install pip-tools`
In case it is needed, rebuild the requitements.txt (maybe remove the old version and start from scratch).
Install the required packages using `pip install -r requirements.txt`

Build the html and serve locally:

```
$ make html
$ make serve
$ open http://localhost:8000
or
$ make html
$ make serve-global SERVER=1.2.3.4
$ open http://1.2.3.4:8000

```

Deploy to github pages

```
$ make publish-to-github
```

## Development

To regenerate the main CSS:

```
$ lessc main.less > main.css
```
