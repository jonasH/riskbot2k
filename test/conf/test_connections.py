__author__ = 'rickard'

def test_connections(config):
    correct_geography = True
    connection_dict = {}
    for continent in config.keys():
        for country in config[continent]:
            connection_dict.update({country:config[continent][country]['connections']})

    for dict_country in connection_dict:
        for conn_country in connection_dict[dict_country]:
            if dict_country in connection_dict[conn_country]:
                pass
            else:
                correct_geography = False
    return correct_geography