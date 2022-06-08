import connexion
import six

from swagger_server.models.claim import Claim  # noqa: E501
from swagger_server.models.driver import Driver  # noqa: E501
from swagger_server.models.motor_coverage import MotorCoverage  # noqa: E501
from swagger_server.models.vehicle import Vehicle  # noqa: E501
from swagger_server import util


def add_claim(body=None):  # noqa: E501
    """adds a claim

    Adds an item to the system # noqa: E501

    :param body: Claim to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Claim.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_driver(body=None):  # noqa: E501
    """adds a Driver

    Adds an item to the system # noqa: E501

    :param body: Driver to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Driver.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_motor_coverage(body=None):  # noqa: E501
    """adds a MotorCoverage

    Adds an item to the system # noqa: E501

    :param body: motorCoverage to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = MotorCoverage.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_vehicle(body=None):  # noqa: E501
    """adds a vehicle

    Adds an item to the system # noqa: E501

    :param body: Vehicle to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Vehicle.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
