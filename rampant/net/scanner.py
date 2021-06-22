#!/usr/local/bin python3.9
# -*- Coding: utf-8 -*-
"""
Show anything
"""
from typing import Optional, TypeVar, Sequence, Union, NoReturn
import json
import nmap

from rampant.constant import ConstantGlobal as Cg
from rampant.constant import ConstantScanner as Cs
from rampant.constant import EnumScanner as Es
from rampant.constant import EnumGlobal as Eg

_D: Union = Union[list, dict[Union[dict, str, list]]]
_U: Union = Union[dict, list[Union[dict, str]]]
_T: TypeVar = TypeVar('_T', object, Sequence[list[_U]])


class Scanner:
    """
    Show anything
    """
    # pylint: disable=too-few-public-methods
    def __init__(self,
                 /,
                 scanner=Cs.SCANNER,
                 api_key=Cs.API_KEY):
        # type: (..., str, str) -> NoReturn
        """
        Show anything

        :param scanner:
        :param api_key:
        """
        self.__scanner_type = scanner
        self.__api_key = api_key
        self.__scan_info = list()
        self.__scanner = None

    def __set_scanned_host(self,
                           nmap_scanner,
                           /,
                           list_host):
        # type: (_T, ..., _U) -> _T
        """
        Show anything

        :param nmap_scanner:
        :return:
        """
        for host in list_host:
            _ = dict()
            _[Es.HOST] = host
            _[Es.HOST_STATE] = nmap_scanner[host].state()
            _[Es.LAYER4_TCP] = [nmap_scanner[host][Es.LAYER4_TCP]] \
                if Es.LAYER4_TCP in nmap_scanner[host].all_protocols() else Eg.EMPTY
            _[Es.LAYER4_UDP] = [nmap_scanner[host][Es.LAYER4_UDP]] \
                if Es.LAYER4_UDP in nmap_scanner[host].all_protocols() else Eg.EMPTY
            _[Es.LAYER4_SPX] = [nmap_scanner[host][Es.LAYER4_SPX]] \
                if Es.LAYER4_SPX in nmap_scanner[host].all_protocols() else Eg.EMPTY
            self.__scan_info.append(self.__parser_data(_))
        return self.__scan_info

    @staticmethod
    def __parser_data_layer(data, layer4, /):
        # type: (_D, str, ...) -> _D
        """
        Show anything

        :param data:
        :param layer4:
        :return:
        """
        type_layer_data = data[layer4]
        data[layer4] = list()
        for layer in type_layer_data:
            data[layer4].append([{k.__str__(): layer[k]} for k in layer.keys()])
        data[layer4] = data[layer4][0] if data[layer4] else dict()
        return data

    def __parser_data(self, data, /):
        # type: (_D, ...) -> _D
        """
        Show anything

        :param data:
        :return:
        """
        _ = self.__parser_data_layer(data, Es.LAYER4_TCP)
        _ = self.__parser_data_layer(_, Es.LAYER4_UDP)
        _ = self.__parser_data_layer(_, Es.LAYER4_SPX)
        return _

    @property
    def __nmap_scanner(self, /):
        # type: (...) -> _T
        """
        Show anything

        :return:
        """
        return nmap.PortScanner()

    def set_hosts(self, hosts, /):
        # type: (_U, ...) -> _U
        """
        Show anything

        :param hosts:
        :return:
        """
        self.__scan_info = hosts
        return self.__scan_info

    def add_host(self, host, /):
        # type: (_U, ...) -> _U
        """
        Show anything

        :param host:
        :return:
        """
        self.__scan_info.append(host)
        return self.__scan_info

    def scan_info(self, /):
        # type: (...) -> _U
        """
        Show anything

        :return:
        """
        return self.__scan_info

    def run_scan(self,
                 network=Cg.LOCALHOST,
                 /,
                 port_min=Cs.MIN_PORT,
                 port_max=Cs.MAX_PORT,
                 arguments=Cg.ARGUMENTS,
                 superuser=Cg.SUPERUSER):
        # type: (str, ..., Optional[int], Optional[int], str, bool) -> _T
        """
        Show anything

        :param network:
        :param port_min:
        :param port_max:
        :param arguments:
        :param superuser:
        :return:
        """
        # if self.__scanner_type not in cs.SCANNERS:
        #    raise Exception('none')
        nmap_scanner = self.__nmap_scanner
        nmap_scanner.scan(network,
                          ports=f'{port_min}-{port_max}',
                          arguments=arguments,
                          sudo=superuser)
        self.__scanner = nmap_scanner
        return self.__set_scanned_host(nmap_scanner, list_host=nmap_scanner.all_hosts())

    @staticmethod
    def __save_file(name_file, file_type, content, /, delimiter=Eg.DELIMITER):
        # type: (str, str, Union[str, list, dict], ..., str) -> NoReturn
        """
        Show anything

        :param name_file:
        :param file_type:
        :param content:
        :param delimiter:
        :return:
        """
        with open(name_file, Cg.FILE_WRITE) as file:
            if file_type == Eg.EXT_CSV:
                file.write(content.replace(Eg.DELIMITER, delimiter))
            elif file_type == Eg.EXT_JSON:
                file.write(json.dumps(content))
            else:
                file.write(content)
            file.close()

    def save(self, name, /, extension):
        # type: (str, ..., str) -> NoReturn
        """
        Show anything

        :param name:
        :param extension:
        :return:
        """
        if bool(self.__scan_info.__str__()):
            self.__save_file(name + Eg.POINT + extension,
                             extension,
                             self.__scan_info.__str__())

    def save_json(self, name, /):
        # type: (str, ...) -> NoReturn
        """
        Show anything

        :param name:
        :return:
        """
        if bool(json.dumps(self.__scan_info)):
            self.__save_file(name + Eg.POINT + Eg.EXT_JSON,
                             Eg.EXT_JSON,
                             self.__scan_info)

    def save_csv(self, name, /, delimiter):
        # type: (str, ..., str) -> NoReturn
        """
        Show anything

        :param name:
        :param delimiter:
        :return:
        """
        if bool(self.__scanner.csv()):
            self.__save_file(name + Eg.POINT + Eg.EXT_CSV, Eg.EXT_CSV,
                             self.__scanner.csv(),
                             delimiter)

    def nmap_command(self, /):
        # type: (...) -> NoReturn
        """
        Show anything

        :return:
        """
        print("hello ", self.__scan_info)
