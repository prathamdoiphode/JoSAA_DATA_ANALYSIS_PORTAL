from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

## Initialize the WebDriver .....
driver = webdriver.Chrome()

try:

    ## given url (2016-2022) .....
    url1 = "https://josaa.admissions.nic.in/applicant/seatmatrix/openingclosingrankarchieve.aspx"
    driver.get(url1)

    ## Wait for the page to load completely .....
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    ## store for all rows .....
    table_data = []

    for year in ['2016','2017','2018','2019','2020','2021','2022']:
        for round in ['1','2','3','4','5','6']:

            ## list of Year .....
            year_no = driver.find_element(
                By.XPATH, "//div[@id='ctl00_ContentPlaceHolder1_ddlYear_chosen']"
            )
            year_no.click()
            ## all input element store ....
            input_element = driver.find_elements(
                By.XPATH, "//input[@type='text']"
            )
            ## select the Year .....
            input_element[0].send_keys(year + Keys.ENTER)
            ## ................................................................
            
            ## list of Round No .....
            round_no = driver.find_element(
                By.XPATH, "//div[@id='ctl00_ContentPlaceHolder1_ddlroundno_chosen']"
            )
            round_no.click()
            ## all input element store ....
            input_element = driver.find_elements(
                By.XPATH, "//input[@type='text']"
            )
            ## select the Round No .....
            input_element[1].send_keys(round + Keys.ENTER)
            ## ................................................................

            ## list of Institute Type .....
            institute_type = driver.find_element(
                By.XPATH, "//div[@id='ctl00_ContentPlaceHolder1_ddlInstype_chosen']"
            )
            institute_type.click()
            ## all input element store ....
            input_element = driver.find_elements(
                By.XPATH, "//input[@type='text']"
            )
            ## select the Institute Type .....
            input_element[2].send_keys("ALL" + Keys.ENTER)
            ## ................................................................

            ## list of Institute Name .....
            institute_name = driver.find_element(
                By.XPATH, "//div[@id='ctl00_ContentPlaceHolder1_ddlInstitute_chosen']"
            )
            institute_name.click()
            ## all input element store .....
            input_element = driver.find_elements(
                By.XPATH, "//input[@type='text']"
            )
            ## select the Institute Name .....
            input_element[3].send_keys("ALL" + Keys.ENTER)
            ## ................................................................

            ## list of Academic Program .....
            academic_program = driver.find_element(
                By.XPATH, "//div[@id='ctl00_ContentPlaceHolder1_ddlBranch_chosen']"
            )
            academic_program.click()
            ## all input element store .....
            input_element = driver.find_elements(
                By.XPATH, "//input[@type='text']"
            )
            ## select the Academic Program .....
            input_element[4].send_keys("ALL" + Keys.ENTER)
            ## ................................................................

            ## list of Seat Type / Category .....
            category = driver.find_element(
                By.XPATH, "//div[@id='ctl00_ContentPlaceHolder1_ddlSeatType_chosen']"
            )
            category.click()
            ## all input element store .....
            input_element = driver.find_elements(
                By.XPATH, "//input[@type='text']"
            )
            ## select the Type / Category .....
            input_element[5].send_keys("ALL" + Keys.ENTER)
            ## ................................................................

            ## submit element store .....
            submit = driver.find_elements(
                By.XPATH, "//input[@type='submit']"
            )
            submit[0].send_keys("" + Keys.ENTER)

            ## .....  submit completed  ........  now data collect from table ...................

            # ## Wait for the table to be present .....
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_pnlDisplayDetails')))
                                                                                
            # ## Locate the table element .....
            # table = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_GridView1')
            # ## ................................................................

            # ## Extract table rows .....
            # rows = table.find_elements(By.TAG_NAME, 'tr')

            # ## Extract data from each row .....
            # for row in rows[1:]:  # Skip the header row
            #     cells = row.find_elements(By.TAG_NAME, 'td')
            #     row_data = [cell.text for cell in cells]
            #     ## add two element for Round_No and Year columns .....
            #     row_data = row_data + [round,year]
            #     table_data.append(row_data)
            # ## ................................................................

    ## given url 2023 .....
    url2 = "https://josaa.admissions.nic.in/Applicant/seatallotmentresult/currentorcr.aspx"
    driver.get(url2)

    ## Wait for the page to load completely .....
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    for round in ['1','2','3','4','5','6']:
        ## list of Round No .....
        round_no = driver.find_element(
            By.XPATH, "//div[@id='ctl00_ContentPlaceHolder1_ddlroundno_chosen']"
        )
        round_no.click()
        ## all input element store .....
        input_element = driver.find_elements(
            By.XPATH, "//input[@type='text']"
        )
        ## select the Round No .....
        input_element[0].send_keys(round + Keys.ENTER)
        ## ................................................................

        ## list of Institute Type .....
        institute_type = driver.find_element(
            By.XPATH, "//div[@id='ctl00_ContentPlaceHolder1_ddlInstype_chosen']"
        )
        institute_type.click()
        ## all input element store .....
        input_element = driver.find_elements(
            By.XPATH, "//input[@type='text']"
        )
        ## select the Institute Type .....
        input_element[1].send_keys("ALL" + Keys.ENTER)
        ## ................................................................

        ## list of Institute Name .....
        institute_name = driver.find_element(
            By.XPATH, "//div[@id='ctl00_ContentPlaceHolder1_ddlInstitute_chosen']"
        )
        institute_name.click()
        ## all input element store .....
        input_element = driver.find_elements(
            By.XPATH, "//input[@type='text']"
        )
        ## select the Institute Name .....
        input_element[2].send_keys("ALL" + Keys.ENTER)
        ## ................................................................

        ## list of Academic Program .....
        academic_program = driver.find_element(
            By.XPATH, "//div[@id='ctl00_ContentPlaceHolder1_ddlBranch_chosen']"
        )
        academic_program.click()
        ## all input element store ....
        input_element = driver.find_elements(
            By.XPATH, "//input[@type='text']"
        )
        ## select the Academic Program .....
        input_element[3].send_keys("ALL" + Keys.ENTER)
        ## ................................................................

        ## list of Seat Type / Category .....
        category = driver.find_element(
            By.XPATH, "//div[@id='ctl00_ContentPlaceHolder1_ddlSeattype_chosen']"
                                
        )
        category.click()
        ## all input element store ....
        input_element = driver.find_elements(
            By.XPATH, "//input[@type='text']"
        )
        ## select the Type / Category .....
        input_element[4].send_keys("ALL" + Keys.ENTER)
        ## ................................................................

        ## submit element store ....
        submit = driver.find_elements(
            By.XPATH, "//input[@type='submit']"
        )
        # print(len(submit))
        submit[0].send_keys("" + Keys.ENTER)

        ## .....  submit completed  ........  now data collect from table ...................

    #     ## Wait for the table to be present .....
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_pnlDisplayDetails')))
                                                                            
    #     ## Locate the table element .....
    #     table = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_GridView1')
    #     ## ................................................................                                   

    #     ## Extract table rows
    #     rows = table.find_elements(By.TAG_NAME, 'tr')

    #     ## Extract data from each row .....
    #     for row in rows[1:]:  # Skip the header row
    #         cells = row.find_elements(By.TAG_NAME, 'td')
    #         row_data = [cell.text for cell in cells]
    #         ## add two element for Round_No and Year columns .....
    #         row_data = row_data + [round,"2023"]
    #         table_data.append(row_data)
    #     ## ................................................................

    # ## ........ completed data collect from table ...... now convert to DataFrame .............

    # ## Locate the table element .....
    # table = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_GridView1')

    # ## Extract table headers .....
    # headers = table.find_elements(By.TAG_NAME, 'th')
    # header_data = [header.text for header in headers]
    # ## add Round_No and Year columns ......
    # header_data = header_data + ["Round_No","Year"]
    # # print(header_data)
    # ## ................................................................

    # ## Convert to pandas DataFrame .....
    # df = pd.DataFrame(table_data, columns=header_data)

    # ## Display the DataFrame .....
    # # print(df)

    # # Save to CSV if needed .....
    # df.to_csv('josaa_table_data_(2016_2023).csv', index=False)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    time.sleep(5)
    ## Close the browser .....
    driver.quit()
