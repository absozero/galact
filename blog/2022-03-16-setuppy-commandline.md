---
slug: setup-cli
title: Migrating Galact to a cli structure for scalability
authors:
  name: Absozero
  title: Galact maintainer, original author
  url: https://github.com/absozero
  image_url: https://github.com/absozero.png
tags: [Galact, CLI]
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


The whole repo has now been migrated to a comman line setup. This was to improve scalability, improve portability, as well as to make the project migrate from a more **one file -type** structure to a more common and usable format that would help the app have arguments and only a requirement for pip and python.

This new format means that instead of calling `python bot/galact.py` you can just install the package directly using:

<Tabs>
  <TabItem value="main" label="stable" default>
    
    pip install git+https://github.com/absozero/galact.git
    
  </TabItem>
  <TabItem value="testing" label="unstable">
    pip install git+https://github.com/absozero/galact.git@Testing
  </TabItem>
  <TabItem value="pipenv" label="pipenv">
    pipenv install git+https://github.com/absozero/galact.git
  </TabItem>
  <TabItem value="pypi" label="When on pypi(cannot as such)">
    pip install galact
  </TabItem>
</Tabs>
pipenv install -e git+ssh://git@github.com/shearichard/behave-web-api.git#egg=behave-web-api
And then you can run the command and open the help menu with this in the command line:
```bash
galact
```
- The main branch is stable and you will get code that most likely will not break, there is unstable code for installation, and the final one is how the install command would look when the command is on pypi

This should be temporary until the package is published to [PyPi](https://pypi.org), where then the package can just be installed by name.