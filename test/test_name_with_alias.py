# coding: utf-8

"""
    Fideo API

    Fideo Intelligence offers an identity intelligence product that protects the public good. - [Fideo Privacy Policy](https://www.fideo.ai/privacy-policy/)

    The version of the OpenAPI document: 1.0.4
    Contact: support@fideo.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fideo_api.models.name_with_alias import NameWithAlias

class TestNameWithAlias(unittest.TestCase):
    """NameWithAlias unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NameWithAlias:
        """Test NameWithAlias
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NameWithAlias`
        """
        model = NameWithAlias()
        if include_optional:
            return NameWithAlias(
                first = '',
                last = '',
                middle = '',
                given_name = '',
                family_name = '',
                aliases = [
                    fideo_api.models.alias.Alias(
                        first = '', 
                        last = '', 
                        middle = '', )
                    ]
            )
        else:
            return NameWithAlias(
        )
        """

    def testNameWithAlias(self):
        """Test NameWithAlias"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
