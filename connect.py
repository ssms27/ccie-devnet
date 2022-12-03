from ciscoisesdk import IdentityServicesEngineAPI
from ciscoisesdk.exceptions import ApiError


def ise_cisco():
    ISE_SERVER = '10.10.20.77'
    ISE_SERVER_HTTPS = 'https://10.10.20.77'
    ISE_SERVER_PWD = 'C1sco12345'
    ISE_SERVER_UID = 'admin'
    DEVBOX = '10.10.20.50'
    DEVBOX_UID = 'developer'
    DEVBOX_PWD = 'C1sco12345'
    RADIUS = '10.10.20.32'
    RADIUS_UID = 'developer'
    RADIUS_PWD = 'C1sco12345'

    api = IdentityServicesEngineAPI(username=ISE_SERVER_UID,
                                    password=ISE_SERVER_PWD,
                                    uses_api_gateway=True,
                                    base_url=ISE_SERVER_HTTPS,
                                    version='3.1_Patch_1',
                                    verify=True,
                                    debug=False,
                                    uses_csrf_token=False)

