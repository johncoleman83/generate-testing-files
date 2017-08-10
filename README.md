# generate testing files

a python application, to generate testing `main.` files & your code files with
templates for Holberton School projects.

## Environment

  * __language:__ Python 3.6.10
  * __libraries:__ os

## Configuration

* __clone__: clone this repo in the directory you will work in
* __move files__: move files into testing directory and delete repo

```
$ git clone https://github.com/johncoleman83/generate-testing-files.git
$ mv generate-testing-files/*.py .
$ mv generate-testing-files/execute.sh .
$ touch intrapage.txt
$ rm -rf generate-testing-files/
```

* __manual parse__: manually copy and paste the entire contents from intranet
  page that contains the testing `main.` files that you need
* __save file__: create file, paste content from Holberton Intranet into the
  file. In my example, I save the file as: `intrapage.txt`
* __Note:__: the file `intrapage.txt` in this repo is only an example

```
$ emacs intrapage.txt
```

* __read the code__: ensure that your configureations in `generate.py` are
  correct.  If you followed the above instructions correctly, you should not
  have to do anything for this step, except understand the code.  You may need
  to change the string `END` depending on what user generated the testing files
  in the intranet example

## Usage

```
$ ./execute.sh
```

* Then select which tests you want to run based on the intranet page

## To Do

* Make script to create `./tests` directory
* switch file creation method to use `.split(',')` instead of long-parse
* use beautifulsoup to parse intranet for me

## Author

David John Coleman II, [davidjohncoleman.com](http://www.davidjohncoleman.com/)

## License

Public Domain, no copyright protection
