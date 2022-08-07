*** Settings ***
Documentation     Suite description
Resource          common.robot
Variables         ../test_data/qa.py
Library           SeleniumLibrary
Library           String
Library           Collections
Library           py_keyword/pykeyword1.py

*** Test Cases ***
Test 1
    [Tags]    DEBUG
    log    ${testvar1}
    ${x}    test_py    8

*** Keywords ***

