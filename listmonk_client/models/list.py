# coding: utf-8

"""
    Listmonk

    The API collection for listmonk

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, TypeVar, Generic
from pydantic import BaseModel, StrictInt, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

T = TypeVar("T", bound="List")

class List(BaseModel, Generic[T]):
    """
    List
    """ # noqa: E501
    id: Optional[StrictInt] = None
    created_at: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    uuid: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    optin: Optional[StrictStr] = None
    tags: Optional[List[StrictStr]] = None
    subscriber_count: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "created_at", "updated_at", "uuid", "name", "type", "optin", "tags", "subscriber_count"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of List from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of List from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "uuid": obj.get("uuid"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "optin": obj.get("optin"),
            "tags": obj.get("tags"),
            "subscriber_count": obj.get("subscriber_count")
        })
        return _obj

