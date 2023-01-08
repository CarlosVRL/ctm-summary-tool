from src.banner import header, get_inputs, footer
from src.setup_logger import log
from src.util import get_csv, get_props


def main():
    log.info(header())
    log.info('')

    log.info('INPUTS')
    inputs = get_inputs()
    log.info('> chart    : %s', inputs.chart)
    log.info('> strategy : %s', inputs.strategy)
    log.info('> config   : %s', inputs.config)
    log.info('')

    chart_data = get_csv(inputs.chart)

    strategy_data = get_csv(inputs.strategy)

    config_data = get_props(inputs.config)

    # create outputs

    log.info(footer())


if __name__ == "__main__":
    main()
