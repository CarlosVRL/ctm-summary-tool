from src.banner import header, get_inputs, footer
from src.setup_logger import log
from src.util import get_csv, get_props, write_csv
from src.summary import compute_summary


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

    log.info('SUMMARY')
    summary = compute_summary(chart_data, strategy_data, config_data)
    log_summary(summary)
    log.info('')

    log.info('OUTPUT')
    write_summary(summary)
    log.info('')

    log.info(footer())


def log_summary(summary):
    log.info('> asset        : %s', summary.asset)
    log.info('> status       : %s', summary.status)
    log.info('> entry        : %s', round(summary.entry, 2))
    log.info('> stop_val     : %s', round(summary.stop_val, 2))
    log.info('> stop_percent : %s', round(summary.stop_percent, 2))
    log.info('> gain_val     : %s', round(summary.gain_val, 2))
    log.info('> gain_percent : %s', round(summary.gain_percent, 2))
    log.info('> long_val     : %s', round(summary.long_val, 2))
    log.info('> time         : %s', summary.time)


def write_summary(summary):
    write_csv('summary.csv',
              [['asset',
                'status',
                'entry',
                'stop_val',
                'stop_percent',
                'gain_val',
                'gain_percent',
                'long_val',
                'time'],
               [summary.asset,
                summary.status,
                round(summary.entry, 2),
                round(summary.stop_val, 2),
                round(summary.stop_percent, 2),
                round(summary.gain_val, 2),
                round(summary.gain_percent, 2),
                round(summary.long_val, 2),
                summary.time]])
    log.info('> summary.csv')


if __name__ == "__main__":
    main()
