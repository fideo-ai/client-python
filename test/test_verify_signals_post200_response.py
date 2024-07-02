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

from fideo_api.models.verify_signals_post200_response import VerifySignalsPost200Response

class TestVerifySignalsPost200Response(unittest.TestCase):
    """VerifySignalsPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VerifySignalsPost200Response:
        """Test VerifySignalsPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VerifySignalsPost200Response`
        """
        model = VerifySignalsPost200Response()
        if include_optional:
            return VerifySignalsPost200Response(
                name = fideo_api.models.name_with_alias.NameWithAlias(
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
                        ], ),
                demographics = fideo_api.models.demographics.Demographics(
                    age = 56, 
                    age_range = '', 
                    gender = '', 
                    location_general = '', ),
                locations = [
                    fideo_api.models.location.Location(
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
                social_profiles = [
                    fideo_api.models.social_profile_details.SocialProfileDetails(
                        username = '', 
                        userid = '', 
                        url = '', 
                        bio = '', 
                        service = '', 
                        followers = 56, 
                        following = 56, )
                    ],
                employment = [
                    fideo_api.models.employment.Employment(
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
                    ],
                education = [
                    fideo_api.models.education.Education(
                        name = '', 
                        degree = '', 
                        end = fideo_api.models.education_date.EducationDate(
                            year = 56, 
                            month = 56, 
                            day = 56, ), )
                    ],
                photos = [
                    fideo_api.models.photo.Photo(
                        url = '', 
                        label = '', )
                    ],
                economic = fideo_api.models.economic.Economic(
                    dwelling_type = '', 
                    home_ownership = '', 
                    marital_status = '', 
                    presence_of_children = '', 
                    income = '', 
                    net_worth = '', )
            )
        else:
            return VerifySignalsPost200Response(
        )
        """

    def testVerifySignalsPost200Response(self):
        """Test VerifySignalsPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
