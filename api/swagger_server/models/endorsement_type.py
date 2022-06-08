# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class EndorsementType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ADDITION_INCREASE = "addition/increase"
    DELETION_DECREASE = "deletion/decrease"
    POLICY_CANCELLATION = "policy cancellation"
    POLICY_EXTENSION = "policy extension"
    POLICY_DECLARATION = "policy declaration"
    POLICY_TRANSFER = "policy transfer"
    POLICY_RENEWAL = "policy renewal"
    def __init__(self):  # noqa: E501
        """EndorsementType - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'EndorsementType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The endorsementType of this EndorsementType.  # noqa: E501
        :rtype: EndorsementType
        """
        return util.deserialize_model(dikt, cls)
