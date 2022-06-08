# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.claim import Claim  # noqa: E501
from swagger_server.models.driver import Driver  # noqa: E501
from swagger_server.models.motor_coverage import MotorCoverage  # noqa: E501
from swagger_server.models.vehicle import Vehicle  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAdminsController(BaseTestCase):
    """AdminsController integration test stubs"""

    def test_add_claim(self):
        """Test case for add_claim

        adds a claim
        """
        body = Claim()
        response = self.client.open(
            '/JimmysOrg/openinsurance/0.0.0.9999/claim',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_driver(self):
        """Test case for add_driver

        adds a Driver
        """
        body = Driver()
        response = self.client.open(
            '/JimmysOrg/openinsurance/0.0.0.9999/driver',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_motor_coverage(self):
        """Test case for add_motor_coverage

        adds a MotorCoverage
        """
        body = MotorCoverage()
        response = self.client.open(
            '/JimmysOrg/openinsurance/0.0.0.9999/motorCoverage',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_vehicle(self):
        """Test case for add_vehicle

        adds a vehicle
        """
        body = Vehicle()
        response = self.client.open(
            '/JimmysOrg/openinsurance/0.0.0.9999/vehicle',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
