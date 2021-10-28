"""
Show anything
"""


class ConstantGlobal:
    """
    Show anything
    """
    # pylint: disable=too-few-public-methods
    LOCALHOST = '0.0.0.0'
    SUPERUSER = False
    ARGUMENTS = None
    FILE_WRITE = 'w'
    FILE_READ = 'r'
    FILE_APPEND = 'a'
    FILE_WRITE_BINARY = 'wb'
    FILE_READ_BINARY = 'wb'
    FILE_APPEND_BINARY = 'ab'



class EnumGlobal:
    """
    Show anything
    """
    # pylint: disable=too-few-public-methods
    EMPTY = ''
    POINT = '.'
    EXT_CSV = 'csv'
    EXT_JSON = 'json'
    DELIMITER = ';'


class ConstantScanner:
    """
    Show anything
    """
    # pylint: disable=too-few-public-methods
    SCANNERS = ['nmap', 'shodan']
    SCANNER = 'nmap'
    MIN_PORT = 80
    MAX_PORT = 8080
    API_KEY = None


class EnumScanner:
    """
    Show anything
    """
    # pylint: disable=too-few-public-methods
    HOST = 'host'
    HOST_STATE = 'state'
    LAYER4_TCP = 'tcp'
    LAYER4_UDP = 'udp'
    LAYER4_SPX = 'spx'
    EXCEPTION = 'Data not found, try to use the scanner: _.run_scan(...)'
