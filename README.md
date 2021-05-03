German Bulk Translator
=========

Simple bulk German translation script built on the ![rbaron/dict.cc.py API](https://github.com/rbaron/dict.cc.py) in Python. It uses a forked version of the API with additional modifications for UTF-8 support and error debugging.

Installation
------------

No installation is required. 

Usage
-----

```bash
$ python translatebulk.py from_language to_language input_file.csv output_file_name
```

All of the arguments are optional and default to the following:
```bash
$ python translatebulk.py de en words.csv translated
```

It's super easy! Here's a quick example of using it to translate a list of words in (`csv`) format from German (`de`) to English (`en`):

```bash
$ python3 translatebulk.py de en words.csv
Progress:███████████████████████████| 100% Done
```

The code outputs a (`csv`) and (`xlsx`) files in UTF-8 encoding.

Available languages include: `en`, `de`, `sv`, `pt`, `it`, `fr`, `ro`, `nl`.

License
-------

Public domain.

Progressbar.py copied from StackOverFlow
