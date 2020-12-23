# newScraper
A python tool for downloading newspaper articles

## Requirements
- Python 3.x downloadable from [HERE](https://www.python.org/downloads/)
- Chrome driver
    - Check your Chrome version by typing *"chrome://settings/help"* on the search bar and download the corresponding chromedriver from [HERE](https://chromedriver.chromium.org/downloads)
    - Move the downloaded *chromedriver.exe* file in the tool folder

## How to use

### Dataset Nameing
- Place datasets in the *dataset/* folder
- Rename the datasets using the following format
    - For usatoday use *www-usatoday-com.csv*

### Script execution
- Only the first time, open the CMD in the script folder and run `pip install -r requirements.txt`
- Run the script using the following format py main.py website start_index end_index where:
    - website is an integer and represents the website: *1=usatoday*
    - **start_index** and **end_index** are optional and represent the rows range to analyze

Examples:
- `py main.py 1`: execute the script on the entire usatoday's dataset
- `py main.py 1 1000 2000`: execute the script from the record 1000 to 2000 on the usatoday's dataset

The script overwrites the input dataset with the results every 100 records analyzed