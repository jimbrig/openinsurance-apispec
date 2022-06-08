# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ProductModel(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CONVENTIONAL_ANNUAL_PREMIUM = "conventional-annual premium"
    PAY_AS_YOU_DRIVE = "pay as you drive"
    PAY_HOW_YOU_DRIVE = "pay how you drive"
    SUBSCRIPTION_E_G_MONTHLY_FEE_ = "subscription (e.g. monthly fee)"
    GOVERMENT_MARKET_TARRIF = "goverment/market tarrif"
    OTHER = "other"
    def __init__(self):  # noqa: E501
        """ProductModel - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ProductModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The productModel of this ProductModel.  # noqa: E501
        :rtype: ProductModel
        """
        return util.deserialize_model(dikt, cls)
