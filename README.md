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
    $ git clone https://github.com/evandowning/evandowning.github.io.git
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
  - Push website content to Github
    ```
    $ make github
    ```
  - Commit changes and push to `source` branch

## Google Analytics
  - If theme doesn't support updated Google Analytics tags, add this to `base.html` in the theme's folder:
    ```
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={{ GOOGLE_ANALYTICS }}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', '{{ GOOGLE_ANALYTICS }}');
    </script>
    <!-- End Google Analytics -->
    ```
