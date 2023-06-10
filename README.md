# Open Mindset app

Mobile python application

Application developed in Python using KivyMD

### Managing environment

#### Python >= 3.9 on MacOS

    brew update
    brew install python3
    brew upgrade python3

#### Current requirements (freeze them or install from)

    pip freeze > requirements.txt
    pip install -r requirements.txt

#### Upgrade then freeze requirements

    pip install pip-review
    pip-review --local --interactive
    pip freeze > requirements.txt

### Building Android app

    brew install cython
    echo 'export PATH="/opt/homebrew/opt/cython/bin:$PATH"' >> ~/.zshrc

#### Changing default python executable using simlink
    brew install python@3.11
    brew install python@3.8
    brew unlink python@3.11
    brew unlink python@3.8
    brew link --force python@3.8

    sudo rm /usr/local/bin/python
    sudo ln -s /opt/homebrew/Cellar/python@3.8/3.8.17/bin/python3.8 /usr/local/bin/python
    sudo ln -s /opt/homebrew/Cellar/python@3.11/3.11.3/bin/python3 /usr/local/bin/python


* https://kivy.org/doc/stable/guide/packaging-android.html

    python ~/Library/Python/3.8/lib/python/site-packages/buildozer init
    python ~/Library/Python/3.8/lib/python/site-packages/buildozer android debug deploy run

Ugly workaround for [ssl issue](https://github.com/kivy/kivy/issues/5784):
    code /Library/Frameworks/Python.framework/Versions/Current/lib/python3.10/ssl.py

sdkmanager path  does not exist, sdkmanager is notinstalled
    https://github.com/kivy/buildozer/issues/927#issuecomment-533020886

#### Reference

* see https://stackoverflow.com/a/16269635/704681


#### Others

    adb logcat -e org.amwebexpert.openmindset
    