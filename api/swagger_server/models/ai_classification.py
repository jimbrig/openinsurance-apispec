# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AiClassification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    _0_AUTONOMOUS_VEHICLE_SAE_STANDARD_ = "level 0 autonomous vehicle (SAE standard)"
    _1_AUTONOMOUS_VEHICLE_SAE_STANDARD_ = "level 1 autonomous vehicle (SAE standard)"
    _2_AUTONOMOUS_VEHICLE_SAE_STANDARD_ = "level 2 autonomous vehicle (SAE standard)"
    _3_AUTONOMOUS_VEHICLE_SAE_STANDARD_ = "level 3 autonomous vehicle (SAE standard)"
    _4_AUTONOMOUS_VEHICLE_SAE_STANDARD_ = "level 4 autonomous vehicle (SAE standard)"
    _5_AUTONOMOUS_VEHICLE_SAE_STANDARD_ = "level 5 autonomous vehicle (SAE standard)"
    def __init__(self):  # noqa: E501
        """AiClassification - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'AiClassification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The aiClassification of this AiClassification.  # noqa: E501
        :rtype: AiClassification
        """
        return util.deserialize_model(dikt, cls)
