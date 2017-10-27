from selenium import webdriver

from baidu.products.bdproducts import BDProducts
from baidu.products.homepage import HomePage as homepage


def get_driver(context):
    return webdriver.Chrome()


class bdTest(object):
    def __init__(self, driver):
        self.driver = driver
        self.bdpds = BDProducts(self.driver)

    def close_driver(self):
        self.driver.close()


def before_all(context):
    context.driver = get_driver(context)
    context.bdpds = bdTest(context.driver)
    setattr(context.bdpds, 'homepage', homepage)


def after_all(context):
    """ Clean up function"""
    context.driver.quit()
