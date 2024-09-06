# coding: utf-8

"""
    Fideo API

    Fideo Intelligence offers an identity intelligence product that protects the public good. - [Fideo Privacy Policy](https://www.fideo.ai/privacy-policy/)

    The version of the OpenAPI document: 1.0.4
    Contact: support@fideo.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class IPCountry(str, Enum):
    """
    IPCountry
    """

    """
    allowed enum values
    """
    DOMESTIC = 'DOMESTIC'
    FOREIGN = 'FOREIGN'
    UNKNOWN = 'UNKNOWN'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IPCountry from a JSON string"""
        return cls(json.loads(json_str))


