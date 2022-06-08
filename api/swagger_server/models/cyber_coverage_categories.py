# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CyberCoverageCategories(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    DATA_AND_SOFTWARE_LOSS = "Data and software loss"
    BREACH_OF_PRIVACY = "Breach of privacy"
    INCIDENT_MANAGEMENT_AND_NOTIFICATION_COSTS = "Incident management and notification costs"
    KIDNAP_AND_RANSOM_EXTORTION_ = "Kidnap and Ransom (Extortion)"
    BUSINESS_INTERRUPTION = "Business interruption"
    CONTINGENT_BUSINESS_INTERRUPTION = "Contingent business interruption"
    MULTI_MEDIA_LAIBILITIES_DISPARAGEMENT_ = "Multi-media laibilities (disparagement)"
    LEGAL_AND_DEFENCE_COSTS = "Legal and defence costs"
    REPUTATIONAL_DAMAGE = "Reputational damage"
    NETWORK_SERVICE_FAILURE_LIABILITY = "Network service failure liability"
    ERRORS_AND_OMISSIONS = "Errors and omissions"
    PROFESSIONAL_INDEMNITY = "Professional indemnity"
    FIDELITY_FRAUD_AND_THEFT = "Fidelity, fraud and Theft"
    THEFT_OF_INTECTUAL_PROPERTY = "Theft of intectual property"
    PHYSICAL_ASSET_DAMAGE = "Physical asset damage"
    COMPENSATION_TO_INJURED_PARTIES = "Compensation to injured parties"
    CYBER_TERRORISM = "Cyber terrorism"
    FINES_AND_PENALTIES = "Fines and penalties"
    DIRECTORS_AND_OFFICERS_LIABILITY = "Directors and officers liability"
    GENERAL_LIABILITY = "General liability"
    ENVIRONMENTAL_DAMAGE = "Environmental damage"
    def __init__(self):  # noqa: E501
        """CyberCoverageCategories - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'CyberCoverageCategories':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The cyberCoverageCategories of this CyberCoverageCategories.  # noqa: E501
        :rtype: CyberCoverageCategories
        """
        return util.deserialize_model(dikt, cls)
