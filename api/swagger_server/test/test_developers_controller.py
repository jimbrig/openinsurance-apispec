# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.claim import Claim  # noqa: E501
from swagger_server.models.driver import Driver  # noqa: E501
from swagger_server.models.vehicle import Vehicle  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDevelopersController(BaseTestCase):
    """DevelopersController integration test stubs"""

    def test_search_claim_by_claim_id(self):
        """Test case for search_claim_by_claim_id

        returns claim
        """
        query_string = [('search_string', 'search_string_example'),
                        ('skip', 1),
                        ('limit', 50)]
        response = self.client.open(
            '/JimmysOrg/openinsurance/0.0.0.9999/claim',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_driver_by_driver_id(self):
        """Test case for search_driver_by_driver_id

        returns driver
        """
        query_string = [('search_string', 'search_string_example'),
                        ('skip', 1),
                        ('limit', 50)]
        response = self.client.open(
            '/JimmysOrg/openinsurance/0.0.0.9999/driver',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_motor_coverage_by_motor_coverage_id(self):
        """Test case for search_motor_coverage_by_motor_coverage_id

        returns motorCoverage
        """
        query_string = [('search_string', 'search_string_example'),
                        ('skip', 1),
                        ('limit', 50)]
        response = self.client.open(
            '/JimmysOrg/openinsurance/0.0.0.9999/motorCoverage',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_vehicle_by_vehicle_id(self):
        """Test case for search_vehicle_by_vehicle_id

        returns vehicle
        """
        query_string = [('search_string', 'search_string_example'),
                        ('skip', 1),
                        ('limit', 50)]
        response = self.client.open(
            '/JimmysOrg/openinsurance/0.0.0.9999/vehicle',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
