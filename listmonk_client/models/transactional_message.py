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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictInt, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TransactionalMessage(BaseModel):
    """
    TransactionalMessage
    """ # noqa: E501
    subscriber_email: Optional[StrictStr] = None
    subscriber_id: Optional[StrictInt] = None
    template_id: Optional[StrictInt] = None
    from_email: Optional[StrictStr] = None
    data: Optional[Union[str, Any]] = None
    headers: Optional[List[Union[str, Any]]] = None
    messenger: Optional[StrictStr] = None
    content_type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["subscriber_email", "subscriber_id", "template_id", "from_email", "data", "headers", "messenger", "content_type"]

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
        """Create an instance of TransactionalMessage from a JSON string"""
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
        """Create an instance of TransactionalMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "subscriber_email": obj.get("subscriber_email"),
            "subscriber_id": obj.get("subscriber_id"),
            "template_id": obj.get("template_id"),
            "from_email": obj.get("from_email"),
            "data": obj.get("data"),
            "headers": obj.get("headers"),
            "messenger": obj.get("messenger"),
            "content_type": obj.get("content_type")
        })
        return _obj


