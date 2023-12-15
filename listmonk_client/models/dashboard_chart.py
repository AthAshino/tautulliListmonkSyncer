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
from pydantic import BaseModel
from listmonk_client.models.dashboard_chart_link_clicks_inner import DashboardChartLinkClicksInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DashboardChart(BaseModel):
    """
    DashboardChart
    """ # noqa: E501
    link_clicks: Optional[List[DashboardChartLinkClicksInner]] = None
    campaign_views: Optional[List[DashboardChartLinkClicksInner]] = None
    __properties: ClassVar[List[str]] = ["link_clicks", "campaign_views"]

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
        """Create an instance of DashboardChart from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in link_clicks (list)
        _items = []
        if self.link_clicks:
            for _item in self.link_clicks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['link_clicks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in campaign_views (list)
        _items = []
        if self.campaign_views:
            for _item in self.campaign_views:
                if _item:
                    _items.append(_item.to_dict())
            _dict['campaign_views'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DashboardChart from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "link_clicks": [DashboardChartLinkClicksInner.from_dict(_item) for _item in obj.get("link_clicks")] if obj.get("link_clicks") is not None else None,
            "campaign_views": [DashboardChartLinkClicksInner.from_dict(_item) for _item in obj.get("campaign_views")] if obj.get("campaign_views") is not None else None
        })
        return _obj


