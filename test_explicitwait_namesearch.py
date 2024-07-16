""""
Test the filled data in the input boxes,select boxes and dropdown menu using python selenium pytest
"""

from explicitwait_namesearch import Name_Search
import pytest

url="https://www.imdb.com/search/name/"
name_search=Name_Search(url)

def test_start():
    assert name_search.start() == True
    print("Success : web page url is loaded successfully")

def test_search():
    assert name_search.search() == None
    print("Success : Automation of webpage using explicit wait has done ")
