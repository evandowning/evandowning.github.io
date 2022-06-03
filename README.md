# evandowning.github.io
My website

## Modifying
  - Install themes & plugins
    ```
    $ git clone --recursive git@github.com:getpelican/pelican-themes.git
    $ git clone --recursive git@github.com:getpelican/pelican-plugins.git
    ```
  - Download repo
    ```
    $ git clone https://github.com/evandowning/evandowning.github.io.git`
    $ cd evandowning.github.io/
    $ git checkout source
    ```
  - Install requirements
    ```
    $ mkvirtualenv website --python=python3
    (website) $ pip install -r requirements.txt
    ```
  - Make modifications and visit `localhost:8000`
    ```
    $ make devserver
    ```
  - Make output for Github
    ```
    $ make github
    ```
  - Commit changes and push to `source` branch
