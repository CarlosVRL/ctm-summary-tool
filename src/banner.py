import argparse

from src import ROOT_PATH
from src.inputs import Inputs


def header():
    return "CTM Position Summary Tool"


def get_inputs():
    parser = argparse.ArgumentParser(
        prog='ctm-summary-tool',
        description='Create formatted CTM Position Summary output')
    parser.add_argument('chart', help='chart data')
    parser.add_argument('strategy', help='strategy tester data')
    parser.add_argument('config', help='strategy description')
    args = parser.parse_args()
    return Inputs(args.chart, args.strategy, args.config)


def footer():
    return "Summary Complete"


def root_path():
    return ROOT_PATH
