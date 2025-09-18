# evandowning.github.io

My website

## Modifying

* Clone themes & plugins

    ```shell
    git clone --recursive git@github.com:getpelican/pelican-themes.git
    git clone --recursive git@github.com:getpelican/pelican-plugins.git
    ```

* Clone this repo

    ```shell
    git clone https://github.com/evandowning/evandowning.github.io.git
    cd evandowning.github.io/
    git checkout source
    ```

* Install requirements

    ```shell
    # Create a 'website' python virtual environment.
    python3 -m venv website
    source website/bin/activate

    # Install dependencies
    (website) $ pip install --upgrade pip
    (website) $ pip install -r requirements.txt
    ```

* Make modifications and visit `localhost:8000`

    ```shell
    (website) $ make devserver
    ```

* Push all content to `master` branch & Publish website

    ```shell
    (website) $ make github
    ```

* Commit changes and push to `source` branch

## Google Analytics

* If theme doesn't support the updated Google Analytics tags, add this to `base.html` in the theme's folder:

    ```javascript
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={{ GOOGLE_ANALYTICS }}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', '{{ GOOGLE_ANALYTICS }}');
    </script>
    ```
