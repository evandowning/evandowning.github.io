# evandowning.github.io
My website

## Modifying
  - Download repo
    ```
    $ git clone https://github.com/evandowning/evandowning.github.io.git`
    $ git checkout source
    ```

  - Install requirements
    ```
    $ mkvirtualenv website --python=/usr/bin/python3
    $ pip install pelican Markdown ghp-import
    ```

  - Make modifications and test
    ```
    # Start website
    $ make devserver

    # Visit localhost:8000

    # Stop website
    $ make stopserver
    ```

  - Make output for Github
    ```
    $ make github
    ```

  - Commit changes and push to `source` branch
