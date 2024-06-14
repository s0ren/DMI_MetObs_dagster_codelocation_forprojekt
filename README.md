# A dagste project to get ALL weather 

## Limitation
At this time (and probebly forever) it will only get observations from DMI.

## API key


DMI api requires that you provide an API key. Currently you can get one for free, by following theese steps:

1. First setting up an account at https://dmiapi.govcloud.dk/#!/, click __LOGIN__ in upper-left, and the register in the bottum of the popup.

1. then click __APP GALLERY__ in the menu to the left,
    1. navigate to __metObsAPI__
    1. ...

In this demo there is an API key in .env.example, but it is proberbly not active. So get an create your own.

## Data

The first asset is the raw data, storred in json files.

Later assets will hold transformations of this in more structured formats.