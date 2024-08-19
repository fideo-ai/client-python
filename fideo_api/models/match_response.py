# coding: utf-8

"""
    Fideo API

    Fideo Intelligence offers an identity intelligence product that protects the public good. - [Fideo Privacy Policy](https://www.fideo.ai/privacy-policy/)

    The version of the OpenAPI document: 1.0.2
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
from fideo_api.models.evidence import Evidence
from fideo_api.models.score_details import ScoreDetails
from typing import Optional, Set
from typing_extensions import Self

class MatchResponse(BaseModel):
    """
    MatchResponse
    """ # noqa: E501
    address_line1: Optional[StrictStr] = Field(default=None, alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, alias="addressLine2")
    city: Optional[StrictStr] = None
    region: Optional[StrictStr] = None
    region_code: Optional[StrictStr] = Field(default=None, alias="regionCode")
    country: Optional[StrictStr] = None
    continent: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    family_name: Optional[StrictStr] = Field(default=None, alias="familyName")
    given_name: Optional[StrictStr] = Field(default=None, alias="givenName")
    full_name: Optional[StrictStr] = Field(default=None, alias="fullName")
    phone: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    maid: Optional[StrictStr] = None
    social: Optional[StrictStr] = None
    non_id: Optional[StrictStr] = Field(default=None, alias="nonId")
    panorama_id: Optional[StrictStr] = Field(default=None, alias="panoramaId")
    ip_address: Optional[StrictStr] = Field(default=None, alias="ipAddress")
    birthday: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    organization: Optional[StrictStr] = None
    risk: Optional[Union[StrictFloat, StrictInt]] = None
    evidence: Optional[Evidence] = None
    risk_v2: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="riskV2")
    risk_v3: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="riskV3")
    score_details: Optional[List[ScoreDetails]] = Field(default=None, alias="scoreDetails")
    __properties: ClassVar[List[str]] = ["addressLine1", "addressLine2", "city", "region", "regionCode", "country", "continent", "postalCode", "familyName", "givenName", "fullName", "phone", "email", "maid", "social", "nonId", "panoramaId", "ipAddress", "birthday", "title", "organization", "risk", "evidence", "riskV2", "riskV3", "scoreDetails"]

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
        """Create an instance of MatchResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of evidence
        if self.evidence:
            _dict['evidence'] = self.evidence.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in score_details (list)
        _items = []
        if self.score_details:
            for _item in self.score_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['scoreDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MatchResponse from a dict"""
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
            "country": obj.get("country"),
            "continent": obj.get("continent"),
            "postalCode": obj.get("postalCode"),
            "familyName": obj.get("familyName"),
            "givenName": obj.get("givenName"),
            "fullName": obj.get("fullName"),
            "phone": obj.get("phone"),
            "email": obj.get("email"),
            "maid": obj.get("maid"),
            "social": obj.get("social"),
            "nonId": obj.get("nonId"),
            "panoramaId": obj.get("panoramaId"),
            "ipAddress": obj.get("ipAddress"),
            "birthday": obj.get("birthday"),
            "title": obj.get("title"),
            "organization": obj.get("organization"),
            "risk": obj.get("risk"),
            "evidence": Evidence.from_dict(obj["evidence"]) if obj.get("evidence") is not None else None,
            "riskV2": obj.get("riskV2"),
            "riskV3": obj.get("riskV3"),
            "scoreDetails": [ScoreDetails.from_dict(_item) for _item in obj["scoreDetails"]] if obj.get("scoreDetails") is not None else None
        })
        return _obj


