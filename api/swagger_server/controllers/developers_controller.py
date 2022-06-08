import connexion
import six

from swagger_server.models.claim import Claim  # noqa: E501
from swagger_server.models.driver import Driver  # noqa: E501
from swagger_server.models.vehicle import Vehicle  # noqa: E501
from swagger_server import util


def search_claim_by_claim_id(search_string=None, skip=None, limit=None):  # noqa: E501
    """returns claim

    By passing in the appropriate options, you can search for claim in the system  # noqa: E501

    :param search_string: pass an optional search string for looking up claim
    :type search_string: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[Claim]
    """
    return 'do some magic!'


def search_driver_by_driver_id(search_string=None, skip=None, limit=None):  # noqa: E501
    """returns driver

    By passing in the appropriate options, you can search for claim in the system  # noqa: E501

    :param search_string: pass an optional search string for looking up driver
    :type search_string: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[Driver]
    """
    return 'do some magic!'


def search_motor_coverage_by_motor_coverage_id(search_string=None, skip=None, limit=None):  # noqa: E501
    """returns motorCoverage

    By passing in the appropriate options, you can search for claim in the system  # noqa: E501

    :param search_string: pass an optional search string for looking up motorCoverage
    :type search_string: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[Driver]
    """
    return 'do some magic!'


def search_vehicle_by_vehicle_id(search_string=None, skip=None, limit=None):  # noqa: E501
    """returns vehicle

    By passing in the appropriate options, you can search for Vehicle in the system  # noqa: E501

    :param search_string: pass an optional search string for looking up Vehicle
    :type search_string: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[Vehicle]
    """
    return 'do some magic!'
