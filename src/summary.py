class Summary:
    def __init__(self, asset, status, entry, stop_val, stop_percent, gain_val, gain_percent, long_val, time):
        self.asset = asset
        self.status = status
        self.entry = entry
        self.stop_val = stop_val
        self.stop_percent = stop_percent
        self.gain_val = gain_val
        self.gain_percent = gain_percent
        self.long_val = long_val
        self.time = time


def compute_summary(chart_data, strategy_data, config_data):

    asset = config_data["name"]

    check_status_active = strategy_data[1]  # latest trade can be open or closed
    if check_status_active[2].startswith('Open'):
        status = 'Long Trade Active'
    else:
        status = 'Waiting for signal'

    check_entry = strategy_data[2]  # last position information
    entry = float(check_entry[4])

    stop_percent = float(config_data["stop_loss"])

    stop_val = entry * (1.0 - stop_percent/100.0)

    last_chart_record = (chart_data[-1])
    last_close = float(last_chart_record[4])
    gain_val = last_close - entry

    gain_percent = (last_close - entry) / abs(entry) * 100

    long_val = float(last_chart_record[5])

    time = last_chart_record[0]

    return Summary(asset, status, entry, stop_val, stop_percent, gain_val, gain_percent, long_val, time)
