stratotraffic
=============

[![License](http://img.shields.io/badge/license-MIT-red.svg)](https://github.com/KoffeinFlummi/stratotraffic/blob/master/LICENSE)

Read/unlock your strato.de server traffic/speed from the command line.


### Setup

Requires an installation of [tesseract](https://github.com/tesseract-ocr/tesseract) to be installed and in your PATH.

```
$ python3 setup.py install
```


### Usage

```
stratotraffic

Usage:
  stratotraffic status
  stratotraffic unlock
  stratotraffic (-h | --help)
  stratotraffic (-v | --version)

Commands:
  status  Show traffic status
  unlock  Unlock traffic

Options:
  -h --help     Show this help and exit
  -v --version  Show version information and exit
```


### Disclaimer

This project includes code to circumvent Strato's captchas. Please don't use it for any malicious purposes. Also, if you're a Strato employee reading this, please know that the reason why I created this is because there's no easy way to set a custom confirmation limit for traffic or an API for unlocking it. (hinthint)
