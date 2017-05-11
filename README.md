# generate testing files

:a python application, to generate testing files for Holberton School

### python

  * __language:__ Python 3.6.10
  * __libraries:__ os

## Configuration

* __clone__: clone this repo in the directory you will work in
* __move files__: move files into testing directory and delete repo

```
$ git clone https://github.com/johncoleman83/generate-testing-files.git
$ mv generate-testing-files/generatemain.py . && touch intrapage.txt
$ rm -rf generate-testing-files/
```

* __manual parse__: manually copy and paste the entire contents from intranet
  page that contains the testing `main.` files that you need
* __save file__: create file, paste content from Holberton Intranet into the
  file. In my example, I save the file as: `intrapage.txt`

```
$ emacs intrapage.txt
```

* __read the code__: ensure that your configureations in `generatemain.py` are
  correct.  If you followed the above instructions correctly, you should not
  have to do anything for this step, except understand the code.  You may need
  to change the string `END` depending on what user generated the testing files
  in the intranet example

## Usage

```
$ ./generatemain.py
```

## Author

David John Coleman II.	Check out my website [davidjohncoleman.com](http://www.davidjohncoleman.com/)

## License

Public Domain, no copyright protection
