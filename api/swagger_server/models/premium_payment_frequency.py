# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PremiumPaymentFrequency(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ANNUAL = "annual"
    BI_ANNUAL = "bi-annual"
    QUARTERLY = "quarterly"
    MONTHLY = "monthly"
    BI_MONTHLY = "bi-monthly"
    WEEKLY = "weekly"
    DAILY = "daily"
    USAGE_BASED_OR_ON_DEMAND = "usage based or on demand"
    SUBSCRIPTION_NOT_AN_ANNUAL_CONTRACT_ = "subscription (not an annual contract)"
    OTHER = "other"
    def __init__(self):  # noqa: E501
        """PremiumPaymentFrequency - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'PremiumPaymentFrequency':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The premiumPaymentFrequency of this PremiumPaymentFrequency.  # noqa: E501
        :rtype: PremiumPaymentFrequency
        """
        return util.deserialize_model(dikt, cls)
