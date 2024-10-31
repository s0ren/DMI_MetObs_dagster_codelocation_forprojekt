# A dagster project to get ALL weather 

## Limitation
At this time (and probably forever) it will only get observations from DMI.

## Setup

### 0.   Virtual Environment

Lav eventuelt et virtualt environment med VS Code

### 1.  Installer Dagster

Kør:

    winget install rustup
    winget install cargo
    pip install dagster dagster-webserver

Se https://docs.dagster.io/getting-started/install


## 2.   installer afhængigheder i projektet

Kør 

    pip install -e ".[dev]"      

Se [template_README.md](template_README.md)


## API key

DMI api requires that you provide an API key. Currently you can get one for free, by following these steps:

1. First setting up an account at https://dmiapi.govcloud.dk/#!/, click __LOGIN__ in upper-left, and the register in the bottom of the popup.

1. then click __APP GALLERY__ in the menu to the left,
    1. navigate to __metObsAPI__
    1. ...

In this demo there is an API key in .env.example, but it is probably not active. So get an create your own.

## Data

The first asset is the raw data, stored in json files.

Later assets will hold transformations of this in more structured formats.