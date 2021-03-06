##########################################################################
#
# pgAdmin 4 - PostgreSQL Tools
#
# Copyright (C) 2013 - 2019, The pgAdmin Development Team
# This software is released under the PostgreSQL Licence
#
##########################################################################


def close_bgprocess_popup(tester):
    """
    Allows us to close the background process popup window
    """
    screen_shot_taken = False
    # In cases where backup div is not closed (sometime due to some error)
    try:
        if tester.driver.find_element_by_css_selector(
                ".ajs-message.ajs-bg-bgprocess.ajs-visible"):
            tester._screenshot()
            screen_shot_taken = True
            tester.driver.find_element_by_css_selector(
                ".btn.btn-sm-sq.btn-primary.pg-bg-close > i").click()
    except Exception:
        pass

    # In cases where restore div is not closed (sometime due to some error)
    try:
        if tester.driver.find_element_by_xpath(
                "//div[@class='card-header bg-primary d-flex']/div"
                "[contains(text(), 'Restoring backup')]"):
            tester._screenshot()
            screen_shot_taken = True
            tester.driver.find_element_by_css_selector(
                ".btn.btn-sm-sq.btn-primary.pg-bg-close > i").click()
    except Exception:
        pass

    # In cases where maintenance window is not closed (sometime due to some
    # error)
    try:
        if tester.driver.find_element_by_xpath(
                "//div[@class='card-header bg-primary d-flex']/div"
                "[contains(text(), 'Maintenance')]"):
            tester._screenshot()
            screen_shot_taken = True
            tester.driver.find_element_by_css_selector(
                ".btn.btn-sm-sq.btn-primary.pg-bg-close > i").click()
    except Exception:
        pass

    if not screen_shot_taken:
        tester._screenshot()
