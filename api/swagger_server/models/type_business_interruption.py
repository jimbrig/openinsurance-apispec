# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TypeBusinessInterruption(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    BUSINESS_INTERRUPTION = "Business Interruption"
    INCREASED_COST_OF_WORKING_ICOW_ = "Increased Cost of Working (ICOW)"
    CONTINGENT_LOSS_OF_PROFIT = "Contingent Loss of Profit"
    def __init__(self):  # noqa: E501
        """TypeBusinessInterruption - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'TypeBusinessInterruption':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The typeBusinessInterruption of this TypeBusinessInterruption.  # noqa: E501
        :rtype: TypeBusinessInterruption
        """
        return util.deserialize_model(dikt, cls)
