# coding: utf-8

"""
    Fideo API

    This is a representation of the Fideo API based on the OpenAPI 3.0 specification.  You can find out more about Swagger at [https://swagger.io](https://swagger.io). Some useful links: - [Fideo Privacy Policy](https://www.fideo.ai/privacy-policy/)

    The version of the OpenAPI document: 1.0.0
    Contact: support@fideo.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from fideo_api.models.location_type import LocationType
from typing import Optional, Set
from typing_extensions import Self

class LocationReq(BaseModel):
    """
    LocationReq
    """ # noqa: E501
    address_line1: Optional[StrictStr] = Field(default=None, alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, alias="addressLine2")
    city: Optional[StrictStr] = None
    region: Optional[StrictStr] = None
    region_code: Optional[StrictStr] = Field(default=None, alias="regionCode")
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    country: Optional[StrictStr] = None
    country_code: Optional[StrictStr] = Field(default=None, alias="countryCode")
    latitude: Optional[Union[StrictFloat, StrictInt]] = None
    longitude: Optional[Union[StrictFloat, StrictInt]] = None
    time_zone: Optional[StrictStr] = Field(default=None, alias="timeZone")
    formatted: Optional[StrictStr] = None
    type: Optional[LocationType] = None
    __properties: ClassVar[List[str]] = ["addressLine1", "addressLine2", "city", "region", "regionCode", "postalCode", "country", "countryCode", "latitude", "longitude", "timeZone", "formatted", "type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of LocationReq from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LocationReq from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addressLine1": obj.get("addressLine1"),
            "addressLine2": obj.get("addressLine2"),
            "city": obj.get("city"),
            "region": obj.get("region"),
            "regionCode": obj.get("regionCode"),
            "postalCode": obj.get("postalCode"),
            "country": obj.get("country"),
            "countryCode": obj.get("countryCode"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "timeZone": obj.get("timeZone"),
            "formatted": obj.get("formatted"),
            "type": obj.get("type")
        })
        return _obj


