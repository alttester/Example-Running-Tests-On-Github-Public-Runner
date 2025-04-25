# For more info on the setup, check out our docs https://alttester.com/docs/sdk/latest/pages/get-started.html#write-and-execute-first-test-for-your-app  
*** Variables ***
${textscreen__footer_path}    /RuntimePanelSettings/FlexboxDemo-container/background/text-screen__container/text-screen__footer

*** Settings ***
Library    AltTesterLibrary
Suite Setup    Setup Environment
Suite Teardown    Stop AltDriver

*** Keywords ***
Setup Environment
    Initialize AltDriver    127.0.0.1    13000    __default__
    # You might want to load the scene here
    # Load Scene    FlexboxDemo

*** Test Cases ***
Test
    Load Scene    FlexboxDemo
    ${textscreen__footer} =    Wait For Object    PATH    ${textscreen__footer_path}    timeout=20
    Wait For Visual Element Property    ${textscreen__footer}    marginRight    0   20    get_property_as_string=${True}

