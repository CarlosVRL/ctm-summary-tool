from src.banner import header, get_inputs, footer
from src.setup_logger import log
from src.inputs import Inputs


def main():
    log.info(header())
    log.info('')

    log.info('INPUTS')
    inputs = get_inputs()
    log.info('> chart    : %s', inputs.chart)
    log.info('> strategy : %s', inputs.strategy)
    log.info('> config   : %s', inputs.config)
    log.info('')

    # read input 1

    # read input 2

    # read input 3

    # create outputs

    log.info(footer())


if __name__ == "__main__":
    main()
