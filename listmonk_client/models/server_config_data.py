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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from listmonk_client.models.server_config_data_langs_inner import ServerConfigDataLangsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ServerConfigData(BaseModel):
    """
    ServerConfigData
    """ # noqa: E501
    messengers: Optional[List[StrictStr]] = None
    langs: Optional[List[ServerConfigDataLangsInner]] = None
    lang: Optional[StrictStr] = None
    update: Optional[StrictStr] = None
    needs_restart: Optional[StrictBool] = None
    version: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["messengers", "langs", "lang", "update", "needs_restart", "version"]

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
        """Create an instance of ServerConfigData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in langs (list)
        _items = []
        if self.langs:
            for _item in self.langs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['langs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ServerConfigData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "messengers": obj.get("messengers"),
            "langs": [ServerConfigDataLangsInner.from_dict(_item) for _item in obj.get("langs")] if obj.get("langs") is not None else None,
            "lang": obj.get("lang"),
            "update": obj.get("update"),
            "needs_restart": obj.get("needs_restart"),
            "version": obj.get("version")
        })
        return _obj


