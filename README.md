# Alten

> A testing application project that consists of two tests first is to test a REST API and the second is to perform some web testing.

As requested in the description: 

1. Test a REST API: Perform a GET request on a specific [URL](https://api.covid19api.com/total/country/germany) and 
validate that the response status code is 200 and print out some of the response in a specific format.

2. Web Testing: Create a web driver object access the [Alten](https://www.alten.es/) landing page:
    - Verify that the country selected is "SPAIN"
    - List all the sub-menu items text from the "Sectores" item in the nav bar.

## Workflow

##### Initial setup
1. I created my project set up with an `__init__.py` to initialise the directory as a python package.
2. I created a tests directory - to house all of the test files (also initialised with an `__init__.py`.
3. I installed relevant packages using PIP such as `nose2` for testing purposes and `selenium` for creating a webdriver, 
and also `requests` library for performing HTTP methods.

##### Test a REST API
I created a module called `test_rest_api` within the `tests` directory. I created my class `TestRestApi` and provided it 
a `setUp` method to make a HTTP GET request method to the [URL](https://api.covid19api.com/total/country/germany). I used
the Python library `requests` for this action as it is useful to make requests and responses, and the ability to inspect data from 
them with ease.

I wrote a test method to handle checking if the response status code was 200, I asserted equal. I also wrote another test
method to assert a fail if it didn't equal 200.

I printed data to console with a specific format of some of the json loaded response.

##### Web Testing
For this part of the section I had to create a webdriver object, so I choose to use selenium as it is highly suited for this
type of work, by this I mean finding elements, web automation. I actually originally thought to solve this problem with the html parser
BeautifulSoup4 as I would not have needed to create a webdriver object and instead use the requests library to make a HTTP request
and parse the html and then manipulate in my code. However as the problem stated to use a webdriver object I used selenium.

In my `setUp` and `tearDown` methods I created the firefox webdriver and quit respectively.

The first question asked me to determine if the country selected is "SPAIN". I solved this by finding the span element
that displays the country selected by xpath. I choose to use xpath as it is more reliable than class or relative paths. I created
two methods one to assert true if the text value is Spain and another to assert false if France.

The second question asked me to get and list the child elements of the "Sectores" tab. Using the webdriver again. I navigated
to the page using xpath to find element with the text content for "Sectores" I clicked this element, then I found the sub-element
ul. On this element I used selenium to find all the li elements and I ran two assertions to check the text of the first and last
elements in that list (this will fail if the elements are changed, or the html changes). I then printed them out to console.

## Development Setup

##### Pre-requisites

Geckodriver needs to be installed and in the path it can be downloaded from [here]( https://github.com/mozilla/geckodriver/releases).

- If using windows you can put it in the same folder as this one.
- For linux you can store it in the `/usr/local/bin` folder. You will need to use `sudo` for this.

Firefox needs to be installed it can be found [here](https://www.mozilla.org/en-US/firefox/).



Create a virtual environment within the repo and then install `requirements.txt`: 

##### Linux:

``` 
user@pc~Alten/$ python3 -m venv env 

user@pc~Alten/$ source env/bin/activate 

(env) user@pc~Alten/$ pip install -r requirements.txt 

``` 

##### Windows: 

Create a virtual environment within the repo and then install `requirements.txt`: 

``` 
C:\Users\your_user\Documents\Alten\>py -m venv env 

C:\Users\your_user\Documents\Alten\>env\Scripts\activate.bat 

(env) C:\Users\your_user\Documents\Alten\> pip install -r requirements.txt 

```

## Running Tests

I used `nose2` as it has the ability to combine all tests it find into one, but also allows tests to be run individually.


- To run all tests (when in current directory)

`$ nose2`

- To run all tests from one module

`$ nose2 -s tests <module_name>`

Where module name is one of the file names in the tests folder.

- To run specific test from one module

`$ nose2 -s tests <module_name>:<method_name>`

Where `<module_name>` is one of the file names in the tests folder and `<method_name>` is the specific test method you
want to run.

## Release History 

* 0.0.1
