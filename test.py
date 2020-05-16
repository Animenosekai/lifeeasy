import lifeeasy
body = []
lifeeasy.display_title('')
lifeeasy.display(0.1,0.1)

while True:
    lifeeasy.display_body(['Bytes received: {}'.format(lifeeasy.net_total_bytes_received()), 'Bytes sent: {}'.format(lifeeasy.net_total_bytes_sent()), "", 'Ram usage: {}%'.format(lifeeasy.used_ram_percentage())])