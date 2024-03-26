def click_Xpath(driver, wait_time, str_path):
    """
    Clicks on an element using its xpath.

    Args:
        driver: The WebDriver instance.
        wait_time: The amount of time to wait for the element to be clickable.
        str_path: The xpath of the element to click.
    """
    try:
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, str_path))).click()
    except TimeoutException:
        print("Element not found or not clickable")
        raise

