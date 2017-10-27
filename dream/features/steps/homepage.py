from behave import when, then


@when('Launch baidu homepage')
def go_to_bd_homepage(context):
    context.bdpds.homepage.gotoHomepage(context)


@then('Baidu homepage is displayed')
def check_bd_homepage_shown(context):
    currentUrl = context.bdpds.homepage.getCurrentUrl(context)
    assert 'baidu' in currentUrl
