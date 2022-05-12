202205121250

The project specification calls for the addition/creation of a
flask backend to host an existing javascript website. Flask
defines a folder structure and requires various files of the
same type to exist within specific areas of that structure.

Here is an generic example:

my-flask-app
   ├── static/
   │   └── css/
   │       └── main.css
   ├── templates/
   │   ├── index.html
   │   └── student.html
   ├── data.py
   └── students.py

Notice that 'static' would also hold javascript, image and audio
files.

The templates folder holds the html templates, which are hyper
text markup language documents with flask python interleaved
through out. This mixing of the python and html makes the web
pages customizable on demand from the webserver.

Unfortunately this imposed file structure is a requirement of
Flask. Thus the original files may require links adding or
updating to reflect the new location of target files.
