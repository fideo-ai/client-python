# coding: utf-8

"""
    Fideo API

    This is a representation of the Fideo API based on the OpenAPI 3.0 specification.  You can find out more about Swagger at [https://swagger.io](https://swagger.io). Some useful links: - [Fideo Privacy Policy](https://www.fideo.ai/privacy-policy/)

    The version of the OpenAPI document: 1.0.0
    Contact: support@fideo.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fideo_api.models.person_name_req import PersonNameReq

class TestPersonNameReq(unittest.TestCase):
    """PersonNameReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonNameReq:
        """Test PersonNameReq
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonNameReq`
        """
        model = PersonNameReq()
        if include_optional:
            return PersonNameReq(
                given = '',
                family = '',
                middle = '',
                prefix = '',
                suffix = '',
                nickname = '',
                full = ''
            )
        else:
            return PersonNameReq(
        )
        """

    def testPersonNameReq(self):
        """Test PersonNameReq"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
