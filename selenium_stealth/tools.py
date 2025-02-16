import json


def execute_cdp_cmd(driver, cmd, params={}):
    """Alternative cdp_cmd for remote driver"""
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd': cmd, 'params': params})
    response = driver.command_executor._request('POST', url, body)

    return response.get('value')
