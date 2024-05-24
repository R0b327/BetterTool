import os
import sys
import platform
from time import ctime

""" This function will stop the program when a critical error occurs """
class Color:
    VIOLET = '\033[95m'
    RED = '\033[91m'
    RESET = '\033[0m'

def CriticalError():
    print(f"""
    {Color.RED}Python Info:
    {Color.VIOLET}PYTHON VERSION: {platform.python_version()}
    {Color.VIOLET}PYTHON BUILD: {'{}, DATE: {}'.format(*platform.python_build())}
    {Color.VIOLET}PYTHON COMPILER: {platform.python_compiler()}
    {Color.VIOLET}SCRIPT LOCATION: {os.path.dirname(os.path.realpath(sys.argv[0]))}
    {Color.VIOLET}CURRENT LOCATION: {os.getcwd()}
    {Color.RED}System Info:
    {Color.VIOLET}SYSTEM: {platform.system()}
    {Color.VIOLET}RELEASE: {platform.release()}
    {Color.VIOLET}VERSION: {platform.version()}
    {Color.VIOLET}ARCHITECTURE: {'{} {}'.format(*platform.architecture())}
    {Color.VIOLET}PROCESSOR: {platform.processor()}
    {Color.VIOLET}MACHINE: {platform.machine()}
    {Color.VIOLET}NODE: {platform.node()}
    {Color.VIOLET}TIME: {ctime()}
    {Color.RESET}
    """)
