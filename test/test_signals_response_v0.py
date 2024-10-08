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

from fideo_api.models.signals_response_v0 import SignalsResponseV0

class TestSignalsResponseV0(unittest.TestCase):
    """SignalsResponseV0 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SignalsResponseV0:
        """Test SignalsResponseV0
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SignalsResponseV0`
        """
        model = SignalsResponseV0()
        if include_optional:
            return SignalsResponseV0(
                name = fideo_api.models.name.Name(
                    given_name = '', 
                    family_name = '', ),
                demographics = fideo_api.models.demographics.Demographics(
                    age = 56, 
                    age_range = '', 
                    gender = '', 
                    location_general = '', ),
                locations = [
                    fideo_api.models.location.Location(
                        address_line1 = '', 
                        address_line2 = '', 
                        city = '', 
                        region = '', 
                        region_code = '', 
                        country = '', 
                        country_code = '', 
                        postal_code = '', 
                        formatted = '', )
                    ],
                emails = [
                    fideo_api.models.email.Email(
                        first_seen_ms = 56, 
                        last_seen_ms = 56, 
                        observations = 56, 
                        confidence = 1.337, 
                        value = '', 
                        md5 = '', 
                        sha1 = '', 
                        sha256 = '', 
                        label = '', 
                        activity = 1.337, )
                    ],
                phones = [
                    fideo_api.models.phone.Phone(
                        first_seen_ms = 56, 
                        last_seen_ms = 56, 
                        observations = 56, 
                        confidence = 1.337, 
                        label = '', 
                        value = '', )
                    ],
                person_ids = [
                    ''
                    ],
                ip_addresses = [
                    fideo_api.models.ip_address.IpAddress(
                        first_seen_ms = 56, 
                        last_seen_ms = 56, 
                        observations = 56, 
                        confidence = 1.337, 
                        id = '', )
                    ],
                message = '',
                social_profiles = fideo_api.models.social_profile_urls.SocialProfileUrls(
                    twitter_url = '', 
                    linked_in_url = '', ),
                employment = fideo_api.models.employment.Employment(
                    current = True, 
                    company = '', 
                    title = '', 
                    domain = '', 
                    start = fideo_api.models.employment_date.EmploymentDate(
                        year = 56, 
                        month = 56, 
                        day = 56, ), 
                    end = fideo_api.models.employment_date.EmploymentDate(
                        year = 56, 
                        month = 56, 
                        day = 56, ), )
            )
        else:
            return SignalsResponseV0(
        )
        """

    def testSignalsResponseV0(self):
        """Test SignalsResponseV0"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
