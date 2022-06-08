# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Claim(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, claim_type: str=None, location: str=None, loss_cause: str=None, description: str=None, fnol: date=None, claim_number: str=None, liability_share: float=None, reserve: float=None, claim_status: str=None, last_update: date=None, reopen_date: date=None, excess_amount: float=None, payment_method: str=None, documents: str=None, loss_date: date=None):  # noqa: E501
        """Claim - a model defined in Swagger

        :param claim_type: The claim_type of this Claim.  # noqa: E501
        :type claim_type: str
        :param location: The location of this Claim.  # noqa: E501
        :type location: str
        :param loss_cause: The loss_cause of this Claim.  # noqa: E501
        :type loss_cause: str
        :param description: The description of this Claim.  # noqa: E501
        :type description: str
        :param fnol: The fnol of this Claim.  # noqa: E501
        :type fnol: date
        :param claim_number: The claim_number of this Claim.  # noqa: E501
        :type claim_number: str
        :param liability_share: The liability_share of this Claim.  # noqa: E501
        :type liability_share: float
        :param reserve: The reserve of this Claim.  # noqa: E501
        :type reserve: float
        :param claim_status: The claim_status of this Claim.  # noqa: E501
        :type claim_status: str
        :param last_update: The last_update of this Claim.  # noqa: E501
        :type last_update: date
        :param reopen_date: The reopen_date of this Claim.  # noqa: E501
        :type reopen_date: date
        :param excess_amount: The excess_amount of this Claim.  # noqa: E501
        :type excess_amount: float
        :param payment_method: The payment_method of this Claim.  # noqa: E501
        :type payment_method: str
        :param documents: The documents of this Claim.  # noqa: E501
        :type documents: str
        :param loss_date: The loss_date of this Claim.  # noqa: E501
        :type loss_date: date
        """
        self.swagger_types = {
            'claim_type': str,
            'location': str,
            'loss_cause': str,
            'description': str,
            'fnol': date,
            'claim_number': str,
            'liability_share': float,
            'reserve': float,
            'claim_status': str,
            'last_update': date,
            'reopen_date': date,
            'excess_amount': float,
            'payment_method': str,
            'documents': str,
            'loss_date': date
        }

        self.attribute_map = {
            'claim_type': 'claimType',
            'location': 'location',
            'loss_cause': 'lossCause',
            'description': 'description',
            'fnol': 'fnol',
            'claim_number': 'claimNumber',
            'liability_share': 'liabilityShare',
            'reserve': 'reserve',
            'claim_status': 'claimStatus',
            'last_update': 'lastUpdate',
            'reopen_date': 'reopenDate',
            'excess_amount': 'excessAmount',
            'payment_method': 'paymentMethod',
            'documents': 'documents',
            'loss_date': 'lossDate'
        }
        self._claim_type = claim_type
        self._location = location
        self._loss_cause = loss_cause
        self._description = description
        self._fnol = fnol
        self._claim_number = claim_number
        self._liability_share = liability_share
        self._reserve = reserve
        self._claim_status = claim_status
        self._last_update = last_update
        self._reopen_date = reopen_date
        self._excess_amount = excess_amount
        self._payment_method = payment_method
        self._documents = documents
        self._loss_date = loss_date

    @classmethod
    def from_dict(cls, dikt) -> 'Claim':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Claim of this Claim.  # noqa: E501
        :rtype: Claim
        """
        return util.deserialize_model(dikt, cls)

    @property
    def claim_type(self) -> str:
        """Gets the claim_type of this Claim.


        :return: The claim_type of this Claim.
        :rtype: str
        """
        return self._claim_type

    @claim_type.setter
    def claim_type(self, claim_type: str):
        """Sets the claim_type of this Claim.


        :param claim_type: The claim_type of this Claim.
        :type claim_type: str
        """

        self._claim_type = claim_type

    @property
    def location(self) -> str:
        """Gets the location of this Claim.


        :return: The location of this Claim.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """Sets the location of this Claim.


        :param location: The location of this Claim.
        :type location: str
        """

        self._location = location

    @property
    def loss_cause(self) -> str:
        """Gets the loss_cause of this Claim.


        :return: The loss_cause of this Claim.
        :rtype: str
        """
        return self._loss_cause

    @loss_cause.setter
    def loss_cause(self, loss_cause: str):
        """Sets the loss_cause of this Claim.


        :param loss_cause: The loss_cause of this Claim.
        :type loss_cause: str
        """

        self._loss_cause = loss_cause

    @property
    def description(self) -> str:
        """Gets the description of this Claim.


        :return: The description of this Claim.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Claim.


        :param description: The description of this Claim.
        :type description: str
        """

        self._description = description

    @property
    def fnol(self) -> date:
        """Gets the fnol of this Claim.


        :return: The fnol of this Claim.
        :rtype: date
        """
        return self._fnol

    @fnol.setter
    def fnol(self, fnol: date):
        """Sets the fnol of this Claim.


        :param fnol: The fnol of this Claim.
        :type fnol: date
        """

        self._fnol = fnol

    @property
    def claim_number(self) -> str:
        """Gets the claim_number of this Claim.


        :return: The claim_number of this Claim.
        :rtype: str
        """
        return self._claim_number

    @claim_number.setter
    def claim_number(self, claim_number: str):
        """Sets the claim_number of this Claim.


        :param claim_number: The claim_number of this Claim.
        :type claim_number: str
        """

        self._claim_number = claim_number

    @property
    def liability_share(self) -> float:
        """Gets the liability_share of this Claim.


        :return: The liability_share of this Claim.
        :rtype: float
        """
        return self._liability_share

    @liability_share.setter
    def liability_share(self, liability_share: float):
        """Sets the liability_share of this Claim.


        :param liability_share: The liability_share of this Claim.
        :type liability_share: float
        """

        self._liability_share = liability_share

    @property
    def reserve(self) -> float:
        """Gets the reserve of this Claim.


        :return: The reserve of this Claim.
        :rtype: float
        """
        return self._reserve

    @reserve.setter
    def reserve(self, reserve: float):
        """Sets the reserve of this Claim.


        :param reserve: The reserve of this Claim.
        :type reserve: float
        """

        self._reserve = reserve

    @property
    def claim_status(self) -> str:
        """Gets the claim_status of this Claim.


        :return: The claim_status of this Claim.
        :rtype: str
        """
        return self._claim_status

    @claim_status.setter
    def claim_status(self, claim_status: str):
        """Sets the claim_status of this Claim.


        :param claim_status: The claim_status of this Claim.
        :type claim_status: str
        """

        self._claim_status = claim_status

    @property
    def last_update(self) -> date:
        """Gets the last_update of this Claim.


        :return: The last_update of this Claim.
        :rtype: date
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update: date):
        """Sets the last_update of this Claim.


        :param last_update: The last_update of this Claim.
        :type last_update: date
        """

        self._last_update = last_update

    @property
    def reopen_date(self) -> date:
        """Gets the reopen_date of this Claim.


        :return: The reopen_date of this Claim.
        :rtype: date
        """
        return self._reopen_date

    @reopen_date.setter
    def reopen_date(self, reopen_date: date):
        """Sets the reopen_date of this Claim.


        :param reopen_date: The reopen_date of this Claim.
        :type reopen_date: date
        """

        self._reopen_date = reopen_date

    @property
    def excess_amount(self) -> float:
        """Gets the excess_amount of this Claim.


        :return: The excess_amount of this Claim.
        :rtype: float
        """
        return self._excess_amount

    @excess_amount.setter
    def excess_amount(self, excess_amount: float):
        """Sets the excess_amount of this Claim.


        :param excess_amount: The excess_amount of this Claim.
        :type excess_amount: float
        """

        self._excess_amount = excess_amount

    @property
    def payment_method(self) -> str:
        """Gets the payment_method of this Claim.


        :return: The payment_method of this Claim.
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method: str):
        """Sets the payment_method of this Claim.


        :param payment_method: The payment_method of this Claim.
        :type payment_method: str
        """

        self._payment_method = payment_method

    @property
    def documents(self) -> str:
        """Gets the documents of this Claim.


        :return: The documents of this Claim.
        :rtype: str
        """
        return self._documents

    @documents.setter
    def documents(self, documents: str):
        """Sets the documents of this Claim.


        :param documents: The documents of this Claim.
        :type documents: str
        """

        self._documents = documents

    @property
    def loss_date(self) -> date:
        """Gets the loss_date of this Claim.


        :return: The loss_date of this Claim.
        :rtype: date
        """
        return self._loss_date

    @loss_date.setter
    def loss_date(self, loss_date: date):
        """Sets the loss_date of this Claim.


        :param loss_date: The loss_date of this Claim.
        :type loss_date: date
        """

        self._loss_date = loss_date
